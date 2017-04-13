"""
interface to github via CURL

"""

import json
from logging import getLogger
from collections import OrderedDict, defaultdict
import re

from pprint import pprint
from operator import itemgetter

from helperfunctions import parseForReleaseNotes, getCommands, curl2Json, \
                            authorMapping, ghHeaders, versionComp
from parseversion import Version

__RCSID__ = None

class Repo(object):
  """ class representing a given repository"""

  def __init__( self, owner, repo, branch='master', newVersion=None, preRelease=True, dryRun=True):
    self.owner = owner
    self.repo = repo
    self.branch = branch
    self._options = dict( owner=self.owner, repo=self.repo  )
    self.log = getLogger( repo )
    self.latestTagInfo = None
    self._releaseNotes = None
    self.releaseNotesFilename = "doc/ReleaseNotes.md"
    self.cmakeBaseFile = "CMakeLists.txt"
    self._lastCommitOnBranch = None
    self._prsSinceLastTag = None
    ## members dealing with difference between the new full version and the next
    ## tag which can be different because of pre-prereleaseness
    self.isPreRelease = preRelease
    self._newVersion = None
    self.newVersion = newVersion
    self._version = None
    self._getLatestTagInfo()
    self._setNewVersion()
    self._dryRun = dryRun

  def __str__( self ):
    return self.owner+"/"+self.repo

  @property
  def newTag( self ):
    """ return next tag version, differs from newversion by pre release """
    return str( self._version )

  @newTag.setter
  def newTag( self, val):
    """ cannot set this property """
    raise NotImplementedError( "not allowed to change newTag, user 'newVersion' instead ")

  @property
  def newVersion( self ):
    """ return new version """
    if self._newVersion is not None:
      return self._newVersion

    self._setNewVersion()
    return self._newVersion

  @newVersion.setter
  def newVersion( self, val ):
    """ set newVersion to value"""
    if val is None:
      self._setNewVersion()
    else:
      self._newVersion = str(val)

  def _setNewVersion( self ):
    """ get the new version based on the previous tag, increment patch version"""
    if self._newVersion is not None:
      self._version = Version(self._newVersion, makePreRelease=self.isPreRelease )
      return str( self._version )
    lastVersion = self._getLatestTagInfo()['name']
    self._version = Version(lastVersion, makePreRelease=self.isPreRelease )
    self._version.increment()
    self._newVersion = str( self._version )
    self.log.info( "Set new version: %s", self._newVersion )

  def _getLatestTagInfo( self ):
    """ fill the information about the latest tag in the repository, ignore pre commit tags"""
    if self.latestTagInfo is not None:
      self.log.debug( "Latest Tag Info already filled" )
      return self.latestTagInfo ## already filled
    tags = self.getGithubTags()
    sortedTags = sorted(tags, key=itemgetter("name"), reverse=True, cmp=versionComp)
    for di in sortedTags:
      self.latestTagInfo = di
      self.latestTagInfo['pre'] = True if 'pre' in di['name'] else False
      self.latestTagInfo['sha'] = di['commit']['sha']
      self.log.info( "Found latest tag %s", di['name'] )
      break

    if not tags:
      self.log.warning( "No tags found for %s", self )
      self.latestTagInfo={}
      self.latestTagInfo['date'] = "1977-01-01T"
      self.latestTagInfo['sha'] = "SHASHASHA"
      self.latestTagInfo['name'] = "00-00"
    else:
      commitInfo = curl2Json( ghHeaders(), self._github( "git/commits/%s" % self.latestTagInfo['sha'] ) )
      self.latestTagInfo['date'] = commitInfo['committer']['date']

    lastCommitInfo = curl2Json( ghHeaders(), self._github( "branches/%s" % self.branch ) )
    self._lastCommitOnBranch =  lastCommitInfo['commit']

    # tags = self.getGithubReleases()
    # for di in sorted(tags, key=itemgetter('created_at') ):
    #   self.latestTagInfo = di
    #   self.latestTagInfo['pre'] = di['prerelease']
    #   self.latestTagInfo['date'] = di['created_at']
    #   self.log.info( "Found latest tag %s", di['name'] )
    #   break

    return self.latestTagInfo


  def _github( self, action ):
    """ return the url to perform actions on github

    :param str action: command to use in the gitlab API, see documentation there
    :returns: url to be used by curl
    """
    options = dict(self._options)
    options["action"] = action
    ghURL = "https://api.github.com/repos/%(owner)s/%(repo)s/%(action)s" % options
    return ghURL


  def getGithubPRs( self, state="open", mergedOnly=False, perPage=100):
    """ get all PullRequests from github

    :param str state: state of the PRs, open/closed/all, default open
    :param bool merged: if PR has to be merged, only sensible for state=closed
    :returns: list of githubPRs
    """
    url = self._github( "pulls?state=%s&per_page=%s" % (state, perPage) )
    prs = curl2Json( ghHeaders(), url )
    #pprint(prs)
    if not mergedOnly:
      return prs

    ## only merged PRs
    prsToReturn = []
    for pr in prs:
      if pr.get( 'merged_at', None ) is not None:
        prsToReturn.append(pr)

    return prsToReturn

  def getGithubTags( self):
    """ get all tags from github

    u'commit': {u'sha': u'49680c32f9c0734dcbf0efe2f01e2363dab3c64e',
                u'url': u'https://api.github.com/repos/andresailer/Marlin/commits/49680c32f9c0734dcbf0efe2f01e2363dab3c64e'},
    u'name': u'v01-02-01',
    u'tarball_url': u'https://api.github.com/repos/andresailer/Marlin/tarball/v01-02-01',
    u'zipball_url': u'https://api.github.com/repos/andresailer/Marlin/zipball/v01-02-01'},

    :returns: list of tags
    """
    result = curl2Json( ghHeaders(), self._github( "tags" ) )
    if isinstance( result, dict ) and 'Not Found' in result.get('message'):
      raise RuntimeError( "Package not found: %s" % str(self) )
    return result

  def getGithubReleases( self):
    """ get the last few releases from github

    :returns: list of releases
    """
    result = curl2Json( ghHeaders(), self._github( "releases" ) )
    #pprint(result)
    return result


  def getHeadOfBranch( self ):
    """return the commit sha of the head of the branch"""
    result = curl2Json( ghHeaders(),
                        self._github( "git/refs/heads/%s" % self.branch )
                      )
    if 'message' in result:
      raise RuntimeError( "Error:",result['message'] )

    commitsha = result['object']['sha']

    return commitsha
    ## also get the sha of the tree

  def getTreeShaForCommit( self, commit ):
    """ return the sha of the tree for given commit"""
    result = curl2Json( ghHeaders(),
                        self._github( "git/commits/%s" % commit )
                      )
    if 'sha' not in result:
      raise RuntimeError( "Error: Commit not found" )
    treesha = result['tree']['sha']
    return treesha

  # def createGithubTag( self ):
  #   """
  #   create a tag on the repository with `version` and on `branch`, makes tag on last commit of the branch
  #   """
  #   message = "New tag %s" % self.newVersion
  #   prDict = dict( branch=self.branch, version=self.newVersion, message=message,
  #                  gtype="commit"
  #                )

  #   prDict['sha'] = self.getHeadOfBranch()
  #   if self._dryRun:
  #     self.log.info( "DryRun: not actually making tag: %s", prDict )
  #     return {}

  #   result = curl2Json( ghHeaders(),
  #                       '-d { "tag": "%(version)s", "message": "%(message)s", "object":"%(sha)s", "type":"%(gtype)s" '% prDict ,
  #                       self._github( "git/tags" ) )
  #   #pprint(result)

  #   #FIXME: error message is actually different
  #   if 'errors' in result:
  #     for error in result['errors']:
  #       self.log.error( "ERROR creating Tag: %s", error['message'] )
  #     return False

  #   prDict['tagSha'] = result['sha']

  #   result = curl2Json( ghHeaders(),
  #                       '-d { "ref": "refs/tags/%(version)s", "sha": "%(tagSha)s" '% prDict ,
  #                       self._github( "git/refs" ) )
  #   self.log.info( "New tag created" )
  #   return result

  def createGithubRelease( self ):
    """ make a release on github """
    if self.isUpToDate():
      self.log.warning( "Package %s is up to date, will not make new release", self )
      return


    releaseDict = dict( tag_name=self.newTag,
                        target_commitish=self.branch,
                        name=self.newTag,
                        body=self.formatReleaseNotes(),
                        prerelease=self.isPreRelease,
                      )
    if self._dryRun:
      self.log.info( "DryRun: not actually making Release: %s", releaseDict )
      return {}
    result = curl2Json( ghHeaders(), self._github( "releases" ),
                        '-d %s ' % json.dumps( releaseDict )
                      )
    #pprint(result)
    return result



  def isPRMerged( self, prID ):
    """ returns True/False wether the PR has been merged or not

    :param int prID: ID of the pull request
    :returns: True/False
    """
    result = curl2Json( ghHeaders(), self._github( "pulls/%d/merge" %prID ), checkStatusOnly=True )
    for line in result.splitlines():
      if "Status" in line:
        if "204" in line:
          self.log.debug( "PR %d is merged", prID)
          return True
        else:
          self.log.debug( "PR %d is NOT merged", prID)
          return False
    return False


  def _getPRsSinceLatestTag( self ):
    """ return the PRs since the last tag """
    self._getLatestTagInfo()
    if self.isUpToDate():
      return

    mergedPRs = self.getGithubPRs( state="closed", mergedOnly=True )
    #pprint(mergedPRs)
    lastTagDate = self.latestTagInfo['date']
    self.log.info( "Last tag was done: %s ", lastTagDate )

    self._prsSinceLastTag = []

    self.log.info( "Getting PRs...")
    for pr in mergedPRs:
      if pr['merged_at'] > lastTagDate:
        self.log.debug( "PR %s was merged _AFTER_ the last tag", pr['number'] )
        self._prsSinceLastTag.append(pr)
      else:
        self.log.debug( "PR %s was merged _BEFORE_ the last tag", pr['number'] )
    if self._prsSinceLastTag:
      self.log.info( "... PRs merged after Tag: %s", ", ".join( sorted(str( pr['number'] ) for pr in self._prsSinceLastTag )) )
    return

  def getCommentsForPR( self, prID ):
    """get the comments for a PR

    :param int prID: pull request ID to get the comments from
    :returns: list of comments
    """
    self.log.debug( "Getting comments for PR %s", prID )
    comments = curl2Json( ghHeaders(), self._github("issues/%s/comments" %prID  ) )
    commentTexts = []
    for comment in comments:
      commentTexts.append( comment['body'] )

    return commentTexts

  def getAuthorForPR( self, pr ):
    """ return the author name of given PR, check cache if username already known """
    username = pr['user']['login']
    prID = pr['number']
    commands = list(ghHeaders()) + [ self._github( "pulls/%s/commits" % prID ) ]
    authorName = authorMapping( username, commands )
    return authorName
    
    
  def _getReleaseNotes( self ):
    """ parses the PRs and comments for ReleaseNotes to collate them  """
    if self._prsSinceLastTag is None:
      self._getPRsSinceLatestTag()
    if not self._prsSinceLastTag:
      self._releaseNotes = defaultdict( OrderedDict )
      self.log.info( "No PRs found" )
      return

    relNotes = defaultdict( OrderedDict )
    self.log.info( "Getting release notes from PR comments ... ")
    for pr in self._prsSinceLastTag:
      prID = pr['number']
      self.log.debug( "Looking for comments for PR %s", prID )
      date = pr['merged_at'][:10] ## only YYYY-MM-DD
      author = self.getAuthorForPR( pr )
      relNotes[date][prID] = dict( author=author, notes=[], date=pr['merged_at'], prID=pr['number'] )

      notes = parseForReleaseNotes( pr['body'] )
      if notes:
        relNotes[date][prID]['notes'].extend( notes )
      commentTexts = self.getCommentsForPR( prID )
      for comment in commentTexts:
        notes = parseForReleaseNotes( comment )
        if notes:
          relNotes[date][prID]['notes'].extend( notes )
    self._releaseNotes = relNotes
    self.log.info( "... finished getting release notes" )
    return

  def formatReleaseNotes( self ):
    """ print the release notes """
    if self._releaseNotes is None and not self.isUpToDate():
      self._getReleaseNotes()

    if self.isUpToDate():
      return

    releaseNotesString = "# " + self.newVersion.split("-pre")[0] ## never write comments for new releases

    for date, prs in self._releaseNotes.iteritems():
      for prID,content in prs.iteritems():
        if not content.get( 'notes' ):
          continue

        for line in content['notes']:
          thisContent = line.strip()
          indentedContent = "  " + "\n  ".join(thisContent.split("\n"))
          relNoteDict = dict( author=content['author'],
                              prLink="[PR#%s](https://github.com/%s/%s/pull/%s)" % (prID, self.owner, self.repo, prID ),
                              date=date,
                              content=indentedContent.rstrip(),
                            )
          releaseNotesString += """

* %(date)s %(author)s (%(prLink)s)
%(content)s""" % relNoteDict

    ## cleanup "\r" from strings
    releaseNotesString = releaseNotesString.replace("\r","")
    return releaseNotesString


  def commitNewReleaseNotes( self ):
    """ get the new release notes and commit them to the filename """
    content, sha, encodedOld= self.getFileFromBranch( self.releaseNotesFilename )
    if self.latestTagInfo['pre']:
      content = "\n".join(content.split("\n")[2:]) ## remove first line which is the release name
    contentNew = self.formatReleaseNotes() + "\n\n" + content
    
    contentEncoded = contentNew.encode('base64')

    if encodedOld.replace("\n","") == contentEncoded.replace("\n",""):
      self.log.info("No changes in %s, not making commit", self.releaseNotesFilename )
      return
    message = "Release Notes for %s" % self.newVersion
    self.createGithubCommit(self.releaseNotesFilename, sha, contentEncoded, message=message)


  def getFileFromBranch( self, filename ):
    """return the content of the file in the given branch, filename needs to be the full path"""

    result = curl2Json( ghHeaders(), self._github( "contents/%s?branch=%s" %(filename,self.branch) ) )
    encoded = result.get( 'content', None )
    if encoded is None:
      self.log.error( "File %s not found for %s", filename, self )
      raise RuntimeError( "File not found" )
    content = encoded.decode("base64")
    sha = result['sha']
    return content, sha, encoded

  def updateVersionSettings( self ):
    """ get the new release notes and commit them to the filename """

    content, sha, encodedOld = self.getFileFromBranch( self.cmakeBaseFile )
    major, minor, patch = self._version.getMajorMinorPatch()
    pMajor = re.compile('_VERSION_MAJOR [0-9]*')
    pMinor = re.compile('_VERSION_MINOR [0-9]*')
    pPatch = re.compile('_VERSION_PATCH [0-9a-zA-Z]*')
    content = pMajor.sub( "_VERSION_MAJOR %s" % major, content )
    content = pMinor.sub( "_VERSION_MINOR %s" % minor, content )
    content = pPatch.sub( "_VERSION_PATCH %s" % patch, content )
    contentEncoded = content.encode('base64')
    if encodedOld.replace("\n","") == contentEncoded.replace("\n",""):
      self.log.info("No changes in %s, not making commit", self.cmakeBaseFile )
      return

    message = "Updating version to %s" % self.newVersion
    self.createGithubCommit(self.cmakeBaseFile, sha, contentEncoded, message=message)



  def createGithubCommit( self, filename, fileSha, content, message ):
    """
    create a commit on the repository with `version` and on `branch`, makes tag on last commit of the branch

    :param str treeSha: sha of the tree the commit will go
    :param str filename: full path to the file
    :param str content: base64 encoded content of the file


    PUT /repos/:owner/:repo/contents/:path

    Parameters
    Name  Type  Description
    path  string  Required. The content path.
    message   string  Required. The commit message.
    content   string  Required. The updated file content, Base64 encoded.
    sha   string  Required. The blob SHA of the file being replaced.
    branch  string  The branch name. Default: the repository's default branch (usually master)
    Optional Parameters

    """
    coDict = dict( path=filename, content=content, branch=self.branch, sha=fileSha, message=message, force='true' )
    if self._dryRun:
      coDict.pop('content')
      self.log.info( "DryRun: not actually making commit: %s", coDict )
      return

    result = curl2Json( ghHeaders(), '-X','PUT',
                        '-d %s ' % json.dumps( coDict ),
                        self._github( "contents/%s" % filename ) )

    if 'commit' not in result:
      raise RuntimeError( "Failed to update file: %s" % result['message'] )

    return result


  def createGithubPR( self, sourceBranch, targetRepo, targetBranch ):
    """ create a PR on Github


    :param str sourceBranch: branch the PR is based on
    :param str targetRepo: target repository for the PR
    :param str targetBranch: target for the PR
    """

    title = "Mirror from gitlab MR: %s" % sourceBranch
    prDict = dict( branch=sourceBranch, base=targetBranch, title=title, sourceRepo=self.repo, targetRepo=targetRepo )
    if not all( opt in prDict for opt in ( 'branch', 'base', 'title', 'sourceRepo', "FIXME" ) ):
      self.log.error( "Missing some option in the option dict: %s" , prDict )

    result = curl2Json( ghHeaders(),
                        '-d { "title": "%(title)s", "head": "%(branch)s", "base": "%(base)s"}' % prDict ,
                        self._github( "pulls" ) )

    if 'errors' in result:
      for error in result['errors']:
        self.log.error( "ERROR creating PullRequest: %s", error['message'] )
      return False
    else:
      self.log.info( "Created pullrequest" )
      url = result['html_url']
      return url


  def isUpToDate( self ):
    """ return True/False wether we have to make a new tag or not"""
    if self.latestTagInfo['sha'] != self._lastCommitOnBranch['sha']:
      return False

    ## this means the commits are the same, but maybe we want to make a proper tag now
    if 'pre' in self.latestTagInfo['name'] and 'pre' not in self.newTag:
      return False

    return True
