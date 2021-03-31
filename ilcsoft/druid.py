##################################################
#
# Druid module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .baseilc import BaseILC
from .util import *


class Druid(BaseILC):
    """ Responsible for the Druid installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Druid", "Druid")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False
        
        #self.download.supportHEAD = False

        self.download.root = ""

        self.reqmodules = [ "LCIO" , "GEAR", "ROOT" ]

        self.reqfiles = [[ "bin/Druid" ]]

    
    def compile(self):
        """ compile Druid """

        os.chdir( self.installPath + "/src" )

        if( self.rebuild ):
            os_system( "make clean" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["DRUID"] = self.installPath
        self.envpath["PATH"].append( "$DRUID/bin" )
