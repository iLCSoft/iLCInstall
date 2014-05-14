##################################################
#
# FastJet module
#
# Author: Andre Sailer, CERN
# based on GSL module by J. Engels, Desy
# Date: Jul, 2010
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from marlinpkg import MarlinPKG
from util import *


class FastJetClustering(MarlinPKG):
    """ Responsible for the FastJetClustering installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "FastJetClustering", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "CLHEP", "GEAR", "GSL",  "LCIO", "FastJet" ]

        self.download.root = "marlinreco"


class FastJet(BaseILC):
    """ Responsible for the FastJet installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "FastJet", "FastJet")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[ "lib/libfastjet.so", "lib/libfastjet.a", "lib/libfastjet.dylib" ]]
    
    def setMode(self, mode):
        BaseILC.setMode(self, mode)       
        self.download.url = "http://www.lpthe.jussieu.fr/~salam/fastjet/repo/fastjet-" + self.version + ".tar.gz"
        
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

    def compile(self):
        """ compile FastJet """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os.system( "make distclean" )

        if( os.system( "../" + self.name + "/configure --prefix=" + self.installPath + " --enable-shared 2>&1 | tee -a " + self.logfile ) != 0 ):
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

        self.env["FastJet_HOME"] = self.installPath
        self.envpath["PATH"].append( "$FastJet_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$FastJet_HOME/lib" )
