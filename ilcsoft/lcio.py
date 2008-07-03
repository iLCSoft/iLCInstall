##################################################
#
# LCIO module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class LCIO(BaseILC):
    """ Responsible for the LCIO software installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "LCIO", "lcio")
        
        self.reqfiles = [ ["lib/liblcio.a", "lib/liblcio.so", "lib/liblcio.dylib"] ]
        
        # supported cmake modules
        self.cmakebuildmodules = [ "Java" ]

        # flag for building lcio java stuff
        self.buildJava = True

        # flag for building lcio fortran stuff
        self.buildFortran = False

        # supported download types
        self.download.supportedTypes = ["cvs"]

        # set some cvs variables
        # export CVSROOT=:pserver:anonymous@cvs.freehep.org:/cvs/lcio
        self.download.accessmode = "pserver"
        self.download.server = "cvs.freehep.org"
        self.download.root = "cvs/lcio"

    def compile(self):
        """ compile LCIO """
        
        os.chdir( self.installPath )
        
        if( self.rebuild ):
            if( self.useCMake ):
                tryunlink( "build/CMakeCache.txt" )
            else:
                os.system( "ant clean" )
        
        if( self.useCMake ):
            os.chdir( "build" )
            if( os.system( "cmake " + self.genCMakeCmd() + " .. 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to configure!!" )
            if( os.system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( os.system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to install!!" )
        else:
            # generate headers
            if( os.system( "ant aid.generate 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to generate header files!!" )
            # lcio java stuff
            if( self.buildJava ):
                if( os.system( "ant aid 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to compile lcio java!!" )
            if( os.system( "ant cpp 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort( "failed to compile!!" )
            if( self.buildFortran ):
                if( os.system( "ant f77 2>&1 | tee -a " + self.logfile ) != 0 ):
                    self.abort( "failed to compile!!" )
        
    def buildDocumentation(self):
        # build documentation
        if( self.buildDoc ):
            os.chdir( self.installPath )
            print 80*'*' + "\n*** Building documentation for " + self.name + "...\n" + 80*'*'
            if( self.buildJava and not self.useCMake ):
                if(isinPath("javadoc")):
                    print 80*'*' + "\n*** Creating JAVA API documentation for " + self.name + " with javadoc...\n" + 80*'*'
                    os.system( "ant doc 2>&1 | tee -a " + self.logfile )
            if( not self.useCMake ):
                if(isinPath("doxygen")):
                    print 80*'*' + "\n*** Creating C++ API documentation for " + self.name + " with doxygen...\n" + 80*'*'
                    os.system( "ant cpp.doc" )
            if(isinPath("latex")):
                if( not self.useCMake ):
                    print 80*'*' + "\n*** Creating " + self.name + " manual (from tex)...\n" + 80*'*'
                    r = os.system( "ant doc.manual 2>&1 | tee -a " + self.logfile )
                    if( r != 0 ):
                        print 80*'*' + "*** WARNING: sth. went wrong with creating the " + self.name + " manual\n" + 80*'*'
                print 80*'*' + "\n*** Creating " + self.name + " reference manual (from api doc)...\n" + 80*'*'
                r = os.system( "ant doc.ref 2>&1 | tee -a " + self.logfile )
                if( r != 0 ):
                    print 80*'*' + "*** WARNING: sth. went wrong with creating the " + self.name + " reference manual\n" + 80*'*'

    def preCheckDeps(self):
        BaseILC.preCheckDeps(self)

        # in checkDeps() the dependencies from the installed version
        # are compared against the ones in the config file, so we need to
        # ensure that Java is autodetected for comparing versions
        if( self.mode == "use" ):
            if( os.path.exists( self.realPath() + "/lib/lcio.jar" )):
                self.addBuildOnlyDependency( ["Java"] )
            else:
                self.addExternalDependency( ["Java"] )
        
        if( self.mode == "install" ):
            #if( self.buildFortran and self.useCMake ):
            if( self.buildFortran ):
                self.reqfiles.append(["bin/anajob_F"])
            if( self.buildJava ):
                self.addBuildOnlyDependency( ["Java"] )
                self.reqfiles.append(["lib/lcio.jar"])
            else:
                self.addExternalDependency( ["Java"] )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["LCIO"] = self.installPath

        # PATH
        self.envpath["PATH"].append( "$LCIO/tools" )
        self.envpath["PATH"].append( "$LCIO/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$LCIO/lib" )

        if( self.mode == "install" ):

            if( self.useCMake ):
                if( self.buildFortran ):
                    self.envcmake["BUILD_F77_TESTJOBS"]="ON"
                else:
                    self.envcmake["BUILD_F77_TESTJOBS"]="OFF"
                if( self.buildJava ):
                    self.envcmake["INSTALL_JAR"]="ON"
                else:
                    self.envcmake["INSTALL_JAR"]="OFF"

            # check for doc tools
            if( self.buildDoc ):
                if( not isinPath("javadoc")):
                    print "*** WARNING: javadoc was not found!! Part of the " + self.name + " documentation will not be built!!! "
                if( not isinPath("doxygen")):
                    print "*** WARNING: doxygen was not found!! Part of the " + self.name + " documentation will not be built!!! "
                if( not isinPath("latex")):
                    print "*** WARNING: latex was not found!! Part of the " + self.name + " documentation will not be built!!! "
            elif( self.useCMake ):
                self.envcmake["INSTALL_DOC"]="OFF"


