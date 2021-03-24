##################################################
#
# BBQ Module
#
# Author: Jan Engels, DESY
# Date: May 2012
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class BBQ(BaseILC):
    """ Responsible for the BBQ software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "BBQ", "bbq")

        self.reqfiles = [ ["lib/libBBQ.so","lib/libBBQ.a","lib/libBBQ.dylib"] ]

        self.reqmodules = [ "LCIO", "GEAR", "ROOT" ]

        self.download.root = ''
        
        self.hasCMakeFindSupport = False

    def compile(self):
        """ compile BBQ """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

