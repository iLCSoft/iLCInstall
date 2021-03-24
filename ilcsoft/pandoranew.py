##################################################
#
# PandoraPFANew  module
#
# Author: F.Gaede, J.Engels, DESY
# Date: June 8 2010
#
##################################################

from .util import *                                                                                                                                                            

# custom imports
from .marlinpkg import MarlinPKG
from .baseilc import BaseILC

class PandoraPFANew(BaseILC):
    """ Responsible for the PandoraPFANew installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "PandoraPFANew","PandoraPFANew" )

        self.download.supportedTypes = ["git"]
        self.download.svnurl = 'https://github.com/PandoraPFA/PandoraPFA.git'

        self.hasCMakeFindSupport = True

        self.optmodules = [ "ROOT" ]

        self.reqfiles = [ [ 
            'lib/libPandoraSDK.so', 'lib/libPandoraSDK.a', 'lib/libPandoraSDK.dylib',
            'lib/libPandoraMonitoring.so', 'lib/libPandoraMonitoring.a', 'lib/libPandoraMonitoring.dylib',
            'lib/libLCContent.so', 'lib/libLCContent.a', 'lib/libLCContent.dylib',
        ] ]

    def compile(self):
        """ compile  PandoraPFANew"""
        
        os.chdir( self.installPath+'/build' )
        
        if self.rebuild:
            tryunlink( "CMakeCache.txt" )

        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):

        self.env["PANDORAPFANEW"] = self.installPath        
        
        self.envpath["LD_LIBRARY_PATH"].append( "$PANDORAPFANEW/lib" )


class MarlinPandora(MarlinPKG):
    """ Responsible for the MarlinPandora installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinPandora", userInput )

        self.download.supportedTypes = ["git"]
        self.download.svnurl = 'https://github.com/PandoraPFA/MarlinPandora.git'

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "GEAR", "PandoraPFANew", "LCIO" ]


class PandoraAnalysis(MarlinPKG):
    """ Responsible for the PandoraAnalysis installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "PandoraAnalysis", userInput )

        self.download.supportedTypes = ["git"]
        self.download.svnurl = 'https://github.com/PandoraPFA/LCPandoraAnalysis.git'

        # required modules
        self.reqmodules = [ "Marlin", "GEAR", "LCIO", "ROOT" , "MarlinUtil" ]

    def postCheckDeps(self):

        MarlinPKG.postCheckDeps(self)

        self.env["PANDORA_ANALYSIS_DIR"] = self.installPath                
        self.envpath["LD_LIBRARY_PATH"].append( "$PANDORA_ANALYSIS_DIR/lib" )
        self.envpath["PATH"].append( "$PANDORA_ANALYSIS_DIR/bin" )
