##################################################
#
# MarlinPKG module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class MarlinPKG(BaseILC):
	""" Responsible for Marlin Packages installation process. """
	
	def __init__(self, name, userInput):
		BaseILC.__init__(self, userInput, name, name)
		self.isMarlinPKG = True
		self.buildDoc = False
		self.reqfiles = [ [ str("lib/lib" + name + ".a"), str("lib/lib" + name + ".so") ] ]
		# supported cmake "build_with" modules
		self.cmakebuildmodules = [ "Marlin", "MarlinUtil", "LCIO", "LCCD", "GEAR", "CondDBMySQL", "RAIDA", "ROOT", "GSL", "CLHEP", "CERNLIB" ]
	
	def compile(self):
		""" compile MarlinPKG """
		
		if( self.buildInMarlin() ):
			print "*** " + self.name + " will be built together with Marlin!!"
			return
	
		if( self.useCMake ):
			os.chdir( self.installPath + "/build" )
		else:
			os.chdir( self.installPath + "/src" )

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
		if( self.buildDoc ):
			os.chdir( self.installPath + "/src" )
			if(isinPath("doxygen")):
				print 80*'*' + "\n*** Creating C++ API documentation for " + self.name + " with doxygen...\n" + 80*'*'
				os.system( "ant cpp.doc 2>&1 | tee -a " + self.logfile )

	def buildInMarlin(self):
		""" check if this package is going to be built with Marlin """

		if( self.useCMake ):
			return False
		if( (self.marlin != None) and (self.marlin.mode=="install") and (self.name in self.marlin.optmodules) ):
			return True
		return False

	def init(self):
		
		BaseILC.init(self)
		
		# create a reference to the marlin module to avoid always typing self.parent.module("Marlin")
		self.marlin = self.parent.module("Marlin")
	
		if( self.useCMake ):
			if( self.name != "MarlinUtil" ):
				self.marlin.envpath["MARLIN_DLL"].append( self.installPath + "/lib/lib" + self.name + ".so" )
	
		# check if this package is going to be built with marlin
		if( self.buildInMarlin() ):
			# add this package to the list of packages in marlin
			if( self.name == "MarlinUtil" ):
				# small hack to get MarlinUtil in front of the others
				self.marlin.pkgs.insert(0,self)
			else:
				self.marlin.pkgs.append(self)
			# add the dependencies of this package to marlin
			self.marlin.buildWith( self.optmodules + self.reqmodules )
			# build documentation dependent on marlin settings
			self.buildDoc = self.marlin.buildDoc
			# build environment variables
			self.envoptbuild["USERINCLUDES"].append( "-I" + self.installPath + "/include" )
			self.envoptbuild["USERLIBS"].append( "-Wl,-whole-archive -L" + self.installPath \
					+ "/lib -l" + self.name + " -Wl,-no-whole-archive" )

		# check for doc tools
		if( self.buildDoc ):
			if( not isinPath("doxygen")):
				print "*** WARNING: doxygen was not found!! " + self.name + " documentation will not be built!!! "
		

