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
ilcsoft_release='v01-19-01-pre01'
# ----------------------------------------------------------------------------

#-----------------------
# we now always build with c++11 ?
use_cpp11 = True 
if nightlies:
   use_cpp11 = nb_use_cpp11
   print "******************* use_cpp11", use_cpp11


#===============================================================================
# NB: c++11 - needs a newer compiler and compatible python, e.g. run
'''
 source /afs/cern.ch/sw/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
 export PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
 export LD_LIBRARY_PATH=/afs/cern.ch/sw/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
# or on cvmfs:
 source /cvmfs/sft.cern.ch/lcg/external/gcc/4.8.1/x86_64-slc6-gcc48-opt/setup.sh
 export PATH=/cvmfs/sft.cern.ch/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/bin/:$PATH
 export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/external/Python/2.7.4/x86_64-slc6-gcc48-opt/lib/:$LD_LIBRARY_PATH
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

Geant4_version =  "10.02.p02" 
CLHEP_version =  "2.3.1.1"

ROOT_version = "6.08.00"

GSL_version = "2.1" 

QT_version = "4.7.4"

CMake_version = "3.4.3"

CED_version = "v01-09-02"
# -------------------------------------------

LCIO_version = "v02-07-04" 

GEAR_version = "v01-06-01" 

CondDBMySQL_version = "CondDBMySQL_ILC-0-9-6"

ILCUTIL_version = "v01-03"  

FastJet_version = "3.2.0"
FastJetcontrib_version = "1.024"

FastJetClustering_version = "v00-03" 

MarlinFastJet_version = "v00-03" 


# -------------------------------------------

KalTest_version = "v02-02" 

KalDet_version = "v01-13-03" 

aidaTT_version = "v00-05" 

DDKalTest_version = "v01-00-01" # "v00-02"

MarlinTrk_version = "v02-02" # "v02-00-01"

MarlinTrkProcessors_version = "v02-04" # "v02-01"

Clupatra_version = "v00-14" # "v00-12"

KiTrack_version = "v01-07" # "v01-06"

KiTrackMarlin_version = "v01-09" # "v01-07"

ForwardTracking_version = "v01-10" # "v01-08"

ConformalTracking_version = "HEAD" # "v01-08"

LICH_version = "HEAD" # "v01-08"

# -------------------------------------------

GBL_version = "V01-17-01" # "V01-16-04"

LCCD_version = "v01-03-01" # "v01-03"

RAIDA_version = "v01-07" # "v01-06-02"

MarlinUtil_version = "v01-12-01" # "v01-10"

Marlin_version = "v01-10" #"v01-09"

MarlinDD4hep_version = "v00-03" # "v00-02"


Mokka_version = "mokka-08-05" # "mokka-08-05" 

MarlinReco_version = "v01-16" # "v01-13"

FCalClusterer_version = "v00-03" # "v00-01"

ILDPerformance_version = "v01-01" # "v00-01"

#ILDConfig_version = "HEAD" 


LCFIVertex_version = "v00-07-02" # "v00-07"
LCFIPlus_version = "v00-06-05" #  # "v00-05-03"


MarlinKinfit_version = "v00-04" # "v00-01-05"
MarlinKinfitProcessors_version = "v00-02" # "v00-01"

PandoraPFANew_version   = "HEAD" # "v03-01-00"
DDMarlinPandora_version = "HEAD" # "v00-05"
PandoraAnalysis_version = "HEAD" # "v01-02-01"

CEDViewer_version = "v01-12" # "v01-10"

Overlay_version = "v00-16" # "v00-14"

PathFinder_version = "v00-06-01" #  "v00-06" # should be changed 

MarlinTPC_version = "v01-02" # "v01-00"

LCTuple_version = "v01-06" # "v01-04"

BBQ_version = "v00-01-03" #  "v00-01-02"

Druid_version = "2.2" # "2.2" # "1.8" 

Garlic_version = "v3.0.4" # "v3.0.3"

DD4hep_version = "v00-19" 
DD4hepExamples_version = "v00-19" 

lcgeo_version = "v00-09-01-pre" 

Physsim_version = "v00-03" # "v00-02" 


# xerces-c (needed by geant4 for building gdml support - required by mokka)
XERCESC_ROOT_DIR = ilcPath + "/xercesc/3.1.2"

XercesC_version = "3.1.2" 

