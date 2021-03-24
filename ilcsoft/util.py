##################################################
#
# Utilities
#
# Author: Frank Gaede, DESY
# Date: Jan, 2007
#
##################################################

from .version import Version
from subprocess import getstatusoutput
from subprocess import getoutput
import os
import os.path
import sys
import shutil
import glob
import time
import string
import re
import fnmatch
import platform

#--------------------------------------------------------------------------------
def os_system( cmd ):
    """ forces os.system calls wto use bash """
    cmd = cmd.replace('"',r'\"')
    ##print('os_system: ', 'bash -c "'+cmd+'"')
    return os.system('pwd ; bash -c "'+cmd+'"')

#--------------------------------------------------------------------------------

class OSDetect(object):
    """ small class for detecting the OS """

    type = "unknown"
    ver = "unknown"
    platform = "unknown"
    arch = "unknown" # composed of gcc ver + architecture, e.g.: 'gcc34_32bit'

    def __init__(self):

        # Linux
        if( sys.platform == "linux2" ):
            self.type = "Linux"
 
        # MacOs
        if( sys.platform == "mac" or sys.platform == "darwin" ):
            self.type = "Darwin"
        
        # Windows
        if( sys.platform == "win32" ):
            self.type = "Win"

        if( self.type == "Linux" ):
            # description
            out=getstatusoutput("lsb_release -d")
            if( out[0] == 0 ):
                self.ver=out[1].split("Description:")[1].strip()
            # hardware platform
            out=getstatusoutput("uname -i")
            if( out[0] == 0 ):
                self.platform=out[1].strip()


        try:
            sizeofint = platform.architecture()[0]
            # major minor version of compiler
            gccver = ''.join( platform.python_compiler().split()[-1].split('.')[:2] )
            self.arch = 'gcc' + gccver + '_' + sizeofint
        except:
            pass


    def _get_shortver(self):
        if self.isSL():
            return 'SL'+ str(self.isSL()[0])
        elif self.type == "Linux":
            return self.ver
        return self.type

    shortver = property( _get_shortver )

    def __repr__(self):
        return repr( self.type )

    def __str__(self):
        return str(self.type+" - "+self.ver)
        
    # left here for compatibility, use isSL(3) instead
    def isSL3(self):
        """ returns True if this is Scientific Linux 3 """
        return self.isSL(3)
        
    # left here for compatibility, use isSL(4) instead
    def isSL4(self):
        """ returns True if this is Scientific Linux 4 """
        return self.isSL(4)

    def isSL(self, x=None):
        """ if x is given: returns True if os == Scientific Linux x
            if x is not given: returns a Version instance with the SL version
            otherwise returns False """
        if( self.type == "Linux" ):
            if( self.ver.find( "Scientific" ) != -1 or self.ver.find( "RedHat" ) != -1):
                if x != None:
                    return Version( self.ver )[0] == x
                else:
                    return Version( self.ver )
        return False

#--------------------------------------------------------------------------------

class GlobDirectoryWalker:
    # a forward iterator that traverses a directory tree

    def __init__(self, directory, pattern="*"):
        self.stack = [directory]
        self.pattern = pattern 
        self.files = []
        self.index = 0

    def __getitem__(self, index):
        while 1:
            try:
                file = self.files[self.index]
                self.index = self.index + 1
            except IndexError:
                # pop next directory from stack
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.files.sort()
                self.index = 0
            else:
                # got a filename
                fullname = os.path.join(self.directory, file)
                if os.path.isdir(fullname) and not os.path.islink(fullname):
                    self.stack.append(fullname)
                if fnmatch.fnmatch(file, self.pattern):
                    return fullname

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
    if( path.find('$') != -1 ):
        path = os.path.expandvars(path)
    
    # eliminate redundant //
    return os.path.normpath(path)

#--------------------------------------------------------------------------------

def ask_ok( prompt, retries=3, complaint="[y/n] , please !" ):
    """ prompts user for yes or no """

    while 1:
        ok = input( prompt )

        if ok in ( 'y' , 'yes '):
            return True
        if ok in ( 'n' , 'no '):
            return False

        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user ')

        print(complaint)

#--------------------------------------------------------------------------------

