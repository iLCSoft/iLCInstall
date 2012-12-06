#! /usr/bin/python

###################################################################
# Python script for finding libraries, binaries and include files
# from an ILCSoft release and copy them into a directory that can
# afterwards easily be packed into a tar ball for the grid
#
# @author Jan Engels, DESY
###################################################################

import sys
import os
import os.path
import commands
import re

# dictionary for storing options
opt={}

# hash map for matching (lock) types with dirs
opt['lock_dirs'] = {
    'l' : ['lib','sharedlib','staticlib'],
    'i' : ['include'],
    'b' : ['bin']
}

# regular expressions
opt['regex'] = {
    # static libraries
    'a' : ['.*/lib.*\.a$'],
    # shared libraries
    's' : ['.*/lib.*\.so'],
    # includes + binaries
    'i' : ['.*'],
    'b' : ['.*'],
    # exclude binaries
    'b-EXCLUDE' : [
        '.*/bbq/.*/bin/CMakeLists.txt',
        '.*/KalTest/.*/bin/.*',
        '.*/RAIDA/v.*/bin/.*' ,
        '.*/CondDBMySQL/.*/bin/.*',
        '.*/lcio/v.*/bin/.*sh$',
        '.*/lcio/v.*/bin/.*cyg$',
        '.*/lcio/v.*/bin/.*bat$',
        '.*/lcio/v.*/bin/lcio$',
        '.*/.empty_file_for_cvs$'
        ],
    # tree-cutting in search-mode
    'C' : ['^CVS$','^\.svn$','^build','^CMakeFiles$','^packages$','^doc$','^example','^src$','^source','^te?mp$','^test'],
    # tree-cutting in lock-mode
    'c' : ['^CVS$','^\.svn$']
}

# compile re's and store in opt['c_regex']
opt['c_regex'] = {}
for k,v in opt['regex'].iteritems():
    for i in v:
        #opt['c_regex'][k].append(re.compile( i ))
        opt['c_regex'].setdefault(k,[]).append(re.compile( i ))

# maxdepth (until locks are found)
opt['maxdepth'] = {
    'l' : 4,
    'i' : 4,
    'b' : 4,
    'a' : 5 # all
}
# maxdepth (in lock mode)
opt['maxdepth_lock'] = {
    'l' : 3,
    'i' : 7,
    'b' : 3
}

# variables for storing output of search
files = {
    'l' : [], # stores shared & static libs
    'i' : [],
    'b' : [],
    #'s' : [], # not used
    #'a' : [], # not used
    'L' : [],
    'I' : [],
    'B' : []
}

# dictionary for finding duplicate files
dup_files = {
    'l' : {},
    'i' : {},
    'b' : {},
    #'s' : {}, # not used
    #'a' : {}  # not used
}

# per default exclude this stuff
def_exclude=['/java/','/qt/','/root/','/mysql/','/CLHEP/','/gsl/','/cernlib/','/geant4/','/FastJet/' ]

#=============================================================================
# function definitions
#-----------------------------------------------------------------------------

def printUsage( progname ):
    # display usage information
    print
    print ' USE:'
    print '   '+progname,'<path> [options]'
    print
    print ' OPTIONS:'
    print '   -o [dir_name] copy files to dir_name [default=<last_dir_in_<path>>]'
    print '   -t test files in dir_name (only possible after -o option was used!)'
    print '   -z create a tarball and erase dir where files were copied to (ilcsoft_<dir_name>.tar.gz)'
    print '   -p [list of types to search for] for uppercase options the entire dir is copied [default=sb]'
    print '         L - Library dirs (shared and static)'
    print '         I - Include dirs'
    print '         B - Binary dirs'
    print '         b - binary files (single files will be detected matching regex \'.*\' i.o.w.: every file inside a bin dir)'
    print '         s - shared libraries only (single files will be detected matching regex \'^lib.*\.a$\')'
    print '         a - static libraries only (single files will be detected matching regex \'^lib.*\.so\')'
    print '   -i include additional files/dirs (see examples below)'
    print '   -e [colon-separated list of strings] exclude (CASE-INSENSITIVE) any file/dir that matches any of the strings [default='+':'.join(def_exclude)+']'
    print '   -v [0|1|2|3|4] verbosity display (0=very high verbosity, 4=quiet) [default=3]'
    print
    print ' NOTE:'
    print '   if you call:'
    print '     ',progname,'<path_to_ilc_release>'
    print '   it\'s the same as:'
    print '     ',progname,'<path_to_ilc_release> -psB -e'+':'.join(def_exclude)+' -v3'
    print '   if you want java and qt to be included you must override the default options! e.g.:'
    print
    print ' EXAMPLES:'
    print '   ',progname,'$ILCHOME/v01-03'
    print '         shows a preview of shared libraries and binary files found at $ILCHOME/v01-03'
    print
    print '   ',progname,'$ILCHOME/v01-03 -pLIB'
    print '         shows a list of libraries, bins and includes dirs found at $ILCHOME/v01-03'
    print
    print '   ',progname,'$ILCHOME/v01-03 -pLIB -o -z'
    print '         creates tarball ilcsoft_v01-03.tar.gz with libs, bin and includes'
    print
    print '   ',progname,'$ILCHOME/v01-03 -i L/foo/bar/lib:/opt/lib; l/foo/lib/libBar.so:/foo/lib/libFoo.so; B/foo/bin'
    print '         include additional (colon-separated) files/dirs prefixed by it\'s type'
    print '         uppercase options are used for copying whole dirs'
    print '         lowercase are copied to their respective dir (b-bin, l-lib, i-include)'
    print
    sys.exit(1)

