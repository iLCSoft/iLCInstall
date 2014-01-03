##################################################
#
# LCDD module
#
# Author: F.Gaede, DESY
# Date: April 2013
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class LCDD(BaseILC):
    """ Responsible for the LCDD software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "LCDD", "lcdd")
        
        self.reqfiles = [ ["lib/liblcdd.so", "lib/liblcdd.dylib"] ]
                
        self.download.supportedTypes = ["svn"]

        self.reqmodules = [ "GDML" ]

    def compile(self):
        """ compile LCDD """
        
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
        
        self.download.svnurl = 'svn://svn.freehep.org/lcdet/projects/lcdd'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version
        else:
            self.download.svnurl += '/tags/' + self.version


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)                    

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCDD"] = self.installPath
        self.env["GDML_SCHEMA_DIR"]= "$LCDD"            

        self.envpath["LD_LIBRARY_PATH"].append( "$LCDD/lib" )
