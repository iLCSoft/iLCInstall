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

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = True
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [
            ["lib/libQtCore.so", "lib64/libQtCore.so", "lib/libQtCore.dylib", "lib/QtCore.la", \
                "lib/qt-3.1/lib/libqt.so", "lib/qt-3.3/lib/libqt-mt.so"],
            ["lib/libQtGui.so", "lib64/libQtGui.so", "lib/libQtGui.dylib", "lib/QtGui.la", \
                "lib/qt-3.1/lib/libqui.so", "lib/qt-3.3/lib/libqui.so"],
            ["bin/qmake"] ]

        if( userInput=="auto" ):
            self.autoDetect()
    
    def autoDetectPath(self):
        """ tries to auto detect qt dir from system settings.
            - returns empty string in case of failure
            - otherwise returns qt dir """

        # if $QTDIR is set use it
        if os.getenv("QTDIR",""):
            return os.getenv("QTDIR")

        # else try to get from qmake
        if( isinPath("qmake")):
            out = getoutput("which qmake").strip()
            ind = out.find("/bin/qmake")
            return out[:ind]

        # nothing was found
        return ''
        
    def autoDetectVersion(self):
        """ tries to auto detect version by parsing the output of qmake -v.
            - returns empty string in case of failure
            - otherwise returns qt version """

        # qmake -v returns the qmake version and the qt version, it's the qt version we want
        try:
            v = Version( getoutput( self.realPath() + '/bin/qmake -v' ) ).versions[-1]
        except:
            return ''
        else:
            return str(v)


    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if( Version( self.version ) < '4.6' ):
            self.download.url = "http://download.qt-project.org/archive/qt/%s/qt-x11-opensource-src-%s.tar.gz" % (self.version[:3], self.version,)

            if self.os_ver.type == "Darwin":
                self.download.url = "http://download.qt-project.org/archive/qt/%s/qt-mac-opensource-src-%s.tar.gz" % (self.version[:3], self.version,)
        else:
            self.download.url = "http://download.qt-project.org/archive/qt/%s/qt-everywhere-opensource-src-%s.tar.gz" % (self.version[:3], self.version,)

    def compile(self):
        """ compile QT """

        os.chdir( self.installPath )

        if( self.rebuild ):
            os.system( "make distclean" )

#        qt_cfg_options = " -prefix-install -fast -make libs -no-separate-debug-info -no-xkb -no-xinerama -no-qt3support"
#fg: enable qt3-support (on request from Klaus)       
        qt_cfg_options = " -prefix-install -fast -make libs -no-separate-debug-info -no-xkb -no-xinerama"
        
        if( Version( self.version ) < '4.5' ):
            qt_cfg_options += " -no-tablet"

        if( Version( self.version ) >= '4.4' ):
            qt_cfg_options += " -no-webkit"

        if( Version( self.version ) > '4.5' ):
            qt_cfg_options += " -opensource"
            
        if( os.system( "echo \"yes\" | ./configure -prefix " + self.installPath + qt_cfg_options
                + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
    
    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os.system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder=[ "QTDIR" ]
        self.env["QTDIR"] = self.installPath
        
        self.env["QMAKESPEC"] = "$QTDIR/mkspecs/linux-g++"
        self.envpath["PATH"].append( "$QTDIR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$QTDIR/lib" )
