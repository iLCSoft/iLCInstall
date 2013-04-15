##################################################
#
# GDML module
#
# Author: F.Gaede, DESY
# Date: April 2013
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class GDML(BaseILC):
    """ Responsible for the GDML software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "GDML", "gdml")
        
        self.reqfiles = [ ["lib/libgdml.so", "lib/libgdml.dylib"] ]
        
        # java required
        # self.reqmodules_external = [ "Java" ]
        

       # set some cvs variables
        #self.download.env["CVSROOT"]=":pserver:anonymous@cvs.freehep.org:/cvs/lcd"

        self.download.supportedTypes = ["cvs"]
        self.download.accessmode = "pserver"
        self.download.server = "cvs.freehep.org"
        self.download.root = "cvs/lcd"
        self.download.project = "gdml2/CPPGDML"

#        self.reqfiles = [ ["buildtools"] ]
        self.reqmodules = [ "XercesC" ]

    def compile(self):
        """ compile GDML """
        
        os.chdir( self.installPath+'/build' )
        
        if self.rebuild:
            tryunlink( "CMakeCache.txt" )

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

        # execute ctests
        if( self.makeTests ):
            
            if( os.system( "make tests && make test" ) != 0 ):
                self.abort( "failed to execute gdml tests" )


    def setMode(self, mode):
        BaseILC.setMode(self, mode)


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)
       
#        if( self.mode == "install" ):
            # tests
#            if( self.makeTests ):
#                self.envcmake.setdefault("BUILD_GDML_EXAMPLES","ON")
#                self.envcmake.setdefault("BUILD_F77_TESTJOBS","ON")

            #if self.cmakeBoolOptionIsSet( "BUILD_WITH_DCAP" ):
            #    self.addDependency( ['dcap'] )
            #    self.envcmake["DCAP_HOME"]=self.parent.module("dcap").installPath
                

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["GDML"] = self.installPath
        
        # PATH
        #        self.envpath["PATH"].append( "$GDML/tools" )
        #        self.envpath["PATH"].append( "$GDML/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$GDML/lib" )


