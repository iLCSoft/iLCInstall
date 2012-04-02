##################################################
#
# MarlinPKG module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *

class ConfigPKG(BaseILC):
    """ Responsible for Configuration Packages installation,
        i.e. without compilation. """

    def __init__(self, name, userInput):
        BaseILC.__init__(self, userInput, name, name)
        self.reqfiles = []
        self.download.root = "ilctools"
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False
        self.skipCompile = True

class MarlinPKG(BaseILC):
    """ Responsible for Marlin Packages installation process. """
    
    def __init__(self, name, userInput):
        BaseILC.__init__(self, userInput, name, name)
        self.reqfiles = [ [ str("lib/lib" + name + ".a"), str("lib/lib" + name + ".so"), str("lib/lib" + name + ".dylib") ] ]
        self.reqmodules=[ 'LCIO', 'Marlin' ]

    def compile(self):
        """ compile MarlinPKG """
        
        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        #if( os.system( ". ../../../init_ilcsoft.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install" ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        # fill MARLIN_DLL
        if( self.name != "MarlinUtil" and self.name != "PandoraPFANew" ):
            self.parent.module('Marlin').envpath["MARLIN_DLL"].append( 
                self.installPath+"/lib/lib"+self.name+self.shlib_ext )

