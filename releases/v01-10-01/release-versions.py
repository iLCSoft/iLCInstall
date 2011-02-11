###########################################
#
# iLCSoft versions for release v01-10-01
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-10-01'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = "/scratch/ilcsoft/"
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/i386_gcc34_sl4/'
#ilcPath = ilcsoft_afs_path[ arch ]
# ----------------------------------------------------------------------------



# ======================= PACKAGE VERSIONS ===================================


ROOT_version = "5.27.06"

MySQL_version = "5.0.45"

Java_version = "1.6.0"

Geant4_version = "9.3.p02"

CERNLIB_version = "2006" 

CLHEP_version = "2.0.4.5" 

GSL_version = "1.8" 

QT_version = "4.2.2" 

CMake_version = "2.6.2" 



# -------------------------------------------

LCIO_version = "v01-51-02"

GEAR_version = "v00-16"

CED_version = "v01-01-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-2"

CMakeModules_version = "v01-10-01"

dcap_version = "1.9.5-5"

FastJet_version = "2.4.2"
FastJetClustering_version = "v00-01"


StandardConfig_version = "v02-02"
MokkaDBConfig_version = "v02-02"
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-00"

KalDet_version = "v01-00"

LCCD_version = "v01-01-01"

RAIDA_version = "v01-05" 

MarlinUtil_version = "v01-01"

Marlin_version = "v00-13-01"

Mokka_version = "mokka-07-06"

MarlinReco_version = "v00-19-01"

PandoraPFA_version = "v03-02-02" 

PandoraPFANew_version = "v00-04"
MarlinPandora_version = "v00-03"

LCFIVertex_version = "v00-04" 

CEDViewer_version = "v01-01-01"

Overlay_version = "v00-08"

Eutelescope_version = "v00-04-04"     

MarlinTPC_version = "v00-08-03"

SiliconDigi_version = "v00-04-02" 

Druid_version = "1.8" 

Garlic_version = "v2.0.3"

