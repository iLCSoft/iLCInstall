##################################################
#
# LCCD module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class LCCD(BaseILC):
	""" Responsible for the LCCD software installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "LCCD", "lccd")

		self.reqfiles = [ ["lib/liblccd.a", "lib/liblccd.so"] ]

		# LCIO is required for building LCCD
		self.reqmodules = [ "LCIO" ]

		# optional modules
		self.optmodules = [ "CondDBMySQL", "MySQL" ]

		# supported cmake "build_with" modules
		self.cmakebuildmodules = [ "CondDBMySQL" ]

	def compile(self):
		""" compile LCCD """
		
		os.chdir( self.installPath + "/source" )

		if( self.useCMake ):
			os.chdir( self.installPath + "/build" )

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
		
		# build documentation
	def buildDocumentation(self):
		if( self.buildDoc ):
			os.chdir( self.installPath + "/source" )
			if(isinPath("doxygen")):
				print 80*'*' + "\n*** Creating C++ API documentation for " + self.name + " with doxygen...\n" + 80*'*'
				os.system( "gmake doc 2>&1 | tee -a " + self.logfile )

	def init(self):

		BaseILC.init(self)
		
		self.env["LCCD"] = self.installPath

		if( self.mode == "install" ):

			self.env["LCCDVERSION"] = self.version
			if( self.debug ):
				self.env["LCCDDEBUG"] = "1"
			
			# check for doc tools
			if( self.buildDoc ):
				if( not isinPath("doxygen")):
					print "*** WARNING: doxygen was not found!! " + self.name + " documentation will not be built!!! "
