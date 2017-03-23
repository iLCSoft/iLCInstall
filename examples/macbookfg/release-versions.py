###########################################
#
# iLCSoft versions for release v01-17-07
#
# DESY ilcsoft team
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release= "HEAD" # 'v01-17-07'
# ----------------------------------------------------------------------------

#-----------------------
# optionally build with c++11 ?
use_cpp11 = True

#===============================================================================
# NB: c++11 - needs a newer compiler and compatible python, e.g. run
'''
 source /afs/cern.ch/sw/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
'''
# before starting the installation
#================================================================================



# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#

#ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/"
#ilcsoft_install_prefix = "/nfs/dust/ilc/user/voutsina/testarea/ilcsoft_c11/"

ilcsoft_install_prefix = "/data/ilcsoft/"

# ----------------------------------------------------------------------------
#--- the ilcsoft_release is now automatically appended in release-ilcsoft.cfg 
#     but not in release-base.cfg !!

#append_version_to_install_prefix = False
#if(append_version_to_install_prefix):
#    ilcsoft_install_dir = os.path.join(ilcsoft_install_prefix , ilcsoft_release )

# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# ===========================================================
# Modify this path to where you want ilcinstall to look
# for pre-installed (base) packages
# typically this would be left to ilcsoft_install_prefix
# or set to an /afs or /cvmfs base installation that you 
# want to use
# ===========================================================

#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc48_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5'


ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------


#--------------------------------------------------------------------------
ilcPatchPath = "/data/ilcsoft/HEAD"



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.5.22"
MySQL_path = ilcPath + "/mysql/" + MySQL_version

#if( ilcsoft_afs_path[ arch ] == '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc46_ub1204' ):
MySQL_path = "/usr/local"


#------ boost headers files ------------------------------------------
Boost_path = "/usr/local/opt/boost160"

#------ Eigen headers files ------------------------------------------
Eigen_path = "/usr/local/opt/eigen32"


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
#CERNLIB_path = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/cernlib/" + CERNLIB_version



# ----------------------------------------------------------------------------

Fortran_lib_path = ""
# ----- when using gcc48 we need to give a hint where to find the libary:
##if( use_cpp11 ):
##    Fortran_lib_path = "/afs/cern.ch/sw/lcg/contrib/gcc/4.8.1/x86_64-slc6-gcc48-opt/lib64"


##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################



#=============================================================================
# CXX_FLAGS for c++ compiler:
#
#CMAKE_CXX_FLAGS = '-Wall'

#if( use_cpp11 ):
#    CMAKE_CXX_FLAGS = '-Wall -std=c++11'

# ----------------------------------------------------------------------------


# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.03"
CLHEP_version =  "2.3.4.3" #"2.3.1.1"
ROOT_version = "6.08.00"

#Geant4_version = "10.01.p01"  
#ROOT_version = "6.06.02" # "6.04.14" # "5.34.32" 
#CLHEP_version = "2.2.0.4" 

GSL_version = "2.1" # "1.15"

QT_version = "4.7.4"

CMake_version = "3.3.2" #"2.8.5"


# -------------------------------------------

LCIO_version = "HEAD" # "v02-06"

GEAR_version = "HEAD" # "v01-04-02" 

CED_version = "HEAD" # "v01-09-01"

CondDBMySQL_version = "HEAD" # "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "HEAD" # "v01-02-01" 

FastJet_version = "3.2.0"
FastJetcontrib_version = "1.024"

FastJetClustering_version = "HEAD" # "v00-02"

MarlinFastJet_version = "HEAD" # "v00-02"


# -------------------------------------------

KalTest_version = "HEAD" # "v02-00"  

KalDet_version = "HEAD" # "v01-13-02"

aidaTT_version = "HEAD" # "v00-01"

DDKalTest_version = "HEAD" # "v00-01"

MarlinTrk_version = "HEAD" # "v02-00"

MarlinTrkProcessors_version = "HEAD" # "v02-00"

Clupatra_version = "HEAD" # "v00-11"

KiTrack_version = "HEAD" # "v01-06"

KiTrackMarlin_version = "HEAD" # "v01-06"

ForwardTracking_version = "HEAD" # "v01-08"

ConformalTracking_version = "HEAD" # "v01-08"

# -------------------------------------------

GBL_version = "HEAD" # "V01-16-04"

LCCD_version = "HEAD" # "v01-03"

RAIDA_version = "HEAD" # "v01-06-02"

MarlinUtil_version = "HEAD" # "v01-09"

Marlin_version = "HEAD" # "v01-06"

MarlinDD4hep_version = "HEAD" # "v00-01"

DDMarlinPandora_version = "HEAD" # "v00-01"

Mokka_version = "HEAD" # "mokka-08-05" 

MarlinReco_version = "HEAD" # "v01-11"

FCalClusterer_version = "HEAD" # "v00-01"

ILDPerformance_version = "HEAD" # "v00-01"

ClicPerformance_version = "HEAD"

LCFIVertex_version = "HEAD" # "v00-07"
LCFIPlus_version = "HEAD" # "v00-05-03"


MarlinKinfit_version = "HEAD" # "v00-01-05"
MarlinKinfitProcessors_version = "HEAD" # "v00-01-05"

PandoraPFANew_version =  "HEAD" #"v02-03-00"
MarlinPandora_version = "HEAD" # "v02-00-00"
PandoraAnalysis_version = "HEAD" # "v01-00-01" 


CEDViewer_version = "HEAD" # "v01-09"

Overlay_version = "HEAD" # "v00-14"

PathFinder_version =  "HEAD" # "v00-06"

MarlinTPC_version = "HEAD" # "v01-00"

LCTuple_version = "HEAD" # "v01-04"

BBQ_version =  "HEAD" # "v00-01-02"

Druid_version = "HEAD" # "2.2" # "1.8" 

Garlic_version = "HEAD" # "v3.0.3"



#--- slic et al:

## xerces-c (needed by geant4 for building gdml support - required by mokka)
#
XercesC_version = "3.1.4" 
XERCESC_ROOT_DIR = ilcPath + "/xercesc/" + XercesC_version

#
#HepPDT_version = "3.04.01"
#
## versions tagged by J.Strube for this release 
#GDML_version = "ilcsoft-v01-17-07"
#LCDD_version = "ilcsoft-v01-17-07"
#SLIC_version = "ilcsoft-v01-17-07"
#
#SlicPandora_version = "ilcsoft-v01-17-07"

DD4hep_version = "HEAD" # "v00-12"
DD4hepExamples_version = "HEAD" # "v00-12"

lcgeo_version = "HEAD" # "v00-04"

Physsim_version = "HEAD" # "v00-02" 



