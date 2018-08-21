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
ilcsoft_release='v02-00-02-pre02'
# ----------------------------------------------------------------------------

#-----------------------
# we now always build with c++11 ?
use_cpp11 = True 
if nightlies:
   use_cpp11 = nb_use_cpp11
   print "******************* use_cpp11", use_cpp11


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

ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
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

# ----- mysql --------------------------------------------------------
MySQL_version = "5.0.45"
MySQL_path = ilcPath + "/mysql/" + MySQL_version

if( ilcsoft_afs_path[ arch ].find('_ub') > 0 ):
    MySQL_path = "/usr"


#------ boost headers files ------------------------------------------
Boost_path = ilcPath+"/../boost/1.58.0"

#------ Eigen headers files ------------------------------------------
Eigen_path =  ilcPath+"/../Eigen/3.2.9"


##########################################################################################
#
#  end of user configuration section
#  only make changes below if you know what you are doing ...
#
##########################################################################################


# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.03.p02" 
CLHEP_version =  "2.3.4.3"

ROOT_version = "6.08.06"

GSL_version = "2.1" 

QT_version = "4.7.4"

CMake_version = "3.6.3" 

FastJet_version = "3.2.1"
FastJetcontrib_version = "1.025"

CED_version = "v01-09-02"
# -------------------------------------------

LCIO_version = "v02-12-01"

GEAR_version = "v01-08"

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-05"

MarlinFastJet_version = "v00-05-01" 


# -------------------------------------------

KalTest_version = "v02-05"

KalDet_version = "v01-14-01"

aidaTT_version = "v00-09"

DDKalTest_version = "v01-05"

MarlinTrk_version = "v02-07"

MarlinTrkProcessors_version = "v02-10"

Clupatra_version = "v01-03"

KiTrack_version = "v01-09"

KiTrackMarlin_version = "v01-12"

FCalClusterer_version = "v01-00"

ForwardTracking_version = "v01-13"

ConformalTracking_version = "v01-07"

LICH_version = "v00-01" 

# -------------------------------------------

GBL_version = "V02-01-01" #"V02-00-00" 

LCCD_version = "v01-05"

RAIDA_version = "v01-09"

MarlinUtil_version = "v01-15" 

Marlin_version = "v01-16"

MarlinDD4hep_version = "v00-06"

MarlinReco_version = "v01-25"

ILDPerformance_version = "v01-06"

#ILDConfig_version = "HEAD" 


LCFIVertex_version = "v00-07-04"
LCFIPlus_version = "v00-06-08"


MarlinKinfit_version = "v00-06"
MarlinKinfitProcessors_version = "v00-04"

PandoraPFANew_version   = "v03-09-00"
DDMarlinPandora_version = "v00-10"
PandoraAnalysis_version = "v02-00-00"

CEDViewer_version = "v01-16"

Overlay_version = "v00-21"

PathFinder_version = "v00-06-01"

MarlinTPC_version = "v01-04"

LCTuple_version = "v01-11"

BBQ_version = "v00-01-03"

Druid_version = "2.2"

Garlic_version = "v03-01"

DD4hep_version = "v01-07-02"
DD4hepExamples_version = "v01-07-02"

lcgeo_version = "v00-16-03"

Physsim_version = "v00-04-01"


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.4"

XercesC_version = "3.1.4" 

