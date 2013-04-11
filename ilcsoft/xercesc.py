##################################################
#
# XercesC module
#
# Author: F.Gaede, DESY
# based on GSL module by J. Engels, Desy
# Date: Apr, 2013
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class XercesC(BaseILC):
    """ Responsible for the XercesC installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "XercesC","xercesc")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[
                "lib/libxerces-c.a",
                "lib/libxerces-c.dylib",
        ]]
    
    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "http://www.apache.org/dist/xerces/c/3/sources/xerces-c-" + self.version + ".tar.gz"
        
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

    def compile(self):
        """ compile XercesC """

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

        self.env["XercesC_HOME"] = self.installPath
        self.envpath["PATH"].append( "$XercesC_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$XercesC_HOME/lib" )
