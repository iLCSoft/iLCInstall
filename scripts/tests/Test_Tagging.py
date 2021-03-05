#!/bin/env python
"""Test the Tagging Modules"""
from __future__ import print_function


import json
import logging
try:
  import __builtin__ as builtins
  builtin_module_name = '__builtin__'
except ImportError:  # for python3
  import builtins
  builtin_module_name = 'builtins'
import unittest
import os
import shutil
import sys
import tempfile
import tarfile
from zipfile import ZipFile
from mock import patch, MagicMock as Mock, mock_open
from pprint import pprint

sys.modules['GitTokens'] = Mock(name="GitTokensMock", return_value=Mock(name="returnedMock"))
sys.modules['requests'] = Mock(name="RequestMock",side_effect=ImportError("nope"))

from tagging.gitinterface import Repo
from tagging.helperfunctions import getCommands, versionComp, parseForReleaseNotes, _curl2Json as curl2Json, authorMapping, checkRate
from tagging.parseversion import Version, getVersionComp

__RCSID__ = "$Id$"

REALIMPORT = builtins.__import__
def myimport(name, globs, locs, fromlist, level=0):
  """ raise error for import """
  if name=="GitTokens" and "GITHUBTOKEN" in fromlist:
    raise ImportError
  return REALIMPORT(name, globs, locs, fromlist)

def mockCurl(*args, **kwargs):
  """ mock the curl2Json calls in the gitinterface """
  logging.error("\nArgs: %r", args)
  logging.error("\nArgs: %r", getCommands(args))
  logging.error("Kwargs: %r", kwargs )

  cmdString = " ".join( getCommands(args) )
  cmdString += str(kwargs)
  logging.error( "ComdString: %s", cmdString )
  if "/tags" in cmdString:
    logging.error("Returning tags structure")
    return [ { "name": "v01-03-19",
               "commit": { "sha": "MyTagSha2",
                           "url": "http://localhost/foo/bar"
                         },
               "zipball_url": "zipball/v0.1",
               "tarball_url": "tarball/v0.1"
             }
           ]

  if "/tag" in cmdString:
    logging.error( "Returning single tag" )
    return { "tag": "v1-03-19",
             "sha": "MyTagSha01",
             "url": "http://localhost/foo/bar/baz",
             "message": "initial version",
             "tagger": { "name": "Foo Bar",
                         "email": "foo@bar.org",
                         "date": "2014-11-07T22:01:45Z"
                       },
             "object": { "type": "commit",
                         "sha": "myCommitSha1",
                         "url": "https://foo.org/git/commits/myCommitSha1"
                       }
           }
  if "/git/commits/" in cmdString:
    logging.error( "Returning single commit" )

    return { "sha": "7638417db6d59f3c431d3e1f261cc637155684cd",
             "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7638417db6d59f3c431d3e1f261cc637155684cd",
             "author": { "date": "2014-11-07T22:01:45Z",
                         "name": "Scott Chacon",
                         "email": "schacon@gmail.com"
                       },
             "committer": { "date": "2014-11-07T22:01:45Z",
                            "name": "Scott Chacon",
                            "email": "schacon@gmail.com"
                          },
             "message": "added readme, because im a good github citizen",
             "tree": { "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/691272480426f78a0138979dd3ce63b77f706feb",
                       "sha": "myCommitSha"
                     },
             "parents": [ { "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/1acc419d4d6a9ce985db7be48c6349a0475975b5",
                            "sha": "1acc419d4d6a9ce985db7be48c6349a0475975b5"
                          }
                        ]
           }

  if "/branches" in cmdString:
    return { "name": "master",
             "commit": { "sha": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
                         "commit": { "author": { "name": "The Octocat",
                                                 "date": "2012-03-06T15:06:50-08:00",
                                                 "email": "octocat@nowhere.com"
                                               },
                                     "url": "https://api.github.com/repos/octocat/Hello-World/git/commits/7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
                                     "message": "Merge pull request #6 from Spaceghost/patch-1\n\nNew line at end of file.",
                                     "tree": { "sha": "b4eecafa9be2f2006ce1b709d6857b07069b4608",
                                               "url": "https://api.github.com/repos/octocat/Hello-World/git/trees/b4eecafa9be2f2006ce1b709d6857b07069b4608"
                                             },
                                     "committer": { "name": "The Octocat",
                                                    "date": "2012-03-06T15:06:50-08:00",
                                                    "email": "octocat@nowhere.com"
                                                  }
                                   },
                         "author": { "gravatar_id": "",
                                     "avatar_url": "https://secure.gravatar.com/avatar/7ad39074b0584bc555d0417ae3e7d974?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png",
                                     "url": "https://api.github.com/users/octocat",
                                     "id": 583231,
                                     "login": "octocat"
                                   },
                         "parents": [ { "sha": "553c2077f0edc3d5dc5d17262f6aa498e69d6f8e",
                                        "url": "https://api.github.com/repos/octocat/Hello-World/commits/553c2077f0edc3d5dc5d17262f6aa498e69d6f8e"
                                      },
                                      { "sha": "762941318ee16e59dabbacb1b4049eec22f0d303",
                                        "url": "https://api.github.com/repos/octocat/Hello-World/commits/762941318ee16e59dabbacb1b4049eec22f0d303"
                                      }
                                    ],
                         "url": "https://api.github.com/repos/octocat/Hello-World/commits/7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
                         "committer": { "gravatar_id": "",
                                        "avatar_url": "https://secure.gravatar.com/avatar/7ad39074b0584bc555d0417ae3e7d974?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png",
                                        "url": "https://api.github.com/users/octocat",
                                        "id": 583231,
                                        "login": "octocat"
                                      }
                       },
             "_links": { "html": "https://github.com/octocat/Hello-World/tree/master",
                         "self": "https://api.github.com/repos/octocat/Hello-World/branches/master"
                       },
             "protected": True,
             "protection_url": "https://api.github.com/repos/octocat/Hello-World/branches/master/protection"
           }
  if "pulls/12/commits" in cmdString:
    return [ {'commit':{'author': {'name':'User Name2'}}}, {'commit':{'author': {'name':'User Name2'}}} ]

  if 'rate_limit' in cmdString:
    return {'rate':{'remaining':444, 'limit':555} }
  ##default
  return {}


