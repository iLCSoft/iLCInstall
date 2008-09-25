##################################################
#
# AIDAJNI module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class AIDAJNI(BaseILC):
    """ Responsible for the AIDAJNI configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "AIDAJNI", "AIDAJNI")

        # no cmake build support
        self.hasCMakeBuildSupport = False
        
        self.reqfiles = [ ["bin/Linux-g++/aidajni-setup.sh", "bin/i386-Linux-g++/aidajni-setup.sh"], \
                ["bin/Linux-g++/aida-config", "bin/i386-Linux-g++/aida-config"] ]

        self.download.supportHEAD = False
        self.download.supportedTypes = [ "wget" ]

        # Java and JAIDA are required for using AIDAJNI
        self.reqmodules = [ "Java", "JAIDA" ]


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "ftp://ftp.slac.stanford.edu/software/freehep/AIDAJNI/v%s/AIDAJNI-%s-src.tar.gz" \
                % (self.version, self.version)

        if( self.mode == "install" ):
            if( Version(self.version) != '3.2.3' ):
                self.abort( "only install of version 3.2.3 is supported!" )

    def downloadSources(self):
        BaseILC.downloadSources(self)

        # undo rename from baseclass
        tryrename( self.version, self.download.tardir )

        os.chdir( self.parent.installPath )
        ryrename( self.alias, 'AIDAJNI-SRC' )
        os.renames( 'AIDAJNI-SRC', self.alias+'/'+self.version+'/'+self.alias )

    def compile(self):
        os.chdir( self.installPath+'/'+self.alias )

        os.environ['FREEHEP']=self.installPath+'/'+self.alias
        os.environ['COMPILER']='g++'
        os.system('chmod +x tools/ant')
        
        if( os.system('tools/ant -Djar=aidajni 2>&1 | tee -a '+ self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        if( os.system('gmake -f GNUmakefile-AIDAJNI 2>&1 | tee -a '+ self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os.system('gmake -f GNUmakefile-AIDAJNI dist 2>&1 | tee -a '+ self.logfile ) != 0 ):
            self.abort( "failed to create tarball!!" )

        trydelenv('FREEHEP')
        trydelenv('COMPILER')
        
        if self.parent.os.isSL(3):
            os.system( 'tar -xzf %s-%s-Linux-g++.tar.gz' % (self.alias, self.version) )
            os.system( 'mv -f %s-%s/* %s' % (self.alias, self.version, self.installPath) )
            os.rmdir( self.alias+'-'+self.version )
        else:
            os.system( 'tar -xzf %s-%s-Linux-g++.tar.gz --strip-path=1 -C %s' \
                % (self.alias, self.version, self.installPath) )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["AIDAJNI_HOME"] = self.installPath
