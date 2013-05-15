##################################################
#
# DD4hep module
#
# Author: F.Gaede, DESY
# Date: May, 2013
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class DD4hep(BaseILC):
    """ Responsible for the DD4hep configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "DD4hep", "DD4hep")

        #self.hasCMakeBuildSupport = False
        #self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "svn"]
        self.download.root = "aidasoft"

        self.reqfiles = [ ["lib/libDD4hepCore.so", "lib/libDD4hepCore.dylib" ]]

        self.reqmodules = [ "ROOT" , "LCIO", "GEAR", "Geant4"]


#    def setMode(self, mode):
#        BaseILC.setMode(self, mode)
#
#        self.download.type = "svn"
#        
#        self.download.svnurl = 'http://llrforge.in2p3.fr/svn/DD4hep'
#
#        if( Version( self.version ) == 'HEAD' ):
#            self.download.svnurl += '/trunk'
#        elif 'pre' in self.version or 'dev' in self.version:
#            self.download.svnurl += '/branches/' + self.version
#        else:
#            self.download.svnurl += '/tags/' + self.version


    def init(self):
        """ init DD4hep """
        BaseILC.init(self)

#        g4mod = self.parent.module("Geant4")
#        self.g4ver = Version( g4mod.version )


    def compile(self):
        """ compile DD4hep """

        trymakedir( self.installPath + "/build" )
        os.chdir( self.installPath + "/build" )
        
        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( " source thisdd4hep.sh 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to source thisdd4hep.sh" )

            
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )



    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'DD4HEP' ] = self.installPath

#        self.envcmds.append("export G4WORKDIR=$DD4HEP")

        self.envpath["PATH"].append( "$DD4HEP/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$DD4HEP/lib" )

        self.envcmds.append('test -r ${G4ENV_INIT} && { cd $(dirname ${G4ENV_INIT}) ; . ./$(basename ${G4ENV_INIT}) ; cd $OLDPWD ; }')
        
        
