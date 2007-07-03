##################################################
#
# JAIDA module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class JAIDA(BaseILC):
	""" Responsible for the JAIDA software installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "JAIDA", "JAIDA")

		self.reqfiles = [ ["bin/aida-setup.sh"], ["lib/aida.jar"] ]

		self.installSupport = False
		self.hasCMakeSupport = False

		# Java is required for JAIDA
		self.reqmodules = [ "Java" ]

	def init(self):

		BaseILC.init(self)
		
		self.env["JAIDA_HOME"] = self.installPath
        
        # get the jar names in ${JAIDA_HOME}/lib
        jars_fp = glob.glob( self.installPath + "/*.jar" )
		jars = [ i.split('/')[-1] for i in jars_fp ]

		for jar in jars:
			self.envpath["CLASSPATH"].append( "$JAIDA_HOME/lib/" + jar + ".jar" )