#pylint: disable=too-many-public-methods, protected-access


def cleanup(tempdir):
  """
  Remove files after run
  """
  try:
    shutil.rmtree(tempdir)
  except OSError:
    pass

@patch("tagging.gitinterface.curl2Json",new=mockCurl)
class TestGit( unittest.TestCase ):
  """ test Gitinterface function """

  def assertIn(self, *args, **kwargs):
    """make this existing to placate pylint"""
    return super(TestGit, self).assertIn(*args, **kwargs)

  def setUp( self ):
    self.repo = None

  def tearDown( self ):
    pass


  def test_ctor_pre_1( self ):
    """ test the constructor """
    self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion=None, preRelease=True, dryRun=True)
    self.assertEqual( self.repo.newVersion, "v01-03-20" )
    self.assertEqual( self.repo.newTag, "v01-03-20-pre" )
    self.assertTrue( self.repo.isPreRelease )
    self.assertTrue( self.repo._dryRun )

  def test_ctor_pre_2( self ):
    """ test the constructor """
    self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion="v01-03-20", preRelease=True, dryRun=True)
    self.assertEqual( self.repo.newVersion, "v01-03-20" )
    self.assertEqual( self.repo.newTag, "v01-03-20-pre" )
    self.assertTrue( self.repo.isPreRelease )
    self.assertTrue( self.repo._dryRun )

  def test_ctor_2( self ):
    """ test the constructor """
    self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion="v01-03-20", preRelease=False, dryRun=True)
    self.assertEqual( self.repo.newVersion, "v01-03-20" )
    self.assertEqual( self.repo.newTag, "v01-03-20" )
    self.assertFalse( self.repo.isPreRelease )
    self.assertTrue( self.repo._dryRun )


  def test_ctor_fail_1( self ):
    """ test the constructor when the desired pre-version is the same as an existing one"""
    myTagInfo=[ { "name": "v01-03-20",
                  "commit": { "sha": "MyTagSha2",
                              "url": "http://localhost/foo/bar"
                            },
                  "zipball_url": "zipball/v0.1",
                  "tarball_url": "tarball/v0.1"
                }
              ]

    with self.assertRaisesRegexp( RuntimeError, "Invalid version required"), \
         patch( "tagging.gitinterface.Repo.getGithubTags", new=Mock( return_value=myTagInfo)):
      self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion="v01-03-20-pre", preRelease=True, dryRun=True)

  def test_ctor_fail_2( self ):
    """ test the constructor when the desired pre-version is the same as an existing one"""
    myTagInfo=[ { "name": "v01-03-20",
                  "commit": { "sha": "MyTagSha2",
                              "url": "http://localhost/foo/bar"
                            },
                  "zipball_url": "zipball/v0.1",
                  "tarball_url": "tarball/v0.1"
                }
              ]
    with self.assertRaisesRegexp( RuntimeError, "Invalid version required"), \
         patch( "tagging.gitinterface.Repo.getGithubTags", new=Mock( return_value=myTagInfo)):
      self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion="v01-03-19", preRelease=True, dryRun=True)

  def test_ctor_fail_3( self ):
    """ test the constructor when the desired pre-version is the same as an existing one"""
    myTagInfo=[ { "name": "v01-03-20-pre2",
                  "commit": { "sha": "MyTagSha2",
                              "url": "http://localhost/foo/bar"
                            },
                  "zipball_url": "zipball/v0.1",
                  "tarball_url": "tarball/v0.1"
                }
              ]


    with self.assertRaisesRegexp( RuntimeError, "Invalid version required"), \
         patch( "tagging.gitinterface.Repo.getGithubTags", new=Mock( return_value=myTagInfo)):
      self.repo = Repo(owner="tester", repo="testrepo", branch="testbranch", newVersion="v01-03-20-pre1", preRelease=True, dryRun=True)


