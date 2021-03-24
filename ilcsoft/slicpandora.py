##################################################
#
# SLIC module
#
# Author: F.Gaede, DESY
# Date: April 2013
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class SlicPandora(BaseILC):
    """ Responsible for the slicPandora software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "SlicPandora", "slicPandora")
        
        self.reqfiles = [ ["build/lib/libslicPandora.so", "build/lib/libslicPandora.dylib", "build/bin/PandoraFrontend" ] ]
            
        # set some cvs variables
        #self.download.env["CVSROOT"]=":pserver:anonymous@cvs.freehep.org:/cvs/lcd"
        #self.download.supportedTypes = ["cvs"]
        #self.download.accessmode = "pserver"
        #self.download.server = "cvs.freehep.org"
        #self.download.root = "cvs/lcd"
        #self.download.project = "slicPandora"

        self.download.supportedTypes = [ "svn" ]

        self.reqmodules = [ "LCIO", "PandoraPFANew" ]

    def setMode(self, mode):

        BaseILC.setMode(self, mode)

        self.download.svnurl = 'svn://svn.freehep.org/lcdet/projects/slicPandora'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version
        else:
            self.download.svnurl += '/tags/' + self.version

        print("slicPandora SVN URL: ", self.download.svnurl)

    def compile(self):
        """ compile slicPandora """
        
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
                self.abort( "failed to execute slic tests" )

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)                       

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["SLICPANDORA"] = self.installPath
        
        # PATH
        self.envpath["PATH"].append( "$SLICPANDORA/build/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$SLICPANDORA/build/lib" )
