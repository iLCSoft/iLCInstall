##################################################
#
# LCFIVertex module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG
from util import *

class LCFIVertex(MarlinPKG):
    """ Responsible for the LCFIVertex installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "LCFIVertex", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR" ]

        # optional modules
        # FIXME not working yet
        #self.optmodules = [ "RAIDA" ]

        # cvs root
        self.download.root="marlinreco"

    def downloadSources(self):
        MarlinPKG.downloadSources(self)

        print "+ Unpacking Boost..."
        os.chdir( self.installPath )
        os.system( "tar -xzvf boost.tgz" )

