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
from .baseilc import BaseILC
from .util import *


class XercesC(BaseILC):
    """ Responsible for the XercesC installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "XercesC","xercesc")

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'apache'
        self.download.gitrepo = 'xerces-c'

        self.reqfiles = [[
                "lib/libxerces-c.a",
                "lib/libxerces-c.so",
                "lib/libxerces-c.dylib",
                "lib64/libxerces-c.a",
                "lib64/libxerces-c.so",
                "lib64/libxerces-c.dylib",
        ]]
    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        self.cmakeconfig = self.installPath + "/lib/cmake/XercesC"
    
    def compile(self):
        """ compile XercesC """

        os.chdir( self.installPath + "/build" )

        if self.rebuild:
            tryunlink( "CMakeCache.txt" )
        
        self.envcmake['CMAKE_INSTALL_PREFIX']=self.installPath

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
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
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$XercesC_HOME/bin" )
            self.envpath["LD_LIBRARY_PATH"].append( "$XercesC_HOME/lib" )
