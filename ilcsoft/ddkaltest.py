##################################################
#
# DDKalTest
#
# Author: F.Gaede CERN/DESY
# Date: Nov, 2014
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


##################################################
# DDKalTest module
##################################################


class DDKalTest(BaseILC):
    """ Responsible for the DDKalTest software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "DDKalTest", "DDKalTest")

        self.reqfiles = [ ["lib/libDDKalTest.so","lib/libDDKalTest.a","lib/libDDKalTest.dylib"] ]

        self.reqmodules = [ "LCIO", "KalTest", "aidaTT", "GSL" ]

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'DDKalTest'


    def compile(self):
        """ compile DDKalTest """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