# list of valid options
valid_opts=['o','t','z','p','i','e','v']

#--------------------------------------------------------------------------------
def abort(msg):
    print '\n Error: ', str(msg)
    sys.exit(1)
#--------------------------------------------------------------------------------
def log_msg(level, msg):
    if level >= args['v']:
        print msg
#--------------------------------------------------------------------------------
def pass_re(type, sstr):
    if opt['c_regex'].has_key( type+'-EXCLUDE' ):
        for i in opt['c_regex'][type+'-EXCLUDE']:
            if i.match( sstr ):
                return 0

    for i in opt['c_regex'][type]:
        if i.match( sstr ):
            return 1
    return 0
#--------------------------------------------------------------------------------
def add_file(type, file, pass_check=True):
    log_msg(0, 'add_file+: type:'+type+' file:'+file)
    
    # add shared & static libs to type 'l'
    if type == 'a' or type == 's':
        type = 'l'
    
    if not files.has_key(type):
        abort('add_file: trying to add file of unknown type:'+type)
    
    f_pass=1
    if args.has_key('e') and pass_check:
        for e in args['e']:
            if file.upper().find(e.upper()) != -1:
                log_msg(1, 'add_file: (-e matched): '+e+' in '+file)
                f_pass=0
    if f_pass:
        files[type].append(file)
        # only files are added for dup checking
        if type.islower():
            k = os.path.basename(file)
            if not dup_files[type].has_key(k):
                dup_files[type][k]=[file]
            else:
                # there is already a file with the same name
                dup_files[type][k].append(file)
        log_msg(3, 'added: ['+type+']: '+file)
    else:
        log_msg(2, 'skipped: ['+type+']: '+file)
    log_msg(0, 'add_file-: (exit)')
#--------------------------------------------------------------------------------
def test_file(type, file):
    log_msg(0, 'test_file+: type:'+type+' file:'+file)
    cmd = 'ldd '+file
    out=commands.getstatusoutput( cmd )
    if out[0] == 0 :
        if out[1].find('=> not found') != -1:
            for l in out[1].split('\n'):
                if l.find('=> not found') != -1:
                    log_msg(3, '['+type+'] Warning: '+file+': '+l)
            log_msg(0, 'test_file: output of "'+cmd+'":'+os.linesep+out[1])
        log_msg(1, 'tested: ['+type+']: '+file)
    else:
        log_msg(2, 'skipped-test: ['+type+']: '+file)
    log_msg(0, 'test_file-: (exit)')
#--------------------------------------------------------------------------------
# FIXME
class GlobDirectoryWalker:
    """ a forward iterator that traverses a directory tree """

    def __init__(self, directory, lock_type='s'):
        self.stack = [directory]
        self.lock_type = lock_type
        self.files = []
        self.index = 0

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                if pass_re( self.lock_type, fullname ):
                    test_file( self.lock_type, fullname )
