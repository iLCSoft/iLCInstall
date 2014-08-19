###########################################
#
# iLCSoft versions for release v01-17-03
#
# Ch. Rosemann, DESY 01.08.2013
# F.G. 14.08
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-17-06'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
#ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/space/ilcsoft/"
#ilcsoft_install_prefix = "/scratch/rosem/ilcsoft/"


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


# ----- java ---------------------------------------------------------
Java_version = "1.6.0"
Java_path = ilcPath + "/java/" + Java_version # comment out to try auto-detect


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = ilcPath + "/cernlib/" + CERNLIB_version





# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "9.5.p02" 
#version 10.00 is on disk

ROOT_version = "5.34.18" 

#CLHEP_version = "2.1.4.1" already on disk -- needed for geant4.10
CLHEP_version = "2.1.1.0" # needed for g4 9.5   # ----- "2.1.3.1"

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "2.8.5"


# -------------------------------------------

LCIO_version = "v02-05" 

GEAR_version = "v01-04-01" 

CED_version = "v01-09-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-02" 

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-02"


# -------------------------------------------

KalTest_version = "v01-05-04"

KalDet_version = "v01-13-01"

GBL_version = "V01-16-04"

LCCD_version = "v01-03"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-08-01"

Marlin_version = "v01-05"

Mokka_version = "mokka-08-04" 

MarlinReco_version = "v01-10"

MarlinTrk_version = "v01-11"

MarlinTrkProcessors_version = "v01-11"

Clupatra_version = "v00-10"

LCFIVertex_version = "v00-06-02"
LCFIPlus_version = "v00-05-02"

KiTrack_version = "v01-05"
KiTrackMarlin_version = "v01-05"
ForwardTracking_version = "v01-07"

MarlinKinfit_version = "v00-01-02"

PandoraPFANew_version = "v00-16" #"v00-09"
MarlinPandora_version = "v00-14" #"v00-09-02"
PandoraAnalysis_version = "v00-06" #"v00-04"

CEDViewer_version = "v01-07-02"

Overlay_version = "v00-14"

PathFinder_version =  "v00-06"

MarlinTPC_version = "v00-17"

LCTuple_version = "v01-03-01"

BBQ_version =  "v00-01-02"

Druid_version = "2.2" # "1.8" 

Garlic_version = "v2.10.1"



#--- slic et al:

# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.1"

XercesC_version = "3.1.1" 

HepPDT_version = "3.04.01"

# new versions by J. McCormick
GDML_version = "v03-01-01"
LCDD_version = "v04-00-00"
SLIC_version = "v04-00-00"

SlicPandora_version = "v01-01-01"

DD4hep_version = "v00-10"
DDSim_version = "v00-02"

Physsim_version = "v00-01" 

#--- EUTelescope et al:
#Eutelescope_version = "trunk" # e.g. "tags/v00-09-00" (checked out via SVN) or "trunk" for git clone of the current dev version
#Eudaq_version = "trunk" # e.g. "tags/v1.2.2" (checked out via SVN) or "trunk" for a full git clone of the current development version
#Millepede2_version = 'trunk'
