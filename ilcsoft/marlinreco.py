##################################################
#
# MarlinReco module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class MarlinReco(MarlinPKG):
    """ Responsible for the MarlinReco installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinReco", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "CLHEP", "GEAR", "GSL", "CERNLIB", "LCIO" ]

        # optional modules
        self.optmodules = [ "AIDA" ]

