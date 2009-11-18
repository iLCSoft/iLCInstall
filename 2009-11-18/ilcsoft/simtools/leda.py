##################################################
#
# Leda module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Leda(BaseILC):
    """ Responsible for the Leda installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Leda", "Leda")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" , "CLHEP", "lcbase" ]
        self.reqfiles = [ ["lib/libAnlib.so"] ]
       
    def compile(self):
        """ compile Leda """

        os.chdir( self.installPath )

        buildcmd='( export IMAKEINCLUDE=\"-I${LCBASEDIR}\" && make )'
        if( os.system( buildcmd + " 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LEDAROOT"]=self.installPath
        self.env["SOSYMLINK"]="true"

        self.envcmds.append('export IMAKEINCLUDE=\"-I${LCBASEDIR}\" ')

