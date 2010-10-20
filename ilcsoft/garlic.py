##################################################
#
# Garlic module
#
# Author: Jan Engels, DESY
# Date: Sep, 2010
#
##################################################

# custom imports
from marlinpkg import MarlinPKG
from util import *

class Garlic(MarlinPKG):
    """ Responsible for the Garlic installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "Garlic", userInput)

        self.reqmodules = [ "LCIO", "GEAR", "Marlin", "MarlinUtil", "ROOT" ]

        self.download.root = ''

