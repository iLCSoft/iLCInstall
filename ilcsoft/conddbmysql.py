##################################################
#
# CondDBMySQL module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class CondDBMySQL(BaseILC):
	""" Responsible for the CondDBMySQL installation process. """
	
	def __init__(self, userInput):
		BaseILC.__init__(self, userInput, "CondDBMySQL", "CondDBMySQL")

		self.reqfiles = [ ["lib/libconddb.so"] ]

		# cvs root
		self.download.root = "calice"

		self.reqmodules_buildonly = [ "MySQL" ]
	
	def downloadSources(self):
		BaseILC.downloadSources(self)

		# move sources to a subdirectory
		os.renames( self.version, self.name )
		os.renames( self.name, self.version + "/" + self.name )

		# create build directory
		os.makedirs( self.installPath + "/build" )

	def compile(self):
		""" compile CondDBMySQL """
		
		os.chdir( self.installPath + "/build" )

		if( self.rebuild ):
			os.system( "make distclean" )

		if( os.system( "../" + self.name + "/configure --prefix=" + self.installPath \
				+ " --with-mysql-lib=" + self.parent.module("MySQL").installPath + "/lib/mysql" \
				+ " --with-mysql-inc=" + self.parent.module("MySQL").installPath + "/include/mysql" \
				+ " --with-conddbprofile=localhost:mydb:calvin:hobbes 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to configure!!" )

		if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to compile!!" )

		if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
			self.abort( "failed to install!!" )

	def cleanupInstall(self):
		BaseILC.cleanupInstall(self)
		os.chdir( self.installPath + "/build" )
		os.system( "make clean" )

	def init(self):

		BaseILC.init(self)
		
		self.env["CondDBMySQL"] = self.installPath
		self.envpath["LD_LIBRARY_PATH"].append( "$CondDBMySQL/lib" )
