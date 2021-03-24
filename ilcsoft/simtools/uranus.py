##################################################
#
# uranus module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Uranus(BaseILC):
    """ Responsible for the Uranus installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Uranus", "Uranus")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" , "CLHEP", "lcbase", "Leda", "lclib", "jsf", "Jupiter" ]
        self.reqfiles = [ ["lib/libU4TPCKalDetector.so"] ]
       
    def compile(self):
        """ compile Uranus """
        os.chdir( self.installPath )
        buildcmd='( export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" && make )'
        print("Compile Uranus will starts")
        print("buildcmd ="+buildcmd)
        if( os.system( buildcmd + " 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["URANUSROOT"]=self.installPath
#        self.envpath["PATH"].append( "$JSFROOT/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$URANUSROOT/lib" )
        self.env["SOSYMLINK"]="true"

        self.envcmds.append('export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" ')

