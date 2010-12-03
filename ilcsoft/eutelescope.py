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
        self.reqmodules = [ "Marlin",  "LCIO" ]

        # optional modules
        self.optmodules = [ "GEAR", "AIDA" , "MarlinUtil", "CLHEP", "GSL", "CED", "ROOT" ]

        # cvs root
        self.download.root = "eutelescope"

    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.env["EUTELESCOPE"] = self.installPath
        self.envpath["PATH"].append( '$EUTELESCOPE/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( '$EUTELESCOPE/lib' )

