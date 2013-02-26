##################################################
#
# ILCSoft module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from util import *
from java import Java
from qt import QT
from cmake import CMake


class ILCSoft:
    """ Container class for the ILC software modules.
    
`        contains the installation path for the whole ILC software 
        and the modules/packages which should be installed """
    
    def __init__(self, installPath):
        self.os = OSDetect()        # operating system detection
        self.installPath = fixPath(installPath)
        self.patchPath = fixPath(installPath)
        self.logsdir = self.installPath + "/.ilcinstall-logs/"
        self.ilcinstallDir = os.path.abspath(sys.path[0])
        self.patch = []             # list of patches
        self.modules = []           # list of modules
        self.autoModules = []       # list of auto detected modules
        self.downloadOnly = False   # global download flag
        self.downloadUser = ""      # global download cvs/ccvssh username
        self.downloadPass = ""      # global download cvs/ccvssh password
        self.downloadType = ""      # global download cvs/ccvssh password
        self.makeTests = False      # global flag for calling "make test" after building the software
        self.noAutomaticRebuilds = False # global flag for automatic rebuilding
        self.rebuild = False        # global flag for rebuilding ilcsoft
        self.env = {
            'ILCSOFT_CMAKE' : self.installPath + '/ILCSoft.cmake' ,
            'ILCSOFT_CMAKE_ENV' : self.installPath + '/ILCSoft.cmake.env.sh' ,
        }               # global environment variables
        self.envcmake = {           # global cmake environment variables
            'CMAKE_BUILD_TYPE' : 'Release',
            'INSTALL_DOC' : 'ON'
        }
        self.cleanInstall = True    # global flag for cleaning temporary files after installation (objects, tarfiles...)

        self.envpathbak = {         # backup path environment variables (PATH, LD_LIBRARY_PATH, CLASSPATH)
            "PATH" : [],
            "LD_LIBRARY_PATH" : [],
            "CLASSPATH" : [],
            "MARLIN_DLL" : []
        }
        # list of supported modules
        # generated from hasCMakeFindSupport flag
        self.cmakeSupportedMods = [ "AIDA" ]

        self.debugInfo={}

        self.debugInfo['PLATFORM']=self.os.type+" - "+self.os.ver
        self.debugInfo['UNAME']=getoutput( "uname -a" ).strip()
        self.debugInfo['LSB_RELEASE']=getoutput( "lsb_release -a 2>/dev/null" ).strip()
        self.debugInfo['GCC_VERSION']=getoutput( "gcc --version | head -n1" ).strip()
        release_string = getoutput( "lsb_release -d 2>/dev/null").strip()

        #fg: release_string might be empty, e.g. if lsb_release does not exis (MacOs)
        self.release_number = '-1'
        if len( release_string ): 
            self.release_number = release_string[re.search('\d', release_string).start()]
        
        for k,v in self.debugInfo.iteritems():
            print "+", k, '\t', str(v).replace("\n","\n\t\t")

        print


    
    def use(self, module):
        """ appends the given module to the list of modules 
            to be used in the installation """
        # check if a module with the same name already exists
        if( self.module(module.name) == None ):
            module.parent = self
            module.setMode("use")
            self.modules.append(module)
        else:
            print "module " + module.name + " defined more than once in your config file!!"
            sys.exit(1)
    
    def link(self, module):
        """ appends the given module to the list of modules 
            to be linked in the installation """
        # check if a module with the same name already exists
        if( self.module(module.name) == None ):
            module.parent = self

            # set the patch path - if it exists 
            if( not os.path.exists( module.userInput() ) and len( self.patchPath ) > 0 ):
                module.patchPath = self.patchPath

            module.setMode("link")

            self.modules.append(module)
        else:
            print "module " + module.name + " defined more than once in your config file!!"
            sys.exit(1)
    
    def install(self, module):
        """ appends the given module to the list of modules
            to be installed in the installation """
        # check if a module with the same name already exists
        if( self.module(module.name) == None ):
            module.parent = self
            module.setMode("install")
            self.modules.append(module)
        else:
            print "module " + module.name + " defined more than once in your config file!!"
            sys.exit(1)

    def module(self, modname, auto=False):
        """ checks for a module with the given name.
            use auto for auto detected modules.
            - returns the module if it exists
            - otherwise returns None """
        if( auto ):
            mods = self.autoModules
        else:
            mods = self.modules
        
        modname=str.upper(modname)
        for mod in mods:
            if( modname == "AIDA" ):
                if( mod.name == "RAIDA" or mod.name == "AIDAJNI" ):
                    return mod
            elif( str.upper(mod.name) == modname ):
                return mod    

        for mod in mods:
            if( str.upper(mod.name) == str.upper(modname) ):
                return mod
        return None

    def setEnv(self):
        """ sets global environment variables """

        for k, v in self.env.iteritems():
            os.environ[k] = str(v)

    def init(self):
        """ this method is called right after reading the configuration file.
            so, it is useful for initializing variables that depend on the
            installation mode or anything that depends on user changes in the
            configuration file """

        if( os.system( "which which > /dev/null 2>&1" ) != 0 ):
            print "\"which\" is not installed on your system!!"
            sys.exit(1)
            

        t = time.gmtime()
        
        # save installation time to variable
        self.time = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2]) + "_" + str(t[3]) + "-" + str(t[4])
        self.ctime = time.ctime()
        
        self.logfile = self.logsdir + self.config_file_prefix + "-" + self.time + ".log"

        # auto detect modules
        if( self.module( "Java" ) == None ):
            auto_java = Java()
            if( auto_java.autoDetected ):
                self.autoModules.append( auto_java )
        if( self.module( "QT" ) == None ):
            auto_qt = QT()
            if( auto_qt.autoDetected ):
                self.autoModules.append( auto_qt )
        if( self.module( "CMake" ) == None ):
            auto_cmake = CMake()
            if( auto_cmake.autoDetected ):
                self.autoModules.append( auto_cmake )
        
        # initialize cmake supported modules
        for mod in self.modules:
            if( mod.hasCMakeFindSupport ):
                self.cmakeSupportedMods.append( mod.name )
        
        # initialize each module
        print "+ Initialize modules..."
        for mod in self.modules:
            mod.init()

        print "\n+ Check for previous installations...\n"
        for mod in self.modules:
            mod.checkInstallConsistency()
        
        # skip dependencies for downloading only
        if( self.downloadOnly ):
            return
        
        print "\n+ Dependencies Pre-Check..."
        for mod in self.modules:
            mod.preCheckDeps()
        
        print "\n+ Dependencies Check..."
        PkgUpdated = True
        while PkgUpdated:
            PkgUpdated = False

            for mod in self.modules:
                mod.checkRequiredDependencies()

            for mod in self.modules:
                mod.checkOptionalDependencies()
                
            for mod in self.modules:
                if( not mod.checkDeps() ):
                    PkgUpdated = True
        
        print "\n+ Dependencies Post-Check..."
        for mod in self.modules:
            mod.postCheckDeps()
            
        print
    
    def writeCMakeEnv(self):
        
        # name of the file ( gets overwritten !! )
        file = self.env[ "ILCSOFT_CMAKE" ]
        file2 = self.env[ "ILCSOFT_CMAKE_ENV" ]
        
        # check if file already exists
        if( os.path.exists( file )):
            os.unlink( file )
            
        # check if file already exists
        if( os.path.exists( file2 )):
            os.unlink( file2 )

        f = open( file, 'w' )
        f2 = open( file2, 'w' )
        
        # write to file
        f.write( 80*'#' + "\n# Environment script generated by ilcsoft-install on " + self.ctime + os.linesep )
        f.write( "# for the installation located at [ " + self.installPath + " ]" + os.linesep + 80*'#' + os.linesep )

        # write to file
        f2.write( 80*'#' + "\n# Environment script generated by ilcsoft-install on " + self.ctime + os.linesep )
        f2.write( "# for the installation located at [ " + self.installPath + " ]" + os.linesep + 80*'#' + os.linesep )
        
        f.write( os.linesep + "SET( ILC_HOME \"" + self.installPath + "\"" \
                + " CACHE PATH \"Path to ILC Software\" FORCE)" + os.linesep )
        f.write( "MARK_AS_ADVANCED( ILC_HOME )" + os.linesep + os.linesep )
       
        f2.write( "export ILC_HOME=" + self.installPath + os.linesep )

        f.write( "SET( CMAKE_PREFIX_PATH " + os.linesep )
        f2.write( "export CMAKE_PREFIX_PATH=\\" + os.linesep )

        for mod in self.modules:
            
            ## fix for setting JAVA_DIR and not Java_DIR
            #if mod.name == "Java":
            #    modname=mod.name.upper()
            #else:
            #    modname=mod.name
            #    

            if( mod.name in self.cmakeSupportedMods ):

                f.write( "\t" )

                # check if install path from module contains base path from ilcsoft
                if( mod.installPath.find( self.installPath) == 0 ):
                    #f.write( "SET( " + modname + "_DIR \"${ILC_HOME}/" + mod.alias + "/" + mod.version + "\"" \
                    #        + " CACHE PATH \"Path to " + modname + "\" FORCE)" )
                    f.write( "${ILC_HOME}/" + mod.alias + "/" + mod.version + ';' )
                    f2.write( "${ILC_HOME}/" + mod.alias + "/" + mod.version + ':\\' )
                else:
                    #f.write( "SET( " + modname + "_DIR \"" + mod.installPath + "\"" \
                    #        + " CACHE PATH \"Path to " + modname + "\" FORCE)" )
                    f.write( mod.installPath + ';' )
                    f2.write( mod.installPath + ':\\' )

                f.write( os.linesep )
                f2.write( os.linesep )

                #f.write( "MARK_AS_ADVANCED( " + modname + "_DIR )" + os.linesep  )

            #    # fix for writing AIDA_DIR
            #    if mod.name == "RAIDA" or mod.name == "AIDAJNI":
            #        f.write( "SET( AIDA_DIR \"${"+modname+"_DIR}\" CACHE PATH \"Path to AIDA\" FORCE)" + os.linesep )
            #        f.write( "MARK_AS_ADVANCED( AIDA_DIR )" + os.linesep  )

        f.write( "CACHE PATH \"CMAKE_PREFIX_PATH\" FORCE )" + os.linesep + os.linesep ) # close CMAKE_PREFIX_PATH
        f2.write( os.linesep )

        #ilcutil = self.module("ILCUTIL")
        #if( ilcutil != None ):
        #    #f.write( os.linesep + "# set CMAKE_PREFIX_PATH to find ILCSOFT_CMAKE_MODULES ILCTEST and streamlog" )
        #    #f.write( os.linesep + "# by setting this variable there is no need to set the correspondent PKG_DIR variables" )
        #    #f.write( os.linesep + "SET( CMAKE_PREFIX_PATH \"${ILCUTIL_DIR}\" CACHE PATH \"CMAKE_PREFIX_PATH\" FORCE)" + os.linesep )

        #    f.write( os.linesep + "# set CMAKE_MODULE_PATH for backwards compatibility directly to ILCUTIL_DIR/cmakemodules" )
        #    f2.write( os.linesep + "# set CMAKE_MODULE_PATH for backwards compatibility directly to ILCUTIL_DIR/cmakemodules" )
        #    if( ilcutil.installPath.find( self.installPath ) == 0 ):
        #        f.write( os.linesep + "SET( CMAKE_MODULE_PATH \"${ILC_HOME}/ilcutil/"+ilcutil.version+\
        #            "/cmakemodules\" CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep )
        #        f2.write( os.linesep + "export CMAKE_MODULE_PATH=\"$CMAKE_MODULE_PATH:$ILC_HOME/ilcutil/"+ilcutil.version+"/cmakemodules\"" + os.linesep )

        #    else:
        #        f.write( os.linesep + "SET( CMAKE_MODULE_PATH \""+ilcutil.installPath+\
        #            "/cmakemodules\" CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep )
        #        f2.write( os.linesep + "export CMAKE_MODULE_PATH=\"$CMAKE_MODULE_PATH:"+ilcutil.installPath+"/cmakemodules\"" + os.linesep )
        #else:
        #    # in case ILCUTIL is not present look if we find the old CMakeModules
        #    cmods = self.module("CMakeModules")
        #    if( cmods != None ):
        #        if( cmods.installPath.find( self.installPath ) == 0 ):
        #            f.write( os.linesep + "SET( CMAKE_MODULE_PATH \"${ILC_HOME}/CMakeModules/" + cmods.version + "\"" \
        #                    + " CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep + os.linesep )
        #            f2.write( os.linesep + "export CMAKE_MODULE_PATH=\"$CMAKE_MODULE_PATH:$ILC_HOME/CMakeModules/"+ cmods.version +"\"" + os.linesep )
        #        else:
        #            f.write( os.linesep + "SET( CMAKE_MODULE_PATH \"" + cmods.installPath + "\"" \
        #                    + " CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep + os.linesep )
        #            f2.write( os.linesep + "export CMAKE_MODULE_PATH=\"$CMAKE_MODULE_PATH:"+cmods.installPath+"\"" + os.linesep )

        f.write( os.linesep )
        f2.write( os.linesep )

        # close file
        f.close()
        f2.close()


    
    def makeinstall(self):
        """ starts the installation process """

        print "\n" + 30*'*' + " Starting installation " + 30*'*' + "\n"

        # create log directory
        trymakedir( self.logsdir )
        
        # copy config file
        try:
            shutil.copyfile( self.config_file, self.logsdir + self.config_file_prefix + "-" + self.time + ".cfg")
        except:
            print "*** FATAL ERROR: you don't have write permissions in " + self.installPath + "!!!\n"
            sys.exit(1)
        
        # initialize log file
        os.system( "echo \"Install started at: " + self.ctime + "\" > " + self.logfile )
        os.system( "echo \"Configuration file: " + self.config_file + "\" >> " + self.logfile )
        os.system( "echo \"Using " + getoutput( "g++ --version | head -n1" ).strip() + "\" >> " + self.logfile )
        os.system( "echo \"Using " + getoutput( "make --version | head -n1" ).strip() + "\" >> " + self.logfile )

        # set global environment
        self.setEnv()

        # make backup of path environment variables
        for k, v in self.envpathbak.iteritems():
            self.envpathbak[k] = getenv(k)
        
        print "\n" + 30*'*' + " Starting ILC Software installation process " + 30*'*' + "\n"
        # write CMake Environment to file ILCSoft.cmake
        self.writeCMakeEnv()

        # write init_ilcsoft.sh
        checked=[]
        f = open(self.installPath + "/init_ilcsoft.sh", 'w')
        
        f.write( 'export ILCSOFT='+self.installPath  + os.linesep  )
        
        for mod in self.modules:
            mod.writeEnv(f, checked)
        geant=self.module('Geant4')
        if geant:
            f.write( os.linesep + '# --- source GEANT4 INIT script ---' + os.linesep )
            f.write( 'test -r ${G4ENV_INIT} && { cd $(dirname ${G4ENV_INIT}) ; . ./$(basename ${G4ENV_INIT}) ; cd $OLDPWD ; }' + os.linesep  )
        if self.os.type == "Darwin":
            f.write( os.linesep + '# --- set DYLD_LIBRARY_PATH to LD_LIBRARY_PATH for MAC compatibility ---' + os.linesep )
            f.write( 'export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH' + os.linesep + os.linesep )
        if ( self.os.ver.find("cientific") and self.release_number == '6'):
            f.write( os.linesep + '# ---  Workaraund for OpenGl bug on SL6  ---' + os.linesep )
            f.write( 'export LIBGL_ALWAYS_INDIRECT=1' + os.linesep  )


        print "\n" + 30*'*' + " Creating symlinks " + 30*'*' + "\n"
        for mod in self.modules:
            mod.createLink()
        print "\n" + 30*'*' + " Checking for rebuilds " + 30*'*' + "\n"
        for mod in self.modules:
            mod.confirmRebuild()
        print "\n" + 30*'*' + " Downloading sources " + 30*'*' + "\n"
        for mod in self.modules:
            if mod.mode == "install":
                if not os.path.exists( mod.installPath ):
                    print 80*'*' + "\n*** Downloading sources for " + mod.name + " version " + mod.version + "...\n" + 80*'*'
                    mod.downloadSources()
                # no point in updating the sources unless 'make install' is called for each of those packages afterwards
                # do we really want this?
                #else:
                #    mod.updateSources()

        # apply patches
        if self.patch:
            print "\n" + 30*'*' + " Patching sources " + 30*'*' + "\n"
            for patchname in self.patch:
                relpatchdir = os.path.join( 'patches/', patchname )
                abspatchdir = os.path.abspath( os.path.join( self.ilcinstallDir, relpatchdir ))

                # FIXME check this in preview mode
                if not os.path.exists( abspatchdir ):
                    print "patch not valid:", patchname
                    sys.exit(1)

                os.chdir( abspatchdir )
                for patchfile in GlobDirectoryWalker( '.', "*.patch"):
                    file2patch = os.path.abspath( os.path.join( self.installPath, os.path.splitext( patchfile )[0] ))
                    dirfile2patch = os.path.dirname( file2patch )
                    patchfilecopy = os.path.join( dirfile2patch, '.'+os.path.basename( patchfile ) )
                    if not os.path.exists( patchfilecopy ):
                        if os.path.exists( file2patch ):
                            print 'patching file: ', file2patch
                            os.system( "patch " + file2patch + ' ' + patchfile )
                            os.system( "cp " + patchfile + ' ' + patchfilecopy ) 
                        else:
                            print 'Warning: file to patch not found:', file2patch
                os.chdir( self.ilcinstallDir )

        if( not self.downloadOnly ):
            print "\n" + 30*'*' + " Installing software " + 30*'*' + "\n"
            for mod in self.modules:
                mod.install([])

        # write dependencies to file
        depsfile=self.installPath+"/.dependencies/external"
        trymakedir( self.installPath + "/.dependencies" )
        os.system( "rm -f %s ; touch %s" % (depsfile, depsfile) )
        for mod in self.modules:
            os.system( "echo '%s:%s' >> %s" % (mod.alias,mod.version,depsfile) )

        print "\n" + 30*'*' + " Finished installation " + 30*'*' + "\n"

    def summary(self):
        """ displays an installation summary """

        print "\n" + 30*'=' + " Installation Summary: " + 40*'='

        print "\n+ ILC Software will be installed to [" + self.installPath + "]"
    
        print "\n+ Following modules will be installed:\n"
        for mod in self.modules:
            if( mod.mode == "install" ):
                print mod
        
        print "\n+ Following modules will be used for the installation:\n"
        for mod in self.modules:
            if( mod.mode == "use" ):
                print mod,

        print "\n" + 30*'=' + " End of Installation Summary: " + 33*'=' + "\n\n"


    def previewinstall(self):
        """ tests the installation process """

        print "\n" + 30*'=' + " Installation Simulation: " + 37*'='
        for mod in self.modules:
            if( mod.mode == "install" ):
                mod.previewinstall()
        print "\n" + 30*'=' + " End of Installation Simulation: " + 30*'=' + "\n"

