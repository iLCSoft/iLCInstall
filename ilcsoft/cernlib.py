##################################################
#
# CERNLIB module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################

# custom imports
from .baseilc import BaseILC
from .util import *


class CERNLIB(BaseILC):
    """ Responsible for the CERNLIB installation process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "CERNLIB", "cernlib")

        self.installSupport = False
        self.hasCMakeBuildSupport = False
        self.download.supportHEAD = False
        self.download.supportedTypes = ["wget"]

        self.reqfiles = [ ["lib/libmathlib.a"], ["lib/libkernlib.a"] ]

    def setMode(self, mode):
        BaseILC.setMode(self, mode)

        urlver=self.version

        if self.version=='2006':
            urlver='2006b'
        
        # don;t remove this line (needed to skip version check in baseilc.py; Version( "2006" ) raises Exception)
        self.download.url = "http://cernlib.web.cern.ch/cernlib/download/"+urlver+"_source/tar/"

    def downloadSources(self):
        
        if( os.path.exists(self.installPath) ):
            return

        trymakedir( self.installPath+'/sources' )
        os.chdir( os.path.dirname(self.installPath) )

        import urllib2 as urllib

        if self.version == '2005' :
            # cernlib fix from Harald Vogt: http://www-zeuthen.desy.de/~hvogt/
            urllib.request.urlretrieve( "http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib-2005-all-new.tgz", "cernlib-2005-all-new.tgz" )
            urllib.request.urlretrieve( "http://www-zeuthen.desy.de/linear_collider/cernlib/new/cernlib.2005.corr.2009.06.13.tgz", "cernlib.2005.corr.2009.06.13.tgz" )

            if( os_system( "tar xzf cernlib-2005-all-new.tgz") != 0 ):
                self.abort("failed to extract cernlib sources")

            # use more recent corrections (64 bit compatible)
            os_system( "mv cernlib.2005.corr.tgz cernlib.2005.corr.tgz-old && ln -s cernlib.2005.corr.2009.06.13.tgz cernlib.2005.corr.tgz")

        elif self.version == '2006' :
            

            # binary tarballs
            #if platform.architecture()[0] == '64bit':
            #    if Version( self.parent.debugInfo['GCC_VERSION'] )[:2] == (4,1) :
            # ...
           
            ## download index.html
            #if( os_system( "wget " + self.download.url ) != 0 ):
            #    self.abort( "Problems ocurred downloading sources!!")
            ## parse index.html for extracting source tarballs
            #src_tarballs = getoutput( r"grep tar.gz index.html | sed -e 's/.*href=\"\(.*\)\".*/\1/'" ).split('\n')
            ## index.html no longer needed
            #os.unlink( "index.html" )

            #index_html=urllib.urlopen( self.download.url ).read()

            #import re
            #regex=re.compile( 'href="(.*)"' , re.VERBOSE )

            #hrefs=regex.findall( index_html )

            #src_tarballs=[ i.strip() for i in hrefs if i.strip()[-7:] == '.tar.gz' ]

            #for tarball in src_tarballs:
            #    print 'downloading:', self.download.url + tarball
            #    urllib.urlretrieve( self.download.url + tarball, tarball )
            #    print 'extracting:', tarball
            #    os_system( "tar xzf " + tarball )
            #    os_system( "mv %s %s/sources" % (tarball, self.installPath) )

            tarballs = [ '2006_src.tar.gz', 'include.tar.gz' ]
            for tarball in tarballs:
                print('downloading:', tarball)
                urllib.request.urlretrieve( self.download.url + tarball, tarball )
                if os_system( "tar xzf " + tarball ) != 0:
                    self.abort( 'failed to extract '+ tarball )
                os_system( "mv " + tarball + " " + self.installPath+'/sources' )


    def compile(self):

        os.chdir( os.path.dirname(self.installPath) )

        # compiling cernlib with -jX crashes
        make_flags=os.getenv("MAKEFLAGS","")
        if make_flags.find('-j') != -1:
            del(os.environ["MAKEFLAGS"])

        if self.version == '2005' :

            install_cmd = """
                type mkdirhier || alias mkdirhier=mkdir
                ./Install_cernlib
                test $? -eq 0 || exit 1
                . cernlib_env
                
                # install headers
                export CERN_INCLUDEDIR=$CERN_ROOT/include
                mkdir $CERN_INCLUDEDIR
                cd $CERN_ROOT/build
                gmake install.include 1>./log/include_install.log 2>&1
                test $? -eq 0 || exit 1

                # move all build generated stuff into a subdirectory
                cd $CERN
                #mkdir $CERN_ROOT/sources
                mv -f $(ls | grep -v ^${CERN_LEVEL}$) $CERN_ROOT/sources
            """
            f = open('install_cernlib.sh', 'w')
            f.write( install_cmd )
            f.close()

            if( os_system( "chmod 755 install_cernlib.sh && ./install_cernlib.sh 2>&1 | tee -a " + self.logfile ) != 0 ):
                self.abort("failed to compile!!")


        if self.version == '2006' :
            
            os.chdir( self.installPath )

            # create directories
            trymakedir( "bin" )
            trymakedir( "lib" )
            trymakedir( "build/log" )

            # Create the top level Makefile with imake
            os.chdir( "build" )
            print("* Creating the top level Makefile with imake...")
            if( os_system( self.installPath + "/src/config/imake_boot" ) != 0 ):
                self.abort( "failed to create the top level Makefile with imake!!")
            
            # Install kuipc and the scripts (cernlib, paw and gxint) in $CERN_ROOT/bin
            print("* Building kuipc...")
            if( os_system( "make bin/kuipc > log/kuipc 2>&1" ) != 0 ):
                self.abort( "failed to compile!!")
            
            print("* Building scripts...")
            if( os_system( "make scripts/Makefile" ) != 0 ):
                self.abort( "failed to compile!!")
            
            os.chdir( "scripts" )

            import platform

            # skip install.bin rule on 64bit
            if platform.architecture()[0] != '64bit': 
                print("* Building install.bin...")
                if( os_system( "make install.bin > ../log/scripts 2>&1" ) != 0 ):
                    self.abort( "failed to compile!!")

            os.chdir( self.installPath + "/build" )
            print("* Building libraries...")
            if( os_system( "make > log/make.`date +%m%d` 2>&1" ) != 0 ):
                self.abort( "failed to compile!!")
    
    def cleanupInstall(self):
        os.chdir( os.path.dirname(self.installPath) )
        #if( not self.rebuild ):
        #    for file in self.tgz_files:
        #        tryunlink(file)
        #    tryunlink( "start_cern" )
        #os.chdir( self.installPath + "/build" )

        ## delete object files
        os_system( "find "+self.installPath + "/build -type f -name *.o -exec rm -f {} \;" )

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.envorder=[ "CERN_ROOT" ]
        self.env["CERN_ROOT"] = self.installPath
        
        #self.env["CERNLIB_HOME"] = "$CERN_ROOT/lib"
        self.env["CVSCOSRC"] = "$CERN_ROOT/src"
        self.env["CERN_LEVEL"] = self.version
        self.env["CERN"] = os.path.dirname(self.installPath)
        
        if self.installPath != "/usr":
            self.envpath["PATH"].append( "$CERN_ROOT/bin" )


        if( self.mode =="install" ):

            # check if some commands are available
            for cmd in ['imake', 'makedepend', 'cpp']:
                if not isinPath( cmd ):
                    self.abort( cmd+" not found!!" )
