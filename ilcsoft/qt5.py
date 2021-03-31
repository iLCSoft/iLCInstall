##################################################
#
# Qt5 module
#
# Author: R.Ete, DESY
# based on Xerces and QT modules
# Date: Sept, 2019
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class Qt5(BaseILC):
    """ Responsible for the Qt5 installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Qt5", "Qt5")

        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = True
        self.download.supportHEAD = False
        self.download.supportedTypes = [ "git" ] 
        self.download.svnurl = 'https://github.com/qt/qt5.git'

        self.reqfiles = [
            ["lib/libQt5Core.so", "lib64/libQt5Core.so", "lib/libQt5Core.dylib", "lib/libQt5Core.la"],
            ["lib/libQt5Gui.so", "lib64/libQt5Gui.so", "lib/libQt5Gui.dylib", "lib/libQt5Gui.la"],
            ["bin/qmake"] ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)
        # installPath does not exists before setMode is called
        self.cmakeconfig = self.installPath + "/lib/cmake/Qt5"
            
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
    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
        os.renames( self.version, self.name )
        os.renames( self.name, self.version + "/" + self.name )

        # create build directory
        trymakedir( self.installPath + "/build" )
        
        # Qt5 is a super module. We need to trigger the package download before-hand
        if( os.path.isfile( self.version + "/" + self.name + "/init-repository" ) ):
            os.chdir( self.version + "/" + self.name )
            if( os_system( "./init-repository --module-subset=essential,qt3d 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to init Qt5 submodules!!" )
        else:
           print(("****** path not found",self.version + "/" + self.name + "/init-repository" ))

        
    def compile(self):
        """ compile Qt5 """

        os.chdir( self.installPath + "/build" )

        if( self.rebuild ):
            os_system( "make distclean" )
        
        qt_cfg_options = " -opensource -confirm-license -nomake tests -make libs "
        cxxStandard = self.envcmake.get("CMAKE_CXX_STANDARD", None)
        if cxxStandard:
            qt_cfg_options += " -c++std c++" + str(cxxStandard)
        
        if( os_system( "../" + self.name + "/configure -prefix " + self.installPath + qt_cfg_options
                + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )

        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )

        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os_system( "make clean" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder=[ "QTDIR" ]
        self.env["QTDIR"] = self.installPath
        
        # self.env["QMAKESPEC"] = "$QTDIR/mkspecs/linux-g++"
        self.envpath["PATH"].append( "$QTDIR/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$QTDIR/lib" )
