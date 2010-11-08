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


class MarlinPandora(MarlinPKG):
    """ Responsible for the MarlinPandora installation process. """

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinPandora", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "GEAR", "PandoraPFANew", "LCIO" ]

        self.download.root = 'PandoraPFANew'
