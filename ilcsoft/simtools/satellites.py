##################################################
#
# Satellites module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Satellites(BaseILC):
    """ Responsible for the Satellites installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Satellites", "Satellites")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" , "CLHEP", "lcbase", "Leda", "lclib", "jsf", "Jupiter", "Uranus" ]
        self.reqfiles = [ ["lib/libS4TPCAnalysis.so"] ]
       
    def compile(self):
        """ compile Satellites """
        os.chdir( self.installPath )
        buildcmd='( export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" && make )'
        print("Compiling Satellites")
        print("buildcmd ="+buildcmd)
        if( os.system( buildcmd + " 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["SATELLITESROOT"]=self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$SATELLITES/lib" )
        self.env["SOSYMLINK"]="true"
        self.envcmds.append('export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" ')

