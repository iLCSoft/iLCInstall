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
from pprint import pprint
from os import environ

import sys
import os
import subprocess
import pprint

#import multiprocessing
#import re
#from subprocess import check_output
#from pipes import quote

class AllPix(BaseILC):
    """ Responsible for the AllPix installation process. """

    def print_PATH(self):
	    print "---- "
	    print os.environ["PATH"] 
	    print "---- "

    def execute_make(self,path, proc=4, log=""):
#    print "make at %s ; on CPUs = %d ; loggin into %s " % (path, proc, log)
#    """Sometime you want to emulate the action of "source" in bash,
#    settings some environment variables. Here is a way to do it."""
#    import subprocess, os

            pwd = os.getcwd()  
            print "execute_make PWD : " + os.getcwd()
	    os.chdir( self.env["ALLPIX"] )
	    print "execute_make : " + os.getcwd()
	    command = ['bash', '-c', 'make -j %s ' % (proc) ]
            print "G4INSTALL :" + os.environ["G4INSTALL"]
	    print command
#            os.system(" make ")
	    proc = subprocess.Popen(command, stdout = subprocess.PIPE, shell=False)
	    proc.communicate()
#            pprint.pprint(dict(os.environ))

#    ps = subprocess.Popen(['ps', '-ef', '--columns', '1000'], stdout=subprocess.PIPE, shell=True)
#    output = ps.communicate()[0]
#    for line in output.splitlines():
#      if 'rtptransmit' in line:
#        print(line)
            os.chdir(pwd)

    def source( self, path, script):
#	    print path + "/" + script
	    """Sometime you want to emulate the action of "source" in bash,
	    settings some environment variables. Here is a way to do it."""
	    import subprocess, os

#            pwd = os.getcwd() 
#	    os.chdir( path )
	    command = ['bash', '-c', 'source '+path+script+' && env'  ]
            print command 
	    proc = subprocess.Popen(command, stdout = subprocess.PIPE)

	    for line in proc.stdout:
	        (key, _, value) = line.partition("=")
	        os.environ[key] = value.strip("\n")
#		print key + " " + value.strip("\n")
	    proc.communicate()

#            os.chdir(pwd)
#    pprint(dict(os.environ))



    def available_cpu_count(self):
	    """ Number of available virtual or physical CPUs on this system, i.e.
	    user/real as output by time(1) when called with an optimally scaling
	    userspace-only program"""
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

    
    def __init__(self, userInput):
        # strip potential 'tags/' or 'branches/' parts from version string
        if os.path.basename(userInput):
            myversion=os.path.basename(userInput)
        else:
            myversion=os.path.dirname(userInput)
#        MarlinPKG.__init__(self, "AllPix", myversion )
        BaseILC.__init__(self, myversion, "allpix", "AllPix")

        # required modules
        self.reqmodules = [ "Geant4",  "XercesC", "ROOT", "QT" ]

        # set download url with full path
        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'+userInput

        self.nproc = self.available_cpu_count()

    def init(self):
        """ init AllPix """
        BaseILC.init(self)

    def compile(self):
        """ compile AllPix """
        # ----- BUILD ALLPIX ----------------------------
#        os.chdir( self.installPath )

#        self.print_PATH()
#        temp_PATH=os.environ["PATH"]
#        print "PWD:" + os.environ["PWD"]
#        print "ALLPIX:" + self.env["ALLPIX"]

        os.environ["G4WORKDIR"]=self.installPath 
	if not os.path.exists(  os.environ["G4WORKDIR"] ) :       
		os.makedirs( os.environ["G4WORKDIR"] ) 
        print "compile : " + os.environ["G4WORKDIR"]

#        qt=self.parent.module("QT").installPath
#        os.environ["QTHOME"] = qt
#        print os.environ["QTHOME"]

        root=self.parent.module("ROOT")
        root_cd = root.installPath
        os.environ["ROOTSYS"]="old/value/before/sourcing/./bin/thisroot.sh" 
        print "ROOTSYS: "  + os.environ["ROOTSYS"]
        print "LD_LIB : " + os.environ["LD_LIBRARY_PATH"]
        print "PATH : " + os.environ["PATH"]
        self.source( root_cd+"/bin/", "thisroot.sh")
        print "ROO ROOTSYS: " + os.environ["ROOTSYS"]
        print "ROO LD_LIB : " + os.environ["LD_LIBRARY_PATH"]
        print "ROO PATH : " + os.environ["PATH"]

        g4=self.parent.module("Geant4")
        g4_cd      = "%s/share/Geant4-9.6.1/geant4make/" % (g4.installPath )
        print "g4_cd : " + g4_cd
#        print ""
#        os.environ["G4LIB_USE_GDML"]="old/value/before/sourcing/./geant4make.sh"
#        print "G4LIB_USE_GDML: " + os.environ["G4LIB_USE_GDML"]

        # geant4 sourcing destroys PATH environment have to record it for the executing time 
        os_PATH = os.environ["PATH"]
        self.source( g4_cd, "geant4make.sh" )
#        print "G4LIB_USE_GDML: " + os.environ["G4LIB_USE_GDML"]

        os.environ["PATH"] = os_PATH+":"+os.environ["G4WORKDIR"]

        print "G4---"
        print "G4 PWD : " + os.environ["PWD"]
        print "G4 ROOTSYS : " + os.environ["ROOTSYS"]
        print "G4 LD_LIB : " + os.environ["LD_LIBRARY_PATH"]
        print "G4 PATH : " + os.environ["PATH"]
        print "G4---"


#        xercesc_lib = self.parent.module("XercesC").installPath + "/lib"
#        print xercesc_lib
#        os.environ["LD_LIBRARY_PATH"]=os.environ["LD_LIBRARY_PATH"]+":"+xercesc_lib
#        os.environ["LD_LIBRARY_PATH"]=os.environ["LD_LIBRARY_PATH"]+":"+os.environ["G4LIB"]+"/../"
#        print os.environ["LD_LIBRARY_PATH"]


#        print "processor : %d" % ( nproc )
        
#        os.chdir( self.installPath  )
#        os.system( "make clean" )
#        os.environ["PATH"]=temp_PATH
#        self.envpath["PATH"]=temp_PATH
#        self.print_PATH()

#        command = 'make -j %d 2>&1 | tee -a %s' % (nproc, self.logfile)
#        print command
        self.execute_make( self.installPath, self.nproc, self.logfile )
#        if( os.system( "make -j %d 2>&1 | tee -a %s" % (nproc, self.logfile)  ) != 0 ):
#            self.abort( "failed to install!!" )

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

    def postCheckDeps(self):
#        MarlinPKG.postCheckDeps(self)
        BaseILC.postCheckDeps(self)

        self.env["ALLPIX"] = self.installPath
        self.envpath["PATH"].append( '$ALLPIX/bin/Linux-g++' )
        self.envpath["LD_LIBRARY_PATH"].append( '$ALLPIX/lib' )

        self.env["QTHOME"]=self.parent.module("QT").installPath

    def setMode(self, mode):
        BaseILC.setMode(self,mode)

        self.download.type = "svn"
        # reset url to remove path to branches, trunk, etc.
#        self.download.svnurl = 'http://svn.cern.ch/guest/allpix/'
