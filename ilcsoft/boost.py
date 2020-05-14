##################################################
#
# Boost module
# needs boost to be installed on the system
# just checks if header files are there
#
# Author: F.Gaede, DESY/CERN
# Date: May 2015
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Boost(BaseILC):
    """ Responsible for the Boost configuration process. """

    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Boost", "boost")

        self.installSupport = True
        self.hasCMakeBuildSupport = False
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [
            ["include/boost/version.hpp", "include/boost/spirit.hpp", "boost/version.hpp", "boost/spirit.hpp"],
            ["lib/libboost_system.so", "lib/libboost_system.dylib","lib/libboost_filesystem.so", "lib64/libboost_system.so", "lib64/libboost_filesystem.so"]
        ]

        # The boost build options.
        # See: https://boostorg.github.io/build/manual/develop/index.html
        self.buildopts = {}

    def genBuildOpts(self):
        opts = ""
        for k, v in self.buildopts.iteritems():
            opts = opts + k + "=" + str(v).strip() + " "
        return opts

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if( self.mode == "install" ):
            if( Version( self.version ) > "1.63.0" ):
                # Example: https://dl.bintray.com/boostorg/release/1.71.0/source/boost_1_71_0.tar.gz
                self.download.url = "https://dl.bintray.com/boostorg/release/%s/source/boost_%s.tar.gz" % (self.version, self.version.replace( "." , "_" ) )
            else:
                # Example: https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz
                self.download.url = "https://sourceforge.net/projects/boost/files/boost/%s/boost_%s.tar.gz" % (self.version, self.version.replace( "." , "_" ) )
        self.cmakeconfig = self.installPath + "/lib/cmake/Boost-" + self.version
        
    def compile(self):
        """ compile Boost """

        trymakedir( self.buildPath )
        os.chdir( self.installPath )

        if( self.rebuild ):
             tryunlink( "b2" )

        # Run the bootstrap script before-hand
        if( os_system( "./bootstrap.sh --prefix=" + self.installPath + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "Failed to run Boost bootstrap!!" )

        # Compile Boost
        if( os_system( "./b2 install --layout=system -q --build-dir=" + self.buildPath + "  --prefix=" + self.installPath + " " + self.genBuildOpts() + " ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "Failed to compile Boost!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "BOOST_ROOT" ]
        self.env["BOOST_ROOT"] = self.installPath
