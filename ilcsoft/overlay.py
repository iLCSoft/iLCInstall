##################################################
#
# Overlay module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class Overlay(MarlinPKG):
    """ Responsible for the Overlay installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "Overlay", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "LCIO", "CLHEP", "MarlinUtil" ]

        # cvs root
        self.download.root="marlin"

