##################################################
#
# Java module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class Java(BaseILC):
    """ Responsible for the Java configuration. """
    
    def __init__(self, userInput="auto" ):
        BaseILC.__init__(self, userInput, "Java", "java")

        self.installSupport = False

        self.reqfiles = [ ["bin/java"], ["bin/javac"] ]

        if( userInput == "auto" ):
            self.autoDetect()


    def autoDetectPath(self):
        """ tries to auto detect jdk path from system settings.
            - returns empty string if not found
            - otherwise returns absolute path"""

        # if $JDK_HOME is set, use it
        if os.getenv("JDK_HOME",""):
            return os.getenv("JDK_HOME")

        # look for SL afs installations
        if os.path.exists( self.ilcHome ):
            if self.os_ver.isSL():
                for v in [ '1.6.0', '1.5.0', '1.4.2' ]:
                    jpath = fixPath( self.ilcHome+'/'+self.alias+'/'+v )
                    if os.path.exists( jpath ):
                        return jpath

        # try to get it from javac
        if( isinPath( "javac" )):
            out = getoutput("which javac").strip()
            out = dereflinks( out )
            ind = out.find("/bin/javac")
            return out[:ind]
        
        # nothing was found
        return ''
        
    def autoDetectVersion(self):
        """ tries to auto detect version by parsing the output of java -version.
            - returns empty string in case of failure
            - otherwise returns java version """
        
        try:
            v = Version( getoutput( self.realPath() + r"/bin/java -version" ), \
                         max_elements = 3, strict = True)
        except ValueError:
            return ''
        else:
            return str(v)

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "JAVA_HOME" ]
        self.env["JAVA_HOME"] = self.installPath

        self.env["JDK_HOME"] = "$JAVA_HOME"
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$JDK_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JDK_HOME/jre/lib/i386" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JDK_HOME/jre/lib/i386/client" )

