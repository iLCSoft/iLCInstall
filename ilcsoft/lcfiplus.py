#!/usr/bin/env python3

from .marlinpkg import MarlinPKG
from .baseilc import BaseILC


class LCFIPlus(MarlinPKG):
    """LCFIPlus configuration for installing and configuring LCFIPlus"""

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "LCFIPlus", userInput)

        self.reqmodules = ["LCIO", "GEAR", "ROOT", "Marlin", "MarlinUtil", "LCFIVertex"]
        self.reqfiles = [["lib/libLCFIPlus.so", "lib/LCFIPlus.dylib"]]

        self.download.type = "Github"
        self.download.gituser = "lcfiplus"
        self.download.gitrepo = "LCFIPlus"

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.parent.module("Marlin").envpath["MARLIN_DLL"].append(
            f"{self.installPath}/install/lib/libLCFIPlus{self.shlib_ext}"
        )
        self.envpath["ROOT_INCLUDE_PATH"].append(f"{self.installPath}/include")
        self.envpath["LD_LIBRARY_PATH"].append(f"{self.installPath}/install/lib")
