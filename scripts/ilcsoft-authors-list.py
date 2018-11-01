#!/usr/bin/env python


from logging import getLogger
import logging
from pprint import pprint

import argparse

import json
from logging import getLogger
from collections import OrderedDict, defaultdict
import re

from pprint import pprint
from operator import itemgetter

from tagging.helperfunctions import parseForReleaseNotes, curl2Json, authorMapping, versionComp

from tagging.parseversion import Version
from tagging.helperfunctions import checkRate



def _parsePrintLevel( level ):
    """ translate printlevel to logging level"""
    return dict( CRITICAL=logging.CRITICAL,
	     ERROR=logging.ERROR,
	     WARNING=logging.WARNING,
	     INFO=logging.INFO,
	     DEBUG=logging.DEBUG,
	   )[level]


def _github( owner, repo, action ):
    """ return the url to perform actions on github
    :param str action: command to use in the gitlab API, see documentation there
    :returns: url to be used by curl
    """
    options = dict(owner=owner, repo=repo, action=action)
    ghURL = "https://api.github.com/repos/%(owner)s/%(repo)s/%(action)s" % options
    return ghURL

repositories=["ilcsoft/marlin",
	      "ilcsoft/lcio",
	      "ilcsoft/conformaltracking",
	      "ilcsoft/lccalibration",
	      "aidasoft/aidatt",
	      "ilcsoft/ced",
	      "ilcsoft/cedviewer",
	      "ilcsoft/clupatra",
	      "ilcsoft/CondDBMySQL",
	      "ilcsoft/ConformalTracking",
	      "aidasoft/DD4hep",
	      "ilcsoft/DDKalTest",
	      "ilcsoft/DDMarlinPandora",
	      "ilcsoft/ForwardTracking",
	      "ilcsoft/Garlic",
	      "ilcsoft/gear",
	      "ilcsoft/ilcutil",
	      "ilcsoft/ILDPerformance",
	      "ilcsoft/KalDet",
	      "ilcsoft/KalTest",
	      "ilcsoft/KiTrack",
	      "ilcsoft/KiTrackMarlin",
	      "ilcsoft/lccd",
	      "ilcsoft/lcgeo",
	      "ilcsoft/LCTuple",
	      "ilcsoft/MarlinDD4hep",
	      "ilcsoft/MarlinKinfit",
	      "ilcsoft/MarlinKinfitProcessors",
	      "ilcsoft/MarlinReco",
	      "ilcsoft/MarlinTrk",
	      "ilcsoft/MarlinTrkProcessors",
	      "ilcsoft/MarlinUtil",
	      "ilcsoft/Overlay",
	      "ilcsoft/Physsim",
	      "ilcsoft/RAIDA",
	      "FCALSW/FCalClusterer",
	      "lcfiplus/lcfiplus",
	      "ilcsoft/lcfivertex",
	      "PandoraPFA/LCPandoraAnalysis",
	      "PandoraPFA/PandoraPFA",
	      "PandoraPFA/LCContent",
	      "PandoraPFA/PandoraSDK",
	      "PandoraPFA/PandoraMonitoring"]

usersMask = ["PandoraPFA", "lcdprod"]

if __name__ == "__main__":
   parser = argparse.ArgumentParser("Get iLCSoft contributors",
				    formatter_class=argparse.RawTextHelpFormatter)

   parser.add_argument("--output-file", action="store", dest="outputFile", default=None,
		       help="Output file where to store the contributor name (default: no file, print in terminal)")

   parser.add_argument("-v", "--printLevel", action="store", default='INFO', dest="printLevel",
		       choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
		       help="Verbosity DEBUG, INFO, WARNING, ERROR, CRITICAL")

   parsed = parser.parse_args()

   logging.basicConfig( level=_parsePrintLevel( parsed.printLevel ), format='%(levelname)-5s - %(name)-8s: %(message)s' )

   usermap = {}
   
   for repository in repositories:
       owner = repository.split("/")[0]
       repo = repository.split("/")[1]
       url = _github(owner, repo, "contributors")
       print url
       result = curl2Json(url=url)
       #print result

       for user in result:
           login = str(user["login"])
           if login in usersMask:
               continue
           usermap[login] = ""

   finalUserMap = {}
   for key, val in usermap.iteritems():
       result = curl2Json(url="https://api.github.com/users/" + key)
       fullName = result["name"]
       print "Getting user full name for login '{0}".format(key)
       if fullName:
           finalUserMap[key] = fullName.encode('utf-8').strip()


   if parsed.outputFile:
       with open(parsed.outputFile, 'w') as output:
           output.write(str(finalUserMap))
   else:
       print finalUserMap
       

