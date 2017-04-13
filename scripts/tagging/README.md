
# ilcsofttagger 

python script for automatic creation of (pre-)release tags of iLCSoft packages

Author: A. Sailer, CERN

* requires write privilegs on [https://github.com/iLCSoft](https://github.com/iLCSoft)


* usage:
```    
ilcsofttagger --packages lcgeo marlin aidasoft/dd4hep fcalsw/fcalclusterer ... [--properRelease] [--makeTags] [--file packageFile]
```

* default is dry run mode use --makeTags to actually make the tags

* default is pre-release tags, use --properRelease to make real release

* The script will parse github pull requests to collate release notes
  and write them into doc/ReleaseNotes.md

* The script will update the _VERSION_MAJOR, MINOR, PATH in the base
  CMakeLists.txt file to the new version

* One needs a github personal access token in a file called
  GitTokens.py in a constant called GITHUBTOKEN, see helperfunctions
  for details, also the ImportError will give this information

* Will not make another prerelease tag if there are no new commits
  since the last tag Release notes are always written for the new
  version

* to set the version number give the repo onwer (ilcsoft) and the
  version number afterwards ilcsofttagger --packages
  ilcsoft/lcgeo/v10-00 ... [--properRelease] [--makeTags]

* can also use a configuration file which contains the same kind of
  strings

    ilcsofttagger --file configFile

* see ilcsofttagger --help as well
