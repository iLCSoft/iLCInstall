###########################################
#
# iLCSoft versions for release v01-17-07
#
# DESY ilcsoft team
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-17-07-pre05'
# ----------------------------------------------------------------------------

CMAKE_CXX_FLAGS = '-Wall'

#CMAKE_CXX_FLAGS = '-Wall -std=c++11'
# c++11 - needs a newer compiler and compatible python, e.g. run
'''
 source /afs/cern.ch/sw/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
'''
# before starting the installation

# ----- if fortran is needed give a hint where to find the libary, e.g. for c++-11 w/ gcc 4.8 :
Fortran_lib_path = ""
#Fortran_lib_path = "/afs/cern.ch/sw/lcg/contrib/gcc/4.8.1/x86_64-slc6-gcc48-opt/lib64"

# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
#ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/space/ilcsoft/"
#ilcsoft_install_prefix = "/scratch/rosem/ilcsoft/"


#ilcsoft_install_dir = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/v01-17-07-pre01/"
ilcsoft_install_dir = os.path.join(ilcsoft_install_prefix  , ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5'
#ilcPath = ilcsoft_afs_path[ arch ]
ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------

#ilcPatchPath = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5/v01-15"

# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version
#MySQL_path = "/usr"

Boost_path = "/afs/desy.de/project/ilcsoft/sw/boost/1.58.0"







# ----- java ---------------------------------------------------------
#Java_version = "1.6.0"
#Java_path = ilcPath + "/java/" + Java_version # comment out to try auto-detect


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/cernlib/" + CERNLIB_version



# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "10.01"  

ROOT_version = "5.34.30" 

CLHEP_version = "2.1.4.1" 

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "2.8.5"


# -------------------------------------------

LCIO_version = "v02-06-pre"

GEAR_version = "v01-04-02-pre01" 

CED_version = "v01-09-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-02-01" 

FastJet_version = "3.1.2"

FastJetClustering_version = "v00-02"

MarlinFastJet_version = "v00-02"


# -------------------------------------------

KalTest_version = "v02-00-pre"  

KalDet_version = "v01-13-02-pre"

aidaTT_version = "v00-01-pre01"

DDKalTest_version = "v00-01-pre"

MarlinTrk_version = "v02-00-pre01"

MarlinTrkProcessors_version = "v02-00-pre04"

Clupatra_version = "v00-11-pre"

KiTrack_version = "v01-06-pre"

KiTrackMarlin_version = "v01-06-pre"

ForwardTracking_version = "v01-08-pre"

# -------------------------------------------

GBL_version = "V01-16-04"

LCCD_version = "v01-03"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-08-01-pre03"

Marlin_version = "v01-06-pre"

MarlinDD4hep_version = "v00-01-pre"

Mokka_version = "mokka-08-05-pre" 

MarlinReco_version = "v01-11-pre03"

FCalClusterer_version = "v00-01-pre01"

ILDPerformance_version = "v00-01-pre02"


LCFIVertex_version = "v00-06-02"
LCFIPlus_version = "v00-05-03-pre"


MarlinKinfit_version = "v00-01-05-pre"

PandoraPFANew_version = "v02-00-00"
MarlinPandora_version = "v02-00-00"
PandoraAnalysis_version = "v01-00-01" 

CEDViewer_version = "v01-09-pre"

Overlay_version = "v00-14"

PathFinder_version =  "v00-06"

MarlinTPC_version = "v01-00-pre"

LCTuple_version = "v01-04-pre"

BBQ_version =  "v00-01-02"

Druid_version = "2.2" # "1.8" 

Garlic_version = "v3.0.3"



#--- slic et al:

# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.2"

XercesC_version = "3.1.2" 

HepPDT_version = "3.04.01"

# new versions by J. McCormick
GDML_version = "HEAD"
LCDD_version = "HEAD"
SLIC_version = "HEAD"

SlicPandora_version = "HEAD"

DD4hep_version = "v00-12-pre05"
DD4hepExamples_version = "v00-12-pre05"

lcgeo_version = "v00-04-pre03"

Physsim_version = "v00-02-pre" 


