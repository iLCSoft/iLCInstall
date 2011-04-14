##################################################
#
# MySQL module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class MySQL(BaseILC):
    """ Responsible for the MySQL configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "MySQL", "mysql")

        self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.reqfiles = [
            ["lib/mysql/libmysqlclient.so", "lib/libmysqlclient.so",
                "lib64/mysql/libmysqlclient.so", "lib64/libmysqlclient.so",
                "lib/mysql/libmysqlclient.dylib", "lib/libmysqlclient.dylib"]
        ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder = [ "MYSQL_HOME" ]

        self.env["MYSQL_HOME"] = self.installPath
        self.env["MYSQL"] = "$MYSQL_HOME"
        self.env["MYSQL_PATH"] = "$MYSQL_HOME" # needed for mokka
        if platform.architecture()[0] == '64bit':
            self.env["MYSQL_LIBDIR"] = "$MYSQL_HOME/lib64/mysql" # needed for mokka

        self.envpath["PATH"].append( "$MYSQL_HOME/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_HOME/lib64/mysql" )
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_HOME/lib64" )
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_HOME/lib/mysql" )
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_HOME/lib" )

