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

		self.hasCMakeSupport = False

		self.skipCompile = True
