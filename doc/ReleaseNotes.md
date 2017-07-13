# v01-19-03

* 2017-05-10 Felix Reidt ([PR#13](https://github.com/iLCSoft/ilcinstall/pull/13))
  - Fixe inconsistent init_ilcsoft.sh files

* 2017-06-09 Marko Petric ([PR#28](https://github.com/iLCSoft/ilcinstall/pull/28))
  - Remove DNDEBUG from default flags for RELWITHDEBINFO

* 2017-06-09 Marko Petric ([PR#27](https://github.com/iLCSoft/ilcinstall/pull/27))
  - Remove `-DNDEBUG` from the CMake default for `RELWITHDEBINFO`
  - Remove cmake commands from the `ILCSoft.cmake.env.sh`

* 2017-06-30 Marko Petric ([PR#31](https://github.com/iLCSoft/ilcinstall/pull/31))
  - Use LCFIPlus from Github/LCFIPlus instead of lcfiplus/LCFIPlus in nightly

* 2017-06-20 Andre Sailer ([PR#30](https://github.com/iLCSoft/ilcinstall/pull/30))
  - ilcsoft-install: Allow specifying git branch ` pkg.download.branch = "mybranch"` if `version == [HEAD|dev|devel|master]`
  - baseilc: replace tabs with spaces

* 2017-06-20 Andre Sailer ([PR#29](https://github.com/iLCSoft/ilcinstall/pull/29))
  - lcfivertex: adapt to ilcsoft/LCFIVertex#4 splitting LCFIVertex processors in their own library

* 2017-07-05 Remi Ete ([PR#32](https://github.com/iLCSoft/ilcinstall/pull/32))
  - Changed ilcutil.py module to get its sources from Github instead of desy svn as default

* 2017-05-08 Andre Sailer ([PR#26](https://github.com/iLCSoft/ilcinstall/pull/26))
  - Tagging: enable complete tagging of dd4hep, also changing DDSegmentation version
  - Tagging: fix bug when trying to tag a branch that is not master. the CMakeLists file was still taken from the master branch.

* 2017-04-27 Andre Sailer ([PR#25](https://github.com/iLCSoft/ilcinstall/pull/25))
  - Added tests for large parts of the ilcsoft tagger files
  - Prevent the printout of the githubtoken in DEBUG mode
  - Prevent creation of tags that are older than the last tag (e.g., 2.8-pre if 2.8 was created already)
  - Fix a bug in the error reporting of packages causing exception for using variable before it is assigned
  - add --lastTag option to set the tag to use instead of finding the last tag automatically. Only works if a single package is specified