class TestHelpers( unittest.TestCase ):
  """ tests for the helper functions """

  def test_getCommands_tuple( self ):
    t1 = [(1, 2), 3 ]
    self.assertEqual( getCommands(*t1), [1, 2, 3] )
  def test_getCommands_list( self ):
    t1 = [ [[1, 2], 3], 4, 5, [6, 7] ]
    self.assertEqual( getCommands(*t1), [1, 2, 3, 4, 5, 6, 7] )


  def testVersionComp( self ):
    """ test version comparison """

    self.assertEqual( versionComp( "foo", "foo" ), 0 )
    self.assertLess( versionComp( "v01-12", "v2-11" ), 0 )

    self.assertLess( versionComp( "v1r12p12", "v2-11" ), 0 )
    self.assertLess( versionComp( "v1r12p12", "v1r13p12" ), 0 )

    self.assertGreater( versionComp( "v1r13p12", "v1r12p12" ), 0 )
    self.assertGreater( versionComp( "v1-13-12", "v1r12p12" ), 0 )

    self.assertLess( versionComp( "v1-13-12-pre", "v1-13-12" ), 0 )
    self.assertGreater( versionComp( "v1-13-12", "v1-13-12-pre" ), 0 )

    self.assertLess( versionComp( "v1-13-12-pre", "v1-14" ), 0 )
    self.assertGreater( versionComp( "v1-14", "v1-13-12-pre" ), 0 )

    self.assertGreater( versionComp( "v1-13-12-pre2", "v1-13-12-pre" ), 0 )
    self.assertGreater( versionComp( "v1-13-13-pre2", "v1-13-12" ), 0 )
    self.assertLess( versionComp( "v1-13-12", "v1-13-13-pre" ), 0 )

  def test_importError( self ):
    """ test the import error when not having githubtoken """
    try:
      del sys.modules['tagging.helperfunctions']
      del sys.modules['GitTokens']
    except KeyError:
      pass

    with patch(builtin_module_name + ".__import__", myimport):
      with self.assertRaises( ImportError ):
        from tagging.helperfunctions import GITHUBTOKEN
        print(GITHUBTOKEN)

  def test_parseForReleaseNotes( self ):
    """ test parseForReleaseNotes """
    self.assertEqual( parseForReleaseNotes(""" """), [])

    self.assertEqual( parseForReleaseNotes("""BEGINRELEASENOTES """), [])
    self.assertEqual( parseForReleaseNotes("""ENDRELEASENOTES """), [])
    self.assertEqual( parseForReleaseNotes("""BEGINRELEASENOTES my notes ENDRELEASENOTES """), [" my notes "])


  def test_curl2Json( self ):
    """ test curl2Json """

    with patch("tagging.helperfunctions.subprocess", new=Mock()), \
         patch("tagging.helperfunctions.subprocess.check_output", new=Mock(return_value=json.dumps("arg"))) as check:
      value = curl2Json( ["some","repo", "command"] )
      args, kwargs = check.call_args
      self.assertEqual( value, "arg" )
      print(args, kwargs)
      self.assertEqual( 'curl', args[0][0] )
      self.assertEqual( '-s', args[0][1] )

    with patch("tagging.helperfunctions.subprocess", new=Mock()), \
         patch("tagging.helperfunctions.subprocess.check_output", new=Mock(return_value="arg")) as check:
      with self.assertRaises( ValueError ):
        value = curl2Json( ["some","repo", "command"] )

  def test_getAuthor( self ):
    """ test the mapping of the username to authorname """
    with patch("tagging.helperfunctions.curl2Json",new=mockCurl):
      retVal = authorMapping(['commands', 'pulls/12/commits'])
      self.assertEqual( retVal, 'User Name2' )

  def test_checkRate( self ):
    """ test the checkRate function """
    with patch("tagging.helperfunctions.curl2Json",new=mockCurl):
      checkRate()

