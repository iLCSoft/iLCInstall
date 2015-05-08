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

        self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.reqfiles = [
            ["boost/version.hpp", "boost/spirit.hpp"]
        ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "BOOST_HOME" ]
        
        self.env["BOOST_HOME"] = self.installPath

##        self.env["BOOST"] = "$BOOST_HOME"
##        self.env["BOOST_PATH"] = "$BOOST_HOME" # needed for mokka
##        if platform.architecture()[0] == '64bit':
##            self.env["BOOST_LIBDIR"] = "$BOOST_HOME/lib64/boost" # needed for mokka
##
##        self.envpath["PATH"].append( "$BOOST_HOME/bin" )
##        self.envpath["LD_LIBRARY_PATH"].append( "$BOOST_HOME/lib64/boost" )
##        self.envpath["LD_LIBRARY_PATH"].append( "$BOOST_HOME/lib64" )
##        self.envpath["LD_LIBRARY_PATH"].append( "$BOOST_HOME/lib/boost" )
##        self.envpath["LD_LIBRARY_PATH"].append( "$BOOST _HOME/lib" )

