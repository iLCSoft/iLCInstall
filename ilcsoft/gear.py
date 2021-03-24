##################################################
#
# GEAR module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class GEAR(BaseILC):
    """ Responsible for the GEAR software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GEAR", "gear")


        self.optmodules = [ "ROOT" ]
        self.reqmodules = [ "CLHEP" ]

        self.reqfiles = [
                ["lib/libgear.a", "lib/libgear.so", "lib/libgear.dylib"],
                ["lib/libgearxml.a", "lib/libgearxml.so", "lib/libgearxml.dylib"]
        ]

    def compile(self):
        """ compile GEAR """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # execute ctests
        if( self.makeTests ):

            if( os_system( "make tests 2>&1" ) != 0 ):
                self.abort( "failed to compile gear tests" )


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

        if Version( self.version ) < '0.14':
            self.addExternalDependency( ["Java"] )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["GEAR"] = self.installPath

        # PATH
        self.envpath["PATH"].append( "$GEAR/tools" )
        self.envpath["PATH"].append( "$GEAR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$GEAR/lib" )

