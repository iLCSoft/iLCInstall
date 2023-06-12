#!/usr/bin/env python3

from .baseilc import BaseILC
from .util import *


class k4edm4hep2lcioconv(BaseILC):
    """Build the k4EDM4hep2LcioConv package"""

    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "k4edm4hep2lcioconv", "k4edm4hep2lcioconv")

        self.hasCMakeFindSupport = False  # ?

        self.download.supportedTypes = ["GitHub"]
        self.download.gituser = "key4hep"
        self.download.gitrepo = "k4EDM4hep2LcioConv"

        self.reqmodules = ["edm4hep", "LCIO"]

    def init(self):
        """initialize k4edm4hep2lcioconv"""
        BaseILC.init(self)

    def _run_abort(self, cmd, msg):
        """Run the passed command via os_system and abort on failure"""
        if os_system(cmd + " 2>&1 | tee -a " + self.logfile) != 0:
            self.abort(msg)

    def compile(self):
        """Compile k4edm4hep2lcioconv"""
        trymakedir(self.installPath + "/build")
        os.chdir(self.installPath + "/build")

        if self.rebuild:
            tryunlink("CMakeCache.txt")

        self._run_abort(
            self.genCMakeCmd() + " -DCMAKE_INSTALL_PREFIX=../install",
            "failed to configure!!",
        )

        if self.nightlyBuild:
            for targetName in self.nightlyTargets:
                self._run_abort(
                    ". ../build_env.sh; make ${MAKEOPTS} " + targetName,
                    "failed to compile!!",
                )
        else:
            self._run_abort(
                ". ../build_env.sh; make ${MAKEOPTS}", "failed to compile!!"
            )
            self._run_abort(
                ". ../build_env.sh; make ${MAKEOPTS} install", "failed to install!!"
            )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envpath["LD_LIBRARY_PATH"].append(self.installPath + "/install/lib")
        self.envpath["LD_LIBRARY_PATH"].append(self.installPath + "/install/lib64")
        self.envpath["PATH"].append(self.installPath + "/install/bin")
