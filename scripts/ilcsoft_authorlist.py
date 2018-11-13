import os

'''
script for extracting ilcsoft authors from all packages

usage:

 - edit ilcsoft path and version first

   python ./ilcsoft_authorlist.py | sort -k 2 > author_list_sorted.txt


 then run remove_duplicate_authors.py on the outputfile (after removing special characters )
 

'''

##########################################

ilcsoft = "/data/ilcsoft/HEAD"
version = "HEAD"

##########################################

## non git packages:
#"DD4hepExamples",
#"GBL",
#"MarlinTPC",

allPackages = [
    "lcio",
    "gear",
    "lccd",
    "DD4hep",
    "Marlin",
    "RAIDA",
    "lcgeo",
    "MarlinUtil",
    "aidaTT",
    "KiTrack",
    "KiTrackMarlin",
    "KalTest",
    "DDKalTest",
    "MarlinTrk",
    "CEDViewer",
    "Clupatra",
    "ConformalTracking",
    "DDMarlinPandora",
    "FastJetClustering",
    "FCalClusterer",
    "ForwardTracking",
    "Garlic",
    "ILDPerformance",
    "LCFIVertex",
    "LCFIPlus",
    "LCTuple",
    "LICH",
    "MarlinDD4hep",
    "MarlinFastJet",
    "MarlinReco",
    "MarlinTrkProcessors",
    "Overlay",
    "PandoraAnalysis",
    "PandoraPFANew",
    "MarlinKinfit",
    "MarlinKinfitProcessors",
]

packages = allPackages

##########################################

def showauthors( package, version ):
    """ update ilcsoft package ..."""
    
    path = ilcsoft + "/" + package + "/" + version

    cmd = "cd " + path +"\n"

    cmd += "git shortlog -e -s -n \n"

#    print " ================== " , path

    return cmd


##########################################

for pck in packages:

    cmd = showauthors( pck, version )
    os.system( cmd ) 

    

