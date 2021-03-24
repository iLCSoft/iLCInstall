##################################################
#
# CEDViewer module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .marlinpkg import MarlinPKG

class CEDViewer(MarlinPKG):
    """ Responsible for the CEDViewer installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "CEDViewer", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR", "CLHEP", "GSL", "CED" ]

        # optional modules
        #self.optmodules = [ "LCCD", "MarlinTPC" ]

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'CEDViewer'


    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.envpath["PATH"].append( self.installPath+'/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( self.installPath + '/lib' )
