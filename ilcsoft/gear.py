##################################################
#
# GEAR module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class GEAR(BaseILC):
    """ Responsible for the GEAR software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GEAR", "gear")

        # supported cmake "build_with" modules
        self.cmakebuildmodules = []

        # java is required for generating header files with ant
        self.reqmodules_external = [ "Java" ]

        self.reqfiles = [
                ["lib/libgear.a", "lib/libgear.so", "lib/libgear.dylib"],
                ["lib/libgearxml.a", "lib/libgearxml.so", "lib/libgearxml.dylib"]
        ]

    def compile(self):
        """ compile GEAR """
        
        os.chdir( self.installPath )

        if( self.rebuild ):
            if( self.useCMake ):
                tryunlink( "build/CMakeCache.txt" )
            else:
                os.system( "ant clean" )

        # build software
        if( self.useCMake ):
            os.chdir( "build" )
            if( os.system( "cmake " + self.genCMakeCmd() + " .. 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure!!" )
            if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )
        else:
            if( os.system( "ant aid.generate 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to generate header files!!" )
            if( os.system( "ant cpp 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
        
    def buildDocumentation(self):
        # build documentation
        if( not self.useCMake and self.buildDoc ):
            os.chdir( self.installPath )
            if(isinPath("doxygen")):
                print 80*'*' + "\n*** Creating C++ API documentation for " + self.name + " with doxygen...\n" + 80*'*'
                os.system( "ant cpp.doc 2>&1 | tee -a " + self.logfile )

    def init(self):
    
        BaseILC.init(self)
        
        self.env["GEAR"] = self.installPath

        # PATH
        self.envpath["PATH"].append( "$GEAR/tools" )
        self.envpath["PATH"].append( "$GEAR/bin" )

        # USERINCLUDES + USERLIBS
        self.envbuild["USERINCLUDES"].append( "-D USE_GEAR -I" + self.installPath + "/src/cpp/include" )
        self.envbuild["USERLIBS"].append( "-L" + self.installPath + "/lib -lgearxml -lgear" )

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)
        
        if( not self.useCMake and self.mode == "install" ):
            self.env["GEARVERSION"] = self.version
            if( self.debug ):
                self.env["GEARDEBUG"] = "1"
            
            # check for doc tools
            if( self.buildDoc ):
                if( not isinPath("doxygen")):
                    print "*** WARNING: doxygen was not found!! " + self.name + " documentation will not be built!!! "
