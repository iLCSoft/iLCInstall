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
    """ Responsible for the MySQL installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "MySQL", "mysql")

        self.installSupport = False
        self.hasCMakeSupport = False

        self.reqfiles = [ ["lib/mysql/libmysqlclient.so"] ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["MYSQL_PATH"] = self.installPath
        self.envpath["LD_LIBRARY_PATH"].append( "$MYSQL_PATH/lib/mysql" )

