##################################################
#
# SimTools module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class SimTools(BaseILC):
    """ Responsible for the SimTools installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "SimTools", "SimTools")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        # set some cvs variables
        #self.download.env["CVSROOT"]=":pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft"
        self.download.supportedTypes = ["cvs"]
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"
        self.download.project = "SimToolsMaker/Release"

        self.reqfiles = [ ["Jupiter/bin/Linux-g++/Jupiter"] ]
        self.reqmodules = [ "LCIO", "ROOT", "Geant4", "CLHEP", "Java" ]

#    def downloadSources(self):
#        """ downloads SimToolsMaker install script """
#        BaseILC.downloadSources(self)
#
#        os.chdir( self.installPath )
#        os.system( "cp -f "+self.parent.ilcinstallDir+"/setup-simtools.sh ./setup.bash" )

    def compile(self):
        """ compile SimTools """

        os.chdir( self.installPath )
        
        if( self.rebuild ):
            opt="build"
        else:
            opt="all"

        print "build command:", "buildtools -setup build_env.sh -cvsroot",self.download.env["CVSROOT"],opt
        if( os.system( "buildtools -setup build_env.sh -cvsroot "+self.download.env["CVSROOT"]+" "+opt+\
                " | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder=[ "LC_RELEASE_DIR", "LCBASEDIR", "KFLIBROOT", "LCLIBROOT", "LEDAROOT", \
                        "JSFROOT", "JUPITERROOT", "SATELLITESROOT", "URANUSROOT", "G4SYSTEM" ]

        self.env["LC_RELEASE_DIR"]=self.installPath

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
        self.env["GFORTRANLIBDIR"]="-L/usr/lib/gcc/i386-redhat-linux/4.1.0"

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

