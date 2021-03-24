##################################################
#
# LCFIVertex module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .marlinpkg import MarlinPKG
from .baseilc import BaseILC
from .util import *

class LCFIVertex(MarlinPKG):
    """ Responsible for the LCFIVertex installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "LCFIVertex", userInput )

        # required modules
        self.reqmodules = [ "Marlin", "MarlinUtil", "LCIO", "GEAR", "DD4hep", "Boost"]

        # optional modules
        self.optmodules = [ "AIDA" ]
        self.reqfiles = [ ["lib/libLCFIVertex.so", "lib/libLCFIVertex.dylib" ],
                          ["lib/libLCFIVertexProcessors.so", "lib/libLCFIVertexProcessors.dylib"] ]

        # cvs root
        self.download.root="marlinreco"

        # serves as base pkg for lcfiplus
        self.hasCMakeFindSupport = True

    def downloadSources(self):
        MarlinPKG.downloadSources(self)

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        # fill MARLIN_DLL
        self.parent.module('Marlin').envpath["MARLIN_DLL"].append(
          self.installPath+"/lib/libLCFIVertexProcessors"+self.shlib_ext )

        self.envpath["LD_LIBRARY_PATH"].append( self.installPath+"/lib" )

#        print "+ Unpacking Boost..."
#        os.chdir( self.installPath )
#        os_system( "tar -xzvf boost.tgz" )

