##################################################
#
# DD4hep module
#
# Author: F.Gaede, DESY
# Date: May, 2013
#
##################################################

# custom imports
from .baseilc import BaseILC
import sys
from .util import *


class DD4hep(BaseILC):
    """ Responsible for the DD4hep configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "DD4hep", "DD4hep")

        #self.hasCMakeBuildSupport = False
        #self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'AIDASoft'
        self.download.gitrepo = 'DD4hep'

        self.reqfiles = [ ["lib/libDDCore.so", "lib/libDDCore.dylib" ]]

        self.reqmodules = [ "ROOT" , "LCIO", "GEAR", "Geant4" , "CLHEP" ,"Boost" ]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        self.cmakeconfig = self.installPath + "/cmake"


    def init(self):
        """ init DD4hep """
        BaseILC.init(self)

#        g4mod = self.parent.module("Geant4")
#        self.g4ver = Version( g4mod.version )


    def compile(self):
        """ compile DD4hep """

        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )
        
        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )


        if (self.nightlyBuild == True):
            
            for targetName in self.nightlyTargets:
                if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} " + targetName + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to compile!!" )
        else:
            if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )



    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'DD4HEP' ] = self.installPath
        self.env[ 'DD4HEP_ENVINIT' ] = "${DD4HEP}/bin/thisdd4hep.sh"
        self.envcmds.append('test -r ${DD4HEP_ENVINIT} && . ${DD4HEP_ENVINIT}')
        
        
