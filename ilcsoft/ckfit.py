##################################################
#
# CKFit module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .marlinpkg import MarlinPKG

class CKFit(MarlinPKG):
    """ Responsible for the CKFit installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "CKFit", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "LCIO" ]

        # cvs root
        self.download.root = "marlinreco"

