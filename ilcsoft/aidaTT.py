##################################################
#
# aidaTT module
#
# Author: F.Gaede, CERN, DESY
# Date: Nov, 2014
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class aidaTT(BaseILC):
    """ Responsible for the aidaTT configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "aidaTT", "aidaTT")

        self.download.supportedTypes = [ "svn"]
        self.download.root = "aidasoft"

        self.reqfiles = [ ["lib/libaidaTT.so", "lib/libaidaTT.dylib" ]]

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

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "source ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "source ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )



    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'AIDATT' ] = self.installPath

        self.envpath["PATH"].append( "$AIDATT/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$AIDATT/lib" )

        self.envcmds.append('test -r ${G4ENV_INIT} && { cd $(dirname ${G4ENV_INIT}) ; . ./$(basename ${G4ENV_INIT}) ; cd $OLDPWD ; }')
        
        
