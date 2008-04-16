##################################################
#
# SiliconDigi module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG

class SiliconDigi(MarlinPKG):
    """ Responsible for the SiliconDigi installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "SiliconDigi", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "LCIO", "GEAR", "CLHEP", "GSL" ]

        # cvs root
        self.download.root="marlinreco"

        # SiliconDigi is made of 3 packages
        self.sipkgs=["SiDetector","SiDigi","SiClustering"]

        # no documentation available
        self.buildDoc = False
