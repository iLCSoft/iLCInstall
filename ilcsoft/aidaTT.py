##################################################
#
# aidaTT module
#
# Author: F.Gaede, CERN, DESY
# Date: Nov, 2014
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class aidaTT(BaseILC):
    """ Responsible for the aidaTT configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "aidaTT", "aidaTT")

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'AIDASoft'
        self.download.gitrepo = 'aidaTT'

        self.reqfiles = [ ["lib/libaidaTT.so", "lib/libaidaTT.dylib" ]]


#        self.reqmodules = [ "Eigen" , "GBL", "DD4hep" , "LCIO", ]
        self.reqmodules = [ "GSL" , "GBL", "DD4hep" , "LCIO", ]


    def init(self):
        """ init aidaTT """
        BaseILC.init(self)


    def compile(self):
        """ compile aidaTT """

        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )
        
        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )



    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'AIDATT' ] = self.installPath

        self.envpath["PATH"].append( "$AIDATT/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$AIDATT/lib" )
        
        
