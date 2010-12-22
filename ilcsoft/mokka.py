##################################################
#
# Mokka module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Mokka(BaseILC):
    """ Responsible for the Mokka configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Mokka", "Mokka")

        self.hasCMakeBuildSupport = False
        #self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "svn", "svn-export", "cvs" ]
        # set some cvs variables
        # export CVSROOT=:pserver:anoncvs@pollin1.in2p3.fr:/home/flc/cvs
        self.download.accessmode = "pserver"
        self.download.server = "pollin1.in2p3.fr"
        self.download.root = "home/flc/cvs"

        self.reqfiles = [ ["bin/"+self.os_ver.type+"-g++/Mokka"] ]
        self.reqmodules = [ "LCIO", "GEAR", "Geant4", "MySQL" ]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if( Version( self.version ) >= '7.0' ):
            self.download.type = "svn"

            self.download.svnurl = 'http://llrforge.in2p3.fr/svn/Mokka'

            if( Version( self.version ) == 'HEAD' ):
                self.download.svnurl += '/trunk'
            else:
                self.download.svnurl += '/tags/' + self.version
        else:
            self.download.type = "cvs"
        
        if( self.download.username == "anonymous" ):
            self.download.username = "anoncvs"
            self.download.password = "%ilc%"

    def init(self):
        """ init Mokka """
        BaseILC.init(self)

        if( self.download.type == "svn" ):
            self.download.accessmode = 'http'
            self.download.server = 'llrforge.in2p3.fr'
            self.download.root = 'svn'

    def compile(self):
        """ compile Mokka """

        os.chdir( self.installPath + "/source" )

        # TODO for grid binary: export G4VIS_NONE (no visualization drivers built or used)

        if self.rebuild:
            os.system( ". ../build_env.sh ; make clean 2>&1 | tee -a "+self.logfile )
            
        if( os.system( ". ../build_env.sh ; make 2>&1 | tee -a "+self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'MOKKA' ] = self.installPath

        self.envcmds.append("export G4WORKDIR=$MOKKA")
        self.envpath["PATH"].append( "$MOKKA/bin/"+self.os_ver.type+"-g++" )
        self.envcmds.append(" . $G4ENV_INIT ")

        # disable some visualization drivers
        self.envcmds.append("unset G4VIS_BUILD_OIX_DRIVER G4VIS_USE_OIX_DRIVER G4VIS_USE_OIX" ) # G4VIS_USE_OIX_DRIVER changed in ver 9.3 to G4VIS_USE_OIX
        self.envcmds.append("unset G4VIS_BUILD_OPENGLXM_DRIVER G4VIS_USE_OPENGLXM" )
        self.envcmds.append("unset G4UI_BUILD_XAW_SESSION G4UI_USE_XAW" )
        self.envcmds.append("unset G4UI_BUILD_XM_SESSION G4UI_USE_XM" )

        # ---- DEPRECATED cross-compile of 32bit in 64bit ---------------
        #d = self.parent.env.copy()
        #d.update(self.env)
        #if d.setdefault('CXXFLAGS','').find('m32') != -1:
        #    self.envcmds.append('test -d "$OGLHOME/lib" && export OGLLIBS="-L${OGLHOME}/lib -lGLU -lGL"' )
        #    self.envcmds.append('test -d "$CLHEP_BASE_DIR/lib" && export CLHEP_LIB_DIR=${CLHEP_BASE_DIR}/lib' )
        #    self.envcmds.append('test -d "$OIVHOME/lib" && export OIVLIBS="-L${OIVHOME}/lib -lInventor -lInventorXt"' )
        #    self.envcmds.append('test -d "$XERCESCROOT/lib32" && export GDMLLIBS="-L${XERCESCROOT}/lib32 -lxerces-c"' )
         
        # compiling Mokka crashes if LDFLAGS is set. # TODO add bug to geant4 bug tracker
        self.envcmds.append("unset LDFLAGS")

