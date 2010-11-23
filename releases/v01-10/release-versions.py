###########################################
#
# iLCSoft versions for release v01-10
#
# F.Gaede, DESY 07.10.2010
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v01-10-pre04'
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/scratch/ilcsoft/"
#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
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

GEAR_version = "v00-15"

CED_version = "v01-01-01"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-2"

CMakeModules_version = "v01-10-01"

dcap_version = "1.9.5-5"



StandardConfig_version = "v02-01" 
MokkaDBConfig_version = "v02-02-pre"  # v02-02
LCFI_MokkaBasedNets_version = "v00-01" 



# -------------------------------------------

KalTest_version = "v01-00-pre02"       #-- "v00-14-02" 

KalDet_version = "v01-00-pre"       #-- "v00-14-02" 

LCCD_version = "v01-01-pre"  #--- "v01-00" 

RAIDA_version = "v01-05" 

MarlinUtil_version = "v01-01-pre"  #---- "v01-00" 

Marlin_version = "v01-13-pre"  #---- "v00-12" 

Mokka_version = "HEAD"     # --- "mokka-07-05 or 06 ?" 

MarlinReco_version = "v00-19-pre"  #----- "v00-19"

PandoraPFA_version = "v03-02-02-pre" 

PandoraPFANew_version = "v00-03"  #--- "v00-02" 
MarlinPandora_version = "v00-02"  #--- "v00-01" 

LCFIVertex_version = "v00-04-pre" 

CEDViewer_version = "v01-01-pre"  

Overlay_version = "v00-07-04"

Eutelescope_version = "v00-04-04-pre"     

MarlinTPC_version = "v00-07-pre"  #---- v00-07

SiliconDigi_version = "v00-04-02" 

Druid_version = "1.8" 

Garlic_version = "v2.03-pre"

