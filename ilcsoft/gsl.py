##################################################
#
# GSL module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class GSL(BaseILC):
    """ Responsible for the GSL installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GSL", "gsl")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[
                "lib/libgsl.a",
                "lib/libgsl.so",
                "lib64/libgsl.so",
                "lib/libgsl.dylib",
                "lib/shared/libgsl.so",
                "lib64/shared/libgsl.so",
                "lib/shared/libgsl.dylib",
        ]]
    
    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "ftp://ftp.gnu.org/gnu/gsl/gsl-" + self.version + ".tar.gz"
        
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

    def compile(self):
        """ compile GSL """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os.system( "make distclean" )

        if( os.system( "../" + self.name + "/configure --prefix=" + self.installPath + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath + "/build" )
        os.system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["GSL_HOME"] = self.installPath
        self.envpath["PATH"].append( "$GSL_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$GSL_HOME/lib" )
