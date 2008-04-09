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

        self.reqfiles = [ ["bin/Linux-g++/aidajni-setup.sh", "bin/i386-Linux-g++/aidajni-setup.sh"], \
                ["bin/Linux-g++/aida-config", "bin/i386-Linux-g++/aida-config"] ]

        # Java and JAIDA are required for using AIDAJNI
        self.reqmodules = [ "Java", "JAIDA" ]

        self.skipCompile = True

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        # no cmake build support
        self.useCMake = False
        
        # FIXME MAC download address
        self.download.url = "ftp://ftp.slac.stanford.edu/software/freehep/AIDAJNI/v" \
                + self.version + "/aidajni-" + self.version + "-i386-Linux-g++.tar.gz"

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["AIDAJNI_HOME"] = self.installPath

# FIXME write parser for getting environment values out of aidajni-setup.sh
#        
#        # environment variables
#        self.env["AIDAJNI_VERSION"] = self.version
#        self.env["AIDAJNI_INCLUDES"] = "-I" + self.installPath + "/include"
#        self.env["AIDAJNI_LIBS"] = "-L" + self.installPath + "/lib/Linux-g++ -lAIDAJNI -lFHJNI -L" \
#                + self.parent.module("Java").installPath + "/jre/lib/i386/client -ljvm"
#        
#        # path environment variables
#        self.envpath["PATH"].append( "$AIDAJNI_HOME/bin/Linux-g++" )
#        self.envpath["CLASSPATH"].append( "${AIDAJNI_HOME}/lib/freehep-aidajni.jar" )
#        self.envpath["LD_LIBRARY_PATH"].append( "${AIDAJNI_HOME}/lib/Linux-g++" )
#
# end of FIXME

