##################################################
#
# Eutelescope module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from .marlinpkg import MarlinPKG
from .util import *

class Eutelescope(MarlinPKG):
    """ Responsible for the Eutelescope installation process. """
    
    def __init__(self, userInput):
        # strip potential 'tags/' or 'branches/' parts from version string
        if os.path.basename(userInput):
            myversion=os.path.basename(userInput)
        else:
            myversion=os.path.dirname(userInput)
        MarlinPKG.__init__(self, "Eutelescope", myversion )

        # required modules
        self.reqmodules = [ "Marlin",  "LCIO" ]

        # optional modules
        self.optmodules = [ "GEAR", "AIDA" , "MarlinUtil", "CLHEP", "GSL", "CED", "ROOT", "GBL" ]
        
        # set download url with full path
        self.download.svnurl = 'https://github.com/eutelescope/eutelescope/'+userInput


    def compile(self):
        """ compile Eutelescope """
        # ----- DOWNLOAD EXTERNAL DEPENDENCIES ----------------------------
        os_system( "sh "+self.installPath+"/tools/install-externals/install-externals.sh "
                   + self.installPath+"/external" )

        # ----- BUILD EUTELESCOPE ----------------------------
        os.chdir( self.installPath+"/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


        if self.env.get( "EUDAQ_VERSION", "" ):
            # ----- BUILD EUDAQ ---------------------------------
            os.chdir( self.installPath+"/external" )
            if( not self.env["EUDAQ_VERSION"] == 'trunk' ):
                # check out e.g. the tagged version (using svn)
                if( os_system( "svn co https://github.com/eudaq/eudaq/%s eudaq/%s" % (self.env["EUDAQ_VERSION"], os.path.basename(self.env["EUDAQ_VERSION"])) + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to checkout EUDAQ!" )
            else:
                # check out a full git clone of the repository
                if( os_system( "git clone https://github.com/eudaq/eudaq eudaq/%s" % (os.path.basename(self.env["EUDAQ_VERSION"])) + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to clone EUDAQ!" )

            os.chdir( self.env[ "EUDAQ" ] + "/build" ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)

            if( os_system( "cmake -D BUILD_gui=OFF -D BUILD_main=OFF -D BUILD_nreader=ON .." + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure EUDAQ!" )

            if( os_system( "make install" + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build EUDAQ!" )

        if self.env.get( "MILLEPEDEII_VERSION", "" ):
            # ----- BUILD MILLEPEDEII ---------------------------
            os.chdir( self.installPath+"/external" )
            if( os_system( "svn co https://svnsrv.desy.de/public/MillepedeII/%s millepede2/%s" % (self.env["MILLEPEDEII_VERSION"], self.env["MILLEPEDEII_VERSION"]) + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build MILLEPEDE2!" )
            os.chdir( self.env[ "MILLEPEDEII" ] ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)
            if( os_system( "make" + " 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to build MILLEPEDE2!" )


    def preCheckDeps(self):
        MarlinPKG.preCheckDeps(self)

        if self.env.get( "EUDAQ_VERSION", "" ):
            self.env[ "EUDAQ" ] = self.installPath + "/external/eudaq/" + os.path.basename(self.env["EUDAQ_VERSION"])


        if self.env.get( "MILLEPEDEII_VERSION", "" ):
            self.env[ "MILLEPEDEII" ] = self.installPath + "/external/millepede2/" + self.env["MILLEPEDEII_VERSION"]
            self.envpath["PATH"].append( '$MILLEPEDEII' )


    def postCheckDeps(self):
        MarlinPKG.postCheckDeps(self)

        self.env["EUTELESCOPE"] = self.installPath
        self.envpath["PATH"].append( '$EUTELESCOPE/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( '$EUTELESCOPE/lib' )
        # if EUDAQ is installed, adjust paths and Marlin libraries to be loaded
        if self.env.get( "EUDAQ_VERSION", "" ):
            self.envpath["LD_LIBRARY_PATH"].append( '$EUDAQ/lib' )
            self.parent.module('Marlin').envpath["MARLIN_DLL"].append( '$EUDAQ/lib/libNativeReader.so' )

    def setMode(self, mode):
        MarlinPKG.setMode(self, mode)

        # github download via svn or git clone depending on the chosen version
        if( not self.version == 'trunk' ):
            self.download.type = "svn"
        else: # devel version -- use git clone
            self.download.type = "git-clone"
            # reset url to remove path to branches, trunk, etc.
            self.download.svnurl = 'https://github.com/eutelescope/eutelescope'
