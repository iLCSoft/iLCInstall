# v02-01-02

* 2020-07-17 Remi Ete ([PR#116](https://github.com/iLCSoft/ILCInstall/pull/116))
  - Updated packages version:
     - Marlin to v01-17-01
     - LCIO to v02-14-02
  - Added release notes

# v02-01-01

* 2020-07-02 Remi Ete ([PR#115](https://github.com/ilcsoft/ilcinstall/pull/115))
  - Upgraded versions for new release v02-01-01

* 2020-06-16 Andre Sailer ([PR#114](https://github.com/ilcsoft/ilcinstall/pull/114))
  - Fix for the CI, increment pytest version requirement

* 2020-06-16 Placido Fernandez Declara ([PR#113](https://github.com/ilcsoft/ilcinstall/pull/113))
  - ilcsofttagger: Fix first release tagging script

* 2020-06-02 Remi Ete ([PR#112](https://github.com/ilcsoft/ilcinstall/pull/112))
  - Fixed SIO configuration for nightly builds

* 2020-05-29 Frank Gaede ([PR#111](https://github.com/ilcsoft/ilcinstall/pull/111))
  - add standalone SIO library to LCG releases and nightlies
        - will be needed for LCIO and PODIO

* 2020-05-18 Frank Gaede ([PR#109](https://github.com/ilcsoft/ilcinstall/pull/109))
  - make it work again for Ubuntu (18.04)
      - force system calls to be made through bash

* 2020-05-14 Frank Gaede ([PR#108](https://github.com/ilcsoft/ilcinstall/pull/108))
  - update examples/macbookfg to work for v02-01

* 2020-04-06 Marko Petric ([PR#104](https://github.com/ilcsoft/ilcinstall/pull/104))
  - Use github repo for GBL

* 2020-04-03 Daniel Jeans ([PR#105](https://github.com/ilcsoft/ilcinstall/pull/105))
  - increase timeout to prevent installation failures due to slow G4 data downloads (default is 1500 s)

# v02-00-02

* 2018-09-04 Frank Gaede ([PR#57](https://github.com/ilcsoft/ilcinstall/pull/57))
  - update versions for bug fix release v02-00-02 for ILD w/ updates to 
        - LCIO, DD4hep, lcgeo, MarlinReco, KalTest, CEDViewer, LCFIPlus

* 2018-07-03 Andre Sailer ([PR#56](https://github.com/ilcsoft/ilcinstall/pull/56))
  - Tagging:
    - Fix problem for the username. Caching does not work  when the PR author and commits do not come from the same person
    - PRs are only chosen for the branch that should be tagged
    - Sort release notes by date and PR number

* 2018-05-22 Frank Gaede ([PR#55](https://github.com/ilcsoft/ilcinstall/pull/55))
  - update versions and release notes for v02-00-01

# v01-19-04

* 2017-07-26 Frank Gaede ([PR#35](https://github.com/iLCSoft/ilcinstall/pull/35))
  - update to v01-19-04 (identical to v01-19-03.p01)
     - Github does not allow version v01-19-03.p01

# v01-19-03.p01

* 2017-07-20 Ete Remi ([PR#34](https://github.com/iLCSoft/ilcinstall/pull/34))
  - Added PANDORA_ANALYSIS_DIR env var
  - Set LD_LIBRARY_PATH and PATH accordingly

* Frank Gaede 
 - update lcgeo to v00-13-04
 - update ROOT_version = "6.08.06" for HEAD releases"
 - update DD4hep v01-01-01


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

