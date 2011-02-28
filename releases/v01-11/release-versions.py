###########################################
#
# iLCSoft versions for release v01-11
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-11-pre03'
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



# ======================= PACKAGE VERSIONS ===================================


ROOT_version = "5.28.00"

MySQL_version = "5.0.45"

Java_version = "1.6.0"

Geant4_version = "9.3.p02"

CERNLIB_version = "2006" 

CLHEP_version = "2.0.4.5" 

GSL_version = "1.8" 

QT_version = "4.2.2" 

CMake_version = "2.8.3" 



# -------------------------------------------

LCIO_version = "v01-51-02"

GEAR_version = "v00-17"

CED_version = "v01-02"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-3"

#CMakeModules_version = "v01-10-01" # DEPRECATED
ILCUTIL_version = "v00-01-pre02"

dcap_version = "1.9.5-5" # remove?

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

#PandoraPFA_version = "v03-02-02" # DEPRECATED

PandoraPFANew_version = "v00-05"
MarlinPandora_version = "v00-04"

LCFIVertex_version = "v00-05-pre"

CEDViewer_version = "v01-02"

Overlay_version = "v00-09-01"

Eutelescope_version = "v00-05-03-pre" # TODO v00-06-00-pre # FIXME doxygen

MarlinTPC_version = "v00-08-04"

#SiliconDigi_version = "v00-04-02" # update/remove??

Druid_version = "1.8" 

Garlic_version = "v2.0.4"

