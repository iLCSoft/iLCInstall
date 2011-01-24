##################################################
#
# ilcutil module
#
# Author: Jan Engels, DESY
# Date: Jan, 2011
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class ILCUTIL(BaseILC):
    """ Responsible for the ilcutil software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "ILCUTIL", "ilcutil")

        self.reqfiles = [
            [ "ILCSOFT_CMAKE_MODULESConfig.cmake" ],
            [ "lib/libstreamlog.a", "lib/libstreamlog.so", "lib/libstreamlog.dylib"]
        ]

        self.download.root = "ilctools"

    def compile(self):
        """ compile ilcutil """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["ilcutil"] = self.installPath

        # PATH
        self.envpath["LD_LIBRARY_PATH"].append( "$ilcutil/lib" )