#--------------------------------------------------------------------------------
def walk_tree(dir, tree=[], lock=0, curr_lock='n'):
    """ walk down a directory tree, call with:
        walk_tree("/foo/bar") """
    
    log_msg(0, 'walk_tree+: dir:'+dir+' tree:'+str(tree)+' lock:'+str(lock)+' curr_lock:'+curr_lock)
    
    # extract current directory from full path
    if dir.endswith('/'): dir=dir[:-1]
    curr_dir = os.path.basename(dir)

    if lock:
        # don't search beyond limits defined by maxdepth
        if (len(tree) - lock) > opt['maxdepth_lock'][curr_lock]:
            log_msg(1, 'walk_tree('+curr_lock+')-: maxdepth reached '+str(tree)+' (exit)')
            return
        # dir-cutting
        if pass_re( 'c', curr_dir ):
            log_msg(2, 'walk_tree('+curr_lock+')-: cut dir '+dir+' (exit)')
            return
    else:
        # don't search beyond limits defined by maxdepth
        if len(tree) > opt['maxdepth']['a']:
            log_msg(1, 'walk_tree('+curr_lock+')-: maxdepth reached '+str(tree)+' (exit)')
            return
        # dir-cutting
        if pass_re( 'C', curr_dir ):
            log_msg(2, 'walk_tree('+curr_lock+')-: cut dir '+dir+' (exit)')
            return
    
        # if curr_dir matches any of the locking dirs hash map, node makes a lock (if not already locked)
        for t, d in opt['lock_dirs'].iteritems():
            if curr_dir in d:
                # make sure we  don't go beyond limits for the specified types
                if len(tree) >= opt['maxdepth'][t]:
                    log_msg(1, 'walk_tree('+t+')-: maxdepth reached for locking '+dir+'! (exit)')
                    return
                # if limits are ok:
                else:
                    # check if we want to copy the whole dir (cp -r), if so there is no need to
                    # walk further down this tree-branch: just add the dir to the copy list and exit!
                    if t.upper() in args['p']:
                        log_msg(1, 'walk_tree('+t.upper()+')-: '+dir+' (exit)')
                        add_file(t.upper(),dir)
                        return

                    # if the whole dir is not to be copied we still need to check if there is any
                    # option for searching the rest of the tree-branch
                    # this check is a little more tricky because options 's' and 'a' are libraries
                    if t=='l':
                        if not ('s' in args['p'] or 'a' in args['p']):
                            log_msg(2, 'walk_tree('+t+')-: (! in -p) '+dir+' (exit)')
                            return
                    # includes && binaries
                    elif not t in args['p']:
                        log_msg(2, 'walk_tree('+t+')-: (! in -p) '+dir+' (exit)')
                        return
                    
                    # if we got here, it means at least one lower-case option for this type of
                    # lock was found! so, proceed with the lock!
                    
                    # curr_lock is passed to further (locked) nodes
                    curr_lock = t
                    # save the node number who makes the lock
                    lock = (len(tree)+1)
                    log_msg(1, 'walk_tree('+t+'): node '+str(lock)+' locked: '+dir+'!')

    # append leaf directory to tree
    tree.append( curr_dir )
    
    # get current directory contents
    names = os.listdir(dir);
    for name in names:
        path = os.path.join(dir, name)
        # go down the directory tree
        if os.path.isdir(path):
            walk_tree(path, tree, lock, curr_lock)
        # check files for RE's
        elif lock:
            # libraries
            if curr_lock == 'l':
                for i in 'sa': # s=shared, a=static
                    if i in args['p'] and pass_re( i, path ):
                        add_file(i,path)
                            
            # bins & includes
            elif curr_lock in args['p'] and pass_re( curr_lock, path ):
                add_file(curr_lock,path)
    
    # the node that makes the lock also has to remove it
    if len(tree) == lock:
        log_msg(1, 'walk_tree('+t+')-: node '+str(lock)+' released lock! (exit)')
        lock = 0
        curr_lock = 'n'
    else:
        log_msg(1, 'walk_tree('+curr_lock+')-: '+dir+' (exit)')
    # remove leaf directory from the tree (after processing has been done)
    tree.pop()

#=============================================================================

# program called with no arguments
if( len(sys.argv) == 1 ):
    printUsage(os.path.basename(sys.argv[0]))

# extract path from sys.argv
rel_path = sys.argv[1]
if rel_path.endswith('/'): rel_path=rel_path[:-1]

# check if path exists and is a valid directory
if( not os.path.exists( rel_path )):
    abort( rel_path+' does not exist!!' )
if( not os.path.isdir( rel_path )):
    abort( rel_path+' is not a valid directory!!' )
    
# convert path to absolute path
rel_path = os.path.abspath(rel_path)

# split arguments by '-' instead of whitespaces
argl = str.join(' ', sys.argv).split(' -')
# shift command name and release path out of argument list
argl = argl[1:]
# remove empty elements
argl = [ i for i in argl if i ]

# dictionary for storing command line options
args={}

# parse the arguments
for arg in argl:
    if not arg[0] in valid_opts:
        abort( 'Invalid Option [-'+arg[0]+']!!' )
    args[arg[0]] = arg[1:].strip()

# types to search for
if( args.has_key( 'p' )):
    for i in args['p']:
        if not i in 'LIBbas':
            abort( 'invalid option -p'+i )
else:
    args['p'] = 'bs'

# verbosity level
if( args.has_key( 'v' )):
    args['v'] = int(args['v'])
    if args['v'] < 0 or args['v'] > 4:
        abort( 'invalid option -v'+args['v'] )
else:
    args['v'] = int(3)

# check list of strings to exclude
if( args.has_key( 'e' )):
    args['e'] = args['e'].split(':')
    # remove empty elements
    args['e'] = [ i for i in args['e'] if i ]
else:
    args['e'] = def_exclude

