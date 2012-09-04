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
        self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR", "CLHEP", "GSL", "CED" ]

        # optional modules
        #self.optmodules = [ "LCCD", "MarlinTPC" ]

        # cvs root
        self.download.root="marlinreco"


    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.envpath["PATH"].append( self.installPath+'/bin' )

