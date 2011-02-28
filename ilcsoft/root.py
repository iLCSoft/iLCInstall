##################################################
#
# ROOT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class ROOT(BaseILC):
    """ Responsible for the ROOT configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "ROOT", "root")

        #self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.download.supportedTypes = [ "wget", "svn-export", "svn" ]

        self.reqfiles = [
                ["lib/libCore.so", "lib64/libCore.so", "lib/libCore.dylib"], 
                ["lib/libPhysics.so", "lib64/libPhysics.so", "lib/libPhysics.dylib"],
                ["bin/root-config"]
        ]

        self.reqmodules_external = [ "GSL" ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = 'ftp://root.cern.ch/root/root_v%s.source.tar.gz' % self.version
        self.download.svnurl = 'http://root.cern.ch/svn/root'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        else:
            self.download.svnurl += '/tags/v' + self.version.replace('.','-')

    def init(self):
        BaseILC.init(self)

        if( Version( self.version ) == 'HEAD' and self.download.type[:3] != 'svn' ):
            self.download.type="svn-export"


    #def downloadSources(self):
    #    BaseILC.downloadSources(self)

    #    # move sources to a subdirectory
    #    os.renames( self.version, self.name )
    #    os.renames( self.name, self.version + "/" + self.name )

    #    # create build directory
    #    trymakedir( self.installPath + "/build" )


    def compile(self):
        """ compile root """

        #os.chdir( self.installPath + "/build" )
        os.chdir( self.installPath )

        #if( self.rebuild ):
        #    os.system( "make clean" )

        gsl=self.parent.module("GSL")

        if( os.system( "./configure --enable-soversion --enable-roofit --enable-minuit2 --enable-gdml --enable-table --enable-unuran --enable-xrootd --enable-gsl-shared --with-gsl-incdir="+ gsl.installPath +"/include --with-gsl-libdir="+ gsl.installPath + "/lib" ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["ROOTSYS"] = self.installPath
        self.envpath["PATH"].append( "$ROOTSYS/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$ROOTSYS/lib" )

