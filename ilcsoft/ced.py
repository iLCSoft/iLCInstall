##################################################
#
# CED module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class CED(BaseILC):
	""" Responsible for the CED software installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "CED", "CED")

		self.reqfiles = [ ["glced"] ]

		# no documentation available
		self.buildDoc = False

		# supported cmake "build_with" modules
		self.cmakebuildmodules = []

		self.download.root = "marlinreco"

	def compile(self):
		""" compile CED """
		
		os.chdir( self.installPath )

		if( self.useCMake ):
			os.chdir( "build" )

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
		
		self.env["CED"] = self.installPath
		
		self.envpath["PATH"].append( self.installPath )

		# install
		if( self.mode == "install" ):
			if( not os.path.exists( "/usr/include/GL/glut.h" )):
				self.abort( "glut-devel not found in your system!! you can get it from:\n" \
					+ "[ http://freeglut.sourceforge.net/ ]" )


