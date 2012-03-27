###########################################
#
# iLCSoft versions for release v01-13-05
#
# F.Gaede, DESY 09.12.2011
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-13-05-pre01'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
#ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
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

CLHEP_version = "2.1.1.0"  # "2.1.0.1"

GSL_version = "1.14"

QT_version = "4.7.4" # "4.2.2"

CMake_version = "2.8.5"



# -------------------------------------------

LCIO_version = "v02-01-01-pre" # "v02-01"

GEAR_version = "v01-02" # "v01-01"

CED_version = "v01-05" # "v01-05"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-5"

ILCUTIL_version = "v00-03"

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-01"


# -------------------------------------------

KalTest_version = "v01-05" # "v01-04"

KalDet_version = "v01-07-pre" # "v01-06"

LCCD_version = "v01-02"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-05-01" # "v01-05"

Marlin_version = "v01-02-01" # "v01-02"

Mokka_version = "mokka-07-07-p07" # "mokka-07-07-p06"

MarlinReco_version = "v01-01" # "v01-00-01"

MarlinTrk_version = "v01-05-pre" # "v01-04"

MarlinTrkProcessors_version = "HEAD" # "v01-03"

Clupatra_version = "v00-05-01" # "v00-04-01"

LCFIPlus_version = "v00-03" # "v00-03"

ForwardTracking_version = "v01-01-01" # "v01-01-01"

MarlinKinfit_version = "v00-01-01" # "v00-01"

PandoraPFANew_version = "v00-08" # "v00-08"
MarlinPandora_version = "v00-07" # "v00-07"
PandoraAnalysis_version = "v00-03" # "v00-03"


LCFIVertex_version = "v00-06-01"

CEDViewer_version = "v01-05" # "v01-04-01"

Overlay_version = "v00-11-01"

#Eutelescope_version = "v00-06-03"

PathFinder_version =  "v00-01-01" # "v00-01-01"
MarlinTPC_version =  "v00-09-01" # "v00-09-01"

Druid_version = "1.8" 

Garlic_version = "v2.0.4"

