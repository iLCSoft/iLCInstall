##################################################
#
# KiTrack module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class KiTrack(BaseILC):
    """ Responsible for the KiTrack software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "KiTrack", "KiTrack")

        self.reqfiles = [ ["lib/libKiTrack.so","lib/libKiTrack.a","lib/libKiTrack.dylib"] ]

        self.reqmodules = [ "Marlin", "ROOT" ]

        # svn root
        self.download.root = "marlinreco"

    def compile(self):
        """ compile KiTrack """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )



class KiTrackMarlin(BaseILC):
    """ Responsible for the KiTrackMarlin software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "KiTrackMarlin", "KiTrackMarlin")

        self.reqfiles = [ ["lib/libKiTrackMarlin.so","lib/libKiTrackMarlin.a","lib/libKiTrackMarlin.dylib"] ]

        self.reqmodules = [ "KiTrack", "MarlinTrk", "GSL" ]

        # svn root
        self.download.root = "marlinreco"

    def compile(self):
        """ compile KiTrackMarlin """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

