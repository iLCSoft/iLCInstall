"""
module to parse version strings in ilcsoft
"""

from logging import getLogger

class Version( object ):
  """
  e.g.

  v01-00
  v01-00-pre
  v01-00-pre1
  v01-01-01-pre8

  """

  def __init__( self, versionString, makePreRelease=True ):
    self.version = versionString
    self.major = 0
    self.minor = 0
    self.patch = None
    self.pre = None
    self.isPre = False
    self.makePreRelease=makePreRelease
    self.log = getLogger( "Version" )

    try:
      self._parseVersion()
    except ValueError as err:
      self.log.error("Failed to parse version: %s", str(err) )
      raise RuntimeError( "broken version string" )

  def _parseVersion( self ):
    """ parse the version string """
    ## strip starting parts, e.g. CondBMYSQL_ILC-
    self.version = self.version.lstrip('vABCDEFGHIJKLMNOPQRSTUVWXZYabcdefghijklmnopqrstuvwxzy_-')
    parts = self.version.lstrip('v').split("-")
    if 'pre' in self.version:
      self.isPre = True

    if len(parts) >= 2:
      self.major = int(parts[0])
      self.minor = int(parts[1])
    else:
      raise RuntimeError( "Cannot parse this version string: %s" % self.version )

    if len(parts) >= 3:
      if 'pre' == parts[2]:
        self.pre = 0
      elif 'pre' in parts[2]:
        self.pre = int(parts[2].strip('pre'))
      else:
        self.patch = int( parts[2] )

    if len(parts) >= 4:
      if 'pre' == parts[3]:
        self.pre = 0
      elif 'pre' in parts[3]:
        self.pre = int(parts[3].strip('pre'))
      else:
        raise RuntimeError( "Cannot parse this version string: %s" % self.version )


  def __incrementPatch( self ):
    """ return version with patch version incremented """
    if self.patch is None:
      self.patch = 1
    else:
      self.patch += 1
    return str(self)

  def __incrementPreRelease( self ):
    """ return version with prerelease version incremented """
    if self.pre is None:
      self.pre = 0
    else:
      self.pre += 1
    return str(self)

  def increment( self ):
    """ return the version string incremented by patch or pre-release
    if version was pre-release we increment the pre-release if we want to have a pre-release
    if the version was a pre-release, but we do not want a pre-release we drop the pre, but keep the patch.
    if the version was no pre-release, but we want a pre-release we make it a pre-release and increase the patch
    if the version was no pre-release, but and we want a proper release, increase the patch
    """
    if self.isPre and self.makePreRelease:
      self.__incrementPreRelease()
      self.log.info( "Making new PreRelease: %s", self )
      return
    elif self.isPre and not self.makePreRelease:
      self.isPre = False
      self.log.info( "Making new Release: %s", self )
      return
    elif not self.isPre and self.makePreRelease:
      self.isPre = True
      self.__incrementPatch()
      self.__incrementPreRelease()
      self.log.info( "Making new PreRelease: %s", self )
      return
    else: ## no prelrease, proper release
      self.__incrementPatch()
      self.log.debug( "Making new Release: %s", self )
      return

  def __str__( self ):
    """ return version string """
    versionString = "v%02d-%02d" % ( self.major, self.minor )
    if self.patch is not None:
      versionString += "-%02d" % self.patch

    if self.makePreRelease:
      versionString += "-pre"
      if self.pre > 0:
        versionString += "%d" % self.pre

    return versionString

  def getMajorMinorPatch( self ):
    """ :returns: tuple of Major, Minor, Patch """
    patch = 0 if self.patch is None else self.patch
    return self.major, self.minor, patch
