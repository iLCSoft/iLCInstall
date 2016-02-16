###########################################
#
# iLCSoft versions for release v01-17-09
#
# DESY ilcsoft team
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-17-09-pre'
# ----------------------------------------------------------------------------

#-----------------------
# optionally build with c++11 ?
use_cpp11 = False

#===============================================================================
# NB: c++11 - needs a newer compiler and compatible python, e.g. run
'''
 source /afs/cern.ch/sw/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
# or on cvmfs:
# source /cvmfs/sft.cern.ch/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
# export PATH=/cvmfs/sft.cern.ch/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
# export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
'''
# before starting the installation
#================================================================================



# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#

ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/"
#ilcsoft_install_prefix = "/nfs/dust/ilc/user/voutsina/testarea/ilcsoft_c11/"
#ilcsoft_install_prefix = "/scratch/ilcsoft/"

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
#ilcPatchPath = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5/v01-15"



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version

if( ilcsoft_afs_path[ arch ] == '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc46_ub1204' ):
    MySQL_path = "/usr"


#------ boost headers files ------------------------------------------
Boost_path = "/afs/desy.de/project/ilcsoft/sw/boost/1.58.0"


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/cernlib/" + CERNLIB_version



# ----------------------------------------------------------------------------

Fortran_lib_path = ""
# ----- when using gcc48 we need to give a hint where to find the libary:
if( use_cpp11 ):
    Fortran_lib_path = "/afs/cern.ch/sw/lcg/contrib/gcc/4.8.1/x86_64-slc6-gcc48-opt/lib64"


##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################



#=============================================================================
# CXX_FLAGS for c++ compiler:
#
CMAKE_CXX_FLAGS = '-Wall'

if( use_cpp11 ):
    CMAKE_CXX_FLAGS = '-Wall -std=c++11'

# ----------------------------------------------------------------------------


# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "10.01"  

ROOT_version = "5.34.30" 

CLHEP_version = "2.1.4.1" 

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "2.8.5"


# -------------------------------------------

LCIO_version = "v02-07-pre"

GEAR_version = "v01-05-pre" 

CED_version = "v01-09-02"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-02-01" 

FastJet_version = "3.1.2"

FastJetClustering_version = "v00-02"

MarlinFastJet_version = "v00-02"

# -------------------------------------------

DD4hep_version = "v00-15-pre" ## need update for rel. notes
DD4hepExamples_version = "v00-15-pre"

lcgeo_version = "v00-06-pre" ## need update for rel. notes
 
# -------------------------------------------

KalTest_version = "v02-01"  

KalDet_version = "v01-13-02"

aidaTT_version = "v00-03-pre"

DDKalTest_version = "v00-03-pre"

MarlinTrk_version = "v02-01-pre"

MarlinTrkProcessors_version = "v02-02-pre"

Clupatra_version = "v00-13"

KiTrack_version = "v01-06"

KiTrackMarlin_version = "v01-08"

ForwardTracking_version = "v01-09-pre"

# -------------------------------------------

GBL_version = "V01-16-04"

LCCD_version = "v01-03"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-11-pre"

Marlin_version = "v01-08-pre"

MarlinDD4hep_version = "v00-01"

DDMarlinPandora_version = "v00-02-pre"

Mokka_version = "mokka-08-05-01" 

MarlinReco_version = "v01-14-pre"

FCalClusterer_version = "v00-02-pre01"

ILDPerformance_version = "v00-02-pre"


LCFIVertex_version = "v00-07-01"
LCFIPlus_version = "v00-07-pre"


MarlinKinfit_version = "v00-02-pre" ## need update for rel. notes

PandoraPFANew_version = "v02-05-00"
MarlinPandora_version = "v02-02-00"
PandoraAnalysis_version = "v01-02-00" 

CEDViewer_version = "v01-11-pre"

Overlay_version = "v00-14"

PathFinder_version =  "v00-06"

MarlinTPC_version = "v01-01"

LCTuple_version = "v01-05-pre"

BBQ_version =  "v00-01-02"

Druid_version = "2.2" # "1.8" 

Garlic_version = "v3.0.3"

Physsim_version = "v00-02" 


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.2"

XercesC_version = "3.1.2" 

#--- slic et al:

HepPDT_version = "3.04.01"

# versions tagged by J.Strube for this release 
GDML_version = "ilcsoft-v01-17-07"
LCDD_version = "ilcsoft-v01-17-07"
SLIC_version = "ilcsoft-v01-17-07"

SlicPandora_version = "ilcsoft-v01-17-07"




