##################################################
#
# ROOT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
import os
from .baseilc import BaseILC
from .util import *


class ROOT(BaseILC):
    """ Responsible for the ROOT configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "ROOT", "root")

        #self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.download.supportedTypes = [ "wget", "svn-export", "svn" ]

        self.reqfiles = [
                ["lib/libCore.so", "lib64/libCore.so", "lib/libCore.dylib"], 
                ["lib/libPhysics.so", "lib64/libPhysics.so", "lib/libPhysics.dylib"],
                ["bin/root-config"]
        ]

        self.reqmodules_external = [ "GSL" , "MySQL", "CMake" ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        self.download.url = 'https://root.cern.ch/download/root_v%s.source.tar.gz' % self.version
        self.download.svnurl = 'http://root.cern.ch/svn/root'

        if( Version( self.version ) == 'HEAD' ):
            self.download.svnurl += '/trunk'
        else:
            self.download.svnurl += '/tags/v' + self.version.replace('.','-')

        self.cmakeconfig = self.installPath + "/cmake"

    def init(self):
        BaseILC.init(self)

        if Version(self.version) <= '6.19':
            # See: https://root-forum.cern.ch/t/problems-building-root-6-18-04-with-builtin-davix/44225
            self.download.supportedTypes = ['Github']
            self.download.gituser = 'root-project'
            self.download.gitrepo = 'root'
            self.download.branch = 'v6-18-00-patches'
            self.download.type = 'GitHub'


        if( Version( self.version ) == 'HEAD' and self.download.type[:3] != 'svn' ):
            self.download.type="svn-export"


    def downloadSources(self):
        BaseILC.downloadSources(self)

        # move sources to a subdirectory
##        os.renames( self.version, self.name )
##        os.renames( self.name, self.version + "/" + self.name )

    def cleanupInstall(self):
        BaseILC.cleanupInstall(self)
        os.chdir( self.installPath )
        os_system( "rm -rf ./" + self.name )

    def compile(self):
        """ compile root """

#        os.chdir( self.installPath + "/" + self.name )

        #if( self.rebuild ):
        #    os_system( "make clean" )

        gsl=self.parent.module("GSL")
        gsl_bindir = gsl.installPath + "/bin"
        gsl_libdir = gsl.installPath + "/lib"
        gsl_incdir = gsl.installPath + "/include"

        os.environ["LD_RUN_PATH"] = gsl_libdir

##        if( os_system( "./configure --fail-on-missing --enable-builtin-pcre --enable-explicitlink --enable-soversion --enable-roofit --enable-minuit2 --enable-gdml --enable-table --enable-unuran --enable-gsl-shared --with-gsl-incdir="+ gsl_incdir +" --with-gsl-libdir="+ gsl_libdir + " --enable-python") != 0 ):
##            self.abort( "failed to configure!!" )
##
##
##
##        if( os_system( "make 2>&1 | tee -a " + self.logfile ) != 0 ):
##            self.abort( "failed to compile!!" )
##
##        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
##            self.abort( "failed to install!!" )

        trymakedir( self.installPath + "/../build-" + self.version )
        os.chdir( self.installPath + "/../build-" + self.version )

        if( self.rebuild ):
            tryunlink( "CMakeCache.txt" )

        self.envcmake['CMAKE_INSTALL_PREFIX']=self.installPath

        self.envcmake['GSL_ROOT_DIR']=gsl.installPath
        self.envcmake['GSL_CONFIG_EXECUTABLE']=gsl_bindir+'/gsl-config'

        if Version(self.version) < "6.30":
            self.envcmake.setdefault( 'gsl_shared',     'ON' )
            self.envcmake.setdefault( 'builtin_gsl',    'OFF' ) # we provide GSL, don't recompile it !
            self.envcmake.setdefault( 'minuit2',        'ON' )

        self.envcmake.setdefault( 'gdml',           'ON' )
        self.envcmake.setdefault( 'roofit',         'ON' )
        self.envcmake.setdefault( 'unuran',         'ON' )
        self.envcmake.setdefault( 'xrootd',         'ON' )
        self.envcmake.setdefault( 'mathmore',       'ON' )
        self.envcmake.setdefault( 'builtin_xrootd', 'ON' )
        self.envcmake.setdefault( 'fortran',        'OFF' )
        self.envcmake.setdefault( 'mysql',          'OFF' )
        self.envcmake.setdefault( 'sqlite',         'OFF' )

        if( os_system( self.genCMakeCmd() + " 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to configure!!" )
        if( os_system( "make ${MAKEOPTS} 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to compile!!" )
        if( os_system( "make install 2>&1 | tee -a " + self.logfile ) != 0 ):
            self.abort( "failed to install!!" )



        if self.version > "6.19.0":
            # Need to symlink two cmake scripts that are not installed properly
            # otherwise and would break packages that depend on ROOT
            for mod in ['RootMacros.cmake', 'RootTestDriver.cmake']:
                try:
                    link_path = os.path.join(self.installPath, 'cmake', mod)
                    src = os.path.join(self.installPath, 'cmake', 'modules', mod)
                    os.symlink(src, link_path)
                except FileExistsError:
                    pass

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)
        # Required for LCIO installation.
        # LCIO uses its own FindROOT.cmake relying on ROOT_DIR ...
        self.addCMakeCache( "ROOT_DIR", self.installPath, "Path to ROOT" )
        self.envcmds.append('test -r ' + self.installPath + '/bin/thisroot.sh && . ' + self.installPath + '/bin/thisroot.sh')

