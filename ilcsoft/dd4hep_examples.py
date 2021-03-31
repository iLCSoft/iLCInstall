##################################################
#
# DD4hepExamples module
#
# Author: F.Gaede, DESY
# Date: Feb, 2015
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class DD4hepExamples(BaseILC):
    """ Responsible for the DD4hepExamples configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "DD4hepExamples", "DD4hepExamples")

        #self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "svn"]

        self.reqfiles = [ ["lib/libSimpleDetector.so", "lib/libSimpleDetector.dylib" ]]

        self.reqmodules = [ "DD4hep" , "ROOT" , "LCIO", "GEAR", "Geant4"]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)
            
        self.download.type = "svn"
        self.download.svnurl = 'https://github.com/AIDASoft/DD4hep'
        # simply do an svn co from the git repository

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
#        elif 'pre' in self.version or 'dev' in self.version:
#            self.download.svnurl += '/branches/' + self.version
        else:
            self.download.svnurl += '/tags/' + self.version

        self.download.svnurl += '/examples/'

    def init(self):
        """ init DD4hepExamples """
        BaseILC.init(self)

#        g4mod = self.parent.module("Geant4")
#        self.g4ver = Version( g4mod.version )


    def compile(self):
        """ compile DD4hepExamples """

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
        self.env[ 'DD4hepExamples' ] = self.installPath
        self.envpath["PATH"].append( "$DD4hepExamples/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$DD4hepExamples/lib" )
        
        
