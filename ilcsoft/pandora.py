##################################################
#
# PandoraPFA module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class PandoraPFA(MarlinPKG):
	""" Responsible for the PandoraPFA installation process. """
	
	def __init__(self, userInput):
		MarlinPKG.__init__(self, "PandoraPFA", userInput )

		# required modules
		self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR", "GSL", "ROOT" ]

		# cvs root
		self.download.root="marlinreco"
