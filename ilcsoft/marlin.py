##################################################
#
# Marlin module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class Marlin(BaseILC):
    """ Responsible for the Marlin software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Marlin", "Marlin")

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'Marlin'

        self.reqfiles = [ ["lib/libMarlin.a", "lib/libMarlin.so", "lib/libMarlin.dylib"], ["bin/Marlin"] ]

        # LCIO is required for building Marlin
        self.reqmodules = [ "LCIO", "GEAR" ]

        # optional modules
        self.optmodules = [ "CLHEP", "LCCD" , "AIDA" ]

        self.envcmake['MARLIN_GUI']='OFF'
    
    def compile(self):
        """ compile Marlin """
        
        os.chdir( self.installPath )

        os.chdir( "build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        # build software
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( ". ../build_env.sh ; make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( ". ../build_env.sh ; make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # execute ctests
        if( self.makeTests ):

            if( os_system( "unset MARLIN_DLL && make test" ) != 0 ):
                self.abort( "failed to execute Marlin tests" )


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)
        if( self.mode == "install" ):
            if self.cmakeBoolOptionIsSet( "MARLIN_GUI" ):
                if( sys.platform != "mac" and sys.platform != "darwin" ):
                    self.addExternalDependency( ["QT"] )
                self.reqfiles.append(["bin/MarlinGUI"])
    
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["MARLIN"] = self.installPath
        self.envpath["PATH"].append( '$MARLIN/bin' )

        if( self.mode == "install" ):
            # check for QT 4
            if( "QT" in self.reqmodules_external ):
                qt = self.parent.module("QT")
                if( qt != None and Version( qt.version ) < '4.0' ):
                    self.abort( "you need QT 4!! QT version " + qt.version + " found..." )

