##################################################
#
# dcap module
#
# Author: Jan Engels, DESY
# Date: Nov, 2009
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class dcap(BaseILC):
    """ Responsible for building dcap library """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "dcap", "dcap")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        self.download.supportedTypes = [ "svn", "svn-export" ]

        self.reqfiles = [ ["lib/libdcap.so"] ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        # avoid warning 'download forced....'
        if self.download.type != "svn":
            self.download.type='svn-export'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl = 'http://svn.dcache.org/dCache/trunk/modules/dcap'
        else:
            # 1.9.5-5
            self.download.svnurl = 'http://svn.dcache.org/dCache/tags/%s/modules/dcap' % self.version

    def compile(self):
        os.chdir( self.installPath )
        
        if self.rebuild:
            os.system( "make clean 2>&1 | tee -a " + self.logfile )
        
        # 'make install' crashes if MAKEFLAGS includes "-j2"
        if( os.system( "unset MAKEFLAGS; make CC=\"gcc ${CFLAGS}\" LD=\"gcc ${LDFLAGS}\" BIN_PATH=${PWD} install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        #if( os.system( 'export MAKEFLAGS="CC=gcc\ ${CFLAGS} LD=gcc\ ${LDFLAGS} BIN_PATH=${PWD}" ; make install 2>&1 | tee -a ' + self.logfile ) != 0 ):
        #    self.abort( "failed to compile!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.env["DCAP"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$DCAP/lib" )

        # set LD_PRELOAD with envcmds instead of env to
        # avoid endless ERROR messages building the dcap library
        # self.env["LD_PRELOAD"] = "libdcap.so"
        self.envcmds.append( "export LD_PRELOAD=libdcap.so" )
