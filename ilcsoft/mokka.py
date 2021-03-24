##################################################
#
# Mokka module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class Mokka(BaseILC):
    """ Responsible for the Mokka configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Mokka", "Mokka")

        #self.hasCMakeBuildSupport = False
        #self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "svn", "svn-export", "cvs" ]
        # set some cvs variables
        # export CVSROOT=:pserver:anoncvs@pollin1.in2p3.fr:/home/flc/cvs
        self.download.accessmode = "pserver"
        self.download.server = "pollin1.in2p3.fr"
        self.download.root = "home/flc/cvs"

        self.reqfiles = [ ["bin/"+self.os_ver.type+"-g++/Mokka", "bin/Mokka"] ]
        self.reqmodules = [ "LCIO", "GEAR", "Geant4", "MySQL" ]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if( Version( self.version ) >= '7.0' ):
            self.download.type = "svn"

            self.download.svnurl = 'https://llrforge.in2p3.fr/svn/Mokka'

            if( Version( self.version ) == 'HEAD' ):
                self.download.svnurl += '/trunk'
            elif 'pre' in self.version or 'dev' in self.version:
                self.download.svnurl += '/branches/' + self.version
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

        g4mod = self.parent.module("Geant4")
        self.g4ver = Version( g4mod.version )

        if( self.download.type == "svn" ):
            self.download.accessmode = 'https'
            self.download.server = 'llrforge.in2p3.fr'
            self.download.root = 'svn'

    def compile(self):
        """ compile Mokka """

        if self.g4ver < '9.5':
            os.chdir( self.installPath + "/source" )

            # TODO for grid binary: export G4VIS_NONE (no visualization drivers built or used)

            if self.rebuild:
                os_system( ". ../build_env.sh ; make clean 2>&1 | tee -a "+self.logfile )
                
            if( os_system( ". ../build_env.sh ; make -j1 2>&1 | tee -a "+self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
        else:
            trymakedir( self.installPath + "/build" )
            os.chdir( self.installPath + "/build" )

            if( self.rebuild ):
                tryunlink( "CMakeCache.txt" )

            if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure!!" )
            if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )



    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env[ 'MOKKA' ] = self.installPath

        self.envcmds.append("export G4WORKDIR=$MOKKA")

        if self.g4ver < '9.5':
            self.envpath["PATH"].append( "$MOKKA/bin/"+self.os_ver.type+"-g++" )
        else:
            self.envpath["PATH"].append( "$MOKKA/bin" )

        self.envcmds.append('test -r ${G4ENV_INIT} && { cd $(dirname ${G4ENV_INIT}) ; . ./$(basename ${G4ENV_INIT}) ; cd $OLDPWD ; }')

        if self.g4ver < '9.5':
            # disable visualization drivers
            self.envcmds.append("unset G4VIS_BUILD_OIX_DRIVER G4VIS_USE_OIX_DRIVER G4VIS_USE_OIX" ) # G4VIS_USE_OIX_DRIVER changed in ver 9.3 to G4VIS_USE_OIX
            #self.envcmds.append("unset G4VIS_BUILD_DAWN_DRIVER G4VIS_USE_DAWN" )
            #self.envcmds.append("unset G4UI_BUILD_QT_SESSION G4VIS_BUILD_OPENGLQT_DRIVER G4VIS_USE_OPENGLQT G4UI_USE_QT" )
            #self.envcmds.append("unset G4VIS_BUILD_OPENGLX_DRIVER G4VIS_USE_OPENGLX" )
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

