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

class MarlinTPC(MarlinPKG):
    """ Responsible for the MarlinTPC installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "MarlinTPC", userInput)

        # svn export svn://pi.physik.uni-bonn.de/MarlinTPC/trunk HEAD
        # svn export svn://pi.physik.uni-bonn.de/MarlinTPC/tags -version-
        self.download.supportedTypes = [ "svn" ]
        self.download.type = "svn"
        self.download.server = "pi.physik.uni-bonn.de"
        self.download.root = "MarlinTPC"

        self.reqfiles = [["lib/libMarlinTPCReconstruction.a", "lib/libMarlinTPCReconstruction.so", "lib/libMarlinTPCReconstruction.dylib"],
                        [ "lib/libtpcconddata.a", "lib/libtpcconddata.so", "lib/libtpcconddata.dylib"]]

        self.reqmodules = [ "LCIO", "GEAR", "GSL", "Marlin", "LCCD", "ROOT", "RAIDA", "CLHEP" ]

