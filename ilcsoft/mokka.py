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

        # no cmake build support
        self.useCMake = False

        # force download type to cvs for HEAD version
        if( self.download.type == "wget" and self.version=="HEAD" ):
            self.download.type = "cvs"

        # force download type to cvs if set to ccvssh
        if( self.download.type == "ccvssh" ):
            self.download.type = "cvs"
        
        self.download.username = "anoncvs"
        self.download.password = "%ilc%"
        self.download.url = "http://polywww.in2p3.fr/activites/physique/geant4/tesla/www/mokka/software/mokka_tags/Mokka-" \
                + self.version + ".tgz"

    def compile(self):
        """ compile Mokka """

        os.chdir( self.installPath + "/source" )
        
        if( os.system( ". ${G4ENV_INIT}; unset G4UI_USE_XAW ; unset G4UI_USE_XM ; make 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        # force mokka to build itself in the installPath
        if( not self.env.has_key( "G4WORKDIR" )):
            self.env[ "G4WORKDIR" ] = self.installPath

        if( not self.env.has_key( "G4UI_USE_TCSH" )):
            self.env[ "G4UI_USE_TCSH" ] = 1 

        self.envpath["PATH"].append( self.installPath + "/bin/Linux-g++" )
        #self.envpath["LD_LIBRARY_PATH"].append( "$LCIO/lib" )
        self.envcmds.append(" . ${G4ENV_INIT} ")


