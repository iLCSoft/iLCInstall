##################################################
#
# GBL module for general broken lines
#
# Author: Ch. Rosemann, DESY -- based on work by Jan Engels
# Date: Mar, 2013
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class GBL(BaseILC):
    """ Responsible for the GBL software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GBL", "GBL")

        self.reqfiles = [ ["lib/libGBL.so","lib/libGBL.a","lib/libGBL.dylib"] ]

        self.reqmodules = [ "ROOT" ]

    def compile(self):
        """ compile GBL """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["GBL"] = self.installPath

        self.envpath["LD_LIBRARY_PATH"].append( '$GBL/lib' )

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.svnurl = 'https://svnsrv.desy.de/public/GeneralBrokenLines'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk/cpp'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version + '/cpp'
        else:
            self.download.svnurl += '/tags/' + self.version + '/cpp'
