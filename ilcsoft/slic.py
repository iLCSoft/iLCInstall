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


class SLIC(BaseILC):
    """ Responsible for the SLIC software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "SLIC", "slic")
        
        self.reqfiles = [ ["build/lib/libslic.so", "build/lib/libslic.dylib", "build/bin/slic" ] ]
                
        self.download.supportedTypes = ["svn"]

        self.reqmodules = [ "LCDD", "GDML", "HepPDT", "XercesC" ]

    def compile(self):
        """ compile SLIC """
        
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

    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        
        self.download.svnurl = 'svn://svn.freehep.org/lcdet/projects/slic'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        elif '-pre' in self.version or '-dev' in self.version:
            self.download.svnurl += '/branches/' + self.version
        else:
            self.download.svnurl += '/tags/' + self.version


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)
       
#        if( self.mode == "install" ):
            # tests
#            if( self.makeTests ):
#                self.envcmake.setdefault("BUILD_SLIC_EXAMPLES","ON")                

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["SLIC"] = self.installPath
        
        # PATH
        #        self.envpath["PATH"].append( "$SLIC/tools" )
        self.envpath["PATH"].append( "$SLIC/build/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$SLIC/build/lib" )
