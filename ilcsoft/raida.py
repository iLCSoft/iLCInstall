##################################################
#
# RAIDA module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class RAIDA(BaseILC):
    """ Responsible for the RAIDA software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "RAIDA", "RAIDA")

        self.reqfiles = [ ["bin/aida-config"], ["lib/libRAIDA.a", "lib/libRAIDA.so", "lib/libRAIDA.dylib"] ]

        # ROOT is required for building RAIDA
        self.reqmodules = [ "ROOT" ]

        # cvs root
        self.download.root = "ilctools"

    def compile(self):
        """ compile RAIDA """
        
        os.chdir( self.installPath + "/build")

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )
        
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["RAIDA_HOME"] = self.installPath
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$RAIDA_HOME/bin" )

