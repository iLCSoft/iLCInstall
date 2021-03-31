##################################################
#
# lcgeo module
#
# Author: F.Gaede, DESY
# Date: May, 2013
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class lcgeo(BaseILC):
    """ Responsible for the lcgeo configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "lcgeo", "lcgeo")

        #self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'lcgeo'

        self.reqfiles = [ ["lib/liblcgeo.so", "lib/liblcgeo.dylib" ]]

        self.reqmodules = [ "DD4hep" , "ROOT" , "LCIO", "GEAR", "Geant4" ]
#        self.reqmodules = [ "DD4hep" , "ROOT" , "LCIO", "GEAR", "Geant4" , "CLHEP" ]


#    def setMode(self, mode):
#        BaseILC.setMode(self, mode)
#
#        self.download.type = "svn"
#        
#        self.download.svnurl = 'http://llrforge.in2p3.fr/svn/lcgeo'
#
#        if( Version( self.version ) == 'HEAD' ):
#            self.download.svnurl += '/trunk'
#        elif 'pre' in self.version or 'dev' in self.version:
#            self.download.svnurl += '/branches/' + self.version
#        else:
#            self.download.svnurl += '/tags/' + self.version


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

        self.env[ 'lcgeo_DIR' ] = self.installPath
        self.env[ 'lcgeo_ENVINIT' ] = "${lcgeo_DIR}/bin/thislcgeo.sh"
        self.envcmds.append('test -r ${lcgeo_ENVINIT} && . ${lcgeo_ENVINIT}')
        
        
