##################################################
#
# SimTools module
#
# THIS MODULE IS DEPRECATED!! Please use individual
# simtools modules instead
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class SimToolsMaker(BaseILC):
    """ Responsible for the SimTools installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "SimToolsMaker", "SimToolsMaker")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        # set some cvs variables
        #self.download.env["CVSROOT"]=":pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft"
        self.download.supportedTypes = ["cvs"]
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"
        self.download.project = "SimToolsMaker/Release"

        self.reqfiles = [ ["buildtools"] ]
        self.reqmodules = [ "LCIO", "ROOT", "Geant4", "CLHEP", "Java" ]

    def compile(self):
        """ compile SimTools """

        os.chdir( self.parent.installPath )
        
        if( self.rebuild ):
            opt="build"
        else:
            opt="all"

        
        buildcmd="%s/buildtools -setup %s/build_env.sh -cvsroot %s %s" % \
                (self.installPath,self.installPath,self.download.env["CVSROOT"],opt)
        print(">", buildcmd)
        
        if( os.system( buildcmd + " | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder=[ "LC_RELEASE_DIR", "LCBASEDIR", "KFLIBROOT", "LCLIBROOT", "LEDAROOT", \
                        "JSFROOT", "JUPITERROOT", "SATELLITESROOT", "URANUSROOT", "G4SYSTEM" ]

        self.env["LC_RELEASE_DIR"]=self.parent.installPath

        self.env["LCBASEDIR"]="$LC_RELEASE_DIR/lcbase"
        self.env["KFLIBROOT"]="$LC_RELEASE_DIR/physsim"
        self.env["LCLIBROOT"]="$LC_RELEASE_DIR/lclib"
        self.env["LEDAROOT"]="$LC_RELEASE_DIR/Leda"
        self.env["JSFROOT"]="$LC_RELEASE_DIR/jsf"
        self.env["JUPITERROOT"]="$LC_RELEASE_DIR/Jupiter"
        self.env["SATELLITESROOT"]="$LC_RELEASE_DIR/Satellites"
        self.env["URANUSROOT"]="$LC_RELEASE_DIR/Uranus"
        
        self.env["G4SYSTEM"]=self.parent.module("Geant4").env["G4SYSTEM"]
        self.env["SOSYMLINK"]="true"
        
        self.env["IMAKEINCLUDE"]="-I$LCBASEDIR -I$KFLIBROOT -I$LCLIBROOT"

        # provide path to libg2c.so in SL3/SL4/SL5
        if self.os_ver.isSL(4):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/i386-redhat-linux/4.1.0" )
        if self.os_ver.isSL(3):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc-lib/i386-redhat-linux/3.2.3" )
        if self.os_ver.isSL(5):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/x86_64-redhat-linux/3.4.6" )       # 64bit
            #self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/32" )    # 32bit

        self.envpath["PATH"].append( "$LCBASEDIR/bin" )
        self.envpath["PATH"].append( "$JSFROOT/bin" )
        self.envpath["PATH"].append( "$LCLIBROOT/bin" )
        self.envpath["PATH"].append( "$JUPITERROOT/$G4SYSTEM/bin" )

        self.envpath["LD_LIBRARY_PATH"].append( "$JSFROOT/lib" )
        self.envpath["LD_LIBRARY_PATH"].append( "$LEDAROOT/lib" )
        self.envpath["LD_LIBRARY_PATH"].append( "$SATELLITESROOT/lib" )
        self.envpath["LD_LIBRARY_PATH"].append( "$URANUSROOT/lib" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JUPITERROOT/lib/$G4SYSTEM" )

        self.envcmds.append(" . ${G4ENV_INIT} ")

