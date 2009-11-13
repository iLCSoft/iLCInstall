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

        self.reqfiles = [ ["libdcap.so"] ]

    def init(self):
        BaseILC.init(self)

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl = 'http://svn.dcache.org/dCache/trunk/modules/dcap'
        else:
            # 1.9.5-5
            self.download.svnurl = 'http://svn.dcache.org/dCache/tags/%s/modules/dcap' % self.version

    def compile(self):
        os.chdir( self.installPath )
        
        if self.rebuild:
            os.system( "make clean 2>&1 | tee -a " + self.logfile )
            
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        # FIXME this should be done in dcap with make install!!
        trymakedir( "lib" )
        trymakedir( "include" )
        if( os.system( "cp -va lib*so* lib 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )
        if( os.system( "cp -va *.h include 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.env["DCAP_HOME"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( self.installPath )
