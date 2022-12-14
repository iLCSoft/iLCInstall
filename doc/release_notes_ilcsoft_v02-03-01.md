# iLCSoft v02-03-01

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

## External software versions upgrade
None

## New packages

None

## Packages changed wrt. v02-03

### LCIO v02-19

* 2022-12-11 Frank Gaede ([PR#158](https://github.com/iLCSoft/LCIO/pull/158))
  - add utility class `CheckCollections` that allows to parse lcio files for collections that are not present in every event and to patch such events with empty collections of the given (Name,Type) for further processing
  - add example tool `check_missing_cols` that checks for collections that are not in every event in a set of files and prints a summary to stdout:
       - `usage:  check_missing_cols <input-file1> [[input-file2],...]`
  - add example tool `patch_missing_cols` that creates a copy of the input file with the same set of collections in all events:
      -  ` usage:  patch_missing_cols <input-file> <output-file> ` 
  - these tools are needed in cases where code expects consistent sets of collections in every event, as for example in a conversion to `EDM4hep`

### LCIO v02-18

* 2022-11-08 Thomas Madlener ([PR#155](https://github.com/iLCSoft/LCIO/pull/155))
  - Add a previously missed function declaration to the .aid file to fix the java bindings. Fixes #154

* 2022-10-19 Thomas Madlener ([PR#153](https://github.com/iLCSoft/LCIO/pull/153))
  - Make c++17 the default and minimum c++ version for building LCIO. All "major builds" of LCIO have been using c++17 for at least a few years now, so this should not be a big issue.

* 2022-10-19 Thomas Madlener ([PR#152](https://github.com/iLCSoft/LCIO/pull/152))
  - Remove macOS workflow since github hosted runners no longer support all necessary features. See also: https://github.com/AIDASoft/run-lcg-view/pull/3
  - Update used github actions to latest available version for better caching behavior and cleaner log outputs
  - Switch to newer LCG releases for the build environments to target more recent compilers and python versions.
    - Keep one build environment that is close to the one used for the iLCSoft v02-02 to avoid accidental breaks.

* 2022-10-19 Bohdan Dudar ([PR#150](https://github.com/iLCSoft/LCIO/pull/150))
  - Added a utility function to calculate Track momentum based on its track parameters and magnetic field
  - Added methods to the LCRelationNavigator that extract the highest weight with an option to indicate weight encoding type ("track"/"cluster").
  - Added a utility function to get an index of a provided object inside a given LCCollection
  - Added a utility function to return a leading track from ReconstructedParticle in case it has multiple tracks attached.

### ILCUTIL v01-07

* 2022-12-02 Thomas Madlener ([PR#26](https://github.com/iLCSoft/ILCUTIL/pull/26))
  - Remove obsolete gcc8 based workflow and update github actions versions

* 2022-12-02 Thomas Madlener ([PR#25](https://github.com/iLCSoft/ILCUTIL/pull/25))
  - Disable `USE_CXX11` by default since we switched to c++17 quite some time ago and this option needs to be manually disabled in order to make that work via `CMAKE_CXX_STANDARD`.

### Marlin v01-19

* 2022-12-12 Frank Gaede ([PR#49](https://github.com/iLCSoft/Marlin/pull/49))
  - Add a simple processor `PatchCollections` that can patch missing collections in LCIO events by adding empty collections to these events
  -  needs https://github.com/iLCSoft/LCIO/pull/158

* 2022-12-09 Thomas Madlener ([PR#50](https://github.com/iLCSoft/Marlin/pull/50))
  - Add a CI workflow that runs on the latest key4hep nightly builds.

### Marlin v01-18

* 2022-11-23 Thomas Madlener ([PR#47](https://github.com/ilcsoft/Marlin/pull/47))
  - Add a `MarlinWrapperPrivateAccessor` class that allows the `MarlinProcessorWrapper` to access private methods by constructing such a class on the fly, when necessary.

* 2022-11-16 Thomas Madlener ([PR#48](https://github.com/ilcsoft/Marlin/pull/48))
  - Remove no longer working gcc8 based CI workflow and update github actions to latest available versions

* 2022-09-19 Bohdan Dudar ([PR#45](https://github.com/ilcsoft/Marlin/pull/45))
  - Fix #43, a bug where xml comment fields were processed as a legitimate values and shadowed any data that comes after the comment.

* 2022-09-15 Thomas Madlener ([PR#46](https://github.com/ilcsoft/Marlin/pull/46))
  - Migrate to github actions CI workflows and remove travis CI configuration

### MarlinUtil v01-17

* 2022-11-14 Thomas Madlener ([PR#35](https://github.com/iLCSoft/MarlinUtil/pull/35))
  - Remove the no longer supported gcc8 based CI workflow.

* 2022-10-20 Thomas Madlener ([PR#31](https://github.com/iLCSoft/MarlinUtil/pull/31))
  - Adding a basic Catch2 v3 based unittest setup that can be used to easily add unittests.
    - The CMake configuration allows to either build Catch2 on the fly or to discover a suitable installation of Catch2
  - Add the existing test and an example unittest to the test suit that can be run via `ctest` after building the package.
  - Disable building the tests for the coverity workflow for now to avoid polluting the output of that with Catch2 issues

* 2022-10-19 Thomas Madlener ([PR#33](https://github.com/iLCSoft/MarlinUtil/pull/33))
  - Make sure that `.ipp` files are also installed. Necessary since #30, fixes #32

* 2022-10-19 Thomas Madlener ([PR#30](https://github.com/iLCSoft/MarlinUtil/pull/30))
  - Introduce a `HelixClassT` template class and make `HelixClass` and `HellixClass_double` typedefs of this class, instead of having two separate (but practically identical) implementations that are in place currently.
    - Explicitly instantiate both versions that were in place previously to make sure things don't break downstream.
    - Mark getters as `const`

* 2022-09-19 Carl Mikael Berggren ([PR#28](https://github.com/iLCSoft/MarlinUtil/pull/28))
  The header-file has been re-organised and heavily
  commented - should work as a manual.
  
  Bug fix: a missing factor of two in propagateValErrors , the errors
  on the eigen-values (= the error on the estimated variances)
  
  New public methods:
  
  getElipsoid_r1 (_r2, _r3)
  getElipsoid_r1Error (_r2, _r3)
  getElipsoid_r_ave
  * getElipsoid_r_forw (_back)
  getElipsoid_vol
  getElipsoid_density
  getLongitudinalElipsis_eccentricity
  getTransverseElipsis_eccentricity
  * getMaxDist
  * getElipsoid_FractionInside
  
  Transformations:
  
  TransformPointToEigenSyst
  * TransformToEigenSyst
  * TransformAlongDirection (2 versions)
  
  (The ones with a * in front are only useful with Reco-input, since
   they need to have access to the CaloHits)
  getters of transformed properties:
  
  * get_x_trans (_y_, _z_)
  * get_COG_trans
  * get_COGCov_trans
  * get_th_ref
  * get_ph_ref
  * get_xyz_ref
  
  New private methods:
  
  findMaxDist
  findFirstAndLast
  findElipsoid_FractionInside
  
  Symbols defined: _one_sigma, _CL90, _CL95, _CL99

### MarlinTrkProcessors v02-12-02

* 2022-11-23 Thomas Madlener ([PR#62](https://github.com/iLCSoft/MarlinTrkProcessors/pull/62))
  - Make sure that the `_histos` pointer is at least initialized to a `nullptr` to avoid a spurious seg fault when trying to delete it uninitialized.

### KiTrackMarlin v01-13-02

* 2022-12-02 Thomas Madlener ([PR#8](https://github.com/iLCSoft/KiTrackMarlin/pull/8))
  - Remove the deprecate gcc8 based CI build, and update github actions to the latest available versions.

* 2022-12-02 Valentin Volkl ([PR#7](https://github.com/iLCSoft/KiTrackMarlin/pull/7))
  - cmake: exclude Linux-only "Timer" to fix build on macos

### MarlinDD4hep v00-06-02

* 2022-12-02 Thomas Madlener ([PR#10](https://github.com/iLCSoft/MarlinDD4hep/pull/10))
  - Remove the obsolete gcc8 based workflow and update github actions to latest available versions.

* 2022-12-02 Bohdan Dudar ([PR#9](https://github.com/iLCSoft/MarlinDD4hep/pull/9))
  - Verbosity levels now correspondingly control DD4hep printouts

### MarlinReco v01-33-01

* 2022-12-06 Thomas Madlener ([PR#107](https://github.com/ilcsoft/MarlinReco/pull/107))
  - Remove no longer available CI workflow based on gcc8 since the underlying nightly builds are no longer available
  - Update github actions to latest available versions

* 2022-12-06 Bohdan Dudar ([PR#106](https://github.com/ilcsoft/MarlinReco/pull/106))
  - Fix a seg. fault, in rare cases, when the track fit fails in both directions due to the lack of hits.

### lcgeo v00-18

* 2022-12-02 Daniel Jeans ([PR#261](https://github.com/ilcsoft/lcgeo/pull/261))
  - bug fix: no longer carry over energy to next event (sometimes affected lowpt hits)
  - address one FIXME: create highpt hits even if steps have not passed the padrow centre
  - some slight code cleanup and reorganisation to hopefully make it clearer to read

* 2022-11-07 Thomas Madlener ([PR#260](https://github.com/ilcsoft/lcgeo/pull/260))
  - Remove gcc8 based workflow because the underlying nightly builds are no longer available
  - Update github actions to latest available versions.

* 2022-11-07 Daniel Jeans ([PR#250](https://github.com/ilcsoft/lcgeo/pull/250))
  - ILD_l5[_o1,2,3,4]_v09 models with CLIC-inspired all silicon outer tracker in place of TPC+SET
  - otherwise identical to ILD_l5_v02 model

### ILDPerformance v01-11

* 2022-12-09 Ulrich Einhaus ([PR#38](https://github.com/iLCSoft/ILDPerformance/pull/38))
  add option to use RecoMCTruthLink instead of Trak2MCTruthLink
    add plots and fits for angular correction and Bethe-Bloch reference curve for LikelihoodPIDProcessor
    add command line output and text file output of above fit results for calibration

* 2022-11-14 Thomas Madlener ([PR#37](https://github.com/iLCSoft/ILDPerformance/pull/37))
  - Update CI to latest working nightly builds and use the same actions as everywhere else.

* 2022-11-14 Zehvogel ([PR#36](https://github.com/iLCSoft/ILDPerformance/pull/36))
  - fixed memory leak in PIDTree.cc

### podio v00-16-01

* 2022-12-06 jmcarcell ([PR#356](https://github.com/AIDASoft/podio/pull/356))
  - Fix path in the README
  - Use the functionality in argparse to choose between options

* 2022-12-06 Benedikt Hegner ([PR#346](https://github.com/AIDASoft/podio/pull/346))
  - Switched tp Apache 2.0 license to facilitate integration in experiment stacks.

* 2022-12-05 Thomas Madlener ([PR#357](https://github.com/AIDASoft/podio/pull/357))
  - Put `<prefix>/bin` onto `PATH` in order to make `podio-dump` available from environments created with `env.sh`

* 2022-12-02 jmcarcell ([PR#354](https://github.com/AIDASoft/podio/pull/354))
  - Make `env.sh` setup script POSIX compliant to run in shells other than bash
    - Change `==` to `=`
    - Change tabs to spaces (two) to avoid mix of spaces and tabs for indenting
    - Add `<prefix>/include` to `ROOT_INCLUDE_PATH` (as it is required since #343)

* 2022-11-16 Thomas Madlener ([PR#351](https://github.com/AIDASoft/podio/pull/351))
  -  Fix bug in Frame python bindings where empty collections were considered as non-existing. Replacing the original check relying on some implicit boolean conversions (which also caught empty collections) to an explicit check against `nullptr`.
  - Make `podio-dump` more robust in installations without SIO support, by guarding the corresponding import.

* 2022-11-14 Thomas Madlener ([PR#344](https://github.com/AIDASoft/podio/pull/344))
  - Make `podio-dump` work with new Frame based I/O (fixes #339)
  - Keep existing functionality intact by using the legacy readers introduced in #345.

* 2022-11-11 Thomas Madlener ([PR#345](https://github.com/AIDASoft/podio/pull/345))
  - Add a `ROOTLegacyReader` and a `SIOLegacyReader` that read files that have been written prior to #287 into `podio::Frame`s and offers the same interface as the frame readers
    - Also including python bindings for it

* 2022-11-10 Thomas Madlener ([PR#349](https://github.com/AIDASoft/podio/pull/349))
  - Fix bug in setting relations in nested get calls in `podio::Frame`. Fixes #348 
  - Adapt the read test to actually check this. Previously this went unnoticed, because the necessary relations were already set in a previous call.

* 2022-11-10 Thomas Madlener ([PR#343](https://github.com/AIDASoft/podio/pull/343))
  - Add python bindings for `Frame` based I/O
    - Available from `podio.root_io` and `podio.sio_io`, where a `Reader` and a `Writer` is implemented for each.
    - Wrapper around `podio::Frame`. **Requires that the `podio/Frame.h` header is available somewhere on the `ROOT_INCLUDE_PATH`**.
  - Add necessary functionality for python bindings to C++ API
    - untyped `Frame::get` method for getting collections
    - New constructor from `FrameDataT&&`
    - functionality to inspect file and `Frame` contents more easily
  - Reorganize python code into structure that follows the usual python packaging conventions a bit more closely
    - Introduce the `podio` module. Make CMake generate the `__init__.py` with the correct version
    - Move everything except the generator script into `module`. Additionally also keep an `EventStore` wrapper to not break existing code. 
  - Refactor the `CMakeLists.txt` that is responsible for building the core and all required I/O libraries
    - Build more dictionaries for more python bindings.

* 2022-11-02 Thomas Madlener ([PR#342](https://github.com/AIDASoft/podio/pull/342))
  - Migrate to `actions/checkout@v3` as advised by [github](https://github.blog/changelog/2022-09-22-github-actions-all-actions-will-begin-running-on-node16-instead-of-node12/)
  - Use the checkout action to clone the dependencies in the edm4hep workflow instead of doing an explicit clone in the body of the action

* 2022-11-02 Dmitry Kalinkin ([PR#327](https://github.com/AIDASoft/podio/pull/327))
  - fix typo in documentation

* 2022-10-24 Juraj Smiesko ([PR#340](https://github.com/AIDASoft/podio/pull/340))
  - Adding reading of specific entry from frame

* 2022-10-21 Thomas Madlener ([PR#335](https://github.com/AIDASoft/podio/pull/335))
  - Update the `github-action-cvmfs` and `run-lcg-view` actions to their latest available version to pick up the latest improvements (caching of dependencies, log groups)
  - Introduce log groups in github actions for easier to interpret outputs
  - Switch to LCG_102 for lcg based build environments
  - Add a workflow that builds and tests EDM4hep after building podio
  
### EDM4hep v00-07-02

* 2022-11-29 Thomas Madlener ([PR#186](https://github.com/key4hep/EDM4hep/pull/186))
  - Use agreed upon spelling of lower case "hep" on doxygen ref page header.

* 2022-11-15 Thomas Madlener ([PR#185](https://github.com/key4hep/EDM4hep/pull/185))
  - Only build JSON support if a suitable version of nlohmann/json is found. This should fix a few issues in CI.
  - Fix formatting of `edm4hep2json`.
  - Update versions of github actions used in CI to latest available.
