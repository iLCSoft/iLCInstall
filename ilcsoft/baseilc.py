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

class BaseILC:
    """ Base class for ILC Software modules. """

    def __init__(self, userInput, name, alias):
        self.__userInput = userInput
        self.name = name                        # module name (e.g. LCIO, GEAR, Marlin, CEDViewer)
        self.alias = alias                      # module alias (e.g. lcio, gear, Marlin, CEDViewer)
        self.installSupport = True              # flag for install support
        self.download = Download(self)          # download struct ( groups together a bunch of download variables )
        self.hasCMakeSupport = True             # flag for cmake support
        self.isMarlinPKG = False                # flag for Marlin Packages
        self.rebuild = False                    # flag for calling a "make clean" before building the software
        self.skipCompile = False                # flag for skipping the compile step of a module
        self.useLink = False                    # flag for "link" packages
        self.parent = None                      # parent class (this should be set to the ilcsoft object)
        self.reqfiles = []                      # list of required files to "use" this package (libraries, binaries, etc.)
        self.cmakebuildmodules = []             # list of possible modules that this package can be built with (only for cmake)
        self.optmodules = []                    # optional modules (this package will try to build itself with this modules)
        self.reqmodules = []                    # required modules for building or using the libraries of this package
        self.reqmodules_external = []           # required modules for only building the package (their versions do not
                                                # affect the consistency of the package e.g. QT, CMake, Java in some cases..)
        self.reqmodules_buildonly = []          # required modules for only building this package (their environment variables
                                                # will only be written in the build_env.sh of this package
        self.envcmake = {}                      # cmake environment (e.g. BUILD_SHARED_LIBS=ON )
        self.env = {}                           # environment variables
        self.envpath = {                        # path environment variables (e.g. PATH, LD_LIBRARY_PATH, CLASSPATH)
            "PATH" : [],
            "LD_LIBRARY_PATH" : [],
            "CLASSPATH" : [],
            "MARLIN_DLL" : []
        }
        self.envbuild = {                       # build environment variables used to build Marlin (USERINCLUDES, USERLIBS)
            "USERINCLUDES" : [],
            "USERLIBS" : []
        }
        self.envoptbuild = {                    # build environment variables for MARLINWORKDIR
            "USERINCLUDES" : [],
            "USERLIBS" : []
        }
    
    def __repr__(self):
        if( self.mode == "install" ):
            print "\n\t+ " + self.name + ":",
            print "version [ " + self.version + " ]"
            if( not os.path.exists(self.installPath) ):
                print "\t   + will be installed to: [ " + self.installPath + " ]"
                print "\t   + download sources with [ " + self.download.type + " ] from:"
                if( self.download.type == "wget" ):
                    print "\t\t+ URL [ " + self.download.url + " ]"
                else:
                    print "\t\t+ CVSROOT [ " + self.download.env["CVSROOT"] + " ]"
                    if( self.download.password != "" ):
                        print "\t\t+ CVSPass [ " + self.download.password + " ]"

            if( self.downloadOnly ):
                print "\t   + download only: True"
            else:
                print "\t   + build in Debug mode:",
                if( self.debug ):
                    print "Yes"
                else:
                    print "No"
                print "\t   + build Documentation:",
                if( self.buildDoc ):
                    print "Yes"
                else:
                    print "No"
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
            print "\t+ " + self.name + ":",
            print "located at [ " + self.installPath + " ]"

        return str("")

    def abort(self, msg):
        """ used to abort the installation.
            displays the module name and the given message """
        print "*** ERROR in module [ " + self.name + " ]: " + msg
        
        # write error to logfile
        try:
            commands.getoutput( "echo \"*** Error in module [ " + self.name + " ]: " + str(msg).replace("\n","") + "\" >> " + self.logfile )
        except:
            pass
        sys.exit(1)

    def autoDetect(self):
        """ auto detect module """
        
        # auto detect settings
        self.installPath = self.autoDetectPath()
        self.version = self.autoDetectVersion()

        check = self.checkInstall()

        # set a flag for successful auto detection
        self.autoDetected = ( self.installPath and self.version and check )

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
        
        # initialize debug flag
        self.debug = self.parent.debug
        
        # initialize documentation flag
        self.buildDoc = self.parent.buildDoc

        # initialize cmake flag
        self.useCMake = self.parent.useCMake

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

            # backup linkPath
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
                self.installPath = fixPath(self.__userInput)
                # if use( Mod( "vXX-XX" ) is given
                if( not self.checkInstall() ):
                    self.version = self.__userInput
                    self.installPath = self.parent.installPath + "/" + self.alias + "/" + self.version
                else:
                    # extract version from path
                    self.version = basename( self.installPath )

            # check if installed version is functional
            self.checkInstall(True)

        self.mode = mode
    
    def evalVersion(self, v):
        """ evaluates a version string
            - returns 0 if versions are equal
            - returns 1 if self.version < v
            - returns 2 if self.version > v """

        # version must at least contain 3 chars (e.g. 1.0)
        if( (len(v) < 3) or (len(self.version) < 3) ):
            self.abort( "failed to compare versions: [" \
                    + v + "] with self.version [" + self.version + "] !!" )

        if( v == self.version ):
            return 0

        if( self.version == "HEAD" ):
            return 2

        if( v == "HEAD" ):
            return 1

        # create copies for manipulation
        vSelf = self.version
        vTest = v
        
        # substitute version separators through whitespaces
        sep = string.maketrans( ".-_", "   " )
        vSelf = vSelf.translate( sep )
        vTest = vTest.translate( sep )
        
        # split versions by whitespaces
        vSelf = vSelf.split()
        vTest = vTest.split()
        
        # remove characters from list elements
        vSelf = [ i.strip(string.letters) for i in vSelf ]
        vTest = [ i.strip(string.letters) for i in vTest ]

        # remove empty elements
        vSelf = [ i for i in vSelf if i ]
        vTest = [ i for i in vTest if i ]

        # convert to integers
        vSelf = [ int(i) for i in vSelf ]
        vTest = [ int(i) for i in vTest ]

        # now compare the versions
        if( vSelf == vTest ):
            return 0

        return ((( vSelf > vTest ) and [2] or [1])[0])
        
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
                self.abort( "sorry, " + self.download.type + " download type not supported " \
                        + "for this package. Please choose another type..." )
            if( self.download.type == "cvs" or self.download.type == "ccvssh" ):
                if( not isinPath("cvs") ):
                    self.abort( "cvs not found!!" )
                if( self.download.type == "cvs" ):
                    self.download.accessmode = "pserver"
                if( self.download.type == "ccvssh" ):
                    self.download.env["CVS_RSH"] = "ccvssh"
                    self.download.accessmode = "ext"
                    if( not isinPath("ccvssh") ):
                        self.abort( "ccvssh not found!!" )

                # if CVSROOT not set by user generate a default one
                if( not self.download.env.has_key("CVSROOT") ):
                    self.download.env["CVSROOT"] = ":" + self.download.accessmode + ":" + self.download.username \
                            + "@" + self.download.server + ":/" + self.download.root
            elif( self.download.type == "wget" ):
                if( not isinPath("wget") ):
                    self.abort( "wget not found on your system!!" )
                if( not isinPath("tar") ):
                    self.abort( "tar not found on your system!!" )

                # if download url not set by user generate a default one
                if( len(self.download.url) == 0 ):
                    self.download.url = "http://www-zeuthen.desy.de/lc-cgi-bin/cvsweb.cgi/" \
                        + self.download.project + "/" + self.download.project + ".tar.gz?cvsroot=" \
                        + self.download.root + ";only_with_tag=" + self.version + ";tarball=1"
            else:
                self.abort( "download type " + self.download.type + " not recognized!!" )



    def checkInstallConsistency(self):
        """ check installation consistency """
        # switch to use mode if already installed
        if( self.mode == "install" and os.path.exists( self.installPath )):
            print "*** WARNING: " + self.name + " " + self.version + " already installed in: [ " + self.installPath + " ]!!"
            if( os.path.exists( self.installPath + "/.install_failed.tmp" )):
                self.rebuild = True
                print "***\tInstallation status: ERROR: Package install failed last time it was run!! Will try to rebuild package..."   
            elif( os.path.exists( self.installPath + "/.doc_failed.tmp" )):
                self.skipCompile = True
                print "***\tInstallation status: INCOMPLETE: will finish installing this package..."
            elif( not self.checkInstall() ):
                print "***\tInstallation status: INCOMPLETE: will finish installing this package..."
            else:
                print "***\tInstall status: OK: will skip installation and switch to \"use\" mode!!"
                self.mode = "use"

    def preCheckDeps(self):
        """ called before running dependency check
            useful for adding or removing dependencies based on
            environment variables or some other setting """
        if( self.mode == "install" and self.useCMake ):
            self.addExternalDependency( ["CMake","CMakeModules"] )
    
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

            # set debug for cmake builds
            if( self.useCMake ):
                if( self.debug ):
                    self.envcmake["CMAKE_BUILD_TYPE"]="Debug"


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
                if( self.mode == "install" ):
                    print "   - " + self.name + ": " + opt + " not found!!",
                    print self.name + " will NOT be built with " + opt
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

                    print self.name + ": " + req + " version " + self.parent.module( req ).version \
                            + " was automatically detected and will be used in the installation!!"
        
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

                        print "   - " + self.name + ": " + req + " version " + self.parent.module( req ).version \
                                + " was automatically detected and will be used in the installation!!"

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

        # get actual dependecies
        deplist={}
        self.getDepList(deplist)
        del deplist[self.name]
        
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
    
    def downloadSources(self):
        """ download sources """
        
        # create install base directory
        trymakedir( os.path.dirname( self.installPath ))
    
        os.chdir( os.path.dirname(self.installPath) )
        
        if( self.download.type == "cvs" or self.download.type == "ccvssh" ):

            for k, v in self.download.env.iteritems():
                os.environ[k] = v

            if( isinPath( "expect" )):
                os.system( "expect -c 'spawn "+self.download.type+" login'" \
                        + " -c 'expect assword:' -c 'send \""+self.download.password+"""\r"'""" \
                        + " -c 'expect eof'" )
            else:
                if( self.download.type == "ccvssh" ):
                    os.system( "ccvssh login" )
                elif( self.download.password != "" ):
                    os.system( "cvs login" )

            # checkout sources
            if( self.version == "HEAD" ):
                os.system( "cvs co -d " + self.version + " " + self.download.project )
            else:
                os.system( "cvs co -d " + self.version + " -r " + self.version + " " + self.download.project )
        
        elif( self.download.type == "wget" ):

            # name of the tarball file
            self.download.tarball = self.download.project + "_" + self.version + ".tgz"

            if( os.system( "wget " + "\"" + self.download.url + "\"" + " -O " + self.download.tarball ) != 0 ):
                self.abort( "Problems ocurred downloading sources!!")

            if( not os.path.exists( "./" + self.download.tarball) ):
                self.abort( "Problems ocurred downloading sources!!")
                
            # find out directory inside tarball
            os.system("tar -tzf " + self.download.tarball + " > tarlist.tmp")
            directory = commands.getoutput( "head -n1 tarlist.tmp" ).strip()
            os.unlink( "tarlist.tmp" )
            
            # extract the root directory from the directory tree
            if( directory.find('/') != -1 ):
                directory = directory[:directory.find('/')]

            # unpack tarball
            print "+ Unpacking " + self.download.tarball
            os.system( "tar -xzvf " + self.download.tarball )
            
            tryrename( directory, self.version )

        if( self.useCMake and not self.skipCompile ):
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
    
    def buildDocumentation(self):
        """ build documentation.
            does nothing in the base class """
        pass
    
    def buildDoku(self):
        """ small helper function for building documentation """
        
        if( self.buildDoc and os.path.exists( self.installPath + "/.doc_failed.tmp" )):
            # set environment
            self.setEnv(self, [])

            print 80*'#' + "\n##### Building Documentation for " + self.name + "...\n" + 80*'#'
            self.buildDocumentation()
            
            # unset environment
            self.unsetEnv([])
            os.unlink( self.installPath + "/.doc_failed.tmp" )

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
            if( self.useCMake or (not self.isMarlinPKG) or (self.isMarlinPKG and not self.buildInMarlin()) ):
                os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
                os.system( "echo \"" + 10*'#' + " BUILDING " + self.name + "\" >> " + self.logfile )
                os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
                os.system( "echo \"" + 5*'-' + " ENVIRONMENT SNAPSHOT " + 5*'-' + "\" >> " + self.logfile )
                os.system( "env >> " + self.logfile )
                os.system( "echo \"" + 5*'-' + " END OF ENVIRONMENT SNAPSHOT " + 5*'-' + "\" >> " + self.logfile )
                os.system( "touch " + self.installPath + "/.install_failed.tmp" )
                if( self.buildDoc ):
                    os.system( "touch " + self.installPath + "/.doc_failed.tmp" )

            # compile module
            if( not self.skipCompile ):
                if( self.useCMake ):
                    self.setCMakeVars(self,[])
                    cmakeCmdstr = self.genCMakeCmd().split()
                    print "+ CMake build variables:"
                    for i in cmakeCmdstr:
                        print "\t" + i
                    print
                
                self.compile()

            if( self.useCMake or (not self.isMarlinPKG) or (self.isMarlinPKG and not self.buildInMarlin()) ):
                os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
                os.system( "echo \"" + 10*'#' + " FINISHED BUILDING " + self.name + "\" >> " + self.logfile )
                os.system( "echo \"" + 100*'#' + "\" >> " + self.logfile )
            
            # set the module to use mode
            self.mode = "use"

            # just to check if the library was created successfully
            if( self.useCMake or (not self.isMarlinPKG) or (self.isMarlinPKG and not self.buildInMarlin()) ):
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
            
            # Marlin packages
            if( self.isMarlinPKG and self.buildInMarlin() ):
                print "+ " + self.name + " will be built together with Marlin!!"
                print "+ " + self.name + " dependencies added to Marlin!!"
                print '\n' + 20*'-' + " Finished " + self.name + " Installation Test " + 20*'-' + '\n'
                return

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

            print "\n+ " + self.name + " installation finished."
            print '\n' + 20*'-' + " Finished " + self.name + " Installation Test " + 20*'-' + '\n'

    def genCMakeCmd(self):
        """ generates a CMake command out of envcmake """
        cmd = ""
        for k, v in self.parent.envcmake.iteritems():
            cmd = cmd + "-D" + k + "=\"" + str(v).strip() + "\" "
        for k, v in self.envcmake.iteritems():
            cmd = cmd + "-D" + k + "=\"" + str(v).strip() + "\" "
        for k, v in self.env.iteritems():
            cmd = cmd + "-D" + k + "=\"" + str(v).strip() + "\" "
        return cmd.strip()

    def setCMakeVars(self, origin, checked):
        """ sets the cmake variables """
        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        # cmake variables
        if( self.name in self.parent.cmakeSupportedMods ):
            if( not origin.envcmake.has_key(self.name+"_HOME")):
                origin.envcmake[self.name+"_HOME"]=self.realPath()
        if( len(checked) > 1 ):
            if( self.name == "CMakeModules" ):
                origin.envcmake["CMAKE_MODULE_PATH"]=self.realPath()
            if( self.name in origin.cmakebuildmodules and self.name in origin.optmodules ):
                if( not origin.envcmake.has_key("BUILD_WITH")):
                    origin.envcmake["BUILD_WITH"]=""
                origin.envcmake["BUILD_WITH"]=origin.envcmake["BUILD_WITH"]+self.name+" "
    
        # set environment for dependencies
        if( len( checked ) > 1 ):
            mods = self.optmodules + self.reqmodules
        else:
            # buildonly modules are only used for the package were they are needed
            mods = self.optmodules + self.reqmodules + self.reqmodules_buildonly + self.reqmodules_external
        
        for modname in mods:
            self.parent.module(modname).setCMakeVars(origin, checked)



    def setEnv(self, origin, checked, simOnly=False):
        """ sets the environment variables for this module """

        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )
        
        # set environment variables
        if( simOnly ):
            if( len( checked ) == 1 ):
                if( len(self.parent.env) != 0 ):
                    print "\n   + Global Environment variables:"
                    for k, v in self.parent.env.iteritems():
                        print "\t* " + k + ": " + str(v)

            print "\n   + Environment variables set by " + self.name + ":"
            
            if( len(self.env) != 0 ):
                for k, v in self.env.iteritems():
                    print "\t* " + k + ": " + str(v)
        else:
            for k, v in self.env.iteritems():
                os.environ[k] = str(v)

        # print path and build environment variables
        if( simOnly ):
            for k, v in self.envpath.iteritems():
                if( len(v) != 0 ):
                    print "\t* " + k + ": " + str(v)
            for k, v in self.envbuild.iteritems():
                if( len(v) != 0 ):
                    print "\t* " + k + ": " + str(v)
            for k, v in self.envoptbuild.iteritems():
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

        # set path environment variables
        for k, v in self.envpath.iteritems():
            if( len(v) != 0 ):
                env = getenv( k )
                newvalues = ""
                for i in v:
                    rpath = fixPath(i)
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
            
        if( self.isMarlinPKG and self.buildInMarlin() ):
            return

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
        
        # close file
        f.close()
    
    def writeEnv(self, f, checked):
        """ helper function used for writing the environment to a file """
        
        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        if( not self.isMarlinPKG ):
            f.write( 2*os.linesep + "#" + 80*'-' + os.linesep + "#" + 5*' ' + self.name + os.linesep + "#" + 80*'-' + os.linesep )
            
        # environment variables
        for k, v in self.env.iteritems():
            f.write( "export " + str(k) + "=\"" + str(v) + "\"" + os.linesep )
        
        # path environment variables
        for k, v in self.envpath.iteritems():
            if( len(v) != 0 ):
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
            
        if( self.isMarlinPKG and self.buildInMarlin() ):
            return

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

    def writeBuildEnv(self, f, checked, optional=False, recursive=True):
        """ writes the build environment to a file (userlib.gmk) """
        
        # resolve circular dependencies
        if( self.name in checked ):
            return
        else:
            checked.append( self.name )

        # check if there are any build environment variables
        foundreq = False
        foundopt = False
        for k, v in self.envbuild.iteritems():
            if( len(v) != 0 ):
                foundreq = True
        if( optional ):
            for k, v in self.envoptbuild.iteritems():
                if( len(v) != 0 ):
                    foundopt = True

        # write variables
        if( foundreq or foundopt ):
            f.write( 2*os.linesep + "#" + 80*'-' + os.linesep + "#" + 5*' ' + self.name + os.linesep + "#" + 80*'-' + os.linesep )
            for k, v in self.envbuild.iteritems():
                for var in v:
                    f.write( k + " += " + var + os.linesep )
            if( optional ):
                for k, v in self.envoptbuild.iteritems():
                    for var in v:
                        f.write( k + " += " + var + os.linesep )

        if( recursive ):
            mods = self.optmodules + self.reqmodules
            for modname in mods:
                self.parent.module(modname).writeBuildEnv(f, checked, optional, recursive)

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
    """ Small class responsible for the downloads """

    def __init__(self, parent):
        self.parent = parent                        # parent class responsible for this download
        self.project = parent.alias                 # project name
        self.root = str.lower(self.project)         # cvs root
        self.username = "anonymous"                 # cvs username
        self.password = ""                          # cvs password
        self.server = "cvssrv.ifh.de"               # cvs server
        self.url = ""                               # url for getting tarball with wget
        self.tarball = ""                           # name of the tarball used for wget downloads
        self.env = {}                               # environment (CVSROOT, CVS_RSH)
        self.type = "wget"                          # download type (wget, cvs, ccvssh)
        self.supportHEAD = True                     # support for downloading HEAD version
        self.supportedTypes = [ "wget", "ccvssh" ]  # supported download types for the module

#--------------------------------------------------------------------------------