# additionally include
if( args.has_key( 'i' )):
    args['i'] = args['i'].split(';')
    # remove empty elements
    args['i'] = [ i for i in args['i'] if i ]
    args['i'] = [ i.strip() for i in args['i'] ]

    for i in args['i']:
        type = i[0]
        if not files.has_key(type):
            abort( 'invalid option -i: Invalid type \''+type+'\' in '+i )
        v = i[1:].strip().split(':')
        for j in v:
            if( os.path.exists( j )):
                add_file( type, j, False )
            else:
                abort( 'invalid option -i: '+j+' FILE OR DIR NOT FOUND!' )

# output dir
if( args.has_key( 'o' )):
    copy_stuff=True

    # default name for dir
    args['o']=args['o'].strip()
    if args['o']=='':
        args['o']=os.path.basename(rel_path)
else:
    # default name for dir
    args['o']=os.path.basename(rel_path)
    copy_stuff=False

# create tarball
if( args.has_key( 'z' )):
    # if option -z is given and tarball already exists abort
    if os.path.exists( args['o']+'.tar.gz' ):
        abort( args['o']+'.tar.gz already exists in your current directory.'\
                + ' Please remove it first or use option -o with a different name!' )

    # if only option -z is given and dir doesn't exist force copy to True
    if not os.path.exists( args['o'] ):
        copy_stuff=True

# check if dir already exists
if os.path.exists( args['o'] ):
    copy_stuff=False
    if not args.has_key( 'z' ):
        log_msg(3, 80*'*'+'\n\n WARNING: '+args['o'] +' already exists in your current directory!!'\
            + '\n\t  To pack it in a tarball add option -z to your command line!'\
            + '\n\t  To make a new search erase it or use option -o with a different name!\n\n'+80*'*' )
else:
    # do it!
    walk_tree(rel_path)

# remove duplicated files
for k,v in dup_files.iteritems():
    for i,j in v.iteritems():
        m = len(j)
        if m > 1:
            log_msg(3, 'Warning: '+i+' found duplicated!!')
            while m > 1:
                f=dup_files[k][i].pop()
                files[k].remove(f)
                log_msg(3, f+' - Removed!')
                m = len(dup_files[k][i])
            log_msg(3, j[0]+' - Kept!')

# copy stuff
if( copy_stuff ):
    log_msg(3, 'copying files to '+args['o']+'...')
    
    # create dir
    os.makedirs( args['o'] )

    # copy dependencies folder
    deps_folder=rel_path+'/.dependencies'
    if os.path.exists( deps_folder ):
        cmd = 'cp -af %s %s' % (deps_folder, args['o'])

        log_msg(1, 'executing: '+cmd)
        log_msg(3, 'copying: [DEPENDENCIES] '+deps_folder)
        if os.system( cmd ) != 0:
            abort('failed executing: '+cmd)

   
    # copy files
    for k,v in files.iteritems():

        # create bin, lib or include dirs (if necessary)
        if k.islower() and len(v) > 0:
            subdir=os.path.join( args['o'], opt['lock_dirs'][k][0] )
            if not os.path.exists( subdir ):
                os.makedirs( subdir )
        # copy
        for i in v:
            if k.islower():
                cmd = 'cp -af '+i+' '+subdir
            else:
                cmd = 'cp -af '+i+' '+args['o']
            
            log_msg(1, 'executing: '+cmd)
            log_msg(3, 'copying: ['+k+'] '+i)
            if os.system( cmd ) != 0:
                abort('failed executing: '+cmd)


# testing
if( args.has_key( 't' )):
    if not os.path.exists( args['o'] ):
        abort( 'invalid option -t: No files were copied yet!' )

    # set LD_LIBRARY_PATH for testing
    # FIXME LD_PRELOAD
    os.environ['LD_LIBRARY_PATH']=os.path.abspath(args['o'])+'/lib:'+os.getenv( 'LD_LIBRARY_PATH', "" )

    log_msg( 3, 'LD_LIBRARY_PATH: '+os.getenv( 'LD_LIBRARY_PATH', "" ))
    for file in GlobDirectoryWalker( os.path.join(args['o'],'lib'), 's'):
        pass
    for file in GlobDirectoryWalker( os.path.join(args['o'],'bin'), 'b'):
        pass

# create tar-ball
if( args.has_key( 'z' )):
    cmd = 'tar czf '+args['o']+'.tar.gz '+args['o']
    log_msg(3, 'creating tar-ball '+args['o']+'.tar.gz ...')
    log_msg(1, 'executing: '+cmd)
    out=commands.getstatusoutput( cmd )
    if( out[0] != 0 ):
        print os.linesep+out[1]+os.linesep
        abort( 'creating '+args['o']+'.tar.gz' )
    else:
        log_msg(3, 'removing directory '+args['o']+'...')
        cmd='rm -rf '+args['o']
        log_msg(1, 'executing: '+cmd)
        os.system( cmd )

