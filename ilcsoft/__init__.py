# python looks in sys.path when importing modules
# sys.path[0] is the directory containing the script that was used to invoke the Python interpreter (where ilcsoft-install lives)
import sys
sys.path.append( sys.path[0] + '/ilcsoft' )
#sys.path.append( sys.path[0] + '/ilcsoft/simtools' )
#print 'DEBUG: sys.path: ' + str(sys.path)

from ilcsoft import ILCSoft

# core software
from ilcutil import ILCUTIL
from lcio import LCIO
from lccd import LCCD
from gear import GEAR
from raida import RAIDA
from ced import CED
from kaltest import KalTest, KalDet
from pathfinder import PathFinder
from bbq import BBQ
from gbl import GBL

# marlin & friends
from marlinpkg import MarlinPKG
from marlinpkg import ConfigPKG
from marlin import Marlin
from marlinutil import MarlinUtil
from marlinreco import MarlinReco
from cedviewer import CEDViewer
from pandoranew import PandoraPFANew
from pandoranew import PandoraAnalysis
from pandoranew import MarlinPandora
from lcfivertex import LCFIVertex
from eutelescope import Eutelescope
from overlay import Overlay
from marlintpc import MarlinTPC
from ckfit import CKFit
from fastjet import FastJet, FastJetClustering
from marlintrk import MarlinTrk
from kitrack import KiTrack, KiTrackMarlin

#slic et al
from gdml import GDML
from ddsegmentation import DDSegmentation # standalone DDSegmentation install
from lcdd import LCDD
from slic import SLIC
from slicpandora import SlicPandora

#aida
from dd4hep import DD4hep 
from ddsim import DDSim 

# simtools
#from simtoolsmaker import SimToolsMaker
from simtools import *  # modules defined in simtools/__init__.py

# cmake
from cmake import CMake

# external (with install support)
from druid import Druid
from garlic import Garlic
from mokka import Mokka
from conddbmysql import CondDBMySQL
from cernlib import CERNLIB
from clhep import CLHEP
from heppdt import HepPDT
from gsl import GSL
from xercesc import XercesC
from heppdt import HepPDT
from qt import QT
from dcap import dcap



# external (without install support)
from root import ROOT
from geant4 import Geant4
from java import Java
from mysql import MySQL
