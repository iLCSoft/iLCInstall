##################################################
#
# lcbase module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *

class lcbase(BaseILC):
    """ Responsible for the lcbase installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "lcbase", "lcbase")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" ]
        self.reqfiles = [ ["include/LCBASEConfig.h"] ]
       
    def compile(self):
        """ compile lcbase """

        os.chdir( self.installPath )

        if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )
        
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCBASEDIR"]=self.installPath
        self.envpath["PATH"].append("$LCBASEDIR/bin")
        
        
