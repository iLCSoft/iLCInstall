###########################################
#
# iLCSoft versions for installing a current HEAD
# version of the ilcsoft packages.
# The external base tools need to be installed
#
# DESY ilcsoft team
###########################################
import datetime

# --------- ilcsoft release version ------------------------------------------
today = str( datetime.date.today() )
ilcsoft_release='HEAD-'+today

# ----------------------------------------------------------------------------

#-----------------------

# which cxx standard to use
cxx_standard = 17

afsPath = None
try:
    afsPath = ilcsoft_afs_path[ arch ]
except KeyError:
    pass

#===============================================================================
# use a compiler that knows c++17, run
#
'''
# --- gcc from LCG_99
source /cvmfs/sft.cern.ch/lcg/releases/gcc/10.1.0-6f386/x86_64-centos7/setup.sh

# --- python from LCG_99
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.8.6-3199b/x86_64-centos7-gcc10-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.8.6-3199b/x86_64-centos7-gcc10-opt/lib:${LD_LIBRARY_PATH}

# --- git from LCG_99
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-e475b/x86_64-centos7-gcc10-opt/bin:${PATH}

# --- use a suitable mysql (also LCG_99)
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/10.4.12-8f05c/x86_64-centos7-gcc10-opt
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
#ilcsoft_install_prefix = "/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6/"
#ilcsoft_install_prefix = "/nfs/dust/ilc/user/voutsina/testarea/ilcsoft_c11/"
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

#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc48_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5'


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
MySQL_version = "10.4.12"
MySQL_path = platfDefault

# overwrite with a patch set in the environment
my_mysql_path = os.getenv("MYSQL_DIR", default=None)
if( my_mysql_path !=  None ):
    MySQL_path = my_mysql_path

# ----------------------------------------------------------------------------

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################



# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.07.p01"

CLHEP_version =  "2.4.4.1"

ROOT_version = "6.22.08" # Don't be afraid to go on an adventure with the latest root

GSL_version = "2.6"

Qt5_version = "v5.13.1"

CMake_version = "3.18.4"

CED_version = "v01-09-03"

SIO_version = "v00-01"

Boost_version = "1.75.0"

Eigen_version = "3.3.9"

# -------------------------------------------

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-7"

ILCUTIL_version = "v01-06-01"

FastJet_version = "3.3.4"

FastJetcontrib_version = "1.045"

# xerces-c (needed by geant4 for building gdml support - required by mokka)
XercesC_version = "v3.2.2"

XERCESC_ROOT_DIR = ilcPath + "/xercesc/" + XercesC_version

# -------------------------------------------

LCIO_version = "HEAD"

GEAR_version = "HEAD"

MarlinFastJet_version = "HEAD"

KalTest_version = "HEAD" # "v02-00"

KalDet_version = "HEAD" # "v01-13-02"

aidaTT_version = "HEAD" # "v00-02"

DDKalTest_version = "HEAD" # "v00-02"

MarlinTrk_version = "HEAD" # "v02-00-01"

MarlinTrkProcessors_version = "HEAD" # "v02-01"

Clupatra_version = "HEAD" # "v00-12"

KiTrack_version = "HEAD" # "v01-06"

KiTrackMarlin_version = "HEAD" # "v01-07"

ForwardTracking_version = "HEAD" # "v01-08"

ConformalTracking_version = "HEAD" # "v01-08"

LICH_version = "HEAD" # "v01-08"

GBL_version = "HEAD" # "V01-16-04"

LCCD_version = "HEAD" # "v01-03"

RAIDA_version = "HEAD" # "v01-06-02"

MarlinUtil_version = "HEAD" # "v01-10"

Marlin_version = "HEAD" # "v01-07"

MarlinDD4hep_version = "HEAD" # "v00-01"

DDMarlinPandora_version = "HEAD" # "v00-01"

MarlinReco_version = "HEAD" # "v01-13"

FCalClusterer_version = "HEAD" # "v00-01"

ILDPerformance_version = "HEAD" # "v00-01"

ILDConfig_version = "HEAD"

LCFIVertex_version = "HEAD" # "v00-07"

LCFIPlus_version = "HEAD" # "v00-05-03"

MarlinKinfit_version = "HEAD" # "v00-01-05"

MarlinKinfitProcessors_version = "HEAD" # "v00-01-05"

PandoraPFANew_version = "HEAD" # "v02-00-00"

MarlinPandora_version = "HEAD" # "v02-00-00"

PandoraAnalysis_version = "HEAD" # "v01-00-01"

CEDViewer_version = "HEAD" # "v01-10"

Overlay_version = "HEAD" # "v00-20"

PathFinder_version = "HEAD" #  "v00-06"

MarlinTPC_version = "HEAD" # "v01-00"

LCTuple_version = "HEAD" # "v01-04"

BBQ_version = "HEAD" #  "v00-01-02"

Druid_version = "HEAD" # "2.2" # "1.8"

Garlic_version = "HEAD" # "v3.0.3"

DD4hep_version = "HEAD" # "v00-14"

DD4hepExamples_version = "HEAD" # "v00-14"

lcgeo_version = "HEAD" # "v00-05"

Physsim_version = "HEAD" # "v00-02"
