##################################################
#
# Base class for ILC Software modules
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from util import *

import logging

log = logging.getLogger('ilcinstall')
log.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
#ch.setLevel(logging.DEBUG)
#
## bind the console handler to the root logger
##logging.getLogger().addHandler(ch)
#
## bind the console handler to the logger
log.addHandler(ch)


class BaseILC:
    """ Base class for ILC Software modules. """

    ilcHome = '/afs/desy.de/group/it/ilcsoft/'
    os_ver = OSDetect()

    # shared libraries extension
    if os_ver.type == "Darwin":
        shlib_ext=".dylib"
    else:
        shlib_ext=".so"

    def __init__(self, userInput, name, alias):
        self.patchPath = ""
        self.__userInput = userInput
        self.name = name                        # module name (e.g. LCIO, GEAR, Marlin, CEDViewer)
        self.alias = alias                      # module alias (e.g. lcio, gear, Marlin, CEDViewer)
        self.installSupport = True              # flag for install support
        self.download = Download(self)          # download struct ( groups together a bunch of download variables )
        self.hasCMakeBuildSupport = True        # can the package be built with cmake?
        self.hasCMakeFindSupport = True         # if yes PKG_HOME variable is set and package can be used in BUILD_WITH
        self.makeTests = False                  # flag for calling "make test" after building the software
        self.rebuild = False                    # flag for calling a "make clean" before building the software
        self.skipCompile = False                # flag for skipping the compile step of a module
        self.useLink = False                    # flag for "link" packages
        self.parent = None                      # parent class (this should be set to the ilcsoft object)
        self.reqfiles = []                      # list of required files to "use" this package (libraries, binaries, etc.)
        self.optmodules = []                    # optional modules (this package will try to build itself with this modules)
        self.reqmodules = []                    # required modules for building or using the libraries of this package
        self.reqmodules_external = []           # required modules for only building the package (their versions do not
                                                # affect the consistency of the package e.g. QT, CMake, Java in some cases..)
        self.reqmodules_buildonly = []          # required modules for only building this package (their environment variables
                                                # will only be written in the build_env.sh of this package
        self.envcmake = {}                      # cmake environment (e.g. BUILD_SHARED_LIBS=ON)
        self.envorder = []                      # use for environment variables that have priority
        self.env = {}                           # environment variables
        self.envcmds = []                       # cmds added to the environment script (build_env.sh)
        self.envpath = {                        # path environment variables (e.g. PATH, LD_LIBRARY_PATH, CLASSPATH)
            "PATH" : [],
            "LD_LIBRARY_PATH" : [],
            "CLASSPATH" : [],
            "LD_RUN_PATH" : [],
            "DT_RUN_PATH" : [],
            "MARLIN_DLL" : []
        }

        if self.os_ver.type == "Darwin":
            self.download.cmd="curl"
    
    def __repr__(self):
        if( self.mode == "install" ):
            print "\n\t+ " + self.name + ":",
            print "version [ " + self.version + " ]"
            if( not os.path.exists(self.installPath) ):
                print "\t   + will be installed to: [ " + self.installPath + " ]"
                print "\t   + download sources with [ " + self.download.type + " ] from:"
                print self.download
            if( self.downloadOnly ):
                print "\t   + download only: True"
            else:
                mods = self.reqmodules + self.optmodules + self.reqmodules_buildonly
                if( len(mods) > 0 ):
                    print "\t   + will be built with:",
                    for modname in mods:
                        print "[" + modname + "]",
                if( (len(self.reqmodules) > 0) or (len(self.reqmodules_buildonly) > 0) or (len(self.reqmodules_external) > 0)):
                    print "\n\t   + following modules are required:",
                    reqmods = self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external
                    for modname in reqmods:
                        print "[" + modname + "]",
                    print

        if( self.mode == "use" ):
            print "   + [ " + self.installPath + " ]",
            if self.useLink:
                print " -> [ "+ self.realPath() + " ]",
            print

        return str("")

    def abort(self, msg):
        """ used to abort the installation.
            displays the module name and the given message """

        print
        print "*** ERROR in module [ " + self.name + " ]: DEBUG INFO: " + str(self.parent.debugInfo)
        print
        print "*** ERROR in module [ " + self.name + " ]: " + msg

        if ("logfile" in dir(self)):
            print
            print "Logfile for failed module: " + self.logfile

        # write error to logfile
        try:
            getoutput( "echo \"*** Error in module [ " + self.name + " ]: DEBUG INFO: " + str(self.parent.debugInfo).replace("\n","") + "\" >> " + self.logfile )
            getoutput( "echo \"*** Error in module [ " + self.name + " ]: " + str(msg).replace("\n","") + "\" >> " + self.logfile )
        except:
            pass
        sys.exit(1)

