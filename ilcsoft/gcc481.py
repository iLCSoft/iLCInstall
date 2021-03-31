##################################################
#
# GCC481 module
#
# Author: Shaojun Lu, DESY
# Date: May, 2015
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class GCC481(BaseILC):
    """ Responsible for the GCC481 configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GCC481", "GCC481")

        self.installSupport = False

        self.reqfiles = [
                ["lib64/libcloog-isl.so"], 
                ["bin/gcc48"],
                ["bin/g++48"],
                ["bin/gfortran48"]
        ]


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCG_gcc_home"] = self.installPath
        self.envpath["PATH"].append( "$LCG_gcc_home/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$LCG_gcc_home/lib64" )

