##################################################
#
# CLHEP module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class CLHEP(BaseILC):
	""" Responsible for the CLHEP installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "CLHEP", "CLHEP")

		self.download.supportHEAD = False
		self.download.supportedTypes = ["wget"]

		self.reqfiles = [ ["lib/libCLHEP.a", "lib/libCLHEP.so", "lib/libCLHEP.dylib"] ]

	def setMode(self, mode):

		BaseILC.setMode(self, mode)
			
		if( self.mode == "install" ):
			
			# download url
			if( self.version == "1.9.1.1" or self.version == "2.0.1.1" ):
				self.download.url = "http://proj-clhep.web.cern.ch/proj-clhep/export/share/CLHEP/" \
						+ self.version + "/clhep-" + self.version + ".tgz"
			else:
				self.download.url = "http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/distributions/clhep-" + self.version + ".tgz"
	
	def downloadSources(self):
		BaseILC.downloadSources(self)

		# create build directory
		trymakedir( self.installPath + "/build" )
	
	def compile(self):
		""" compile CLHEP """

		os.chdir( self.installPath + "/build" )

		if( os.system( "../CLHEP/configure --prefix=" + self.installPath + " 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to configure!!" )

		if( os.system( "gmake 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to compile!!" )

		if( os.system( "gmake install 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to install!!" )
	
	def cleanupInstall(self):
		BaseILC.cleanupInstall(self)
		os.chdir( self.installPath + "/build" )
		os.system( "gmake clean" )

	def init(self):
		
		BaseILC.init(self)
	
		self.env["CLHEP"] = self.installPath
		
		self.envpath["PATH"].append( "$CLHEP/bin" )
		self.envpath["LD_LIBRARY_PATH"].append( "$CLHEP/lib" )

		# USERINCLUDES + USERLIBS
		self.envbuild["USERINCLUDES"].append( "-D USE_CLHEP -I" + self.installPath + "/include" )
		self.envbuild["USERLIBS"].append( "-L" + self.installPath + "/lib -lCLHEP" )
