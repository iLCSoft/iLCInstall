#!/bin/env python
"""
#################################################################
#  creates ilcsoft_release notes from all packages in
#  the input file, which is in the format used for the ilcsofttagger.py
#  usage:
#  create_ilcsoft_relnotes.py path_to_ilcsoft_release ./tagging_vyy-xx.py doc/release_notes_ilcsoft_vyy-xx.txt
#
#  F. Gaede, DESY
#
#################################################################
"""

import sys
import os.path


if len( sys.argv ) != 5:
    print "usage: \n create_ilcsoft_relnotes.py path_to_ilcsoft_release ./tagging_vyy-xx.py doc/release_notes_ilcsoft_vyy-xx.txt ilcsoftVersion"
    exit(1)

path =  sys.argv[1]
tagf  = open( sys.argv[2] , 'r' )
outf = open( sys.argv[3] , 'w' )

ilcsoftVers = sys.argv[4]


outf.write("# Release notes for iLCSoft "+ilcsoftVers+"\n\n")
outf.write("Packages changed since last version: \n\n")
outf.write("(*automatically created from individual packages' release notes - might by empty if no changes or not documented*))\n\n")

# read the file that was used for tagging the package versions 
# format:    GitHubUser/Package/Version
for line in tagf:
    
    # remove empty and commented out lines
    s = line.strip()
    if len(s)<1 or s[0]=='#':
        continue
    
    # remove the GitHub project (user)
    p = s[ s.find("/"):len(s)]
    #print p

    package = p[p.find("/")+1:len(p)]
    version = package[package.find("/")+1:len(package)]
    package = package[0:package.find("/")]

    print " gathering release notes for : " , package , version
    
    fname = path + p + '/doc/ReleaseNotes.md'
    #print fname

    if not os.path.isfile(fname):
        print " ERROR: file not found :", fname
        continue

    inf = open( fname , 'r' )

    outf.write("## "+package+" - "+version+"\n\n")
    
    for l in inf:
        if l.find('# v')>-1 or l.find('#  v')>-1:
            if l.find('# '+version)<0:
                break
        else:
            outf.write( l ) 
    

    inf.close()



#d = {}
#d['| v'] = '# v'
#d[' |'] = ''
#
#
#for line in inf:
#
#    s = line.strip()
#    n = s.count('-')
#    if n>1 and n == len(s):
#        continue
#
#    for k in d.keys():
#        line = line.replace( k , d[k] )
#
#
#    outf.write(line)
#
#
#inf.close()
#outf.close()

tagf.close()
