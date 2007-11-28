##################################################
#
# Java module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class Java(BaseILC):
    """ Responsible for the Java configuration. """
    
    def __init__(self, userInput="auto" ):
        BaseILC.__init__(self, userInput, "Java", "java")

        self.installSupport = False
        #self.hasCMakeSupport = False

        self.reqfiles = [ ["bin/java"], ["bin/javac"] ]

        if( userInput == "auto" ):
            self.autoDetect()


    def autoDetectPath(self, abort=False):
        """ tries to auto detect jdk path from system settings.
            - returns empty string if not found
            - otherwise returns absolute path"""

        # if jdk home is set, we use it
        jdk_home = os.getenv("JDK_HOME","")

        if( not jdk_home ):
            # else try to get it from javac
            if( isinPath( "javac" )):
                out = commands.getoutput("which javac").strip()
                javac = dereflinks( out )
                ind = javac.find("/bin/javac")
                jdk_home = javac[:ind]
            # no jdk home set and no compiler on path ....
            elif( abort ):
                self.abort( "failed trying to get the default Java settings!!\n" \
                        + "Please define the module Java(\"path_to_JDK_HOME\") in your config file..." )
        
        return jdk_home
        
    def autoDetectVersion(self,abort=False):
        """ tries to auto detect version by parsing the output of java -version.
            - returns empty string in case of failure
            - otherwise returns java version """
        
        javaversion = ""
        out = commands.getstatusoutput( self.realPath() + r"/bin/java -version 2>&1" )

        if( out[0] == 0 ):
            ind1 = out[1].find("\"")
            # for java versions of type 1.X.X_X
            ind2 = out[1][ind1+1:len(out[1])].find("_")
            if( ind2 == -1 ):
                # for java versions of type 1.X.X
                ind2 = out[1][ind1+1:len(out[1])].find("\"")
            javaversion = out[1][ind1+1:ind1+ind2+1]
        elif(abort):
            self.abort( "failed to execute java -version" )

        return javaversion
    
    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["JDK_HOME"] = self.installPath
        self.env["JAVA_HOME"] = self.installPath
        self.envpath["PATH"].append( "$JDK_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JDK_HOME/jre/lib/i386" )
        self.envpath["LD_LIBRARY_PATH"].append( "$JDK_HOME/jre/lib/i386/client" )
