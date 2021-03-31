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
from .baseilc import BaseILC
from .marlinpkg import MarlinPKG
from .util import *


class FastJetClustering(MarlinPKG):
    """ Responsible for the FastJetClustering installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "FastJetClustering", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "CLHEP", "GEAR", "GSL",  "LCIO", "FastJet" ]

        self.download.supportedTypes = [ "GitHub" ]
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'obsolete_FastJetClustering'


class FastJet(BaseILC):
    """ Responsible for the FastJet installation process. """

    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "FastJet", "FastJet")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[ "lib/libfastjet.so", "lib/libfastjet.a", "lib/libfastjet.dylib" ]]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        self.download.url = "http://fastjet.fr/repo/fastjet-" + self.version + ".tar.gz"

    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )

        #optionally donwload the fjcontrib package
        if len(self.fjcontrib_version) > 0:
            self.reqfiles.append( [ "lib/libfastjetcontribfragile.so",  "lib/libfastjetcontribfragile.dylib" ] )

            os.chdir( self.installPath )
            print("+ Downloading FastJetContrib version : ", self.fjcontrib_version)

            os_system( "wget http://fastjet.hepforge.org/contrib/downloads/fjcontrib-"+self.fjcontrib_version+".tar.gz")
            os_system( "tar -xzvf fjcontrib-"+self.fjcontrib_version+".tar.gz")

    def compile(self):
        """ compile FastJet """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os_system( "make distclean" )

        if( os_system( "../" + self.name + "/configure --prefix=" + self.installPath + " CXXFLAGS=\"$CXXFLAGS\" --enable-auto-ptr=no --enable-shared 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


        if( len(self.fjcontrib_version) > 0) :

            os.chdir( self.installPath+"/fjcontrib-"+self.fjcontrib_version )

            if( os_system( "./configure --fastjet-config="+self.installPath+"/bin/fastjet-config CXXFLAGS=\"$CXXFLAGS\"  2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure!!" )

            if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )

            if( os_system( "make ${MAKEOPTS} fragile-shared-install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )

            if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath + "/build" )
        os_system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["FastJet_HOME"] = self.installPath
        self.envpath["PATH"].append( "$FastJet_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$FastJet_HOME/lib" )
        
        self.addCMakeCache( "FastJet_DIR", self.installPath, "Path to FastJet" ) 
