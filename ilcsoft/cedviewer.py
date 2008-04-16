##################################################
#
# CEDViewer module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class CEDViewer(MarlinPKG):
    """ Responsible for the CEDViewer installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "CEDViewer", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR", "CLHEP", "GSL" ]

        # cvs root
        self.download.root="marlinreco"

