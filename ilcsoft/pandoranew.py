##################################################
#
# PandoraPFANew  module
#
# Author: F.Gaede, J.Engels, DESY
# Date: June 8 2010
#
##################################################

from util import *                                                                                                                                                            

# custom imports
from marlinpkg import MarlinPKG

class PandoraPFANew(MarlinPKG):
    """ Responsible for the PandoraPFANew installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "PandoraPFANew", userInput )

        self.download.root = 'PandoraPFANew'

        self.hasCMakeFindSupport = True

        self.optmodules = [ "ROOT" ]

        self.reqfiles = [ [ 
            'lib/libPandoraFramework.so', 'lib/libPandoraFramework.a', 'lib/libPandoraFramework.dylib',
            'lib/libPandoraPFANew.so', 'lib/libPandoraPFANew.a', 'lib/libPandoraPFANew.dylib',
            'lib/libPandoraSDK.so', 'lib/libPandoraSDK.a', 'lib/libPandoraSDK.dylib',
        ] ]

    def postCheckDeps(self):

        self.env["PANDORAPFANEW"] = self.installPath        
        
        self.envpath["LD_LIBRARY_PATH"].append( "$PANDORAPFANEW/lib" )


class MarlinPandora(MarlinPKG):
    """ Responsible for the MarlinPandora installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinPandora", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "GEAR", "PandoraPFANew", "LCIO" ]

        self.download.root = 'PandoraPFANew'


class PandoraAnalysis(MarlinPKG):
    """ Responsible for the PandoraAnalysis installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "PandoraAnalysis", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "GEAR", "LCIO", "ROOT" ]

        self.download.root = 'PandoraPFANew'

