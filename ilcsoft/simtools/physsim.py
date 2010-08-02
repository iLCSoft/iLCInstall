##################################################
#
# physsim module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class physsim(BaseILC):
    """ Responsible for the physsim installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "physsim", "physsim")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" , "CLHEP", "lcbase", "lclib", "jsf", "Leda" ]
        self.reqfiles = [ ["lib/libPHYLIBTTNEW.a"] ]
       
    def compile(self):
        """ compile physsim """

        os.chdir( self.installPath )

        buildcmd='( export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${KFLIBROOT} -I${LCLIBROOT}\" && make )'
        if( os.system( buildcmd + " 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["KFLIBROOT"]=self.installPath
        self.env["SOSYMLINK"]="true"
        self.envcmds.append('export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${KFLIBROOT} -I${LCLIBROOT}\" ')

