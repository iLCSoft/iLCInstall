##################################################
#
# Geant4 module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class Geant4(BaseILC):
    """ Responsible for the Geant4 configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Geant4", "geant4")

        self.installSupport = False
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.env["G4SYSTEM"] = "Linux-g++"

        self.reqfiles = [ ["lib/Linux-g++/libG4run.a", "sharedlib/Linux-g++/libG4run.so"] ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "G4INSTALL" ]
        self.env["G4INSTALL"] = self.installPath

        self.env["G4INCLUDE"] = "$G4INSTALL/include"

        if( not self.env.has_key( "G4ENV_INIT" )):
            if( not os.path.exists( self.realPath() + "/env.sh" )):
                self.abort( "you must specify a valid path for a geant4 environment shell script e.g.:\n"\
                        + "ilcsoft.module(\"Geant4\").env[\"G4ENV_INIT\"]=\"/foo/bar/env.sh\"" )
            self.env["G4ENV_INIT"]="$G4INSTALL/env.sh"

        self.envpath["LD_LIBRARY_PATH"].append( "$G4INSTALL/sharedlib/Linux-g++" )