#    def exe_cmd(self, cmd, abort=True):
#        log.debug( 'run cmd: ' + cmd )
#        r = getstatusoutput( cmd )
#
#        log.debug( 'cmd output: \n%s' % r[1] )
#        log.debug( 'cmd exit status: %s' % r[0] )
#
#        if r[0] != 0 and abort:
#            raise Exception( "failed to execute cmd: "+ cmd )
#
#        return r

    def userInput(self):
        return self.__userInput

    def autoDetect(self):
        """ auto detect module """

        self.autoDetected = False
        
        # auto detect settings
        self.installPath = self.autoDetectPath()
        if self.installPath:
            self.version = self.autoDetectVersion()
            if self.version:
                check = self.checkInstall()
                if check:
                    self.autoDetected=True

    def setMode(self, mode):
        """ sets this module to be used as an already existing
            version or to be installed from scratch.
            this method is also a good place to initialize variables
            that dependend on the installation mode and need a
            default value before the init method is called (e.g. 
            if you need a default download.url based on the module
            version and still want the user to be able to define a
            download.url in the config file :) """

        # initialize download only flag 
        self.downloadOnly = self.parent.downloadOnly

        # initialize download type flag
        if( self.parent.downloadType != "" ):
            self.download.type = self.parent.downloadType

        # initialize download username
        if( self.parent.downloadUser != "" ):
            self.download.username = self.parent.downloadUser

        # initialize download password 
        if( self.parent.downloadPass != "" ):
            self.download.password = self.parent.downloadPass

        # initialize cleanInstall flag
        self.cleanInstall = self.parent.cleanInstall
        
        self.rebuild = self.parent.rebuild

        self.envcmake.update(self.parent.envcmake)
        self.makeTests = self.parent.makeTests

        if( mode == "install" ):

            if( not self.installSupport ):
                self.abort( "Sorry, it is not possible to install " \
                        + self.name + " with this installation script!!" )

            # software version
            self.version = self.__userInput

            # name of the tarball for wget downloads
            self.download.tarball = self.alias + "_" + self.version + ".tgz"
            
            # install path
            self.installPath = self.parent.installPath + "/" + self.alias + "/" + self.version
        
        elif( mode == "link" ):
            
            # set link flag to true
            self.useLink = True

            # linkPath
            if( len( self.patchPath ) > 0 ):
                self.linkPath = fixPath( self.patchPath + "/" + self.alias + "/" + self.__userInput )
            else:
                self.linkPath = fixPath( self.__userInput )
            
            # check if installation where the link points to is ok 
            self.checkInstall(True)
            
            # extract version from Path
            self.version = basename( self.linkPath )
        
            # now override installPath
            newPath = self.parent.installPath + "/" + self.alias + "/" + self.version
            self.installPath = fixPath( newPath )

            mode = "use"
            
        elif( mode == "use" ):
            if( self.__userInput != "auto" ):
                # 1st case: full path to installation is given
                self.installPath = fixPath(self.__userInput)
                # extract version from path
                self.version = basename( self.installPath )
                # 2nd case: use( Mod( "vXX-XX" ) is given
                if( not self.checkInstall() ):
                    self.version = self.__userInput
                    self.installPath = self.parent.installPath + "/" + self.alias + "/" + self.version
                    # 1st and 2nd cases failed:
                    if( not self.checkInstall() ):
                        print 'failed to find', self.name, 'in', self.installPath
                        # revert installPath back to user input
                        self.installPath = fixPath(self.__userInput)
                        self.version = basename( self.installPath )

            # check if installed version is functional, abort otherwise
            self.checkInstall(True)

        self.buildPath = self.installPath + '/build'

        self.mode = mode

    def realPath(self):
        """ returns the path where the module is actually living.
            if module is in link mode the linkPath is returned
            else the installPath is returned """
        
        return (self.useLink and [self.linkPath] or [self.installPath])[0]

    def init(self):
        """ this method is called right after reading the configuration file and
            before dependencies are checked """

        # init logfile
        self.logfile = self.parent.logfile
            
        if( self.mode == "install" ):
            # initialize download data
            if( not self.download.supportHEAD and self.version == "HEAD" ):
                self.abort( "sorry, HEAD version of this package cannot be installed!! " \
                        + "Please choose a release version..." )
            if( not self.download.type in self.download.supportedTypes ):
                #if len(self.download.supportedTypes) != 1:
                #    print "*** WARNING: "+self.name+" download.type forced from \'"+self.download.type \
                #            + "\' to \'" + self.download.supportedTypes[0] + "\'"
                self.download.type=self.download.supportedTypes[0]
            if( self.download.type == "cvs" or self.download.type == "ccvssh" ):
                if( not isinPath("cvs") ):
                    self.abort( "cvs not found!!" )
                if( self.download.type == "cvs" ):
                    self.download.accessmode = "pserver"
                if( self.download.type == "ccvssh" ):
                    if( not isinPath("ccvssh") ):
                        self.abort( "ccvssh not found!!" )
                    self.download.env.setdefault('CVS_RSH', 'ccvssh')
                    self.download.accessmode = "ext"

                # if CVSROOT not set by user generate a default one
                self.download.env.setdefault('CVSROOT', ":" + self.download.accessmode + ":" \
                        + self.download.username + ":" + self.download.password \
                        + "@" + self.download.server + ":/" + self.download.root )

            elif( self.download.type == "wget" ):
                if( not isinPath(self.download.cmd) ):
                    self.abort( self.download.cmd + " not found on your system!!" )
                if( not isinPath("tar") ):
                    self.abort( "tar not found on your system!!" )

                # if download url not set by user generate a default one
                if( len(self.download.url) == 0 ):
                    if Version( self.version ) == 'HEAD':
                        dir='trunk'
                    elif '-pre' in self.version or '-dev' in self.version or '-exp' in self.version:
                        dir='branches/%s' % self.version
                    else:
                        dir='tags/%s' % self.version
                        
                    self.download.url = "http://svnsrv.desy.de/viewvc/%s/%s/%s?view=tar" % ( self.download.root, self.download.project, dir )

            elif ( self.download.type[:3] == "svn" ):
                if( not isinPath("svn") ):
                    self.abort( "svn not found on your system!!" )

                # if svnurl not set by user generate a default one
                if( len(self.download.svnurl) == 0 ):
                    # initialize svn settings for desy
                    self.download.accessmode = "https"
                    self.download.server = "svnsrv.desy.de"
                    #if( self.download.username == "anonymous" ):
                    #    self.download.root = "public/" + self.download.root
                    if( self.download.type == 'svn-desy' ):
                        self.download.root = "desy/" + self.download.root
                    elif( self.download.type == 'svn-p12cert' ):
                        self.download.root = "svn/" + self.download.root
                    else:
                        self.download.root = "public/" + self.download.root

                    self.download.svnurl = "%s://%s/%s/%s/" % (self.download.accessmode,self.download.server,self.download.root,self.download.project)

                    if Version( self.version ) == 'HEAD': 
                        self.download.svnurl += 'trunk'
                    elif '-pre' in self.version or '-dev' in self.version or '-exp' in self.version:
                        self.download.svnurl += 'branches/'+self.version
                    else:
                        self.download.svnurl += 'tags/'+self.version
            # git access to repository
            elif ( self.download.type[:3] == "git" ):
                if( not isinPath("git") ):
                    self.abort( "git not found on your system!!" )

                # if svnurl not set by user generate a default one
                if( len(self.download.svnurl) == 0 ):
                    # initialize svn settings for github
                    self.download.accessmode = "https"
                    self.download.server = "github.com"
                    self.download.root = self.download.project
                    self.download.svnurl = "%s://%s/%s/%s/" % (self.download.accessmode,self.download.server,self.download.root,self.download.project)
            else:
                self.abort( "download type " + self.download.type + " not recognized!!" )

    def checkInstallConsistency(self):
        """ check installation consistency """
        # switch to use mode if already installed
        if( self.mode == "install" and os.path.exists( self.installPath )):
            if( os.path.exists( self.installPath + "/.install_failed.tmp" )):
                self.rebuild = True
                print "   + [%s] %s installation status: failed - set to rebuild" % \
                    (self.installPath, (55-len(self.installPath))*' ')
            elif( not self.checkInstall() ):
                print "   + [%s] %s installation status: incomplete" % \
                    (self.installPath, (55-len(self.installPath))*' ')
            elif( self.rebuild ):
                print "   + [%s] %s installation status: OK - rebuild flag set to true" % \
                    (self.installPath, (55-len(self.installPath))*' ')
            else:
                print "   + [%s] %s installation status: OK - set to use mode" % \
                    (self.installPath, (55-len(self.installPath))*' ')
                #print "   + %-55s installation status: OK - set to use mode" % \
                #    ('['+self.installPath+']',)
                self.mode = "use"

    def preCheckDeps(self):
        """ called before running dependency check
            useful for adding or removing dependencies based on
            environment variables or some other setting """
        
        # add cmake dependency
        if( self.mode == "install" and self.hasCMakeBuildSupport ):
            self.addExternalDependency( ["CMake" ] )
            if self.name != "LCIO":
                self.addExternalDependency( ["ILCUTIL" ] )


    def postCheckDeps(self):
        """ called after running dependency check
            useful for checking version incompatibilities
            or setting environment variables
            also usefull for testing things that depend on
            the install modus, since this can change in the
            checkDeps phase """
        if( self.mode == "install" ):

            # check for make
            if( not isinPath( "make" )):
                self.abort( "make not found on your system!!" )

            # check for tee
            if( not isinPath( "tee" )):
                self.abort( "tee not found on your system!!" )

    def checkOptionalDependencies(self):
        """ check dependencies for the installation
            this is called right after the init method """
    
        # skip dependency check for downloading only
        if( self.downloadOnly ):
            return

        # soft dependencies
        failed = []
        for opt in self.optmodules:
            mod = self.parent.module(opt)
            if( mod == None ):
                failed.append(opt)
        
        # remove soft dependencies that were not found
        self.buildWithout(failed)

    def checkRequiredDependencies(self):
        """ check for required dependencies """
    
        # skip dependency check for downloading only
        if( self.downloadOnly ):
            return

        # hard dependencies
        for req in self.reqmodules:
            if( self.parent.module(req) == None ):
                # check if there is an auto detected module
                if( self.parent.module(req, True) == None ):
                        self.abort( self.name + " requires " + req \
                                + " and it wasn't found in your config file!!" )
                else:
                    # use auto detected module
                    self.parent.use( self.parent.module(req, True) )
                    self.parent.module( req ).init()

                    print self.name + ": auto-detected " + req + " version " + self.parent.module( req ).version
        
        # build only dependencies
        if( self.mode == "install" ):
            mods = self.reqmodules_buildonly + self.reqmodules_external
            for req in mods:
                if( self.parent.module(req) == None ):
                    # check if there is an auto detected module
                    if( self.parent.module(req, True) == None ):
                        self.abort( req + " not found in your config file!! " + self.name \
                                + " cannot be built without " + req )
                    else:
                        # use auto detected module
                        self.parent.use( self.parent.module(req, True) )
                        self.parent.module( req ).init()

                        print "   - " + self.name + ": auto-detected " + req + " version " + self.parent.module( req ).version

    def checkDeps( self ):
        """ check if a package needs to be rebuilt by checking the 
            versions of the dependencies used in the build process
            against the versions defined in the configuration file
            - returns True if test succeeds
            - returns False if test fails """

        # skip dependency check for downloading only
        if( self.downloadOnly ):
            return True

        # skip dependency check if package is going to be installed
        if( self.mode == "install" ):
            return True

        log.debug( 'Checking dependencies of %s', self.name )
        
        file = self.realPath() + "/.dependencies"
        
        r = True

        # if file doesn't exist return True
        if( not os.path.exists( file )):
            return True

        # open dependencies file
        f = open( file )
        filedeplist = {}
        for line in f.readlines():
            line = line.strip()
            if( (not line.startswith(os.linesep)) and (not line.startswith("#")) \
                    and (len(line) > 0 )):
                tokens = line.split(":")
                filedeplist[ tokens[0] ] = tokens[1]
        f.close()

        log.debug( 'Dependencies read from file: %s', filedeplist )

        # get actual dependecies
        deplist={}
        self.getDepList(deplist)
        del deplist[self.name]

        log.debug( 'Dependencies found in current cfg file: %s', deplist )
        
        # compare dependencies
        for k, v in filedeplist.iteritems():
            if( deplist.has_key( k )):
                if( deplist[k] != v ):
                    if( os.path.basename(deplist[k]) != os.path.basename(v) ):
                        if( r ):
                            print "*** WARNING: ***\n***\tFollowing dependencies from " + self.name + " located at [ "  \
                                    + self.realPath() + " ] failed:\n***"
                        print "***\t * " + k + " " + os.path.basename(v) + " differs from version " \
                                + os.path.basename(deplist[k]) + " defined in your config file.."
                        r = False
            else:
                if( r ): #just print this once
                    print "*** WARNING: ***\n***\tFollowing dependencies from " + self.name + " located at [ "  + self.realPath() \
                            + " ] failed:\n***"
                print "***\t * " + k + " not found in your config file!!"
                r = False
                

        if( not r ):
            print "***"
            if( self.useLink ):
                print "***\t" + self.name + " is in \"link\" mode, if you want to rebuild it with the new dependencies set it to \"use\" mode..."
                r = True
            else:
                if( not self.parent.noAutomaticRebuilds ):
                    print "***\t * " + self.name + " changed to \"install\" mode and rebuild flag set to True..."
                    self.mode = "install"
                    self.rebuild = True
                    self.preCheckDeps()
                    print "***\n***\tUpdating dependency tree ( modules that depend on " + self.name + " need also to be rebuilt )...\n***"
                    self.updateDepTree([])
                    print "***\n***\tif you do NOT want to rebuild this module(s) just answer \"no\" later on in the installation process,\n" \
                            + "***\tor set the global flag ilcsoft.noAutomaticRebuilds=True in your config file..."
                else:
                    print "***\n***\tglobal flag ilcsoft.noAutomaticRebuilds is set to True, nothing will be done...\n***"
        return r

    def getDepList(self, dict):
        """ helper function for getting a list of the dependencies
            and their installPath for this module """
        
        if( dict.has_key( self.name) ):
            return
        else:
            dict[ self.name ] = self.installPath

        if( len( dict ) > 1 ):
            mods = self.reqmodules + self.optmodules
        else:
            mods = self.reqmodules + self.optmodules + self.reqmodules_buildonly
        
        for modname in mods:
            if( self.parent.module(modname) != None ):
                self.parent.module(modname).getDepList( dict )

    def updateDepTree(self,checked):
        """ updates the package dependency tree to ensure that every package
            gets updated if one or more dependencies changes """

        if( self.name in checked ):
            return
        else:
            checked.append(self.name)

        for mod in self.parent.modules:
            if( mod.name != self.name ):
                mods = mod.reqmodules + mod.optmodules + mod.reqmodules_buildonly
                if( self.name in mods ):
                    if( mod.mode != "install" or not mod.rebuild ):
                    #if( mod.mode != "install" and not mod.rebuild ):
                        if( mod.useLink ):
                            print "***\t * WARNING: " + mod.name + " is in \"link\" mode, " \
                                    + "if you want to rebuild it with the new dependencies set it to \"use\" mode...!!"
                        else:
                            if( not self.parent.noAutomaticRebuilds ):
                                if( mod.mode != "install" ):
                                    print "***\t * " + mod.name + " changed to \"install\" mode and rebuild Flag set to true!!"
                                    mod.mode = "install"
                                    mod.rebuild = True
                                    mod.preCheckDeps()
                                    mod.updateDepTree(checked)

    def confirmRebuild( self ):
        """ confirms rebuild of module """
        if( self.mode == "install" and self.rebuild ):
            input = ask_ok( self.name + " at [ " + self.installPath + " ] is going to be rebuild, are you sure? [y/n] " )
            if( not input ):
                self.mode = "use"
                self.rebuild = False

    def checkInstall(self, abort=False):
        """ check if everything is ok for using this package (libraries, binaries, etc.).
            If abort flag is set to True the installation aborts if a test fails.
            - returns True if all tests succeed
            - returns False if a test fails """
        
        for i in self.reqfiles:
            found = False
            files = []
            for j in i:
                if( os.path.exists( self.realPath() + "/" + j )):
                    found = True
                else:
                    files.append( self.realPath() + "/" + j )
            if( not found ):
                if( abort ):
                    if( len( files ) > 1 ):
                        self.abort( "At least one of these files: " + str(files) + "\n" \
                                + "is required for using this installation of " + self.name )
                    else:
                        self.abort( "Required file not found: " + str(files) )
                return False
        return True
    

    def updateSources(self):
        """ update sources """
        
        if Version( self.version ) == 'HEAD':

            if 'svn' in self.download.type and not 'export' in self.download.type:


                cmd = "svn update %s" % self.installPath
                print cmd

                if( os.system( cmd ) != 0 ):
                    self.abort( "error updating sources" )
            elif 'git' in self.download.type:
                cmd = "cd %s && git pull origin && cd -" % self.installPath
                print cmd

                if( os.system( cmd ) != 0 ):
                    self.abort( "error updating sources" )


    def downloadSources(self):
        """ download sources """
        
        # create install base directory
        trymakedir( os.path.dirname( self.installPath ))
    
        os.chdir( os.path.dirname(self.installPath) )

        if( self.download.type == "cvs" or self.download.type == "ccvssh" ):

            # set env
            for k, v in self.download.env.iteritems():
                os.environ[k] = v

            cvsroot=os.environ["CVSROOT"]

            # CVSROOT with pass example:
            # :ext:engels:****@cvssrv.ifh.de:/ilctools
            # CVSROOT without pass example:
            # :ext:engels@cvssrv.ifh.de:/ilctools
            # entries in ~/.cvspass
            # :pserver:engels@cvssrv.ifh.de:2405/ilctools 

            i1 = cvsroot.find("@")

            # check if there is a password coded in $CVSROOT
            if( cvsroot.count(":",0,i1) == 3 ):
                i2=cvsroot.rfind(':',0,i1)
                cvsroot_nopass = cvsroot[:i2]+cvsroot[i1:]
            # use default
            else:
                cvsroot_nopass = cvsroot

            # dirty hack (but works ;)
            i2=cvsroot_nopass.rfind(':',0,i1)
            i4=cvsroot_nopass.rfind(':')+1

            if( os.system( 'grep "'+cvsroot_nopass[i2:i4]+'[0-9]*'+cvsroot_nopass[i4:]+'" ~/.cvspass &>/dev/null' ) != 0 ):
                print "logging in to cvs server..."
                if( os.system( self.download.type + " login" ) != 0 ):
                    self.abort( "Problems ocurred downloading sources ("+self.download.type+" login)!!")
            else:
                print "password found in ~/.cvspass, will skip login..."

            os.environ["CVSROOT"] = cvsroot_nopass

            # checkout sources
            print "checking out sources..."
            if( self.version == "HEAD" ):
                if( os.system( "cvs co -d " + self.version + " " + self.download.project ) != 0 ):
                    self.abort( "Problems ocurred downloading sources with "+self.download.type+"!!")
            else:
                if( os.system( "cvs co -d " + self.version + " -r " + self.version + " " + self.download.project ) != 0 ):
                    self.abort( "Problems ocurred downloading sources with "+self.download.type+"!!")
        
        elif( self.download.type[:3] == "svn" ):

            if( self.download.type == "svn-export" ):
                svncmd = "svn export"
            else:
                svncmd = "svn checkout"

            if( self.version == "HEAD" ):
                cmd="%s %s HEAD" % (svncmd, self.download.svnurl)
            else:
                cmd="%s %s %s" % (svncmd, self.download.svnurl, self.version)

            print "svn download cmd:",cmd
            if( os.system( cmd ) != 0 ):
                self.abort( "Problems ocurred downloading sources with "+self.download.type+"!!")

        elif( self.download.type[:3] == "git" ):

            # defaults to clone
            gitcmd = "git clone"
            cmd="%s %s %s" % (gitcmd, self.download.svnurl, self.version)

            print "git download cmd:",cmd
            if( os.system( cmd ) != 0 ):
                self.abort( "Problems ocurred downloading sources with "+self.download.type+"!!")

        elif( self.download.type == "wget" ):

            # name of the tarball file
            self.download.tarball = self.download.project + "_" + self.version + ".tgz"

            if self.download.cmd == "wget":
                dopt='O'
            else:
                dopt='o'

            if( os.system( '%s "%s" -%s %s' % (self.download.cmd, self.download.url, dopt, self.download.tarball) ) != 0 ):
                self.abort( "Problems ocurred downloading sources!!")

            if( not os.path.exists( "./" + self.download.tarball) ):
                self.abort( "Problems ocurred downloading sources!!")
                
            # find out directory inside tarball
            os.system("tar -tzf " + self.download.tarball + " > tarlist.tmp")
            self.download.tardir = getoutput( "head -n1 tarlist.tmp" ).strip()
            os.unlink( "tarlist.tmp" )
            
            # extract the root directory from the directory tree
            if( self.download.tardir.find('/') != -1 ):
                self.download.tardir = self.download.tardir[:self.download.tardir.find('/')]

            # unpack tarball
            print "+ Unpacking " + self.download.tarball
            os.system( "tar -xzvf " + self.download.tarball )
            
            tryrename( self.download.tardir, self.version )

        if( self.hasCMakeBuildSupport and not self.skipCompile ):
            trymakedir( self.version + "/build" )

    def cleanupInstall(self):
        """ clean up temporary files used for the installation """

        os.chdir( os.path.dirname(self.installPath) )
        tryunlink( self.download.tarball )
    
    def createLink(self):
        """ if package is to be linked only """
    
        if( self.useLink ):
            trymakedir( self.parent.installPath + "/" + self.alias )

            os.chdir( self.parent.installPath + "/" + self.alias )
            
            # check for already existing symlinks or dirs 
            if( os.path.islink( self.version )):
                os.unlink( self.version )
            elif( os.path.isdir( self.version )):
                self.abort( "could not create link to [ " + self.linkPath + " ]\nin [ " \
                        + os.path.basename( self.installPath ) + " ]!!!" )

            os.symlink( self.linkPath , self.version )
            print "+ Linking " + self.parent.installPath + "/" + self.alias + "/" + self.version \
                    + " -> " + self.linkPath

    def compile(self):
        """ method used for compiling module.
            does nothing in the base class """
        print "+ Nothing to be done ;)"

    def install(self, installed=[]):
        """ install this module """

        # install
        if( self.mode == "install" and not self.downloadOnly ):

            # resolve circular dependencies
            if( self.name in installed ):
                return
            else:
                installed.append( self.name )

            # install dependencies if there are any to be installed
            mods = self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external + self.optmodules
            for modname in mods:
                mod = self.parent.module(modname)
                mod.install(installed)
    
            print 80*'#' + "\n##### Compiling " + self.name + " version " + self.version + "...\n" + 80*'#'

            # create install directory if it hasn't already been created
            trymakedir( self.installPath )

            # write environment to file
            self.writeLocalEnv()

            # set environment
            self.setEnv(self, [])

            # write snapshot of environment to logfile for debugging
            os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
            os.system( "echo \"" + 10*'#' + " BUILDING " + self.name + "\" >> " + self.logfile )
            os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
            os.system( "echo \"" + 5*'-' + " ENVIRONMENT SNAPSHOT " + 5*'-' + "\" >> " + self.logfile )
            os.system( "env >> " + self.logfile )
            os.system( "echo \"" + 5*'-' + " END OF ENVIRONMENT SNAPSHOT " + 5*'-' + "\" >> " + self.logfile )
            os.system( "touch " + self.installPath + "/.install_failed.tmp" )

            # compile module
            if( not self.skipCompile ):
                if( self.hasCMakeBuildSupport ):
                    #self.setCMakeVars(self,[])
                    print "+ Generated cmake build command:"
                    print '  $ ', self.genCMakeCmd()
                    print os.linesep
                
                self.compile()

            os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
            os.system( "echo \"" + 10*'#' + " FINISHED BUILDING " + self.name + "\" >> " + self.logfile )
            os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
            
            # set the module to use mode
            self.mode = "use"

            # just to check if the library was created successfully
            self.checkInstall(True)
            os.unlink( self.installPath + "/.install_failed.tmp" )
            
            # write dependencies to file
            self.writeLocalDeps()
            
            if( self.cleanInstall ):
                self.cleanupInstall()
            
            # unset environment
            self.unsetEnv([])

    def previewinstall(self, installed=[]):
        """ preview installation of this module """

        if( self.mode == "install"):
            
            # resolve circular dependencies
            if( self.name in installed ):
                return
            else:
                installed.append( self.name )
        
            print "\n" + 20*'-' + " Starting " + self.name + " Installation Test " + 20*'-' + '\n'
            
            # additional modules
            mods = self.optmodules + self.reqmodules + self.reqmodules_external + self.reqmodules_buildonly
            if( len(mods) > 0 ):
                for modname in mods:
                    mod = self.parent.module(modname)
                    if( mod.mode == "install" and not mod.name in installed ):
                        print "+ " + self.name + " will launch installation of " + mod.name
                    mod.previewinstall(installed)
                    print "+ "+ self.name + " using " + mod.name + " at [ " + mod.installPath + " ]"

            print "\n+ Environment Settings used for building " + self.name + ":"
            # print environment settings recursively
            self.setEnv(self, [], True )

            if( self.hasCMakeBuildSupport ):
                #self.setCMakeVars(self, [])
                print "\n+ Generated CMake command for building " + self.name + ":"
                print '  $ ',self.genCMakeCmd()
            
            print "\n+ " + self.name + " installation finished."
            print '\n' + 20*'-' + " Finished " + self.name + " Installation Test " + 20*'-' + '\n'


    def cmakeBoolOptionIsSet(self, opt):
        """ checks if a cmake option is set """

        if self.envcmake.has_key( opt ):

            val = str(self.envcmake.get(opt,""))

            if val == "1" or val == "ON" or val == "YES":

                return True

        return False
        

    def genCMakeCmd(self):
        """ generates a CMake command out of envcmake """
        
        cmd = "cmake -C " + self.parent.env["ILCSOFT_CMAKE"] + " "
        for k, v in self.envcmake.iteritems():
            cmd = cmd + "-D" + k + "=\"" + str(v).strip() + "\" "

        cmd += self.installPath

        return cmd.strip()


    def setEnv(self, origin, checked, simOnly=False):
        """ sets the environment variables for this module """

        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        # set values to strings
        for k in self.env.keys():
            self.env[k]=str(self.env[k])
        
        # set environment variables
        if( simOnly ):
            if( len( checked ) == 1 ):
                if( len(self.parent.env) != 0 ):
                    print "\n   + Global Environment variables:"
                    for k, v in self.parent.env.iteritems():
                        print "\t* " + k + ": " + str(v)

            print "\n   + Environment variables set by " + self.name + ":"
            
            for k, v in self.env.iteritems():
                print "\t* " + k + ": " + str(v)
        else:
            # first set the priority values
            for k in self.envorder:
                if( self.env[k].find('$') != -1 ):
                    os.environ[k]=os.path.expandvars(self.env[k])
                else:
                    os.environ[k] = self.env[k]
            # then set the rest
            for k, v in self.env.iteritems():
                if k not in self.envorder:
                    if( v.find('$') != -1 ):
                        os.environ[k] = os.path.expandvars(v)
                    else:
                        os.environ[k] = v

        # print path and build environment variables
        if( simOnly ):
            for k, v in self.envpath.iteritems():
                if( len(v) != 0 ):
                    print "\t* " + k + ": " + str(v)

        # set environment for dependencies
        if( len( checked ) > 1 ):
            mods = self.optmodules + self.reqmodules
        else:
            # buildonly modules are only used for the package were they are needed
            mods = self.optmodules + self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external
        
        for modname in mods:
            self.parent.module(modname).setEnv(origin, checked, simOnly)

        # list of "trivial" paths we do not want to add again to PATH and co
        ignorepaths = ['/usr/bin','/usr/lib','/sbin','/usr/sbin']
        # set path environment variables
        for k, v in self.envpath.iteritems():
            if( len(v) != 0 ):
                env = getenv( k )
                newvalues = ""
                for i in v:
                    rpath = fixPath(i)
                    if rpath in ignorepaths:
                        continue
                    newvalues = newvalues + rpath + ':'
                os.environ[k] = newvalues + env

    def unsetEnv(self, checked):
        """ unsets the environment variables for this module """

        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        # delete environment variables
        for k, v in self.env.iteritems():
            trydelenv(k)

        # restore path variables (only need to do this at the root module, skip recursivity!)
        if( len( checked ) == 1 ):
            for k, v in self.parent.envpathbak.iteritems():
                os.environ[k] = v

        # delete environment for dependencies
        mods = self.optmodules + self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external
        for modname in mods:
            if( self.parent.module(modname) != None ):
                self.parent.module(modname).unsetEnv(checked)

    def writeLocalEnv(self):
        """ writes the environment used for building the package to a file (build_env.sh) """
            
        # open file
        f = open(self.installPath + "/build_env.sh", 'w')
        
        # write to file
        f.write( 80*'#' + os.linesep + "# Environment script generated by ilcsoft-install on " + time.ctime() + os.linesep )
        f.write( "# for " + self.name + " located at [ " + self.installPath + " ]" + os.linesep + 80*'#' + os.linesep )

        # global environment variables
        if( len( self.parent.env ) > 0 ):
            f.write( 2*os.linesep + "#" + 80*'-' + os.linesep + "#" + 5*' ' + "Global Environment Variables" + os.linesep \
                    + "#" + 80*'-' + os.linesep )
            for k, v in self.parent.env.iteritems():
                f.write( "export " + str(k) + "=\"" + str(v) + "\"" + os.linesep )
        

        # write environment recursively to file
        self.writeEnv(f, [])
        

        f.write( "# --- additional comands ------- " + os.linesep ) 
        print "\n   ----- adding additional commands to build_env.sh : \n "
        for c in self.envcmds:
            f.write( c + os.linesep ) 
            print "\n   ----- adding additional command to build_env.sh " + c + "\n"

        # close file
        f.close()
    
    def writeEnv(self, f, checked):
        """ helper function used for writing the environment to a file """
        
        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        if self.env or sum(map(len, self.envpath.values()), 0):
            f.write( 2*os.linesep + "#" + 80*'-' + os.linesep + "#" + 5*' ' \
                    + self.name + os.linesep + "#" + 80*'-' + os.linesep )
        
        # first write the priority values
        for k in self.envorder:
            f.write( "export " + str(k) + "=\"" + str(self.env[k]) + "\"" + os.linesep )
        # then write the rest
        for k, v in self.env.iteritems():
            if k not in self.envorder:
                f.write( "export " + str(k) + "=\"" + str(self.env[k]) + "\"" + os.linesep )

        # list of "trivial" paths we do not want to add again to PATH and co
        ignorepaths = ['/usr/bin','/usr/lib','/sbin','/usr/sbin']
        # path environment variables
        for k, v in self.envpath.iteritems():
            if( len(v) != 0 ):
                # expand every variable we introduced previously
                exp = str().join(v)
                for e, ev in self.env.iteritems():
                    p = re.compile(r"\$"+str(e)) # compile regular expression to match shell variable
                    exp = p.sub(str(ev), exp)  # replace with expanded variable for absolute path
                # check for match
                if exp in ignorepaths:
                    continue
                path = str.join(':', v)
                path = path + ':'
                f.write( "export " + k + "=\"" + path + "$" + k + "\"" + os.linesep )

        if( len(checked) > 1 ):
            mods = self.optmodules + self.reqmodules
        else:
            # buildonly modules are only written for the package were they are needed
            mods = self.optmodules + self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external
        
        for modname in mods:
            self.parent.module(modname).writeEnv(f, checked)
    
    def writeLocalDeps(self):
        """ writes the dependencies + their installation paths 
            used for building this package into a file """
            
        # open file
        f = open(self.installPath + "/.dependencies", 'w')
        
        # write to file
        f.write( 80*'#' + os.linesep + "# Software dependencies generated by ilcsoft-install on " + time.ctime() + os.linesep )
        f.write( "# for " + self.name + " located at [ " + self.installPath + " ]" + os.linesep + 80*'#' + os.linesep )
    
        # write environment recursively to file
        self.writeDeps(f, [])
        
        # close file
        f.close()

    def writeDeps(self, f, checked):
        """ helper function for writing paths of dependencies
            used for building this module into a file """
        
        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        if( len( checked ) > 1 ):
            f.write( self.name + ":" + self.installPath + os.linesep )
            mods = self.optmodules + self.reqmodules
        else:
            mods = self.optmodules + self.reqmodules + self.reqmodules_buildonly

        for modname in mods:
            self.parent.module(modname).writeDeps(f, checked)

    def buildWith(self, mods):
        """ use this to build the software with the extra modules
            defined in the mods list (e.g. to build LCIO with CLHEP) """
        for modname in mods:
            if( (not modname in self.optmodules) and \
                (not modname in self.reqmodules) and \
                (not modname in self.reqmodules_buildonly) and \
                (not modname in self.reqmodules_external) and \
                self.name != modname ):
                self.optmodules.append(modname)
    
    def buildWithout(self, mods):
        """ use this if you want to remove some default modules that
            are set by default when building the software """
        for modname in mods:
            try:
                self.optmodules.remove(modname)
            except:
                print "\n*** WARNING: " + modname + " not found in the list of modules from " + self.name + "!!"
                print "please recheck your config file: names are case-sensitive!!"
    
    def addDependency(self, mods):
        """ use this to add a dependency to the module """
        for modname in mods:
            # if one adds a dependency that is found in optional modules
            # change it from optional to required
            if( modname in self.optmodules ):
                self.buildWithout([modname])

            if( (not modname in self.reqmodules) and \
                (not modname in self.reqmodules_buildonly) and \
                (not modname in self.reqmodules_external) and \
                self.name != modname ):
                self.reqmodules.append(modname)
    
    def remDependency(self, mods):
        """ use this to remove a dependency from the module """
        for mod in mods:
            try:
                self.reqmodules.remove(mod)
            except:
                print "\n*** WARNING: " + mod + " not found in the list of dependencies from " + self.name + "!!"
                print "please recheck your config file: names are case-sensitive!!"
    
    def addExternalDependency(self, mods):
        """ use this to add external dependencies to the module """
        for modname in mods:
            # if one adds a dependency that is found in optional modules
            # change it from optional to external
            if( modname in self.optmodules ):
                self.buildWithout([modname])

            # if one adds a dependency that is found in build only dependencies
            # change it from build only to external
            if( modname in self.reqmodules_buildonly ):
                self.remBuildOnlyDependency([modname])
            
            if( (not modname in self.reqmodules) and \
                (not modname in self.reqmodules_external) and \
                (not modname in self.reqmodules_buildonly) and \
                self.name != modname ):
                self.reqmodules_external.append(modname)
    
    def remExternalDependency(self, mods):
        """ use this to remove external dependencies from the module """
        for mod in mods:
            try:
                self.reqmodules_external.remove(mod)
            except:
                print "\n*** WARNING: " + mod + " not found in the list of external dependencies from " + self.name + "!!"
                print "please recheck your config file: names are case-sensitive!!"

    def addBuildOnlyDependency(self, mods):
        """ use this to add a "build only" dependency to the module """
        for modname in mods:
            # if one adds a dependency that is found in optional modules
            # change it from optional to required to build
            if( modname in self.optmodules ):
                self.buildWithout([modname])

            # if one adds a dependency that is found in external dependencies
            # change it from external to build only
            if( modname in self.reqmodules_external ):
                self.remExternalDependency([modname])
            
            if( (not modname in self.reqmodules) and \
                (not modname in self.reqmodules_external) and \
                (not modname in self.reqmodules_buildonly) and \
                self.name != modname ):
                self.reqmodules_buildonly.append(modname)

    def remBuildOnlyDependency(self, mods):
        """ use this to remove a "build only" dependency from the module """
        for mod in mods:
            try:
                self.reqmodules_buildonly.remove(mod)
            except:
                print "\n*** WARNING: " + mod + " not found in the list of build only dependencies from " + self.name + "!!"
                print "please recheck your config file: names are case-sensitive!!"
    

