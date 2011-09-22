###########################################
#
# iLCSoft versions for release v01-12
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-12-dev04'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/scratch/$USER/ilcsoft/"
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc41_sl5/'
#ilcPath = ilcsoft_afs_path[ arch ]
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


# ----- geant4 -------------------------------------------------------
Geant4_version = "9.3.p02"
Geant4_path = ilcPath + "/geant4/" + Geant4_version
# path to geant4 environment initialization script
# comment out if not needed
G4ENV_INIT_path = ilcPath + "/geant4/" + "env_" + Geant4_version + ".sh"


# ----- CERNLIB ------------------------------------------------------
CERNLIB_version = "2006" 
CERNLIB_path = ilcPath + "/cernlib/" + CERNLIB_version




# ======================= PACKAGE VERSIONS ===================================


ROOT_version = "5.28.00f" # p.v. 5.28.00

CLHEP_version = "2.0.4.5" 

GSL_version = "1.14" # p.v. 1.8

QT_version = "4.2.2" # mac osx needs version >= 4.7.3

CMake_version = "2.8.5"  # p.v. 2.8.3



# -------------------------------------------

LCIO_version = "v02-00-pre00"

GEAR_version = "HEAD" # p.v. v00-17

CED_version = "v01-03-pre01" # p.v. v01-02

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-5-pre" # p.v. CondDBMySQL_ILC-0-9-3

ILCUTIL_version = "v00-02-pre01" # p.v. v00-01

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"
MarlinFastJet_version = "v00-01-pre00"


StandardConfig_version = "v03-00"
MokkaDBConfig_version = "v03-00" # p.v. v02-02
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-02-pre00" # p.v. v01-01-01

KalDet_version = "v01-02-pre01" # p.v. v01-01-01

LCCD_version = "v01-02"

RAIDA_version = "v01-06-01"

MarlinUtil_version = "v01-04-pre01" # p.v. v01-03

Marlin_version = "v01-01-pre00" # p.v. v01-00

Mokka_version = "HEAD" # "mokka-07-06-p03-SDHcal" # p.v. mokka-07-06-p02

MarlinReco_version = "v00-30-pre00" # p.v. v00-20

MarlinTrk_version = "HEAD"
MarlinTrkProcessors_version = "HEAD"

MarlinKinfit_version = "v00-01-pre00"

PandoraPFANew_version = "v00-07"
MarlinPandora_version = "v00-06"
PandoraAnalysis_version = "v00-03"


LCFIVertex_version = "HEAD" # p.v. v00-05

CEDViewer_version = "v01-03-pre00" # p.v. v01-02

Overlay_version = "v00-11-pre01" # p.v. v00-10

Eutelescope_version = "v00-06-03-pre" # p.v. v00-05-03

MarlinTPC_version =  "v00-09-00" # p.v. v00-08-04

Druid_version = "1.8" 

Garlic_version = "v2.0.4"

