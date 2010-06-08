##################################################
#
# PandoraPFANew  module
#
# Author: F.Gaede, J.Engels, DESY
# Date: June 8 2010
#
##################################################

from util import *                                                                                                                                                            

# custom imports
from marlinpkg import MarlinPKG

class PandoraPFANew(MarlinPKG):
    """ Responsible for the PandoraPFANew installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "PandoraPFANew", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "GEAR", "PandoraPFANew", "LCIO" ]

        # optional modules
        self.optmodules = [ "AIDA" ]

    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)
        
        # avoid warning 'download forced....'
        if self.download.type != "svn":
            self.download.type="svn-export"

        self.download.svnurl = 'https://svnsrv.desy.de/public/PandoraPFANew/PandoraPFANew'


        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        else:
            self.download.svnurl += '/tags/' + self.version

        #FIXME ---- this we need for non-conforming version strings and releases in branches...
#        if( self.version.upper() == 'HEAD' ):
#            self.download.svnurl += '/trunk'
#        else:
#            self.download.svnurl += '/branches/' + self.version
