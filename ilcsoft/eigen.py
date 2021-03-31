##################################################
#
# Eigen module
# needs eigen to be installed on the system
# just checks if header files are there
#
# Author: F.Gaede, DESY/CERN
# Date: Sep 2016
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class Eigen(BaseILC):
    """ Responsible for the Eigen configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Eigen", "eigen")

        # technically possible but set this to false
        self.download.supportHEAD = False
        self.hasCMakeBuildSupport = True
        
        self.reqmodules = [ "CMake" ]
        self.download.supportedTypes = [ "wget" ]

        self.reqfiles = [
            ["include/eigen3/Eigen/src/Core/Matrix.h", "include/eigen3/Eigen/Core",
             "Eigen/src/Core/Matrix.h", "Eigen/Core" ]
        ]
        
    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        # installPath does not exists before setMode is called
        self.cmakeconfig = self.installPath + "/share/eigen3/cmake/"

        self.download.url = 'https://gitlab.com/libeigen/eigen/-/archive/%s/eigen-%s.tar.gz' % (self.version, self.version)
        
    def compile(self):
        """ compile Eigen """
	     	
        trymakedir( self.buildPath )
        os.chdir( self.buildPath )
        
        self.envcmake["CMAKE_INSTALL_PREFIX"] = self.installPath
        
        if( self.rebuild ):
             tryunlink( "CMakeCache.txt" )
			
        # build software
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )
    
    def preCheckDeps(self):
        pass
        
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.addCMakeCache( "EIGEN3_DIR", self.installPath, "Path to Eigen3" )
