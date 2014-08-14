##################################################
#
# Standalone DDSegmentation module seperate from 
# DD4hep for SLIC installation
#
# Author: Jeremy McCormick, SLAC
# Date: 14 August 2014
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class DDSegmentation(BaseILC):
    """ Responsible for the software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "DDSEGMENTATION", "ddsegmentation")
        
        self.reqfiles = [ ["lib/libDDSegmentation.so", "lib/libDDSegmentation.dylib"] ]
                
        self.download.supportedTypes = ["svn"]

    def compile(self):
        """ compile """
        
        os.chdir( self.installPath+'/build' )
        
        if self.rebuild:
            tryunlink( "CMakeCache.txt" )

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # execute ctests
        if( self.makeTests ):
            
            if( os.system( "make tests && make test" ) != 0 ):
                self.abort( "failed to execute lcdd tests" )


    def setMode(self, mode):
        
        BaseILC.setMode(self, mode)

        self.download.svnurl = 'https://svnsrv.desy.de/public/aidasoft/DD4hep'
        
        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk/DDSegmentation/'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version + '/DDSegmentation/'
        else:
            self.download.svnurl += '/tags/' + self.version + '/DDSegmentation/'


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)                    

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["DDSEGMENTATION"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$DDSEGMENTATION/lib" )
