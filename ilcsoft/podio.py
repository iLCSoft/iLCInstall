##################################################
#
# podio module
#
# Author: F.Gaede, DESY
# Date: Nov, 2020
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class podio(BaseILC):
    """ Responsible for the podio configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "podio", "podio")

        self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'AIDASoft'
        self.download.gitrepo = 'podio'

        self.reqfiles = [ ["install/lib/libpodio.so", "install/lib/libpodio.dylib" ]]

        self.reqmodules = [ "ROOT" ]
        self.optmodules = [ "SIO" ]

        
    def init(self):
        """ init podio """
        BaseILC.init(self)



    def compile(self):
        """ compile podio """

        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )
        
        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        if( os_system( self.genCMakeCmd() + " -DCMAKE_INSTALL_PREFIX=../install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if (self.nightlyBuild == True):

            for targetName in self.nightlyTargets:
                if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} " + targetName + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to compile!!" )
        else:
            if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'podio_DIR' ] = self.installPath + "/install/lib/cmake/podio"
