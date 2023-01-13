##################################################
#
# MarlinPKG module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

import os

# custom imports
from .baseilc import BaseILC
from .util import *

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
        self.reqfiles = [ [ folder + "lib" + name + ext for ext in ('.so', '.a', '.dylib') for folder in ('lib/', 'lib64/') ] ]
        self.reqmodules=[ 'LCIO', 'Marlin' ]

        self.download.gitrepo = name
        # Marlin packages just provide libraries. 
        # They are not supposed to be found via CMake 
        self.hasCMakeFindSupport = False
        
    def compile(self):
        """ compile MarlinPKG """
        
        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( ". ../build_env.sh ; " + self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        #if( os_system( ". ../../../init_ilcsoft.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
        if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install" ) != 0 ):
            self.abort( "failed to install!!" )

    def checkInstall(self, abort=True):
        BaseILC.checkInstall(self)
        if self.name not in ("MarlinUtil", "PandoraPFANew", "Physsim", "LCFIVertex"):
            for libdir in ("/lib/", "/lib64/"):
                libname = self.installPath + libdir + "lib" + self.name + self.shlib_ext
                print("MarlinDLL: looking for ", libname)
                if os.path.exists(libname):
                    print("MarlinDLL: Found ", libname)
                    self.parent.module('Marlin').envpath["MARLIN_DLL"].append(libname)
                    break
            else:
                print("Error: did not find any library for the MarlinDLL", self.name)
                return False
        return True
