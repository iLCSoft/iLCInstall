##################################################
#
# CMakeModules module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import ConfigPKG

class CMakeModules(ConfigPKG):
    """ Responsible for installing the CMakeModules. """
    
    def __init__(self, userInput):
        ConfigPKG.__init__(self, "CMakeModules", userInput )

        self.reqfiles = [ ["LoadPackageMacro.cmake", "MacroLoadPackage.cmake"] ]

