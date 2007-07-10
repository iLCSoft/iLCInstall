##################################################
#
# QT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class QT(BaseILC):
    """ Responsible for the QT installation process. """
    
    def __init__(self, userInput="auto"):
        BaseILC.__init__(self, userInput, "QT", "QT")

        self.download.supportHEAD = False
        self.hasCMakeSupport = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [
            ["lib/libQtCore.so", "lib/libQtCore.dylib", "lib/qt-3.1/lib/libqt.so"],
            ["lib/libQtGui.so", "lib/libQtGui.dylib", "lib/qt-3.1/lib/libqui.so"],
            ["bin/qmake"] ]

        if( userInput=="auto" ):
            self.autoDetect()
    
    def autoDetectPath(self, abort=False):
        """ tries to auto detect qt dir from system settings.
            - returns empty string in case of failure
            - otherwise returns qt dir """

        # if QTDIR is set we use it
        qtdir = os.getenv("QTDIR","")
        
        if( not qtdir ):
            # else try to get from qmake
            if( isinPath("qmake")):
                out = commands.getoutput("which qmake").strip()
                ind = out.find("/bin/qmake")
                qtdir = out[:ind]
            elif(abort):
                self.abort( "failed trying to get the default QT settings!!\n" )

        return qtdir
        
    def autoDetectVersion(self, abort=False):
        """ tries to auto detect version by parsing the output of qmake -v.
            - returns empty string in case of failure
            - otherwise returns qt version """

        version = ""

        if( isinPath( "grep" ) and isinPath( "sed" )):
            version = commands.getoutput( self.realPath() \
                + r"/bin/qmake -v 2>&1 | grep 'Qt' | sed -e 's/.*Qt .*\([0-9]\.[0-9]\.[0-9]\).*/\1/'" )
        elif(abort):
            self.abort( "grep or sed not installed on your system!! QT version could not be verified!!!" )

        return version


    def setMode(self, mode):

        BaseILC.setMode(self, mode)
            
        if( self.mode == "install" ):

            print "*** WARNING: QT takes a LOT of time to compile (3-4 hours on a fast machine)!!! "
            
            # download url
            self.download.url = "ftp://ftp.trolltech.com/qt/source/qt-x11-opensource-src-" \
                    + self.version + ".tar.gz"
        
    
    def compile(self):
        """ compile QT """

        os.chdir( self.installPath )

        if( self.rebuild ):
            os.system( "make distclean" )

        if( os.system( "./configure -prefix " + self.installPath \
                + " -prefix-install -fast 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
    
    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os.system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["QTDIR"] = self.installPath
        self.env["QMAKESPEC"] = self.installPath + "/mkspecs/linux-g++"
        self.envpath["PATH"].append( "$QTDIR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$QTDIR/lib" )
