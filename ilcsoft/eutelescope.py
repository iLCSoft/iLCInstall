##################################################
#
# Eutelescope module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class Eutelescope(MarlinPKG):
    """ Responsible for the Eutelescope installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "Eutelescope", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "CLHEP", "GSL", "LCIO" ]

        # optional modules
        self.optmodules = [ "GEAR", "AIDA" ]

        # cvs root
        self.download.root = "eutelescope"
