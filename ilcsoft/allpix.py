##################################################
#
# AllPix module
#
# Author: Igor Rubinskiy, DESY
# Date: July, 2014
#
##################################################
                                                                                                                                                            
# custom imports
#from marlinpkg import MarlinPKG
from baseilc import BaseILC
from util import *

class AllPix(BaseILC):
    """ Responsible for the AllPix installation process. """
    
    def __init__(self, userInput):
        # strip potential 'tags/' or 'branches/' parts from version string
        if os.path.basename(userInput):
            myversion=os.path.basename(userInput)
        else:
            myversion=os.path.dirname(userInput)
#        MarlinPKG.__init__(self, "AllPix", myversion )
        BaseILC.__init__(self, myversion, "AllPix_sub", "AllPix")

        # required modules
        self.reqmodules = [ "Geant4",  "XercesC", "ROOT" ]

        # set download url with full path
        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'+userInput

    def init(self):
        BaseILC.init(self)



    def compile(self):
        """ compile AllPix """
        # ----- BUILD ALLPIX ----------------------------
        os.chdir( self.installPath )

        root=self.parent.module("ROOT")
        root_loadenv = root.installPath + "/bin/thisroot.sh"
        print "root:" + root_loadenv

        g4=self.parent.module("Geant4")
        g4_loadenv = g4.installPath + "/share/Geant4-9.6.1/geant4make/geant4make.sh"
        print "g4:" + g4_loadenv

        os.system( "sh " + root_loadenv )
        os.system( "sh " + g4_loadenv )      

        if( os.system( "make  2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

    def postCheckDeps(self):
#        MarlinPKG.postCheckDeps(self)
        BaseILC.postCheckDeps(self)

        self.env["ALLPIX"] = self.installPath
        self.envpath["PATH"].append( '$ALLPIX/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( '$ALLPIX/lib' )

#        self.env["G4INSTALL"]=self.parent.module("Geant4").env["G4INSTALL"]
#        self.env["ROOTSYS"]=self.parent.module("ROOT").env["ROOTSYS"]
#        print "Geatn4 : " +  self.env["G4INSTALL"] 
#        print "Roo : " +  self.env["ROOTSYS"] 

    def setMode(self, mode):
        BaseILC.setMode(self,mode)

        self.download.type = "svn"
        # reset url to remove path to branches, trunk, etc.
#        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'
