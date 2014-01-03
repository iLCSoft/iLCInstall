##################################################
#
# GDML module
#
# Author: F.Gaede, DESY
# Date: April 2013
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class GDML(BaseILC):
    """ Responsible for the GDML software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GDML", "gdml")
        
        self.reqfiles = [ ["lib/libgdml.so", "lib/libgdml.dylib"] ]
        
        self.download.supportedTypes = ["svn"]

        self.reqmodules = [ "XercesC" ]

    def compile(self):
        """ compile GDML """
        
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
                self.abort( "failed to execute gdml tests" )


    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        
        self.download.svnurl = 'svn://svn.freehep.org/lcdet/projects/gdml'

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

        self.env["GDML"] = self.installPath
        
        self.envpath["LD_LIBRARY_PATH"].append( "$GDML/lib" )
