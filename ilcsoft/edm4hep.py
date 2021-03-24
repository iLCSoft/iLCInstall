##################################################
#
# edm4hep module
#
# Author: F.Gaede, DESY
# Date: Nov, 2020
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class edm4hep(BaseILC):
    """ Responsible for the edm4hep configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "edm4hep", "edm4hep")

        self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'key4hep'
        self.download.gitrepo = 'edm4hep'

        self.reqfiles = [ ["install/lib/libedm4hep.so", "install/lib/libedm4hep.dylib" ]]

        self.reqmodules = [ "podio" ]
#        self.optmodules = [ "SIO" ]

        
    def init(self):
        """ init edm4hep """
        BaseILC.init(self)



    def compile(self):
        """ compile edm4hep """

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

        self.env[ 'edm4hep_DIR' ] = self.installPath + "/install/lib/cmake/EDM4HEP"
