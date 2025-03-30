###########################################
#
# iLCSoft versions for installing the v02-03 series of developer releases
# version of the ilcsoft packages.
# The external base tools need to be installed
#
# DESY ilcsoft team
###########################################

# --------- ilcsoft release version ------------------------------------------
ilcsoft_release = "v02-03-04"
# ----------------------------------------------------------------------------

# which cxx standard to use
cxx_standard = 20

# ===============================================================================
# use a compiler that knows c++20, use e.g. scripts/use_gcc103_cvmfs_centos7.sh
#
"""
# --- gcc from LCG_106
source /cvmfs/sft.cern.ch/lcg/releases/gcc/13.1.0-b3d18/x86_64-el9/setup.sh

# --- python from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/lib/python3.11/site-packages

# --- git from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/bin:${PATH}
export GIT_EXEC_PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/libexec/git-core
"""
# before starting the installation
# ================================================================================


# --------- install dir ------------------------------------------------------
# ===========================================================
# Modify this path to where you want to install the software
# ===========================================================
#

if installPrefix is None:
    ilcsoft_install_prefix = ilcsoft_afs_path[arch]
else:
    ilcsoft_install_prefix = installPrefix

# ----------------------------------------------------------------------------
# --- the ilcsoft_release is now automatically appended in release-ilcsoft.cfg
#     but not in release-base.cfg !!

# append_version_to_install_prefix = False
# if(append_version_to_install_prefix):
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


# --------------------------------------------------------------------------
# ilcPatchPath = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5/v01-15"


# ======================= PACKAGES WITH NO INSTALL SUPPORT ===================

# these packages need to be pre-installed for your system
# please adjust the path variables accordingly

# detect the default software installation path
# when using package manager like apt-get, yum or brew
platfDefault = None

if platform.system().lower().find("linux") >= 0:
    platfDefault = "/usr"
elif platform.system().lower().find("darwin") >= 0:
    platfDefault = "/usr/local"

# ----- mysql --------------------------------------------------------
MySQL_version = "10.5.20"
MySQL_path = platfDefault

# overwrite with a patch set in the environment
my_mysql_path = os.getenv("MYSQL_DIR", default=None)
if my_mysql_path != None:
    MySQL_path = my_mysql_path

# ----------------------------------------------------------------------------

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################


# ======================= PACKAGE VERSIONS ===================================

Geant4_version = "11.3.1"

CLHEP_version = "2.4.7.1"

ROOT_version = "6.32.10"

GSL_version = "2.7"

Qt5_version = "v5.15.15-lts-lgpl"

CMake_version = "3.31.6"

CED_version = "v01-10"

SIO_version = "v00-02"

Boost_version = "1.87.0"

Eigen_version = "3.4.0"

# -------------------------------------------

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-7"

ILCUTIL_version = "v01-07-03"

FastJet_version = "3.4.3"

FastJetcontrib_version = "1.056"

# xerces-c (needed by geant4 for building gdml support - required by mokka)
XercesC_version = "v3.2.3"
XERCESC_ROOT_DIR = ilcPath + "/xercesc/" + XercesC_version

# -------------------------------------------

LCIO_version = "v02-22-04"

GEAR_version = "v01-09-04"

MarlinFastJet_version = "v00-05-03"

KalTest_version = "v02-05-02"

KalDet_version = "v01-14-01"

aidaTT_version = "v00-10"

DDKalTest_version = "v01-07-01"

MarlinTrk_version = "v02-09-02"

MarlinTrkProcessors_version = "v02-12-06"

Clupatra_version = "v01-03-01"

KiTrack_version = "v01-10-01"

KiTrackMarlin_version = "v01-13-02"

ForwardTracking_version = "v01-14-02"

ConformalTracking_version = "v01-12"

LICH_version = "v00-01"

GBL_version = "V02-02-01"

LCCD_version = "v01-05-03"

RAIDA_version = "v01-11"

MarlinUtil_version = "v01-18-01"

Marlin_version = "v01-19-04"

MarlinDD4hep_version = "v00-06-02"

DDMarlinPandora_version = "v00-12-02"

MarlinReco_version = "v01-36-01"

FCalClusterer_version = "v01-00-06"

ILDPerformance_version = "v01-12"

# ILDConfig_version = "v02-03"

LCFIVertex_version = "v00-09"

LCFIPlus_version = "v00-10-01"

MarlinKinfit_version = "v00-06-01"

MarlinKinfitProcessors_version = "v00-05"

PandoraPFANew_version = "v04-12"

PandoraAnalysis_version = "v02-00-01"

CEDViewer_version = "v01-20"

Overlay_version = "v00-23"

PathFinder_version = "v00-06-01"

MarlinTPC_version = "v01-07"

LCTuple_version = "v01-14"

BBQ_version = "v00-01-04"

# Druid_version = "HEAD" # "2.2" # "1.8"

Garlic_version = "v03-01"

DD4hep_version = "v01-31"

DD4hepExamples_version = "v01-30"

lcgeo_version = "v00-21"

podio_version = "v01-01"

edm4hep_version = "v00-99-01"

k4edm4hep2lcioconv_version = "v00-09"

Physsim_version = "v00-05"
