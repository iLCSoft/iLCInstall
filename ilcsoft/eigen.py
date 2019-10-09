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
from baseilc import BaseILC
from util import *


class Eigen(BaseILC):
    """ Responsible for the Eigen configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Eigen", "eigen")

        # technically possible but set this to false
        self.download.supportHEAD = False
        self.hasCMakeBuildSupport = True
        
        self.reqmodules = [ "CMake" ]
        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'eigenteam'
        self.download.gitrepo = 'eigen-git-mirror'

        self.reqfiles = [
            ["include/eigen3/Eigen/src/Core/Matrix.h", "include/eigen3/Eigen/Core",
             "Eigen/src/Core/Matrix.h", "Eigen/Core" ]
        ]
        
    def compile(self):
        """ compile Eigen """
	     	
        trymakedir( self.buildPath )
        os.chdir( self.buildPath )
        
        self.envcmake["CMAKE_INSTALL_PREFIX"] = self.installPath
        
        if( self.rebuild ):
             tryunlink( "CMakeCache.txt" )
			
        # build software
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )
    
    def preCheckDeps(self):
        pass
        
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
