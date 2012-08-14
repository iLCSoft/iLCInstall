###########################################
#
# iLCSoft versions for release v01-15
#
# F.Gaede, DESY 09.12.2011
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-15-pre00'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc41_sl5/'
#ilcPath = ilcsoft_afs_path[ arch ]
#ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------



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


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "xercesc/2.7.0"



# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "9.5.p01"

ROOT_version = "5.28.00f"

CLHEP_version = "2.1.1.0"

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "2.8.5"



# -------------------------------------------

LCIO_version = "v02-01-02"

GEAR_version = "v01-02-02"

CED_version = "v01-07-pre" #"v01-06"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-5"

ILCUTIL_version = "v01-00"

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-01"


# -------------------------------------------

KalTest_version = "v01-05"

KalDet_version = "v01-09"

LCCD_version = "v01-02"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-05-03"

Marlin_version = "v01-03"

Mokka_version = "mokka-08-00-03"

MarlinReco_version = "v01-04-pre" #"v01-03"

MarlinTrk_version = "v01-08-pre" #"v01-07"

MarlinTrkProcessors_version = "v01-06-01-pre01" #"v01-06"

Clupatra_version = "v00-07-01"

LCFIVertex_version = "v00-06-01"
LCFIPlus_version = "v00-05"

KiTrack_version = "v01-03-pre" #"v01-02"
KiTrackMarlin_version = "v01-03-pre" #"v01-02"
ForwardTracking_version = "v01-06-pre" #"v01-05"

MarlinKinfit_version = "v00-01-02"

PandoraPFANew_version = "v00-09"
MarlinPandora_version = "v00-09" # "v00-08"
PandoraAnalysis_version = "v00-04"

CEDViewer_version = "v01-05-02"

Overlay_version = "v01-12-pre" #"v00-11-02"

#Eutelescope_version = "v00-06-03"

PathFinder_version =  "v00-01-01"
MarlinTPC_version =  "v00-09-01"

LCTuple_version = "v01-00"

BBQ_version =  "v00-01-02"

Druid_version = "1.8" 

Garlic_version = "v2.10"

