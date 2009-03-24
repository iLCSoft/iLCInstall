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

        self.reqfiles = [ ["lib/mysql/libmysqlclient.so", "lib/libmysqlclient.so", "lib/mysql/libmysqlclient.dylib", "lib/libmysqlclient.dylib"] ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["MYSQL_PATH"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_PATH/lib/mysql" )
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_PATH/lib" )

