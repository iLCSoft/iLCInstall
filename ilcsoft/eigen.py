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

        self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.reqfiles = [
            ["include/eigen3/Eigen/src/Core/Matrix.h", "include/eigen3/Eigen/Core" ]
        ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "EIGEN_INCLUDE_DIR" ]
        self.env["EIGEN_INCLUDE_DIR"] = self.installPath+'/include/eigen3/'

