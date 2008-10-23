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
        self.hasCMakeFindSupport = False
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [
            ["lib/libQtCore.so", "lib/libQtCore.dylib", "lib/QtCore.la", \
                "lib/qt-3.1/lib/libqt.so", "lib/qt-3.3/lib/libqt-mt.so"],
            ["lib/libQtGui.so", "lib/libQtGui.dylib", "lib/libQtGui.la", \
                "lib/qt-3.1/lib/libqui.so", "lib/qt-3.3/lib/libqui.so"],
            ["bin/qmake"] ]

        if( userInput=="auto" ):
            self.autoDetect()
    
    def autoDetectPath(self):
        """ tries to auto detect qt dir from system settings.
            - returns empty string in case of failure
            - otherwise returns qt dir """

        # look for SL afs installations
        if self.os_ver.isSL() != None:
            if os.path.exists( self.ilcHome ):
                for v in [ '4.2.2' ]:
                    qtdir = fixPath( self.ilcHome+'/'+self.alias+'/'+v )
                    if os.path.exists( qtdir ):
                        return qtdir

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

        self.download.url = "ftp://ftp.trolltech.com/qt/source/qt-x11-opensource-src-%s.tar.gz" % (self.version,)

    def compile(self):
        """ compile QT """

        os.chdir( self.installPath )

        if( self.rebuild ):
            os.system( "make distclean" )

        if( os.system( "echo \"yes\" | ./configure -prefix " + self.installPath \
                + " -prefix-install -fast 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
    
    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os.system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        if( self.mode == "install" ):
            print "*** WARNING: QT takes a LOT of time to compile (3-4 hours on a fast machine)!!! "

        self.envorder=[ "QTDIR" ]
        self.env["QTDIR"] = self.installPath
        
        self.env["QMAKESPEC"] = "$QTDIR/mkspecs/linux-g++"
        self.envpath["PATH"].append( "$QTDIR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$QTDIR/lib" )
