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

        self.download.supportedTypes = [ "svn-export", "svn" ]

        self.reqfiles = [["lib/libMarlinTPCReconstruction.a", "lib/libMarlinTPCReconstruction.so", "lib/libMarlinTPCReconstruction.dylib"],
                        [ "lib/libtpcconddata.a", "lib/libtpcconddata.so", "lib/libtpcconddata.dylib"]]

        self.reqmodules = [ "LCIO", "GEAR", "GSL", "Marlin", "LCCD", "ROOT", "AIDA", "CLHEP" ]

    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)
        
        # avoid warning 'download forced....'
        if self.download.type != "svn":
            self.download.type="svn-export"

        self.download.svnurl = 'svn://pi.physik.uni-bonn.de/MarlinTPC'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        else:
            self.download.svnurl += '/tags/' + self.version


    def init(self):
        MarlinPKG.init(self)

        # override desy default settings
        self.download.accessmode = "svn"
        self.download.server = "pi.physik.uni-bonn.de"
        self.download.root = ""

