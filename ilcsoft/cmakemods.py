##################################################
#
# CMakeModules module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class CMakeModules(BaseILC):
    """ Responsible for installing the CMakeModules. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CMakeModules", "CMakeModules")

        # no documentation available
        self.buildDoc = False
    
        # cvs root
        self.download.root = "ilctools"
        
        self.reqfiles = [ ["LoadPackageMacro.cmake", "MacroLoadPackage.cmake"] ]

        # There is no FindCMakeModules.cmake module ;)
        self.hasCMakeSupport = False

        # CMakeModules are just 'unpacked'
        self.skipCompile = True

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        # CMakeModules are just 'unpacked'
        self.useCMake = False
