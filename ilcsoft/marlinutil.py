##################################################
#
# MarlinUtil module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class MarlinUtil(MarlinPKG):
    """ Responsible for the MarlinUtil installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinUtil", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "GSL", "CLHEP", "GEAR", "LCIO" ]

        # cvs root
        self.download.root = "marlinreco"
