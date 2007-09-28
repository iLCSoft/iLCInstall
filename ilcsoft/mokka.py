##################################################
#
# Mokka module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Mokka(BaseILC):
    """ Responsible for the Mokka configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Mokka", "Mokka")

        self.hasCMakeSupport = False

        self.download.supportedTypes = ["wget", "cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anoncvs@pollin1.in2p3.fr:/home/flc/cvs
        self.download.accessmode = "pserver"
        self.download.server = "pollin1.in2p3.fr"
        self.download.root = "home/flc/cvs"

        self.reqfiles = [ ["bin/Linux-g++/Mokka"] ]
        self.reqmodules = [ "LCIO", "GEAR", "Geant4", "MySQL" ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.username = "anoncvs"
        self.download.password = "%ilc%"
        self.download.url = "http://polywww.in2p3.fr/activites/physique/geant4/tesla/www/mokka/software/mokka_tags/Mokka-mokka-" \
                + self.version + ".tgz"

    def compile(self):
        """ compile Mokka """

        os.chdir( self.installPath + "/source" )

        if( os.system( ". ${G4ENV_INIT}; make 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
    
    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

        if( self.download.type == "wget" and self.version=="HEAD" ):
            self.abort( "please download the HEAD version with cvs only, e.g.:\n" \
                    "ilcsoft.module(\"Mokka\").download.type=\"cvs\"" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        # force mokka to build itself in the installPath
        if( not self.env.has_key( "G4WORKDIR" )):
            self.env[ "G4WORKDIR" ] = self.installPath

        self.envpath["PATH"].append( self.installPath + "/bin" )
