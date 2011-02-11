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

        self.installSupport = False
        self.hasCMakeBuildSupport = False
        self.hasCMakeFindSupport = False

        # Linux-g++ / Darwin-g++
        self.env["G4SYSTEM"] = self.os_ver.type+"-g++"

        self.reqfiles = [ ["lib/"+self.env["G4SYSTEM"]+"/libG4run.a", "sharedlib/"+self.env["G4SYSTEM"]+"/libG4run.so", "sharedlib/"+self.env["G4SYSTEM"]+"/libG4run.dylib"] ]

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

        depsdir=self.parent.installPath+"/.dependencies"
        g4dataversfile = depsdir+"/g4data"

        trymakedir( depsdir )
        os.system( "> " + g4dataversfile )
        
        for envvar in datasetsenv:
            envval=getoutput( ". "+self.env["G4ENV_INIT"]+" >/dev/null 2>&1 ; echo $"+envvar )
            if envval:
                ver=Version(envval).versions[-1]
                os.system( "echo %s:%s >> %s" % (envvar,ver,g4dataversfile) )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "G4INSTALL" ]
        self.env["G4INSTALL"] = self.installPath

        self.env["G4INCLUDE"] = "$G4INSTALL/include"

        if( not self.env.has_key( "G4ENV_INIT" )):
            if( not os.path.exists( self.realPath() + "/env.sh" )):
                self.abort( "you must specify a valid path for a geant4 environment shell script e.g.:\n"\
                        + "ilcsoft.module(\"Geant4\").env[\"G4ENV_INIT\"]=\"/foo/bar/env.sh\"" )
            self.env["G4ENV_INIT"]="$G4INSTALL/env.sh"

        self.envpath["LD_LIBRARY_PATH"].append( "$G4INSTALL/sharedlib/"+self.env["G4SYSTEM"] )