class TestParseVersion( unittest.TestCase ):
  """ tests for the helper functions """

  def test_v1( self ):
    """ test from pre to pre """
    version = Version( "v00-00", makePreRelease=True )
    self.assertEqual( str(version), "v00-00-pre" )
    version.increment()
    self.assertEqual( str(version), "v00-00-01-pre" )


  def test_v2( self ):
    """ test 2"""
    version = Version( "v00-00", makePreRelease=False )
    self.assertEqual( str(version), "v00-00" )
    self.assertFalse( version.isPre )
    version.increment()
    self.assertEqual( str(version), "v00-00-01" )


  def test_pre_increment( self ):
    """ test from pre to increment pre"""
    version = Version( "v01-02-03-pre", makePreRelease=True )
    self.assertEqual( str(version), "v01-02-03-pre" )
    self.assertTrue( version.isPre )
    version.increment()
    self.assertEqual( str(version), "v01-02-03-pre1" )


  def test_v3( self ):
    """ test from pre to release"""
    version = Version( "v01-02-03-pre", makePreRelease=False )
    self.assertEqual( str(version), "v01-02-03" )
    self.assertTrue( version.isPre )
    version.increment()
    self.assertEqual( str(version), "v01-02-03" )


  def test_v4( self ):
    """ test from release to release"""
    version = Version( "v01-02-04", makePreRelease=False )
    self.assertEqual( str(version), "v01-02-04" )
    self.assertFalse( version.isPre )
    version.increment()
    self.assertEqual( str(version), "v01-02-05" )

  def test_parseVersions( self ):
    """ test different version strings """

    with self.assertRaises( RuntimeError ):
      Version( "v01" )

    with self.assertRaises( RuntimeError ):
      Version( "v01-arg" )

    with self.assertRaises( RuntimeError ):
      Version( "v01-03-20-arg" )


    self.assertEqual( str(Version( "v01-02-pre" )), "v01-02-pre" )

    version = Version( "v01-02-pre13" )
    self.assertEqual( str(version), "v01-02-pre13" )
    self.assertEqual( version.getMajorMinorPatch(), (1, 2, 0) )

    version = Version( "v01-02-13", makePreRelease=False )
    self.assertEqual( str(version), "v01-02-13" )
    self.assertEqual( version.getMajorMinorPatch(), (1, 2, 13) )



    version = Version( "v01-02-14-pre13" )
    self.assertEqual( str(version), "v01-02-14-pre13" )
    self.assertEqual( version.getMajorMinorPatch(), (1, 2, 14) )

    version = Version( "v01-02-13-pre16", makePreRelease=False )
    self.assertEqual( str(version), "v01-02-13" )
    self.assertEqual( version.getMajorMinorPatch(), (1, 2, 13) )



  def test_getMajorMinorPatch( self ):
    """ test from pre to increment pre"""
    version = Version( "v01-02", makePreRelease=True )
    self.assertEqual( str(version), "v01-02-pre" )
    self.assertFalse( version.isPre )
    self.assertEqual( version.getMajorMinorPatch(), (1, 2, 0) )


  def test_sortVersions(self):

    versions = ['v01-12', 'v00-10', 'v01-12-01', 'v02-22-00-pre3', 'v00-01']
    sv = sorted(versions, key=getVersionComp)
    assert sv == ['v00-01', 'v00-10', 'v01-12', 'v01-12-01', 'v02-22-00-pre3']
    sv = sorted(versions, reverse=True, key=getVersionComp)
    assert sv == [
      'v02-22-00-pre3',
      'v01-12-01',
      'v01-12',
      'v00-10',
      'v00-01',
    ]



def runTests():
  """Runs our tests"""
  suite = unittest.TestSuite()
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestGit ) )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestHelpers ) )

  testResult = unittest.TextTestRunner( verbosity = 2 ).run( suite )
  print(testResult)

if __name__ == '__main__':
  runTests()
