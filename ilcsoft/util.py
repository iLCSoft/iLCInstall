##################################################
#
# Utilities
#
# Author: Frank Gaede, DESY
# Date: Jan, 2007
#
##################################################

import os
import os.path
import sys
import shutil
import commands
import glob
import time
import string


#--------------------------------------------------------------------------------

class OSDetect:
    """ small class for detecting the OS """
    def __init__(self):
        self.type="unknown"
        self.ver="unknown"
        self.detected=False
        
        # Linux
        if( not self.detected ):
            out=commands.getstatusoutput("uname -s")
            if( out[0] == 0 ):
                if( out[1].find("Linux") != -1 ):
                    self.detected = True
                    self.type = "Linux"
 
         # MacOs
        if( not self.detected ):
            out=commands.getstatusoutput("sys")
            if( out[0] == 0 ):
                if( out[1].find("darwin") != -1 ):
                    self.detected = True
                    self.type = "MacOS"
        
         # Windows
        if( not self.detected ):
            out=commands.getstatusoutput("ver")
            if( out[0] == 0 ):
                if( out[1].find("Windows") != -1 ):
                    self.detected = True
                    self.type = "Windows"
 
        if( self.type == "Linux" ):
            out=commands.getstatusoutput("lsb_release -d")
            if( out[0] == 0 ):
                self.ver=out[1].split("Description:")[1].strip()

    def __repr__(self):
        print self.type+"-"+self.ver
        
    def isLinux(self):
        """ returns True if the OS is Linux """
        if( self.detected ):
            if( self.type == "Linux" ):
                return True
        return False

    def isMac(self):
        """ returns True if the OS is Mac """
        if( self.detected ):
            if( self.type == "MacOS" ):
                return True
        return False

    def isSL3(self):
        """ returns True if this is Scientific Linux 3 """
        if( self.detected ):
            if( self.ver.find( "Scientific Linux SL" ) != -1 ):
                if( self.ver.find( "release 3." ) != -1 ):
                    return True
        return False
        
    def isSL4(self):
        """ returns True if this is Scientific Linux 4 """
        if( self.detected ):
            if( self.ver.find( "Scientific Linux SL" ) != -1 ):
                if( self.ver.find( "release 4." ) != -1 ):
                    return True
        return False

#--------------------------------------------------------------------------------

def trydelenv(key):
    """ try to delete environment variable
        does not raise any exception in case of failure
        - returns True if successfull
        - returns False if fails """
    try:
        del os.environ[key]
    except:
        return False
    return True

#--------------------------------------------------------------------------------

def trymakedir(dir):
    """ try to create dir
        does not raise any exception in case of failure
        - returns True if successfull
        - returns False if fails """
    try:
        os.makedirs( dir )
    except:
        return False
    return True

#--------------------------------------------------------------------------------

def tryrename(old, new):
    """ try to rename a file or dir
        does not raise any exception in case of failure
        - returns True if successfull
        - returns False if fails """
    try:
        os.rename( old, new )
    except:
        return False
    return True

#--------------------------------------------------------------------------------

def tryunlink(file):
    """ try to unlink a file
        does not raise any exception in case of failure
        - returns True if successfull
        - returns False if fails """
    try:
        os.unlink( file )
    except:
        return False
    return True

#--------------------------------------------------------------------------------

def isinPath(prog):
    """ looks if a program exists and is in the current path
        - returns True if prog exists in current path (is executable)
        - returns False otherwise """
    return( os.system("which " + prog + " > /dev/null 2>&1") == 0 )

#--------------------------------------------------------------------------------

def getenv(name):
    """ checks if the given environment variable is set
        - returns it's value if set
        - else returns an empty string """
    return os.getenv( name, "" )

#--------------------------------------------------------------------------------

def dereflinks(path):
    """ dereference symbolic links
    - returns the real path to where the link points to """
    
    p = fixPath(path)

    if( os.path.islink(p) ):
        return os.path.realpath(p)
    return p

#--------------------------------------------------------------------------------

def basename(path):
    """ extract the basename from a path """
    
    p = fixPath(path)

    if( p[-1] == '/' ):
        return os.path.basename( p[:-1] )
    else:
        return os.path.basename( p )

#--------------------------------------------------------------------------------

def fixPath(path):
    """ expands ~ and $VARS in a path """
    
    # fix for home symbol ~
    if( path[0] == '~' ):
        path = os.path.expanduser(path)
    
    # expand environment variables
    p = os.path.expandvars(path)
    
    # eliminate redundant //
    return os.path.normpath(p)

#--------------------------------------------------------------------------------

def ask_ok( prompt, retries=3, complaint="[y/n] , please !" ):
    """ prompts user for yes or no """

    while 1:
        ok = raw_input( prompt )

        if ok in ( 'y' , 'yes '):
            return True
        if ok in ( 'n' , 'no '):
            return False

        retries = retries - 1
        if retries < 0:
            raise IOError , 'refusenik user '

        print complaint

#--------------------------------------------------------------------------------

