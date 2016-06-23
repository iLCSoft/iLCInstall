###########################################
#
# iLCSoft versions for release v01-17-07
#
# DESY ilcsoft team
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-17-07-pre00'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
#ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/space/ilcsoft/"
#ilcsoft_install_prefix = "/scratch/rosem/ilcsoft/"
ilcsoft_install_prefix = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc48_sl5/"

#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
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
Java_version = "1.6.0"
Java_path = ilcPath + "/java/" + Java_version # comment out to try auto-detect


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = ilcPath + "/cernlib/" + CERNLIB_version


# ----- if fortran is needed give a hint where to find the libary
Fortran_lib_path = "/afs/cern.ch/sw/lcg/contrib/gcc/4.8.1/x86_64-slc6-gcc48-opt/lib64"




# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "10.01"  #"9.5.p02" 
#version 10.00 is on disk

ROOT_version = "5.34.18" 

CLHEP_version = "2.1.4.1" #already on disk -- needed for geant4.10
#CLHEP_version = "2.1.1.0" # needed for g4 9.5   # ----- "2.1.3.1"

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "3.4.3" #"2.8.5"


# -------------------------------------------

LCIO_version = "HEAD" 

GEAR_version = "HEAD" 

CED_version = "v01-09-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-02-01" 

FastJet_version = "3.1.2"

FastJetClustering_version = "v00-02"

MarlinFastJet_version = "v00-02"


# -------------------------------------------

KalTest_version = "HEAD"

KalDet_version = "HEAD"

DDKalTest_version = "HEAD"

aidaTT_version = "HEAD"

GBL_version = "V01-16-04"

LCCD_version = "v01-03"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-08-01"

Marlin_version = "v01-06-pre"

MarlinDD4hep_version = "HEAD"

Mokka_version = "HEAD" 

MarlinReco_version = "HEAD"

MarlinTrk_version = "HEAD"

MarlinTrkProcessors_version = "HEAD"

ILDPerformance_version = "HEAD"

Clupatra_version = "HEAD"

LCFIVertex_version = "v00-06-02"
LCFIPlus_version = "HEAD"

KiTrack_version = "HEAD"
KiTrackMarlin_version = "v01-05"
ForwardTracking_version = "HEAD"

MarlinKinfit_version = "HEAD"

PandoraPFANew_version = "HEAD" #"v00-16"
MarlinPandora_version = "HEAD" #"v00-14"
PandoraAnalysis_version = "HEAD" #"v00-06"

CEDViewer_version = "HEAD"

Overlay_version = "v00-14"

PathFinder_version =  "v00-06"

MarlinTPC_version = "HEAD"

LCTuple_version = "v01-03-01"

BBQ_version =  "v00-01-02"

Druid_version = "2.2" # "1.8" 

Garlic_version = "HEAD"



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

DD4hep_version = "HEAD"
DD4hepExamples_version = "HEAD"
lcgeo_version = "HEAD"

Physsim_version = "HEAD" 

#--- EUTelescope et al:
#Eutelescope_version = "trunk" # e.g. "tags/v00-09-00" (checked out via SVN) or "trunk" for git clone of the current dev version
#Eudaq_version = "trunk" # e.g. "tags/v1.2.2" (checked out via SVN) or "trunk" for a full git clone of the current development version
#Millepede2_version = 'trunk'
