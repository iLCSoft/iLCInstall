#!/usr/bin/env python3

from .marlinpkg import MarlinPKG

class Physsim(MarlinPKG):
    """Responsible for the Physsim installation"""

    def __init__(self, userInput):
        MarlinPKG.__init__(self, "Physsim", userInput)
        self.reqfiles = [ ["lib/libPhyssim.so", "lib64/libPhyssim.so", "lib/libPhyssim.dylib"] ]
        self.reqmodules = ["LCIO", "ROOT"]
        self.hasCMakeFindSupport = True
