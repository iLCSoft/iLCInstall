##################################################
#
# Geant4 module
#
# Author: Jan Engels, DESY
# Date: Sep, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class Geant4(BaseILC):
    """ Responsible for the Geant4 configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "Geant4", "geant4")

        #self.installSupport = False
        #self.hasCMakeBuildSupport = False
        #self.hasCMakeFindSupport = False

        # Linux-g++ / Darwin-g++
        self.env["G4SYSTEM"] = self.os_ver.type+"-g++"

        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [ [
            "sharedlib/"+self.env["G4SYSTEM"]+"/libG4run.so",
            "sharedlib/"+self.env["G4SYSTEM"]+"/libG4run.dylib",
            "lib64/libG4run.so",
            "lib64/libG4run.dylib",
            "lib/libG4run.so",
            "lib/libG4run.dylib",
            "lib/Geant4-9.5.0/"+self.env["G4SYSTEM"]+"/libG4run.dylib"
        ] ]

        self.optmodules = [ 'QT', 'CLHEP' ]

    def createLink(self):
        BaseILC.createLink(self)

        if( not os.path.exists( self.env["G4ENV_INIT"] )):
            #print "cannot read G4Data versions, G4ENV_INIT not defined properly!"
            return
        
        if Version(self.version, max_elements=2 ) < "9.0":
            #print "cannot read G4Data versions, this is only supported for Geant4 versions >= 9.0"
            return

        datasetsenv = [ "G4LEDATA", "G4NEUTRONHPDATA", "G4LEVELGAMMADATA", "G4RADIOACTIVEDATA" ]

        if Version(self.version, max_elements=2 ) >= "9.1":
            datasetsenv.insert(0, 'G4ABLADATA')

        if Version(self.version, max_elements=2 ) >= "9.3":
            datasetsenv.append('G4REALSURFACEDATA')

        if Version(self.version, max_elements=2 ) >= "9.4":
            datasetsenv.append('G4PIIDATA')


        depsdir=self.parent.installPath+"/.dependencies"
        g4dataversfile = depsdir+"/g4data"

        trymakedir( depsdir )
        os.system( "> " + g4dataversfile )
        
        for envvar in datasetsenv:
            envval=getoutput( ". "+self.env["G4ENV_INIT"]+" >/dev/null 2>&1 ; echo $"+envvar )
            if envval:
                ver=Version(envval).versions[-1]
                os.system( "echo %s:%s >> %s" % (envvar,ver,g4dataversfile) )

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        if( self.mode == "install" ):
            if( Version( self.version ) < "9.5" ):
                self.abort( "ilcinstall only supports installation of Geant4 9.5 or greater!" )

            # download url
            self.download.url = "http://geant4.cern.ch/support/source/geant4.%s.tar.gz" % self.version


    def compile(self):
        """ compile Geant4 """

        trymakedir( self.installPath + "/../build-" + self.version )
        os.chdir( self.installPath + "/../build-" + self.version )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )


        self.envcmake['CMAKE_INSTALL_PREFIX']=self.installPath
        self.envcmake.setdefault( 'GEANT4_INSTALL_DATA', 'ON' )
        #self.envcmake.setdefault( 'CMAKE_INSTALL_DATAROOTDIR', self.installPath + "/../g4data" )


        if( os.system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        if( os.system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )


    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

        if( self.mode == "install" ):

            if self.cmakeBoolOptionIsSet( "GEANT4_USE_SYSTEM_CLHEP" ):

                if not self.envcmake.has_key('CLHEP_ROOT_DIR'):

                    self.addExternalDependency( ["CLHEP"] )

                    clhepmod = self.parent.module("CLHEP")
                    if not clhepmod:
                        self.abort( "please set GEANT4_USE_SYSTEM_CLHEP=OFF or add CLHEP to your ilcinstall cfg file")

                    self.envcmake[ "CLHEP_ROOT_DIR"] = clhepmod.installPath

            if self.cmakeBoolOptionIsSet( "GEANT4_USE_QT" ):

                if not self.envcmake.has_key('QT_QMAKE_EXECUTABLE'):

                    self.addExternalDependency( ["QT"] )

                    qtmod = self.parent.module("QT")
                    if not qtmod:
                        self.abort( "please set QT_QMAKE_EXECUTABLE if using option GEANT4_USE_QT or add QT to your ilcinstall cfg file")
                    
                    self.envcmake[ "QT_QMAKE_EXECUTABLE"] = qtmod.installPath + "/bin/qmake"
                else:
                    self.envcmake["QT_QMAKE_EXECUTABLE"]=fixPath( self.envcmake["QT_QMAKE_EXECUTABLE"] )
                    if not os.path.exists( self.envcmake["QT_QMAKE_EXECUTABLE"] ):
                        self.abort( "QT_QMAKE_EXECUTABLE points to an invalid location: " + self.envcmake["QT_QMAKE_EXECUTABLE"] )



            #if self.cmakeBoolOptionIsSet( "GEANT4_USE_GDML" ):

            #    if not self.envcmake.has_key( "XERCESC_INCLUDE_DIR" ):
            #        self.abort( "XERCESC_INCLUDE_DIR not specified" )

            #    self.envcmake["XERCESC_INCLUDE_DIR"]=fixPath( self.envcmake["XERCESC_INCLUDE_DIR"] )

            #    if not os.path.exists( self.envcmake["XERCESC_INCLUDE_DIR"] ):
            #        self.abort( "XERCESC_INCLUDE_DIR points to an invalid location: " + self.envcmake["XERCESC_INCLUDE_DIR"] )

            #    if not self.envcmake.has_key( "XERCESC_LIBRARY" ):
            #        self.abort( "XERCESC_LIBRARY not specified" )

            #    self.envcmake["XERCESC_LIBRARY"]=fixPath( self.envcmake["XERCESC_LIBRARY"] )

            #    if not os.path.exists( self.envcmake["XERCESC_LIBRARY"] ):
            #        self.abort( "XERCESC_LIBRARY points to an invalid location: " + self.envcmake["XERCESC_LIBRARY"] )


            if self.envcmake.has_key( "XERCESC_ROOT_DIR" ):
                import platform
                if platform.architecture()[0] == '64bit':
                    self.envpath["LD_LIBRARY_PATH"].append( self.envcmake[ "XERCESC_ROOT_DIR" ] + "/lib64" )
                else:
                    self.envpath["LD_LIBRARY_PATH"].append( self.envcmake[ "XERCESC_ROOT_DIR" ] + "/lib" )


    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "G4INSTALL" ]
        self.env["G4INSTALL"] = self.installPath

        if Version(self.version, max_elements=2 ) < "9.5":
            self.env["G4INCLUDE"] = "$G4INSTALL/include"
            self.envpath["LD_LIBRARY_PATH"].append( "$G4INSTALL/sharedlib/"+self.env["G4SYSTEM"] )

        if( not self.env.has_key( "G4ENV_INIT" )):
            if Version(self.version, max_elements=2 ) < "9.5":
                if( not os.path.exists( self.realPath() + "/env.sh" )):
                    self.abort( "you must specify a valid path for a geant4 environment shell script e.g.:\n"\
                            + "ilcsoft.module(\"Geant4\").env[\"G4ENV_INIT\"]=\"/foo/bar/env.sh\"" )
                self.env["G4ENV_INIT"]="$G4INSTALL/env.sh"
            else:
                self.env["G4ENV_INIT"]="$G4INSTALL/bin/geant4.sh"



