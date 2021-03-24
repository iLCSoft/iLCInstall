##################################################
#
# CED module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class CED(BaseILC):
    """ Responsible for the CED software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CED", "CED")

        self.reqfiles = [ ["lib/libCED.so","lib/libCED.a","lib/libCED.dylib"] ]

        self.download.supportedTypes = [ "GitHub" ] 
        self.download.gituser = 'iLCSoft'
        self.download.gitrepo = 'CED'

        self.envcmake['CED_SERVER']='OFF'
        self.envcmake['CED_NOT_INCLUDE_OPENGL_LINKER_PATH']='TRUE'

    def compile(self):
        """ compile CED """
        
        os.chdir( self.installPath+'/build' )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )
        
        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        self.envpath["PATH"].append( self.installPath + '/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( self.installPath + '/lib' )

        if self.mode == "install":

            if self.cmakeBoolOptionIsSet( "CED_SERVER" ):

                if self.os_ver.type == "Darwin":
                    if( not os.path.exists( "/usr/X11/include/GL/glut.h" ) and not os.path.exists( "/System/Library/Frameworks/GLUT.framework/Versions/A/Headers/glut.h" )):
                        print("glut not found in your system!! CED_SERVER forced to OFF")
                        self.envcmake["CED_SERVER"] = "OFF"
                else:
                    if( not os.path.exists( "/usr/include/GL/glut.h" ) and not os.path.exists( "/usr/include/glut.h" ) ):
                        print("glut-devel not found in your system!! you can get it from:\n[ http://freeglut.sourceforge.net/ ]")
                        print("CED_SERVER forced to OFF")
                        self.envcmake["CED_SERVER"] = "OFF"

