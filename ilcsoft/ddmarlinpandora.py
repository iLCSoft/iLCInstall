##################################################
#
# DDMarlinPandora
#
# Author: Shaojun Lu CERN/DESY
# Date: Sep, 2015
#
##################################################

# custom imports
from marlinpkg import MarlinPKG

##################################################
# DDMarlinPandora module
##################################################


class DDMarlinPandora(MarlinPKG):
    """ Responsible for the DDMarlinPandora software installation process. """
    
    def __init__(self, userInput):
        MarlinPKG.__init__(self, "DDMarlinPandora", userInput)

        self.reqfiles = [ ["lib/libDDMarlinPandora.so","lib/libDDMarlinPandora.a","lib/libDDMarlinPandora.dylib"] ]

        self.reqmodules = [ "Marlin", "MarlinUtil", "PandoraPFANew", "BOOST", "ROOT", "DD4hep" ]

        self.download.root = "marlinreco"

    def compile(self):
        """ compile DDMarlinPandora """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

