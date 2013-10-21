###########################################
#
# iLCSoft versions for release v01-17-03
#
# Ch. Rosemann, DESY 01.08.2013
# F.G. 14.08
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-17-03'
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


# xerces-c (needed by geant4 for building gdml support - required by mokka)
#XERCESC_ROOT_DIR = ilcPath + "/xercesc/2.7.0"




# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "9.6.p01"

ROOT_version = "5.34.05" 

CLHEP_version = "2.1.3.1"

GSL_version = "1.14"

QT_version = "4.7.4"

CMake_version = "2.8.5"


# -------------------------------------------

LCIO_version = "v02-04-02" 

GEAR_version = "v01-03-01" 

CED_version = "v01-09-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-01" 

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-01"


# -------------------------------------------

KalTest_version = "v01-05-03"

KalDet_version = "v01-12"

GBL_version = "V01-15-03"

LCCD_version = "v01-03"

RAIDA_version = "v01-06-02"

MarlinUtil_version = "v01-07-01"

Marlin_version = "v01-05"

Mokka_version = "mokka-08-02" 

MarlinReco_version = "v01-07"

MarlinTrk_version = "v01-11"

MarlinTrkProcessors_version = "v01-09-01"

Clupatra_version = "v00-10"

LCFIVertex_version = "v00-06-01"
LCFIPlus_version = "v00-05-02"

KiTrack_version = "v01-04"
KiTrackMarlin_version = "v01-04"
ForwardTracking_version = "v01-07"

MarlinKinfit_version = "v00-01-02"

PandoraPFANew_version = "v00-12" #"v00-09"
MarlinPandora_version = "v00-11" #"v00-09-02"
PandoraAnalysis_version = "v00-05" #"v00-04"

CEDViewer_version = "v01-07"

Overlay_version = "v00-13"

PathFinder_version =  "v00-05"

MarlinTPC_version = "v00-14"

LCTuple_version = "v01-03"

BBQ_version =  "v00-01-02"

Druid_version = "2.2" # "1.8" 

Garlic_version = "v2.10.1"



#--- slic et al:

XercesC_version = "3.1.1" 

HepPDT_version = "3.04.01"

# new versions by J. McCormick
GDML_version = "v03-00-00"
LCDD_version = "v03-02-00"
SLIC_version = "v03-01-03"  

DD4hep_version = "v00-04"



#--- EUTelescope et al:
Eutelescope_version = "v00-09-02" # or: "HEAD" for dev version
Eudaq_version = "tags/v01-01-00" # or: "trunk" for dev version (i.e. git master at https://github.com/eudaq/eudaq)
Millepede2_version = 'tags/V04-00-02'
