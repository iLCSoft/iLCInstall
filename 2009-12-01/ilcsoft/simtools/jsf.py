##################################################
#
# jsf module ( part of SimTools package )
#
# Author: Akiya Miyamoto, KEK
# Date: June, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class jsf(BaseILC):
    """ Responsible for the jsf installation. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "jsf", "jsf")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = ["cvs"]
        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@jlccvs.kek.jp:/home/cvs/soft
        self.download.accessmode = "pserver"
        self.download.server = "jlccvs.kek.jp"
        self.download.root = "home/cvs/soft"

        self.reqmodules = [ "ROOT" , "CLHEP", "lcbase", "lclib" ]
        self.reqfiles = [ ["lib/libJSF.so"] ]
       
    def compile(self):
        """ compile jsf """

        os.chdir( self.installPath )
        
        buildcmd='( export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" && make install)'
        if( os.system( buildcmd + " 2>&1 | tee -a " + self.logfile ) != 0 ) :
            self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["JSFROOT"]=self.installPath
        self.envpath["PATH"].append( "$JSFROOT/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JSFROOT/lib" )
        self.env["SOSYMLINK"]="true"

        # provide path to libgfortran in SL3/SL4/SL5
        if self.os_ver.isSL(3):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc-lib/i386-redhat-linux/3.2.3" )
        if self.os_ver.isSL(4):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/i386-redhat-linux/4.1.0" )
        if self.os_ver.isSL(5):
            self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/x86_64-redhat-linux/3.4.6" )       # 64bit
            #self.env.setdefault( "GFORTRANLIBDIR", "-L/usr/lib/gcc/x86_64-redhat-linux/3.4.6/32" )    # 32bit

        self.envcmds.append('export IMAKEINCLUDE=\"-I${LCBASEDIR} -I${LCLIBROOT}\" ')

