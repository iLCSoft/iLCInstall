##################################################
#
# PathFinder module
#
# Author: Jan Engels, DESY
# Date: Jan, 2012
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class PathFinder(BaseILC):
    """ installs the PathFinder package """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "PathFinder", "pathfinder")

        self.reqfiles = [ ["lib/libPathFinder.a", "lib/libPathFinder.so", "lib/libPathFinder.dylib"] ]

        self.reqmodules = [ "ROOT" ]

        self.download.root = ''

    def compile(self):
        """ compile PathFinder """
        
        os.chdir( self.installPath + "/build")

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )
        
#    def postCheckDeps(self):
#        BaseILC.postCheckDeps(self)
#
#        self.env["PathFinder_HOME"] = self.installPath
#        self.envpath["PATH"].append( "$PathFinder_HOME/bin" )

