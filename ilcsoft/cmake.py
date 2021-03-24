##################################################
#
# CMake module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class CMake(BaseILC):
    """ Responsible for the CMake installation process. """
    
    def __init__(self, userInput="auto"):
        BaseILC.__init__(self, userInput, "CMake", "CMake")

        self.download.supportHEAD = False
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [ ["bin/cmake"], ["bin/cpack"], ["bin/ctest"] ]

        if( userInput == "auto" ):
            self.autoDetect()

    def autoDetectPath(self):
        """ tries to auto detect cmake dir from system settings.
            - returns empty string in case of failure
            - otherwise returns cmake dir """

        # else try to get from cmake
        if( isinPath("cmake")):
            out = getoutput("which cmake").strip()
            ind = out.find("/bin/cmake")
            return out[:ind]

        return ''

    def autoDetectVersion(self):
        """ tries to auto detect version by parsing the output of cmake --version.
            - returns empty string in case of failure
            - otherwise returns cmake version """

        try:
            v = Version( getoutput( self.realPath() + '/bin/cmake --version' ).replace( 'patch ','' ), strict=True)
        except ValueError:
            return ''
        else:
            return str(v)

    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        versionDirectory = ".".join(self.version.split('.')[0:2])
        self.download.url = "https://cmake.org/files/v%s/cmake-%s.tar.gz" % (versionDirectory, self.version)
        
    def downloadSources(self):
        
        print("downloadSources from : " , self.download.url)

        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        os.makedirs( self.installPath + "/build" )


    def compile(self):
        """ compile CMake """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os_system( "make clean" )

        if( os_system( "../" + self.name + "/configure --prefix=" + self.installPath + \
            " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath + "/build" )
        os_system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.envpath["PATH"].append( self.installPath+"/bin" )

