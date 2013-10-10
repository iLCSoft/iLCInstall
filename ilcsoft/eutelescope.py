##################################################
#
# Eutelescope module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from marlinpkg import MarlinPKG
from util import *

class Eutelescope(MarlinPKG):
    """ Responsible for the Eutelescope installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "Eutelescope", userInput )

        # required modules
        self.reqmodules = [ "Marlin",  "LCIO" ]

        # optional modules
        self.optmodules = [ "GEAR", "AIDA" , "MarlinUtil", "CLHEP", "GSL", "CED", "ROOT", "GBL" ]

        # cvs root
        self.download.root = "eutelescope"


    def compile(self):
        """ compile Eutelescope """

        # ----- BUILD EUTELESCOPE ----------------------------
        os.chdir( self.installPath+"/build" )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


        if self.env.get( "EUDAQ_VERSION", "" ):

            # ----- BUILD EUDAQ ---------------------------------
            os.chdir( self.installPath+"/external" )
            os.system( "svn co https://github.com/eudaq/eudaq/%s eudaq/%s" % (self.env["EUDAQ_VERSION"], os.path.basename(self.env["EUDAQ_VERSION"])) )

            os.chdir( self.env[ "EUDAQ" ] ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)

            if( self.rebuild ):
                os.system( "make clean" )

            os.system( "make USE_LCIO=1 USE_EUTELESCOPE=1 main" )

            # ----- RE-BUILD EUTELESCOPE ---------------------------
            os.chdir( self.installPath + "/build" )

            os.system( self.genCMakeCmd() + " -DEUDAQ_DIR="+self.env[ "EUDAQ" ] )
            os.system( "make install" )


        if self.env.get( "MILLEPEDEII_VERSION", "" ):
            # ----- BUILD MILLEPEDEII ---------------------------
            os.chdir( self.installPath+"/external" )
            os.system( "svn co https://svnsrv.desy.de/public/MillepedeII/%s millepede2/%s" % (self.env["MILLEPEDEII_VERSION"], self.env["MILLEPEDEII_VERSION"]) )
            os.chdir( self.env[ "MILLEPEDEII" ] ) # needs to be defined in preCheckDeps (so it is written to build_env.sh)
            os.system( "make" )


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

