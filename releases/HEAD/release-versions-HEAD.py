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
# we now always build with c++11 ?
use_cpp11 = True 
if nightlies:
   use_cpp11 = nb_use_cpp11
   print "******************* use_cpp11", use_cpp11

afsPath = None
try:
    afsPath = ilcsoft_afs_path[ arch ]
except KeyError:
    pass

#===============================================================================
# use a compiler that knows c++11, run 
#
'''
 source /afs/cern.ch/sw/lcg/contrib/gcc/4.9.3/x86_64-slc6/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/bin:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/lib:$LD_LIBRARY_PATH

# or on cvmfs:

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

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version

if( platf.lower().find('linux') >= 0 ):
    MySQL_path = "/usr"

# ----------------------------------------------------------------------------

##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################



# ======================= PACKAGE VERSIONS ===================================

#Geant4_version =  "10.02.p02" 
#CLHEP_version =  "2.3.1.1"

Geant4_version =  "10.05.p01" 
CLHEP_version =  "2.3.4.3"

ROOT_version = "6.18.02"

GSL_version = "2.1" 

QT_version = "4.7.4"

CMake_version = "3.6.3"

CED_version = "v01-09-02"

SIO_version = "v00-00-02"

Boost_version = "1.65.0"

Eigen_version = "3.3.7"

# -------------------------------------------

LCIO_version = "HEAD"

GEAR_version = "HEAD"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-05"

FastJet_version = "3.2.1"
FastJetcontrib_version = "1.025"

MarlinFastJet_version = "HEAD"


# -------------------------------------------

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

# -------------------------------------------

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


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.4"

XercesC_version = "3.1.4" 




