###########################################
#
# iLCSoft versions for release v01-11
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-11-pre04'
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
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc34_sl4/'
#ilcPath = ilcsoft_afs_path[ arch ]
# ----------------------------------------------------------------------------



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version


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


ROOT_version = "5.28.00"

CLHEP_version = "2.0.4.5" 

GSL_version = "1.8" 

QT_version = "4.2.2" 

CMake_version = "2.8.3" 



# -------------------------------------------

LCIO_version = "v01-51-02"

GEAR_version = "v00-17"

CED_version = "v01-02"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-3"

ILCUTIL_version = "v00-01-pre02"

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-02"


StandardConfig_version = "HEAD" # TODO v03-00-pre
MokkaDBConfig_version = "v02-02"
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-01-01"

KalDet_version = "v01-01-01"

LCCD_version = "v01-02"

RAIDA_version = "v01-06-01"

MarlinUtil_version = "v01-02"

Marlin_version = "v01-00"

Mokka_version = "mokka-07-06-p01"

MarlinReco_version = "HEAD" # TODO

PandoraPFANew_version = "v00-06"
PandoraAnalysis_version = "v00-02"
MarlinPandora_version = "v00-05"


LCFIVertex_version = "v00-05-pre" #TODO

CEDViewer_version = "v01-02"

Overlay_version = "v00-09-01"

Eutelescope_version = "v00-05-03-pre" # TODO v00-06-00-pre # FIXME doxygen

MarlinTPC_version = "v00-08-04"

Druid_version = "1.8" 

Garlic_version = "v2.0.4"

