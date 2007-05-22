##################################################
#
# CMake module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class CMake(BaseILC):
	""" Responsible for the CMake installation process. """
	
	def __init__(self, userInput="auto"):
		BaseILC.__init__(self, userInput, "CMake", "CMake")

		self.download.supportHEAD = False
		self.hasCMakeSupport = False
		self.download.supportedTypes = ["wget"]

		self.reqfiles = [ ["bin/cmake"], ["bin/cpack"], ["bin/ctest"] ]

		if( userInput == "auto" ):
			self.autoDetect()

	def autoDetectPath(self, abort=False):
		""" tries to auto detect cmake dir from system settings.
			- returns empty string in case of failure
			- otherwise returns cmake dir """

		dir = ""

		if( isinPath("cmake")):
			out = commands.getoutput("which cmake").strip()
			ind = out.find("/bin/cmake")
			dir = out[:ind]
		elif(abort):
			self.abort( "failed trying to get the default CMake settings!!\n" )

		return dir

	def autoDetectVersion(self, abort=False):
		""" tries to auto detect version by parsing the output of cmake --version.
			- returns empty string in case of failure
			- otherwise returns cmake version """

		out = commands.getstatusoutput( self.realPath() + r"/bin/cmake --version 2>&1" )

		if( out[0] != 0 ):
			return ""

		# substitute version separators through whitespaces
		sep = string.maketrans( ".-_", "   " )
		ver = out[1].translate( sep )
		# split versions by whitespaces
		ver = ver.split()
		# remove characters from list elements
		ver = [ i.strip(string.letters) for i in ver ]
		# remove empty elements
		ver = [ i for i in ver if i ]
		# create a string out of the elements
		dot = "."
		return dot.join(ver)

	def setMode(self, mode):

		BaseILC.setMode(self, mode)
			
		if( self.mode == "install" ):
			# download url
			self.download.url = "http://www.cmake.org/files/v" + \
					self.version[:3] + "/cmake-" + self.version + ".tar.gz"
		
	def downloadSources(self):
		BaseILC.downloadSources(self)

		# move sources to a subdirectory
		os.renames( self.version, self.name )
		os.renames( self.name, self.version + "/" + self.name )

		# create build directory
		os.makedirs( self.installPath + "/build" )


	def compile(self):
		""" compile CMake """

		os.chdir( self.installPath + "/build" )

		if( self.rebuild ):
			os.system( "gmake clean" )

		if( os.system( "../" + self.name + "/configure --prefix=" + self.installPath + " 2>&1 | tee -a " + self.logfile ) != 0 ):
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
		
		self.env["CMake_HOME"] = self.installPath
		self.envpath["PATH"].append( "$CMake_HOME/bin" )
