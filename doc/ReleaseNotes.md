# v02-03-02

* 2023-07-12 tmadlener ([PR#164](https://github.com/iLCSoft/iLCInstall/pull/164))
  - Add new package
    - k4EDM4hep2LcioConv v00-05 (LCIO to EDM4hep conversion)
  
  - Update base package versions
    - DD4hep 01-25-01
    - ROOT 6.28/04
    - Geant4 11.1.1
  
  - Update package versions to latest tags
      - MarlinReco v01-34
      - podio v00-16-05
      - EDM4hep v00-10
      - iLCUtil v01-07-01
      - LCIO v02-20
      - lcgeo (k4geo) v00-18-01
      - MarlinUtil v01-17-01
      - RAIDA v01-10
      - ConformalTracking v01-11-01
      - MarlinTrkProcessors v02-12-03
      - Overlay v00-23
      - ILDPerformance v01-12

* 2023-06-26 tmadlener ([PR#166](https://github.com/iLCSoft/iLCInstall/pull/166))
  - Add the `k4EDM4hep2LcioConv` package
  - Bump a few external versions in the HEAD releases

* 2023-06-26 tmadlener ([PR#165](https://github.com/iLCSoft/iLCInstall/pull/165))
  - Make sure that `CMAKE_PREFIX_PATH` points to the right place for Geant4 > v11.1 where it has been moved to a more standard location.

* 2023-02-20 Thomas Madlener ([PR#162](https://github.com/iLCSoft/iLCInstall/pull/162))
  - Make `Physsim` its own package to accomodate more easily for changed behavior after CMake config updates in iLCSoft/Physsim#2
  - Make `MarlinPKG` slightly more clever for discovering libraries that need to be put on `MARLIN_DLL`

# v02-03-01

* 2022-12-21 Thomas Madlener ([PR#159](https://github.com/iLCSoft/iLCInstall/pull/159))
  - Include latest version of packages
    - LCIO v02-19
    - Marlin v01-19
    - ILCUtil v01-07
    - MarlinTrkProcessors v02-12-02
    - KiTrackMarlin v01-13-02
    - MarlinUtil v01-17
    - MarlinDD4hep v00-06-02
    - MarlinReco v01-33-01
    - ILDPerformance v01-11
    - lcgeo v00-18
    - podio v00-16-01
    - EDM4hep v00-07-02

* 2022-12-07 Thomas Madlener ([PR#160](https://github.com/iLCSoft/iLCInstall/pull/160))
  - Disable `PathFinder`, `MarlinTPC`, and `BBQ` packages from being installed by default, as they are no longer available from the DESY SVN server and have not yet been fully migrated to the DESY gitlab server.
  - Fix tests to work with latest versions of `pytest`. The main reason is that starting with pytest 7.2.0(?) py.test.raises only works if py is also installed. Given https://github.com/pytest-dev/py/issues/288 it is probably easiest to just use pytest directly if possible.
  - Fix a few escape sequence warnings in packages.

* 2022-10-20 Andre Sailer ([PR#158](https://github.com/iLCSoft/iLCInstall/pull/158))
  - Make sure that `GIT_EXEC_PATH` is also present in `init_ilcsoft.sh` if it has been present in the build environment to ensure git is usable.

* 2022-08-24 Thomas Madlener ([PR#157](https://github.com/iLCSoft/iLCInstall/pull/157))
  - Remove ILDConfig from installed packages again as it is installed separately in any case.

# v02-03

* 2022-08-17 Thomas Madlener ([PR#156](https://github.com/iLCSoft/iLCInstall/pull/156))
  - Major upgrades to external software, most importantly **switching from python2 to python3**, and to newer version of gcc.
  - Update all external software to latest available versions
  - Include latest versions of iLCSoft packages
    - CED v01-09-04
    - MarlinFastJet v00-05-03
    - MarlinReco v01-33
    - lcgeo v00-16-08
    - CEDViewer v01-19-01
    - KalTest v02-05-01
    - DDKalTest v01-07
    - LCIO v02-17-01
    - MarlinKinfitProcessors v00-05
    - LCCD v01-05-01 
    - GEAR v01-09-01 
    - MarlinDD4hep v00-06-01 
    - MarlinUtil v01-16-02 
    - MarlinTrk v02-09-01 
    - MarlinTrkProcessors v02-12-01 
    - MarlinKinfit v00-06-01 
    - Overlay v00-22-04 
    - KiTrackMarlin v01-13-01 
    - ForwardTracking v01-14-01 
    - LCTuple v01-14
    - ILDConfig v02-03
    - Physsim v00-04-02

* 2022-06-29 Thomas Madlener ([PR#144](https://github.com/iLCSoft/iLCInstall/pull/144))
  - Update versions of base installation
  - Switch to using gcc and python from LCG_99 (i.e. gcc10 and python3)

* 2022-01-25 tmadlener ([PR#134](https://github.com/iLCSoft/iLCInstall/pull/134))
  - migrate CI to github actions and run python unittests with python2 and python3.
  - Remove coveralls instrumentation from CI

* 2022-01-18 Frank Gaede ([PR#152](https://github.com/iLCSoft/iLCInstall/pull/152))
  - add EDM4hep and PODIO to HEAD releases

* 2022-01-18 Thomas Madlener ([PR#143](https://github.com/iLCSoft/iLCInstall/pull/143))
  - Make `ilcsoft-install` work with python3. Most of the trivial changes are done via `2to3`. Some others that are necessary for this to work with both python2 and python3 are:
    - Fixes to some (relative) imports
    - Importing `getoutput` and `getstatusoutput` from the `subprocess` module if possible and only fallback to the `commands` module if it does not exist.
    - Replace `execfile` with `exec`, `compile` and `open` combination.
    - Some changes to the `Version` class to make it work with the much stricter comparison rules in python3.
  - Fix installation of root 6.18/04 by pulling in the patched sources from git directly, instead of using the release tar ball. See: https://root-forum.cern.ch/t/problems-building-root-6-18-04-with-builtin-davix/44225

* 2022-01-17 Frank Gaede ([PR#150](https://github.com/iLCSoft/iLCInstall/pull/150))
  - update versions in HEAD release scripts:
  - geant4 11.0 root 6.24.06,...
  -

* 2022-01-14 Frank Gaede ([PR#149](https://github.com/iLCSoft/iLCInstall/pull/149))
  - add support for installing edm4hep and podio
  - update macbookfg example install scripts

* 2022-01-14 Frank Gaede ([PR#148](https://github.com/iLCSoft/iLCInstall/pull/148))
  - add support for (central) ubuntu installations w/ 20.04
  - update download path for boost

# v02-02-03

* 2021-11-22 Thomas Madlener ([PR#147](https://github.com/iLCSoft/iLCInstall/pull/147))
  - Update LCIO to v02-17
  - Update MarlinReco to v01-32
  - Update MarlinTrk to v02-09
  - Update MarlinUtil to v01-16-01
  - Update CEDViewer to v01-19
  - Update LCTuple to v01-13
  - Update ConformalTracking to v01-11
  - Update MarlinTrkProcessors to v02-12
  - Update Overlay to v00-22-03
  - Update DDMarlinPandora to v00-12
  - Update iLCUtil to v01-06-02
  - Update lcgeo to v00-16-07
  - Update LCFIPlus to v00-10-01

# v02-02-02

* 2021-06-15 Thomas Madlener ([PR#145](https://github.com/iLCSoft/iLCInstall/pull/145))
  - Update ILDPerformance to v01-10
  - Update MarlinUtil to v01-16
  - Update MarlinReco to v01-31

* 2021-03-16 Placido Fernandez Declara ([PR#141](https://github.com/iLCSoft/iLCInstall/pull/141))
  - Add support for "." version delimiter

# v02-02-01

* 2021-03-08 Andre Sailer ([PR#139](https://github.com/iLCSoft/iLCInstall/pull/139))
  - ilcsofttagger: make python3 compatible, keep python2 compatibility for the moment
  - ilcsofttagger: add --ignoreMissingCmake flag to ignore the absence of CMakeLists.txt in the repository
  - ilcsofttagger: no longer look up release notes in comments to PRs, only the opening post
  - ilcsofttagger: try to get author name from the first commit of a PR not the last, might fix issue with wrongly attributed changes in the release notes

* 2021-03-07 tmadlener ([PR#140](https://github.com/iLCSoft/iLCInstall/pull/140))
  - Fix small typo in README for cvmfs installation

* 2021-03-04 tmadlener ([PR#138](https://github.com/iLCSoft/iLCInstall/pull/138))
  - Update cvmfs installation docker container

* 2021-03-03 tmadlener ([PR#137](https://github.com/iLCSoft/iLCInstall/pull/137))
  - Update MarlinReco version to v01-30

* 2021-03-01 tmadlener ([PR#136](https://github.com/iLCSoft/iLCInstall/pull/136))
  - Make sure that `libsio` is found after CMake updates to sio

* 2021-03-01 tmadlener ([PR#135](https://github.com/iLCSoft/iLCInstall/pull/135))
  - Upgrade Overlay to v00-22-02

* 2021-02-26 Remi Ete ([PR#133](https://github.com/iLCSoft/iLCInstall/pull/133))
  - Upgrade MarlinReco to v01-29
  - Upgrade ILDPerformance to v01-09
  - Upgrade SIO to v00-01
  - Upgrade LCIO to v02-16-01

* 2020-12-08 Frank Gaede ([PR#130](https://github.com/iLCSoft/iLCInstall/pull/130))
  - add edm4hep and podio install scripts
  - update macbook example
        - add edm4hep and podio
        - updated to Catalina (10.15.7)

* 2020-10-14 Frank Gaede ([PR#127](https://github.com/iLCSoft/iLCInstall/pull/127))
  - fix cvmfs readme wrt. using singularity
         - using a dedicated home_dir on startup

* 2020-10-13 tmadlener ([PR#126](https://github.com/iLCSoft/iLCInstall/pull/126))
  - Add proper cvmfs repository for installing cvmfs in Docker image

* 2020-10-07 Remi Ete ([PR#125](https://github.com/iLCSoft/iLCInstall/pull/125))
  - Moved CVMFS user images in a separate directory
  - Added image for using iLCSoft in a centos 7 image by mounting CVMFS

* 2020-10-07 tmadlener ([PR#124](https://github.com/iLCSoft/iLCInstall/pull/124))
  - Add a few more packages in order to start installing things with spack inside the cvmfs installation container.

* 2020-10-06 Remi Ete ([PR#123](https://github.com/iLCSoft/iLCInstall/pull/123))
  - Added Dockerfile for CVMFS installation on centos7. 
   - Added complete Readme file with corresponding installation procedure

* 2020-09-10 Remi Ete ([PR#122](https://github.com/iLCSoft/iLCInstall/pull/122))
  - Provide Dockerfile for CVMFS installation based on SL6
  - Image and documentation available here: https://hub.docker.com/repository/docker/ilcsoft/ilcsoft-cvmfs-sl6
  - Run it with:
  ```shell
  docker run -it --privileged ilcsoft/ilcsoft-cvmfs-sl6
  ```

* 2020-09-04 Remi Ete ([PR#120](https://github.com/iLCSoft/iLCInstall/pull/120))
  - Upgraded MarlinReco version. 
  - Updated release notes for v02-02

# v02-02

* 2020-08-13 Frank Gaede ([PR#117](https://github.com/ilcsoft/ilcinstall/pull/117))
  - ilcsoft release v02-02
      - update LCIO to v02-15

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

