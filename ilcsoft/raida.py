##################################################
#
# RAIDA module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class RAIDA(BaseILC):
	""" Responsible for the RAIDA software installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "RAIDA", "RAIDA")

		self.reqfiles = [ ["bin/aida-config"], ["lib/libRAIDA.a", "lib/libRAIDA.so", "lib/libRAIDA.dylib"] ]

		# ROOT is required for building RAIDA
		self.reqmodules = [ "ROOT" ]

		# supported cmake "build_with" modules
		self.cmakebuildmodules = []

		# no documentation available
		self.buildDoc = False
	
		# cvs root
		self.download.root = "ilctools"

	def compile(self):
		""" compile RAIDA """
		
		os.chdir( self.installPath + "/src")

		if( self.useCMake ):
			os.chdir( self.installPath + "/build")

		if( self.rebuild ):
			if( self.useCMake ):
				tryunlink( "CMakeCache.txt" )
			else:
				os.system( "gmake clean" )

		# build software
		if( self.useCMake ):
			if( os.system( "cmake " + self.genCMakeCmd() + " .. 2>&1 | tee -a " + self.logfile ) != 0 ):
				self.abort( "failed to configure!!" )

		if( os.system( "gmake 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to compile!!" )

		if( self.useCMake ):
			if( os.system( "gmake install 2>&1 | tee -a " + self.logfile ) != 0 ):
				self.abort( "failed to install!!" )
		
	def init(self):

		BaseILC.init(self)
		
		self.env["RAIDA_HOME"] = self.installPath
		self.envpath["PATH"].append( "$RAIDA_HOME/bin" )

		if( self.mode == "install" ):
			if( self.debug ):
				self.env["RAIDADEBUG"] = "1"
			else:
				self.env["RAIDADEBUG"] = "0"
