##################################################
#
# HepPDT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class HepPDT(BaseILC):
    """ Responsible for the HepPDT installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "HepPDT", "HepPDT")

        self.hasCMakeSupport = False
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [ ["lib/libHepPDT.a", "lib/libHepPDT.so", "lib/libHepPDT.dylib"] ]

    def setMode(self, mode):

        BaseILC.setMode(self, mode)

        # no cmake build support
        self.useCMake = False
            
        if( self.mode == "install" ):
            self.download.url = "http://lcgapp.cern.ch/project/simu/HepPDT/download/HepPDT-" \
                    + self.version + ".tar.gz"
    
    def downloadSources(self):
        BaseILC.downloadSources(self)

        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )
        
        # create build directory
        trymakedir( self.installPath + "/build" )
    
    def compile(self):
        """ compile HepPDT """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os.system( "make distclean" )

        if( os.system( "../" + self.name + "/configure --prefix=" + self.installPath \
                + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath + "/build" )
        os.system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["HEPPDT"] = self.installPath
        
        self.envpath["LD_LIBRARY_PATH"].append( "$HEPPDT/lib" )

        # USERINCLUDES + USERLIBS
        self.envbuild["USERINCLUDES"].append( "-DUSE_SEPARATE_HEPPDT -I" + self.installPath + "/include" )
        self.envbuild["USERLIBS"].append( "-L" + self.installPath + "/lib -lHepPDT -lHepPID" )
