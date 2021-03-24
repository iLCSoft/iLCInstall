##################################################
#
# LCCD module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class LCCD(BaseILC):
    """ Responsible for the LCCD software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "LCCD", "lccd")

        self.reqfiles = [ ["lib/liblccd.a", "lib/liblccd.so", "lib/liblccd.dylib"] ]

        # LCIO is required for building LCCD
        self.reqmodules = [ "LCIO" ]

        # optional modules
        self.optmodules = [ "CondDBMySQL" ]

    def compile(self):
        """ compile LCCD """
        
        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCCD"] = self.installPath

