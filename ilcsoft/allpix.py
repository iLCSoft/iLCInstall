#! /usr/bin/env python

##################################################
#
# AllPix module
#
# Author: Igor Rubinskiy, DESY
# Date: July, 2014
#
##################################################
                                                                                                                                                            
# custom imports
#from marlinpkg import MarlinPKG

from baseilc import BaseILC
from util import *

from subprocess import Popen, PIPE
#from subprocess import check_output
#from pipes import quote
#from pprint import pprint
#from os import environ

#import os
#import re
#import subprocess
#import multiprocessing
#import pprint

#import os
#import sys

def source(path,script):
    print path + " " + script
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    import subprocess, os

    os.chdir( path )   
    command = ['bash', '-c', 'source '+script+' && env'  ]
    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

    for line in proc.stdout:
        (key, _, value) = line.partition("=")
        os.environ[key] = value
    proc.communicate()

#    pprint(dict(os.environ))



def available_cpu_count():
    """ Number of available virtual or physical CPUs on this system, i.e.
    user/real as output by time(1) when called with an optimally scaling
    userspace-only program"""

    # cpuset
    # cpuset may restrict the number of *available* processors
#    try:
#        m = re.search(r'(?m)^Cpus_allowed:\s*(.*)$',
#                      open('/proc/self/status').read())
#        if m:
#            res = bin(int(m.group(1).replace(',', ''), 16)).count('1')
#            if res > 0:
#                return res
#    except IOError:
#        pass

    # Linux
    try:
        res = open('/proc/cpuinfo').read().count('processor\t:')

        if res > 0:
            return res
    except IOError:
        pass

    # Python 2.6+
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # http://code.google.com/p/psutil/
    try:
        import psutil
        return psutil.NUM_CPUS
    except (ImportError, AttributeError):
        pass

class AllPix(BaseILC):
    """ Responsible for the AllPix installation process. """
    
    def __init__(self, userInput):
        # strip potential 'tags/' or 'branches/' parts from version string
        if os.path.basename(userInput):
            myversion=os.path.basename(userInput)
        else:
            myversion=os.path.dirname(userInput)
#        MarlinPKG.__init__(self, "AllPix", myversion )
        BaseILC.__init__(self, myversion, "AllPix_sub", "AllPix")

        # required modules
        self.reqmodules = [ "Geant4",  "XercesC", "ROOT", "QT" ]

        # set download url with full path
        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'+userInput

    def init(self):
        """ init AllPix """
        BaseILC.init(self)

    def compile(self):
        """ compile AllPix """
        # ----- BUILD ALLPIX ----------------------------
        os.chdir( self.installPath )

        os.environ["G4WORKDIR"]=self.installPath + "/bin/"
	if not os.path.exists(  os.environ["G4WORKDIR"] ) :       
		os.mkdir( os.environ["G4WORKDIR"] ) 


#        qt=self.parent.module("QT").installPath
#        os.environ["QTHOME"] = qt
#        print os.environ["QTHOME"]


        root=self.parent.module("ROOT")
        os.environ["ROOTSYS"]="old/value/before/sourcing/./bin/thisroot.sh" 
        print "ROOTSYS: "  + os.environ["ROOTSYS"]
        source( root.installPath, "./bin/thisroot.sh"  )
        print "ROOTSYS: " + os.environ["ROOTSYS"]

        g4=self.parent.module("Geant4")
        g4_cd      = "%s/share/Geant4-9.6.1/geant4make/" % (g4.installPath )
        os.environ["G4LIB_USE_GDML"]="old/value/before/sourcing/./geant4make.sh"
        print "G4LIB_USE_GDML: " + os.environ["G4LIB_USE_GDML"]
        source( g4_cd, "./geant4make.sh" )
        print "G4LIB_USE_GDML: " + os.environ["G4LIB_USE_GDML"]

        xercesc_lib = self.parent.module("XercesC").installPath + "/lib"
        print xercesc_lib
        os.environ["LD_LIBRARY_PATH"]=os.environ["LD_LIBRARY_PATH"]+":"+xercesc_lib
        os.environ["LD_LIBRARY_PATH"]=os.environ["LD_LIBRARY_PATH"]+":"+os.environ["G4LIB"]+"/../"
        print os.environ["LD_LIBRARY_PATH"]


        nproc = available_cpu_count()
        print "processor : %d" % ( nproc )
        
        os.chdir( self.installPath  )
#        os.system( "make clean" )

        command = "make -j %d 2>&1 | tee -a %s" % (nproc, self.logfile)
        print command
        if( os.system( command ) != 0 ):
            self.abort( "failed to install!!" )

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

    def postCheckDeps(self):
#        MarlinPKG.postCheckDeps(self)
        BaseILC.postCheckDeps(self)

        self.env["ALLPIX"] = self.installPath
        self.envpath["PATH"].append( '$ALLPIX/bin' )
        self.envpath["LD_LIBRARY_PATH"].append( '$ALLPIX/lib' )

        self.env["QTHOME"]=self.parent.module("QT").installPath

    def setMode(self, mode):
        BaseILC.setMode(self,mode)

        self.download.type = "svn"
        # reset url to remove path to branches, trunk, etc.
#        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'
