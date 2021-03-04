#!/bin/env python
"""

Tagging System for iLCSoft libraries. Make tags, collate release notes via command line or steering file


owner, repository, branch, tag (optional), createReleaseNotes(bool), prerelease(bool)

"""
from __future__ import print_function

from logging import getLogger
import logging
from pprint import pprint

import argparse

__RCSID__ = None

from tagging.gitinterface import Repo
from tagging.helperfunctions import checkRate, MissingFileError

def _parsePrintLevel( level ):
  """ translate printlevel to logging level"""
  return dict( CRITICAL=logging.CRITICAL,
               ERROR=logging.ERROR,
               WARNING=logging.WARNING,
               INFO=logging.INFO,
               DEBUG=logging.DEBUG,
             )[level]

class ILCSoftTagger(object):
  """ object to hold the interface to make tags, read command line options, etc"""

  def __init__( self ):
    self.configFile = None
    self.printLevel = "INFO"
    self.packages = []
    self.repos = []
    self.makeTags = False
    self.properRelease = False
    self.ignoreMissingCmake = False
    self.errors = []
    self.log = getLogger( "Tagger" )
    self.lastTag = None

  def abort( self ):
    """ print error messages and raise exception """
    for line in self.errors:
      self.log.error( "ERROR: %s", line )
    raise RuntimeError( "ERROR" )

  def parseOptions(self):
    """parse the command line options"""
    parser = argparse.ArgumentParser("Makking ILCSoft Tags",
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--file", action="store", default=self.configFile, dest="configFile",
                        help="file holding packages to tag")

    parser.add_argument("-v", "--printLevel", action="store", default=self.printLevel, dest="printLevel",
                        choices=('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
                        help="Verbosity DEBUG, INFO, WARNING, ERROR, CRITICAL")

    parser.add_argument("--packages", action="store", default=self.packages, nargs='+',
                        help="packages to check: [owner/]package[/version[/branch]]")

    parser.add_argument("--makeTags", action="store_true", dest="makeTags", default=self.makeTags,
                        help="Create the tags, commit release notes")

    parser.add_argument("--properRelease", action="store_true", dest="properRelease", default=self.properRelease,
                        help="if set make proper release, if not set make pre release only")

    parser.add_argument("--checkRate", action="store_true", dest="checkRate", default=False,
                        help="Print out remaining number of queries for this hour")

    parser.add_argument("--lastTag", action="store", dest="lastTag", default=None,
                        help="consider this version to be the last version and take all PRs following this tag. Only works with a single package")

    parser.add_argument("--ignoreMissingCmake", action="store_true", dest="ignoreMissingCmake", default=False,
                        help="Ignore the error associated with a missing CMakeLists.txt file containing the version to update")

    parsed = parser.parse_args()

    self.configFile = parsed.configFile
    self.printLevel = _parsePrintLevel( parsed.printLevel )
    logging.basicConfig( level=self.printLevel, format='%(levelname)-5s - %(name)-8s: %(message)s' )

    self.packages = parsed.packages
    self.makeTags = parsed.makeTags
    self.properRelease = parsed.properRelease
    self.lastTag = parsed.lastTag
    self._parseConfigFile()
    self.ignoreMissingCmake = parsed.ignoreMissingCmake
    if parsed.checkRate:
      checkRate()

    if self.lastTag is not None and len(self.packages) > 1:
      self.errors.insert( "lastTag is set but there is more than 1 (one) package")

    if self.errors:
      self.abort()

  def _printVersionsFile( self ):
    """ print the versions.cfg file to be used in ilcsoft-install config files"""
    self.log.info( "New version configuration:")
    versionsContent = ""
    for package in self.repos:
      versionsContent += '\n%s_version = "%s" ' % ( package.repo, package.newTag )

    print("*"*80)
    print(versionsContent)
    print("*"*80)


  def _parseConfigFile( self ):
    """ parses the config file and files packages list"""
    if self.configFile is None:
      return


    with open(self.configFile) as conf:
      for line in conf.readlines():
        if not line.strip():
          continue
        if line.strip()[0]=="#":
          continue
        parts = line.strip().split(" ")
        if len(parts) != 1:
          self.errors.append( "Line '%s' cannot be parsed" % line.strip() )
        else:
          self.packages.append( line.strip() )

    return


  def parsePackage( self, packageString ):
    """ return tuple of owner, repo, branch, version

    default owner: ilcsoft
    default branch: master
    default version: None
    """
    slashCount = packageString.count('/')
    if slashCount == 0:
      owner = "iLCSoft"
      package = packageString
      version=None
      branch='master'
    elif slashCount == 1:
      owner = packageString.split('/')[0]
      package = packageString.split('/')[1]
      version=None
      branch='master'
    elif slashCount == 2:
      owner = packageString.split('/')[0]
      package = packageString.split('/')[1]
      version = packageString.split('/')[2]
      branch='master'
    elif slashCount == 3:
      owner = packageString.split('/')[0]
      package = packageString.split('/')[1]
      version = packageString.split('/')[2]
      branch = packageString.split('/')[3]

    self.log.debug( "Added package: %s %s %s %s", owner, package, branch, version )
    return owner, package, branch, version

  def _printReleaseNotes( self ):
    """ print release notes for all packages """
    for thisPackage in self.repos:
      if thisPackage.isUpToDate():
        continue
      separateString = "*"*80
      if self.makeTags:
        self.log.info( "Create new release for %s: %s", thisPackage.repo, thisPackage.newTag )
      else:
        self.log.info( "Dry Run for new %s release: %s", thisPackage.repo, thisPackage.newTag )
      self.log.info( "Release notes for %s:\n%s\n%s\n%s",
                     thisPackage,
                     separateString,
                     thisPackage.formatReleaseNotes(),
                     separateString, )


  def _commitAndTag( self ):
    """ commit release notes and updated versions settings and make release """
    for package in self.repos:
      if package.isUpToDate():
        self.log.info( "Package %s has no updates since last tag", package )
        continue
      self.log.info( "Committing release notes for: %s", package )
      package.commitNewReleaseNotes()
      self.log.info( "Updating version: %s to %s", package, package.newVersion )
      try:
        package.updateVersionSettings()
      except MissingFileError:
        if self.ignoreMissingCmake:
          self.log.info('Ignoring missing file to update version')
        else:
          self.log.error('Failed to update Version in CMakeLists! Ignore this error with `--ignoreMissingCmake`')
          raise
      package.createGithubRelease()


  def run( self ):
    """ execute everything """
    for package in self.packages:
      self.log.info( "Checking package: %s", package )
      owner, package, branch, version = self.parsePackage( package )
      prerelease = not self.properRelease
      try:
        dryRun = not self.makeTags
        thisPackage = Repo( owner, package, branch=branch, newVersion=version, preRelease=prerelease, dryRun=dryRun, lastTag=self.lastTag)
        self.repos.append( thisPackage )
      except RuntimeError as e:
        self.log.error( "Failure for %s/%s/%s/%s", owner, package, branch, version )
        self.errors.append( str(e) )

    if self.errors:
      self.abort()
      
    self._printReleaseNotes()
    self._commitAndTag()

    
    self._printVersionsFile()
    checkRate()


if __name__ == "__main__":
  #logging.basicConfig( level=logging.INFO)
  RUNNER = ILCSoftTagger()
  try:
    RUNNER.parseOptions()
  except RuntimeError as e:
    print ("Error during runtime: %s", e)
    exit(1)

  try:
    RUNNER.run()
  except RuntimeError as e:
    logging.error("Error during runtime: %s", e)
    exit(1)


### Get list of tags, get latest tag, get all PRs merged after this date, get
### comments for this PR, parse comments for "Relase Notes" and collate them
### into release notes for the pacakge, add commit with release notes, add
### commit with new version, ignore pre-release tags for collating release notes
