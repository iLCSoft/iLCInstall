##################################################
#
# CondDBMySQL module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class CondDBMySQL(BaseILC):
    """ Responsible for the CondDBMySQL installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CondDBMySQL", "CondDBMySQL")

        self.reqfiles = [ ["lib/libconddb.so","lib/libconddb.dylib"] ]

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'CondDBMySQL'

        
        self.reqmodules_buildonly = [ "MySQL" ]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if Version( self.version ) > '0.7.3':
            self.hasCMakeBuildSupport = True
        else:
            self.hasCMakeBuildSupport = False



    def downloadSources(self):
        BaseILC.downloadSources(self)

        if Version( self.version ) > '0.7.3':
            return

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

    def compile(self):
        """ compile CondDBMySQL """
        
        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            if Version( self.version ) <= '0.7.3':
                os_system( "make distclean" )
            tryunlink( "CMakeCache.txt" )

        if Version( self.version ) <= '0.7.3':
            cfg_cmd = "../" + self.name + "/configure --prefix=" + self.installPath \
                + " --with-mysql-lib=" + self.parent.module("MySQL").installPath + "/lib/mysql" \
                + " --with-mysql-inc=" + self.parent.module("MySQL").installPath + "/include/mysql" \
                + " --with-conddbprofile=localhost:mydb:calvin:hobbes 2>&1 | tee -a " + self.logfile 
        else:
            cfg_cmd = self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile

        if( os_system( cfg_cmd ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath + "/build" )
        os_system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["CondDBMySQL"] = self.installPath
        self.env["COND_DB_DEBUGLOG"] = '/dev/stdout'
        self.envpath["LD_LIBRARY_PATH"].append( "$CondDBMySQL/lib" )
