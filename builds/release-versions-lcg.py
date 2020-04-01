#!/usr/bin/env python
###########################################
#
# iLCSoft versions for installing a current HEAD 
# version of the ilcsoft packages.
#
###########################################
import datetime

# --------- ilcsoft release version ------------------------------------------
today = datetime.date.today()

release_date=today.strftime('%Y-%m-%d')

use_cpp11 = False

build_directory = os.getenv("BUILD_PATH", release_date)
build_arch = os.getenv("BUILD_ARCH", "x86_64-centos7-gcc8-opt")
lcg_release = os.getenv("LCG_RELEASE", "97")

ilcsoft_install_prefix = '/cvmfs/clicdp.cern.ch/iLCSoft/lcg/'+ lcg_release + '/' + build_directory + '/' + build_arch + '/'


ilcPath = ilcsoft_install_prefix

Boost_path = "/cvmfs/clicdp.cern.ch/software/LCG/" + lcg_release + '/' + build_arch + '/'


# ======================= PACKAGE VERSIONS ===================================

Geant4_version =  "10.03.p03" # "10.02.p01" # "10.01"

ROOT_version = "6.12.06"

CLHEP_version =  "2.3.4.3" # "2.3.1.1" #  "2.1.4.1"

GSL_version = "2.4" # "1.14"

QT_version = "4.7.4"

CMake_version = "3.14.3" # "2.8.5"

CED_version = "HEAD"

# -------------------------------------------

LCIO_version = "HEAD" # "v02-06"

GEAR_version = "HEAD" # "v01-04-02" 

CondDBMySQL_version = "HEAD"

ILCUTIL_version = "HEAD" 

FastJet_version = "HEAD"

MarlinFastJet_version = "HEAD" # "v00-02"


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

# -------------------------------------------

GBL_version = "HEAD" # "V01-16-04"

LCCD_version = "HEAD" # "v01-03"

RAIDA_version = "HEAD" # "v01-06-02"

MarlinUtil_version = "HEAD" # "v01-10"

Marlin_version = "HEAD" # "v01-07"

MarlinDD4hep_version = "HEAD" # "v00-01"

DDMarlinPandora_version = "HEAD" # "v00-01"

Mokka_version = "HEAD" # "mokka-08-05" 

MarlinReco_version = "HEAD" # "v01-13"

FCalClusterer_version = "HEAD" # "v00-01"

ILDPerformance_version = "HEAD" # "v00-01"
ClicPerformance_version = "HEAD" # "v00-01"

ILDConfig_version = "HEAD" 


LCFIVertex_version = "HEAD" # "v00-07"
LCFIPlus_version = "HEAD" # "v00-05-03"


MarlinKinfit_version = "HEAD" # "v00-01-05"

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

ConformalTracking_version = "HEAD"

LICH_version = "HEAD"

