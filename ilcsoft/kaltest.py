##################################################
#
# KalTest and KalDet modules
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class KalTest(BaseILC):
    """ Responsible for the KalTest software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "KalTest", "KalTest")

        self.reqfiles = [ ["lib/libKalTest.so","lib/libKalTest.a","lib/libKalTest.dylib"] ]

        self.reqmodules = [ "ROOT" ]

    def compile(self):
        """ compile KalTest """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["KALTEST"] = self.installPath

        self.envpath["LD_LIBRARY_PATH"].append( '$KALTEST/lib' )



##################################################
# KalDet module
##################################################


class KalDet(BaseILC):
    """ Responsible for the KalDet software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "KalDet", "KalDet")

        self.reqfiles = [ ["lib/libKalDet.so","lib/libKalDet.a","lib/libKalDet.dylib"] ]

        self.reqmodules = [ "KalTest", "Marlin", "MarlinUtil", "GEAR", "ROOT" ]

        self.download.root = "kaltest"

    def compile(self):
        """ compile KalDet """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

