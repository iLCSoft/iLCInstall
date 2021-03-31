##################################################
#
# SIO module
#
# Author: Remi Ete, DESY
# Date: Oct, 2019
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class SIO(BaseILC):
    """ Responsible for the SIO software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "SIO", "sio")
        
        self.reqfiles = [ ["lib64/libsio.a", "lib64/libsio.so",
                          "lib/libsio.a", "lib/libsio.so", "lib/libsio.dylib" ] ]
        self.reqmodules = [ "CMake" ]

        # supported download types
        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'SIO'
        
    def preCheckDeps(self):
        pass

    def compile(self):
        """ compile SIO """
        
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
                self.abort( "failed to execute sio tests" )
                

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.env["SIO_DIR"] = self.installPath
        # PATH and LD_LIBRARY_PATH
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$SIO_DIR/bin" )
            self.envpath["LD_LIBRARY_PATH"].append( "$SIO_DIR/lib" )

