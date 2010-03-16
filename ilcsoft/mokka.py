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
        self.hasCMakeFindSupport = False

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
            os.system( "export G4WORKDIR=$MOKKA; . ../build_env.sh ; make clean 2>&1 | tee -a "+self.logfile )
            
        if( os.system( "export G4WORKDIR=$MOKKA; . ../build_env.sh ; make 2>&1 | tee -a "+self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'MOKKA' ] = self.installPath

        self.envpath["PATH"].append( "$MOKKA/bin/"+self.os_ver.type+"-g++" )
        self.envcmds.append(" . $G4ENV_INIT ")

        # disable some visualization drivers
        self.envcmds.append("unset G4VIS_BUILD_OPENGLXM_DRIVER G4VIS_BUILD_OIX_DRIVER" )
        self.envcmds.append("unset G4VIS_USE_OPENGLXM G4VIS_USE_OIX_DRIVER" )
        self.envcmds.append("unset G4UI_BUILD_XAW_SESSION G4UI_BUILD_XM_SESSION" )
        self.envcmds.append("unset G4UI_USE_XAW G4UI_USE_XM" )

        # small hack required for cross-compiling 32bit on 64bit (check $ARCH in $G4ENV_INIT)
        d = self.parent.env.copy()
        d.update(self.env)
        if d.setdefault('CXXFLAGS','').find('m32') != -1:
            self.envcmds.append('test -d "$OGLHOME/lib" && export OGLLIBS="-L${OGLHOME}/lib -lGLU -lGL"' )
            self.envcmds.append('test -d "$CLHEP_BASE_DIR/lib" && export CLHEP_LIB_DIR=${CLHEP_BASE_DIR}/lib' )
         
        # compiling Mokka crashes if LDFLAGS is set. # TODO add bug to geant4 bug tracker
        self.envcmds.append("unset LDFLAGS")

