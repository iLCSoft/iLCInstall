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
    
        contains the installation path for the whole ILC software 
        and the modules/packages which should be installed """
    
    def __init__(self, installPath):
        self.os = OSDetect()        # operating system detection
        self.installPath = fixPath(installPath)
        self.modules = []           # list of modules
        self.autoModules = []       # list of auto detected modules
        self.debug = False          # global debug flag
        self.buildDoc = True        # global documentation flag
        self.downloadOnly = False   # global download flag
        self.downloadUser = ""      # global download cvs/ccvssh username
        self.downloadPass = ""      # global download cvs/ccvssh password
        self.downloadType = ""      # global download cvs/ccvssh password
        self.downloadLogin2Server=False # set to True if no cvs passwords are stored in your ~/.cvspass
        self.useCMake = False       # global flag for using cmake
        self.noAutomaticRebuilds = False # global flag for automatic rebuilding
        self.env = {}               # global environment variables
        self.envcmake = {}          # global cmake environment variables
        self.cleanInstall = True    # global flag for cleaning temporary files after installation (objects, tarfiles...)

        self.envpathbak = {         # backup path environment variables (PATH, LD_LIBRARY_PATH, CLASSPATH)
            "PATH" : [],
            "LD_LIBRARY_PATH" : [],
            "CLASSPATH" : [],
            "MARLIN_DLL" : []
        }
        # list of supported modules
        # generated from hasCMakeSupport flag
        self.cmakeSupportedMods = [ "AIDA" ]
    
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
        
        self.logfile = self.installPath + "/ilcinstall/" + self.config_file_prefix + "-" + self.time + ".log"

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
            if( mod.hasCMakeSupport ):
                self.cmakeSupportedMods.append( mod.name )
        
        # initialize each module
        for mod in self.modules:
            print "+ Initializing " + mod.name + "..."
            mod.init()

        print "\n+ Checking for installation consistency..."
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
        
        # name of the file
        file = self.installPath + "/ILCSoft.cmake"
        
        # this will be a list of lists for storing entries of a previously existing
        # ILCSoft.cmake pre-cache file.. It will store on the first element the cmake
        # variable being set and on the 2nd element the rest of the cmake
        # command.
        #
        # for example the following line in a cmake pre-cache file:
        # SET( LCIO_HOME "${ILC_CMAKE}/lcio/HEAD" CACHE PATH "Path to LCIO" FORCE )
        #
        # will turn out into a python list element like follows:
        # ['LCIO_HOME',' "${ILC_CMAKE}/lcio/HEAD" CACHE PATH "Path to LCIO" FORCE )']
        #
        # example of what dicHP looks like:
        # [ ['LCIO_HOME',' "${ILC_CMAKE}/lcio/HEAD" CACHE PATH "Path to LCIO" FORCE )'],
        #   ['LCCD_HOME',' "${ILC_CMAKE}/lccd/HEAD" CACHE PATH "Path to LCCD" FORCE )'] ]
        dicHP=[]

        # this will be the list of entries to be removed at the end, i.e. entries
        # that were defined in a previous file and that are redefined in this installation
        # FIXME put this into a set
        dicHP_remove=["ILC_HOME", "CMAKE_MODULE_PATH" ]
        
        # check if file already exists
        if( os.path.exists( file )):
            
            # open the file
            f = open( file )
            
            list = []
            l=f.readline()
            while( not l=="" ):
                # ignore comments in file
                if( l[0] != '#' ):
                    # append lines to a list
                    list.append(l)
                l=f.readline()

            # close file
            f.close()

            # strip whitespaces and remove empty elements
            list = [ i.strip() for i in list if i ]
            # concatenate everything into a list
            s=str.join(' ',list)
            # split by SET instruction
            list=s.split("SET")
            # strip whitespaces and remove empty entries
            list = [ i.strip() for i in list if i ]

            # this will be a list of lists:
            for i in list:
                s = i.split("(")
                # strip whitespaces and remove empty entries
                s = [ j.strip() for j in s if j ]
                for j in s:
                    p=j.find(' ')
                    dicHP.append([ j[:p],j[p:] ])
        
        # open file (overwrite if already exists)
        f = open( file, 'w' )
        
        # write to file
        f.write( 80*'#' + "\n# Environment script generated by ilcsoft-install on " + self.ctime + os.linesep )
        f.write( "# for the installation located at [ " + self.installPath + " ]" + os.linesep + 80*'#' + os.linesep )

        
        f.write( os.linesep + "SET( ILC_HOME \"" + self.installPath + "\"" \
                + " CACHE PATH \"Path to ILC Software\" FORCE)" + os.linesep + os.linesep )

        for mod in self.modules:
            
            # fix for setting JAVA_HOME and not Java_HOME
            if mod.name == "Java":
                modname=mod.name.upper()
            else:
                modname=mod.name
                

            if( mod.name in self.cmakeSupportedMods ):
                # check if install path from module contains base path from ilcsoft
                if( mod.installPath.find( self.installPath) == 0 ):
                    f.write( "SET( " + modname + "_HOME \"${ILC_HOME}/" + mod.alias + "/" + mod.version + "\"" \
                            + " CACHE PATH \"Path to " + modname + "\" FORCE)" + os.linesep )
                else:
                    f.write( "SET( " + modname + "_HOME \"" + mod.installPath + "\"" \
                            + " CACHE PATH \"Path to " + modname + "\" FORCE)" + os.linesep )

                # fix for writing AIDA_HOME
                if mod.name == "RAIDA" or mod.name == "AIDAJNI":
                    f.write( "SET( AIDA_HOME \"${"+modname+"_HOME}\" CACHE PATH \"Path to AIDA\" FORCE)" + os.linesep )
                    dicHP_remove.append( "AIDA_HOME" )

                dicHP_remove.append( modname+"_HOME" )
        
        cmods = self.module("CMakeModules")
        if( cmods != None ):
            if( cmods.installPath.find( self.installPath ) == 0 ):
                f.write( os.linesep + "SET( CMAKE_MODULE_PATH \"${ILC_HOME}/CMakeModules/" + cmods.version + "\"" \
                        + " CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep + os.linesep )
            else:
                f.write( os.linesep + "SET( CMAKE_MODULE_PATH \"" + cmods.installPath + "\"" \
                        + " CACHE PATH \"Path to CMakeModules\" FORCE)" + os.linesep + os.linesep )
       
        # remove entries from dicHP
        for r in dicHP_remove:
            for k in dicHP:
                if( k[0] == r ):
                    del( dicHP[dicHP.index(k)])

        # finally check if there are still any entries in dicHP and write them out
        # in the new file
        for k in dicHP:
            f.write( "SET( " + k[0] + k[1] + os.linesep )

        # close file
        f.close()


    
    def makeinstall(self):
        """ starts the installation process """
        # create log directory
        trymakedir( self.installPath + "/ilcinstall" )
        
        # copy config file
        try:
            shutil.copyfile( self.config_file, self.installPath + "/ilcinstall/" + \
                    self.config_file_prefix + "-" + self.time + ".cfg")
        except:
            print "*** FATAL ERROR: you don't have write permissions in " + self.installPath + "!!!\n"
            sys.exit(1)
        
        # initialize log file
        os.system( "echo \"Install started at: " + self.ctime + "\" > " + self.logfile )
        os.system( "echo \"Configuration file: " + self.config_file + "\" >> " + self.logfile )
        os.system( "echo \"Using " + commands.getoutput( "g++ --version | head -n1" ).strip() + "\" >> " + self.logfile )
        os.system( "echo \"Using " + commands.getoutput( "make --version | head -n1" ).strip() + "\" >> " + self.logfile )

        # set global environment
        self.setEnv()

        # make backup of path environment variables
        for k, v in self.envpathbak.iteritems():
            self.envpathbak[k] = getenv(k)
        
        print "\n" + 30*'*' + " Starting ILC Software installation process " + 30*'*' + "\n"
        # write CMake Environment to file
        self.writeCMakeEnv()
        print "\n" + 30*'*' + " Creating symlinks " + 30*'*' + "\n"
        for mod in self.modules:
            mod.createLink()
        print "\n" + 30*'*' + " Checking for rebuilds " + 30*'*' + "\n"
        for mod in self.modules:
            mod.confirmRebuild()
        print "\n" + 30*'*' + " Downloading sources " + 30*'*' + "\n"
        for mod in self.modules:
            if( (mod.mode == "install") and (not os.path.exists( mod.installPath ))):
                print 80*'*' + "\n*** Downloading sources for " + mod.name + " version " + mod.version + "...\n" + 80*'*'
                mod.downloadSources()
        if( not self.downloadOnly ):
            print "\n" + 30*'*' + " Installing software " + 30*'*' + "\n"
            for mod in self.modules:
                mod.install([])
            print "\n" + 30*'*' + " Building documentation " + 30*'*' + "\n"
            for mod in self.modules:
                mod.buildDoku()

    def summary(self):
        """ displays an installation summary """
        print "\n" + 30*'=' + " Installation Summary: " + 40*'='
        print "\n+ Operating System: " + self.os.type+" - "+self.os.ver
        print "\n+ Using " + commands.getoutput( "g++ --version | head -n1" ).strip()
        print "\n+ Using " + commands.getoutput( "make --version | head -n1" ).strip()
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

