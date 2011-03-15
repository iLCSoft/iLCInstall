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

        self.hasCMakeFindSupport = True

        # required modules
        self.reqmodules = [ "Marlin", "GSL", "CLHEP", "GEAR", "LCIO" , "CED" ]

        # cvs root
        self.download.root = "marlinreco"

