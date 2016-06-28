##################################################
#
# lcgeo module
#
# Author: F.Gaede, DESY
# Date: May, 2013
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class lcgeo(BaseILC):
    """ Responsible for the lcgeo configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "lcgeo", "lcgeo")


        self.reqfiles = [ ["lib/liblcgeo.so", "lib/liblcgeo.dylib" ]]

        self.reqmodules = [ "DD4hep" , "ROOT" , "LCIO", "GEAR", "Geant4" ]

        self.download.supportedTypes = ["GitHub"]
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'lcgeo'

    def init(self):
        """ init lcgeo """
        BaseILC.init(self)

#        g4mod = self.parent.module("Geant4")
#        self.g4ver = Version( g4mod.version )


    def compile(self):
        """ compile lcgeo """

        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )
        
        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if (self.nightlyBuild == True):

            for targetName in self.nightlyTargets:
                if( os.system( "source ../build_env.sh ; make ${MAKEOPTS} " + targetName + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to compile!!" )
        else:
            if( os.system( "source ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os.system( "source ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'lcgeo_DIR' ] = self.installPath

        self.envpath["PATH"].append( "$lcgeo_DIR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$lcgeo_DIR/lib" )
        self.envpath["PYTHONPATH"].append( "$lcgeo_DIR/lib/python" )

        
