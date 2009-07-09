##################################################
#
# jupiter module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Jupiter(BaseILC):
    """ Responsible for the Jupiter installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Jupiter", "Jupiter")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqfiles = [ ["bin/"+self.os_ver.type+"-g++/Jupiter"] ]
        self.reqmodules = [ "Geant4" , "CLHEP" ]
       
    def compile(self):
        """ compile Jupiter """

        os.chdir( self.installPath )

        if( os.system( ". ${G4ENV_INIT}; unset G4UI_USE_XAW ; unset G4UI_USE_XM; make 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["JUPITERROOT"]=self.installPath
        self.env.setdefault( 'G4WORKDIR', self.installPath)
        
        self.envpath["PATH"].append( "$JUPITERROOT/bin/"+self.os_ver.type+"-g++" )
        self.envcmds.append(". ${G4ENV_INIT}")
