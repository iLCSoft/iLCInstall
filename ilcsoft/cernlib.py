##################################################
#
# CERNLIB module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from baseilc import BaseILC
from util import *


class CERNLIB(BaseILC):
    """ Responsible for the CERNLIB installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CERNLIB", "cernlib")

        self.hasCMakeBuildSupport = False
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [ ["lib/libmathlib.a"], ["lib/libkernlib.a"] ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = "http://cernlib.web.cern.ch/cernlib/download/"+self.version+"_source/tar/"

    def downloadSources(self):
        
        if( os.path.exists(self.installPath) ):
            return

        # create install base directory
        trymakedir( os.path.dirname(self.installPath) )

        os.chdir( os.path.dirname(self.installPath) )

        # download installation script
        if( os.system( "wget http://wwwasd.web.cern.ch/wwwasd/cernlib/install/start_cern" ) != 0 ):
            self.abort( "Problems ocurred downloading sources!!")
        
        os.chmod( "start_cern", 0700 )

        # download index.html
        if( os.system( "wget " + self.download.url ) != 0 ):
            self.abort( "Problems ocurred downloading sources!!")

        # extract tar.gz files from index.html and put them into a list
        self.tgz_files = getoutput( r"grep tar.gz index.html | sed -e 's/.*href=\"\(.*\)\".*/\1/'" ).split('\n')

        # index.html no longer needed
        os.unlink( "index.html" )

        unneeded_files = []
        
        # download sources
        for file in self.tgz_files:
            if( int(self.version) < 2006 ):
                if( file.find("src_") == 0 ):
                    if( os.system( "wget " + self.download.url + file ) != 0 ):
                        self.abort( "Problems ocurred downloading sources!!" )
                else:
                    unneeded_files.append(file)
            else:
                if( (file == self.version + "_src.tar.gz") or \
                        (file == "include.tar.gz" )):
                    if( os.system( "wget " + self.download.url + file ) != 0 ):
                        self.abort( "Problems ocurred downloading sources!!" )
                    # unpack sources
                    if( os.system( "tar -xzf " + file ) != 0 ):
                        self.abort( "Problems ocurred unpacking sources!!")
                else:
                    unneeded_files.append(file)

        # delete unneeded files
        for file in unneeded_files:
            self.tgz_files.remove(file)
    
    def compile(self):
        
        os.chdir( os.path.dirname(self.installPath) )
        
        #if( self.rebuild ):
            #os.system( "rm -rf " + self.version )
        
        print "Compiling CERNLIB... This takes a LOT of time and displays " \
                + "no screen output, so just leave it running :)"
        
        if( int(self.version) < 2006 ):
            if( os.system( "./start_cern 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort("failed to compile!!")
        else:
            
            os.chdir( self.installPath )

            os.system( "echo \"Compiling CERNLIB... This takes a LOT of time and displays " \
                + "no screen output, so just leave it running :)\" >> " + self.logfile )
            
            # create directories
            trymakedir( "bin" )
            trymakedir( "lib" )
            trymakedir( "build/log" )

            # Create the top level Makefile with imake
            os.chdir( "build" )
            print "* Creating the top level Makefile with imake..."
            if( os.system( self.installPath + "/src/config/imake_boot" ) != 0 ):
                self.abort( "failed to create the top level Makefile with imake!!")
            
            # Install kuipc and the scripts (cernlib, paw and gxint) in $CERN_ROOT/bin
            print "* Building kuipc..."
            if( os.system( "make bin/kuipc > log/kuipc 2>&1" ) != 0 ):
                self.abort( "failed to compile!!")
            
            print "* Building scripts..."
            if( os.system( "make scripts/Makefile" ) != 0 ):
                self.abort( "failed to compile!!")
            
            os.chdir( "scripts" )
            print "* Building install.bin..."
            if( os.system( "make install.bin > ../log/scripts 2>&1" ) != 0 ):
                self.abort( "failed to compile!!")

            os.chdir( self.installPath + "/build" )
            print "* Building libraries..."
            if( os.system( "make > log/make.`date +%m%d` 2>&1" ) != 0 ):
                self.abort( "failed to compile!!")
    
    def cleanupInstall(self):
        os.chdir( os.path.dirname(self.installPath) )
        if( not self.rebuild ):
            for file in self.tgz_files:
                tryunlink(file)
            tryunlink( "start_cern" )
        os.chdir( self.installPath + "/build" )

        # delete object files
        os.system( "find -type f -name *.o -exec rm -f {} \;" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["CERNLIB_HOME"] = self.installPath + "/lib"
        
        if( self.mode =="install" ):

            # imake
            if( not isinPath( "imake" )):
                self.abort( "imake not found!!")
            # makedepend
            if( not isinPath( "makedepend" )):
                self.abort( "makedepend not found!!")
            # cpp
            if( not isinPath( "cpp" )):
                self.abort( "cpp not found!!")
            # grep
            if( not isinPath( "grep" )):
                self.abort( "grep not found!!")
            # sed
            if( not isinPath( "sed" )):
                self.abort( "sed not found!!")

            self.env["CERN_LEVEL"] = self.version
            self.env["CERN"] = os.path.dirname(self.installPath)
            self.env["CERN_ROOT"] = self.installPath
            self.env["CVSCOSRC"] = self.installPath + "/src"
            self.envpath["PATH"].append( "$CERN_ROOT/bin" )

