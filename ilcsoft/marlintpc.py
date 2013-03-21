##################################################
#
# MarlinTPC module
#
# Author: Peter Wienemann, University of Bonn
# Date: November 2007
#
##################################################

# custom imports
from marlinpkg import MarlinPKG
from util import *

class MarlinTPC(MarlinPKG):
    """ Responsible for the MarlinTPC installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinTPC", userInput)

        self.reqmodules = [ "LCIO", "GEAR", "GSL", "Marlin", "LCCD", "ROOT", "AIDA", "CLHEP" ]
        self.optmodules = [ "KalTest", "KalDet", "Mokka", "PathFinder", "GBL" ]

        # serves as base pkg for cedviewer
        # FIXME this dependency should be removed
        self.hasCMakeFindSupport = True

    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)
        
        self.download.project = 'marlintpc'
        self.download.root = ''

    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.env["MARLINTPC"] = self.installPath
        self.envpath["PATH"].append( '$MARLINTPC/bin' )

