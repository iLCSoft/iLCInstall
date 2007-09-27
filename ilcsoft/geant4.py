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
        self.hasCMakeSupport = False

        self.reqfiles = [ ["lib/Linux-g++/libG4run.a", "sharedlib/Linux-g++/libG4run.so"] ]

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

        if( not self.env.has_key( "G4ENV_INIT" )):
            if( not os.path.exists( self.installPath + "/env.sh" )):
                self.abort( "you must specify a valid path for a geant4 environment shell script"\
                        + "e.g. ilcsoft.module(\"Geant4\").env[\"G4ENV_INIT\"]=\"/foo/bar/env.sh\"" )
            self.env["G4ENV_INIT"]=self.installPath + "/env.sh"

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["G4INSTALL"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$G4INSTALL/sharedlib/Linux-g++" )
