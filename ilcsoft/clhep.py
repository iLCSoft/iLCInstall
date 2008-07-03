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
        
        # no cmake build support
        self.useCMake = False
        
        if( self.mode == "install" ):
            if( Version( self.version ) < "1.9.1.1" ):
                self.abort( "ilcinstall only supports installation of CLHEP 1.9.1.1 or greater!" )
            if( Version( self.version ) == "2.0.3.0" and not isinPath( "xiar" )):
                self.abort( "CLHEP 2.0.3.0 requires xiar, that wasn't found in your system!" )

            # download url
            if( Version( self.version ) == "1.9.1.1" or Version( self.version ) == "2.0.1.1" ):
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

        self.env["CLHEP"] = self.installPath
        
        self.envpath["PATH"].append( "$CLHEP/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$CLHEP/lib" )

        # USERINCLUDES + USERLIBS
        self.envbuild["USERINCLUDES"].append( "-DUSE_CLHEP -I" + self.installPath + "/include" )
        self.envbuild["USERLIBS"].append( "-L" + self.installPath + "/lib -lCLHEP" )
