###########################################
#
# iLCSoft versions for installing a current HEAD
# version of the ilcsoft packages.
# The external base tools need to be installed
#
# DESY ilcsoft team
###########################################
import datetime
import platform

# --------- ilcsoft release version ------------------------------------------
ilcsoft_release='v02-01-pre'
# ----------------------------------------------------------------------------

#-----------------------
# we now always build with c++11 ?
# use_cpp11 = True
# if nightlies:
#    use_cpp11 = nb_use_cpp11
#    print "******************* use_cpp11", use_cpp11

# which cxx standard to use
cxx_standard = 17

afsPath = None
try:
    afsPath = ilcsoft_afs_path[ arch ]
except KeyError:
    pass

#===============================================================================
# use a compiler that knows c++11, run
#
'''
#===== gcc 4.9:
# . ./scripts/use_gcc49_afs.sh
 source /afs/cern.ch/sw/lcg/contrib/gcc/4.9.3/x86_64-slc6/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/bin:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/lib:$LD_LIBRARY_PATH


# or on cvmfs:
# . ./scripts/use_gcc49_cvmfs.sh
 source /cvmfs/sft.cern.ch/lcg/contrib/gcc/4.9.3/x86_64-slc6/setup.sh
 export PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/bin:$PATH
 export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/lib:$LD_LIBRARY_PATH
'''
# before starting the installation
#================================================================================



# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#
if installPrefix is None:
    ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
else:
    ilcsoft_install_prefix = installPrefix
#ilcsoft_install_prefix = "/cvmfs/ilc.desy.de/sw/x86_64_gcc48_sl6/"
#ilcsoft_install_prefix = "/scratch/ilcsoft/"

# ----------------------------------------------------------------------------
#--- the ilcsoft_release is now automatically appended in release-ilcsoft.cfg
#     but not in release-base.cfg !!

#append_version_to_install_prefix = False
#if(append_version_to_install_prefix):
#    ilcsoft_install_dir = os.path.join(ilcsoft_install_prefix , ilcsoft_release )

# ----------------------------------------------------------------------------


# --------- ilcsoft home -----------------------------------------------------
# ===========================================================
# Modify this path to where you want ilcinstall to look
# for pre-installed (base) packages
# typically this would be left to ilcsoft_install_prefix
# or set to an /afs or /cvmfs base installation that you
# want to use
# ===========================================================

ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------


#--------------------------------------------------------------------------
#ilcPatchPath = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5/v01-15"



# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# detect the default software installation path
# when using package manager like apt-get, yum or brew
platfDefault = None

if platform.system().lower().find('linux') >= 0:
   platfDefault = '/usr'
elif platform.system().lower().find('darwin') >= 0:
   platfDefault = '/usr/local'

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = platfDefault

# overwrite with a patch set in the environment
my_mysql_path = os.getenv("MYSQL_DIR", default=None)
if( my_mysql_path !=  None ):
    MySQL_path = my_mysql_path


#MySQL_path = ilcPath + "/mysql/" + MySQL_version

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################


# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.04.p03"

CLHEP_version =  "2.3.4.3"

ROOT_version = "6.18.04"

GSL_version = "2.6"

Qt5_version = "v5.13.1"

CMake_version = "3.15.5"

FastJet_version = "3.2.1"
FastJetcontrib_version = "1.025"

CED_version = "v01-09-03"

SIO_version = "v00-00-02"

Boost_version = "1.71.0"

Eigen_version = "3.3.7"

# -------------------------------------------

LCIO_version = "v02-13-01"

GEAR_version = "v01-09"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-7"

ILCUTIL_version = "v01-06"

MarlinFastJet_version = "v00-05-02"


# -------------------------------------------

KalTest_version = "v02-05"

KalDet_version = "v01-14-01"

aidaTT_version = "v00-10"

DDKalTest_version = "v01-06"

MarlinTrk_version = "v02-08"

MarlinTrkProcessors_version = "v02-11"

Clupatra_version = "v01-03"

KiTrack_version = "v01-10"

KiTrackMarlin_version = "v01-13"

FCalClusterer_version = "v01-00-01"

ForwardTracking_version = "v01-14"

ConformalTracking_version = "v01-10"

LICH_version = "v00-01"

# -------------------------------------------

GBL_version = "V02-02-00" #"V02-00-00"

LCCD_version = "v01-05"

RAIDA_version = "v01-09"

MarlinUtil_version = "v01-15-01"

Marlin_version = "v01-17"

MarlinDD4hep_version = "v00-06"

MarlinReco_version = "v01-26"

ILDPerformance_version = "v01-07"

#ILDConfig_version = "HEAD"


LCFIVertex_version = "v00-08"
LCFIPlus_version = "v00-09"


MarlinKinfit_version = "v00-06"
MarlinKinfitProcessors_version = "v00-04-01"

PandoraPFANew_version   = "v03-13-02"
DDMarlinPandora_version = "v00-11"
PandoraAnalysis_version = "v02-00-01"

CEDViewer_version = "v01-17"

Overlay_version = "v00-22"

PathFinder_version = "v00-06-01"

MarlinTPC_version = "v01-06"

LCTuple_version = "v01-12"

BBQ_version = "v00-01-04"

Druid_version = "2.2"

Garlic_version = "v03-01"

DD4hep_version = "v01-11"
DD4hepExamples_version = "v01-11"

lcgeo_version = "v00-16-05"

Physsim_version = "v00-04-01"


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XercesC_version = "v3.2.2"
XERCESC_ROOT_DIR = ilcPath + "/xercesc/" + XercesC_version