#--------------------------------------------------------------------------------

class Download:
    """ class responsible for the downloads """

    def __init__(self, parent):
        self.parent = parent                        # parent class responsible for this download
        self.project = parent.alias                 # project name
        self.root = str.lower(self.project)         # root
        self.username = "anonymous"                 # username
        self.password = ""                          # password
        self.server = "cvssrv.ifh.de"               # server
        self.accessmode = "ext"                     # server access mode
        self.url = ""                               # url for getting tarball with wget
        self.svnurl = ""                            # url for getting tarball with wget
        self.tarball = ""                           # name of the tarball used for wget downloads
        self.env = {}                               # environment (CVSROOT, CVS_RSH)
        self.type = "wget"                          # download type (wget, cvs, ccvssh)
        self.supportHEAD = True                     # support for downloading HEAD version
        self.supportedTypes = [ "wget", "svn", "svn-desy", "svn-p12cert", "svn-export", "git", "git-clone", "ccvssh" ]  # supported download types for the module
        self.url = {}
        self.cmd = "wget"

    def __repr__(self):
        if( self.type == "wget" ):
            return "\t\t+ URL [ " + self.url + " ]"
        elif ( self.type[:3] == "svn" ):
            return "\t\t+ SVN [ " + self.svnurl + " ]"
        elif ( self.type[:3] == "git" ):
            return "\t\t+ git [ " + self.svnurl + " ]"
        else:
            return "\t\t+ CVSROOT [ " + self.env["CVSROOT"] + " ]"



#--------------------------------------------------------------------------------

