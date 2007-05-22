##################################################
#
# ROOT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class ROOT(BaseILC):
	""" Responsible for the ROOT installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "ROOT", "root")

		self.installSupport = False

		self.reqfiles = [ ["lib/libCore.so"], ["lib/libPhysics.so"], ["bin/root-config"] ]

	def init(self):

		BaseILC.init(self)

		self.env["ROOTSYS"] = self.installPath
		self.envpath["PATH"].append( "$ROOTSYS/bin" )
		self.envpath["LD_LIBRARY_PATH"].append( "$ROOTSYS/lib" )

		self.envbuild["USERLIBS"].append( "`root-config --libs`" )

