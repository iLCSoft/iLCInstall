##################################################
#
# ninja module
#
# Author: M. Petric, CERN
# Date: mar, 2017
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class ninja(BaseILC):
    """ Responsible for the ninja installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "ninja","Ninja")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [[
                "ninja",
        ]]
    
    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "https://github.com/ninja-build/ninja/archive/v" + self.version + ".tar.gz"
        
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )


    def compile(self):
        """ compile ninja """


        if( self.rebuild ):
            os_system( "./configure.py --bootstrap" )

        if( os_system( "configure.py --bootstrap" ) ):
            self.abort( "failed to bootstrap!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os_system( "find . \! -name 'ninja' -delete" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["ninja_HOME"] = self.installPath
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$ninja_HOME" )
