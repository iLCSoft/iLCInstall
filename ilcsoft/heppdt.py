##################################################
#
# HepPDT module
#
# Author: F.Gaede, DESY
# based on GSL module by J. Engels, Desy
# Date: Apr, 2013
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class HepPDT(BaseILC):
    """ Responsible for the HepPDT installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "HepPDT","heppdt")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[
                "lib/libHepPDT.a",
                "lib/libHepPDT.dylib",
                "lib/libHepPID.a",
                "lib/libHepPID.dylib",
        ]]
    
    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "http://lcgapp.cern.ch/project/simu/HepPDT/download/HepPDT-" + self.version + ".tar.gz"
        
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

    def compile(self):
        """ compile HepPDT """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os_system( "make distclean" )

        if( os_system( "../" + self.name + "/configure --prefix=" + self.installPath + " 2>&1 | tee -a " + self.logfile ) != 0 ):
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

        self.env["HepPDT_HOME"] = self.installPath
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$HepPDT_HOME/bin" )
            self.envpath["LD_LIBRARY_PATH"].append( "$HepPDT_HOME/lib" )
