# iLCSoft v02-03-01

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

## External software versions upgrade
- ROOT 6.28/04 :arrow_right: 6.30/04
- DD4hep 01-25-01 :arrow_right: 01-28
- Geant4 11.1.1 :arrow_right: 11.2.1
- CLHEP 2.4.6.4 :arrow_right: 2.4.7.1
- CMake 3.23.3 :arrow_right: 3.28.3
- boost 1.77.0 :arrow_right: 1.84.0
- FastJet 3.4.0 :arrow_right: 3.4.2
- FastJet Contrib 1.049 :arrow_right: 1.054

## New packages

None

## Packages changed wrt. v02-03-02

### LCIO v02-21

* 2024-01-15 Thomas Madlener ([PR#187](https://github.com/iLCSoft/LCIO/pull/187))
  - Switch to c++20 for the key4hep nightlies based CI

* 2024-01-11 tmadlener ([PR#184](https://github.com/iLCSoft/LCIO/pull/184))
  - Make sure that LCIO installations can be used in downstream projects if they are built with builtin SIO. Fixes https://github.com/iLCSoft/LCIO/issues/183
    - Add a test to make sure that this works as intended
  - Bump the minimum required version for SIO to v00-01 in order to have CMake targets available.

* 2023-12-15 jmcarcell ([PR#175](https://github.com/iLCSoft/LCIO/pull/175))
  - Bump the minimum CMake version to 3.14

* 2023-12-13 jmcarcell ([PR#178](https://github.com/iLCSoft/LCIO/pull/178))
  - Bump the SIO version to v00-02
  - Fix two compiler warnings with clang

* 2023-12-06 Andre Rummler ([PR#181](https://github.com/iLCSoft/LCIO/pull/181))
  - Replace the copy of SIO that is used for builtin SIO support with the necessary cmake configuration to fetch it on the fly via CMake's `FetchContent` as this simplifies the maintenance of the vendored version of SIO greatly. **This is a transparent change for users, as long as internet connection to fetch the SIO sources during building is available**
  
### Marlin v01-19-02

* 2024-02-16 tmadlener ([PR#55](https://github.com/iLCSoft/Marlin/pull/55))
  - Allow to have empty constant values in steering files and only throw if there really is no constant specified.
  
### MarlinReco  v01-35

* 2024-02-23 Ulrich Einhaus ([PR#130](https://github.com/iLCSoft/MarlinReco/pull/130))
  Minor changes in CPID:
  - allow for no automatic creation of root file or plots
  - if no output root file and no training then no intermediate TTree is filled
  - add efficiency numbers on additional confusion matrix plot
  - in TOF algorithm use mass² instead of beta
  
  LeptonID: Remove inheritance from EventModifier

* 2024-02-16 tmadlener ([PR#129](https://github.com/iLCSoft/MarlinReco/pull/129))
  - Populate the type information for the output relation collection in the `SimpleFCalDigi`
  - Fix some warnings there as well. (Fixes [#100](https://github.com/iLCSoft/MarlinReco/issues/100))

* 2024-02-12 tmadlener ([PR#128](https://github.com/iLCSoft/MarlinReco/pull/128))
  - Use the key4hep-build action for building against key4hep stacks
  - Switch to LCG_104 based clicdp nightlies for CI

* 2024-02-12 tmadlener ([PR#126](https://github.com/iLCSoft/MarlinReco/pull/126))
  - Make the KinkFinder always produce all output collections even if some of them are empty
  
### MarlinTrk v02-09-02

* 2024-03-08 tmadlener ([PR#27](https://github.com/iLCSoft/MarlinTrk/pull/27))
  - Update CI to latest clicdp nightlies and add key4hep based workflows

* 2024-03-08 Bohdan Dudar ([PR#26](https://github.com/iLCSoft/MarlinTrk/pull/26))
  - Set d0 and z0 of the TrackStateAtCalo always to 0 #25

  
### MarlinTrkProcessors v02-12-05

* 2024-02-16 tmadlener ([PR#69](https://github.com/iLCSoft/MarlinTrkProcessors/pull/69))
  - Use the `LCRelationNavigator` to create output relation collections with the necessary type information.
    - This is necessary for automatic conversion from LCIO to EDM4hep when used within the MarlinWrapper and Gaudi.

* 2024-02-16 tmadlener ([PR#68](https://github.com/iLCSoft/MarlinTrkProcessors/pull/68))
  - Switch to the `key4hep-build` github action for building against key4hep stacks
  - Update the clicdp nightlies based workflow to the latest available version of the nightlies
  
* 2023-06-12 tmadlener ([PR#66](https://github.com/iLCSoft/MarlinTrkProcessors/pull/66))
  - Switch from `dd4hep::long64` to the more appropriate `dd4hep::CellID` after [AIDASoft/DD4hep#1125](https://github.com/AIDASoft/DD4hep/pull/1125)
  - Update CI
    - Switch to latest versions of github actions
    - Remove gcc8 based workflows
    - Add key4hep based workflow
  - Remove unused and deprecated usage of `std::binary_function` 
  
### iLCUtil v01-07-02

* 2024-01-15 tmadlener ([PR#31](https://github.com/iLCSoft/iLCUtil/pull/31))
  - Move to LCG_104 based nightlies for clicdp workflow.
  - Add Key4hep based workflows

* 2024-01-15 jmcarcell ([PR#30](https://github.com/iLCSoft/iLCUtil/pull/30))
  - Check if the tests target exists before creating it

* 2023-07-17 jmcarcell ([PR#29](https://github.com/iLCSoft/iLCUtil/pull/29))
  - Don't make the uninstall target if it already exists
  
### GEAR v01-09-02

* 2024-01-15 tmadlener ([PR#12](https://github.com/iLCSoft/GEAR/pull/12))
  - Remove no longer working gcc8 based workflow
  - Update github actions versions
  - Add key4hep based workflow

* 2023-08-15 jmcarcell ([PR#13](https://github.com/iLCSoft/GEAR/pull/13))
  - Respect CMAKE_INSTALL_<dir>

* 2023-07-17 jmcarcell ([PR#11](https://github.com/iLCSoft/GEAR/pull/11))
  - Drop the CMake test target that is not doing anything

* 2023-07-17 jmcarcell ([PR#9](https://github.com/iLCSoft/GEAR/pull/9))
  - Fix build with docs ON
  
### Clupatra v01-03-01

* 2024-01-17 tmadlener ([PR#19](https://github.com/iLCSoft/Clupatra/pull/19))
  - Migrate to github actions for CI

* 2020-04-13 Frank Gaede ([PR#16](https://github.com/iLCSoft/Clupatra/pull/16))
  - make compatible w/ c++17 for macos/clang
        - patch provided by K.Fujii
  
### LCCD v01-05-02

* 2024-01-18 jmcarcell ([PR#10](https://github.com/iLCSoft/LCCD/pull/10))
  - Fix compiler warnings with clang about `using namespace` in headers and `throw()` being deprecated
  - Change to using `LCIO::lcio` instead of `${LCIO_LIBRARIES}`
  - Fix a couple of CMake warnings due to incomplete file names

* 2024-01-15 tmadlener ([PR#11](https://github.com/iLCSoft/LCCD/pull/11))
  - Switch clicdp nightlies workflow to existing release
  - Add key4hep based CI workflows

* 2023-08-16 tmadlener ([PR#9](https://github.com/iLCSoft/LCCD/pull/9))
  - Remove the no longer working gcc8 based workflow
  - Bump action versions

* 2023-08-16 jmcarcell ([PR#8](https://github.com/iLCSoft/LCCD/pull/8))
  - Fix compilation warnings

* 2023-08-15 jmcarcell ([PR#6](https://github.com/iLCSoft/LCCD/pull/6))
  - Remove the unneeded tests custom target

### LCFIVertex v00-09

* 2024-01-15 jmcarcell ([PR#9](https://github.com/iLCSoft/LCFIVertex/pull/9))
  - Fix compilation errors with C++20

* 2024-01-12 tmadlener ([PR#10](https://github.com/iLCSoft/LCFIVertex/pull/10))
  - Add github actions based CI and remove travis-ci configuration
    - Based on clic nightlies and key4hep nightlies.

* 2020-04-02 Marko Petric ([PR#8](https://github.com/iLCSoft/LCFIVertex/pull/8))
  - Fix linking of base library (needs `tinyxml`)

### SIO v00-02

* 2023-12-04 tmadlener ([PR#20](https://github.com/iLCSoft/SIO/pull/20))
  - Remove K&R style definitions in builtin zlib since they will no longer be supported by newer C standars.

* 2023-12-04 tmadlener ([PR#19](https://github.com/iLCSoft/SIO/pull/19))
  - Update CI to latest LCG stacks and compilers, fail on warnings

* 2023-12-04 tmadlener ([PR#18](https://github.com/iLCSoft/SIO/pull/18))
  - Remove a pessimizing `std::move`

* 2022-07-19 Valentin Volkl ([PR#17](https://github.com/iLCSoft/SIO/pull/17))
  - Tests: Make tests that require inputs depend on the ones that provide it
  
### ConformalTracking v01-12

* 2023-11-08 Leonhard Reichenbach ([PR#62](https://github.com/ilcsoft/ConformalTracking/pull/62))
  - Emit an error message and skip further steps when too many tracks are created instead of throwing a SkipEventException

### ForwardTracking v01-14-02

* 2023-06-12 tmadlener ([PR#15](https://github.com/iLCSoft/ForwardTracking/pull/15))
  -  Replace `dd4hep::long64` by more appropriate `dd4hep::CellID` after [AIDASoft/DD4hep#1125](https://github.com/AIDASoft/DD4hep/pull/1125)
  - Bump versions of github action versions
  - Add key4hep based CI workflow
  - Fix several compiler warnings

### MarlinUtil v01-17-02

* 2023-07-07 Leonhard Reichenbach ([PR#41](https://github.com/iLCSoft/MarlinUtil/pull/41))
  - HelixClass: cleanup includes
  
### lcgeo v00-20-00

* 2024-02-22 BrieucF ([PR#323](https://github.com/key4hep/k4geo/pull/323))
  - Increase IDEA test timeout

* 2024-02-21 Giovanni Marchiori ([PR#318](https://github.com/key4hep/k4geo/pull/318))
  * ALLEGRO: Update some xml config files

* 2024-02-16 Andre Sailer ([PR#320](https://github.com/key4hep/k4geo/pull/320))
  - CMake: Add shim for older LCIO versions that do not have LCIO::lcio yet
  - LinearSortingPolicy: adapt check for existing extension to silence error message from DD4hep

* 2024-02-09 Andre Sailer ([PR#317](https://github.com/key4hep/k4geo/pull/317))
  - ALLEGRO: EcalBarrel: fix the length of the Z extent for the calorimeter data extension for reconstruction

* 2024-02-06 BrieucF ([PR#315](https://github.com/key4hep/k4geo/pull/315))
  - [ALLEGRO_o1_v02] Replace the simplified drift chamber with the detailed one
  - [TESTS] Add a test for ALLEGRO_o1_v02
  - [ALLEGRO_o1_v02] File and variable renaming plus propagation of overlap fix to upstream and calibration xml's

* 2024-02-06 Juraj Smiesko ([PR#309](https://github.com/key4hep/k4geo/pull/309))
  - CMake: Add printing of "Found k4geo" message in downstream projects picking up k4geoConfig.cmake

* 2024-01-18 jmcarcell ([PR#310](https://github.com/key4hep/k4geo/pull/310))
  - Change LCIO::LCIO to LCIO::lcio. The target provided by LCIO is LCIO::lcio; DD4hep provides LCIO::LCIO so building without DD4hep and using LCIO::LCIO doesn't seem to work.

* 2024-01-09 Jana ([PR#308](https://github.com/key4hep/k4geo/pull/308))
  - fixing the overlaps in ALLEGRO Ecal barrel geometry by increasing the LAr bath volume.

* 2023-12-18 Swathi Sasikumar ([PR#312](https://github.com/key4hep/k4geo/pull/312))
  - CLD_o4_v05: The name of the inclined calorimeter was given as `EmCaloBarrelInclined` before. This is now changed to the latest naming convention as `ECalBarrel_NobleLiquid_InclinedTrapezoids_o1_v01`
  - ECalBarrel_NobleLiquid_InclinedTrapezoids_o1_v01: The units for cell sizes has been added to the CaloLayerData ensure that they are given correctly and not mistaken due to confusion in units. now they are represented in mm.

* 2023-12-14 BrieucF ([PR#307](https://github.com/key4hep/k4geo/pull/307))
  - Added DriftChamber_o1_v01, a first version of the detailed IDEA drift chamber to enable further technical developments (digitization, tracking, PFlow, ...)

* 2023-12-13 Giovanni Marchiori ([PR#304](https://github.com/key4hep/k4geo/pull/304))
  - Code changes related to k4geo migration of FCC segmentation classes and related utilities
  - Also moves HCal readout for Allegro from eta-based to theta-based
  - Basically a rebasing of https://github.com/key4hep/k4geo/pull/296 after https://github.com/key4hep/k4geo/pull/298 was merged

* 2023-12-12 BrieucF ([PR#311](https://github.com/key4hep/k4geo/pull/311))
  - Changed the sensitive detector type of the ALLEGO simplified drift chamber to be able to run with ddsim

  
### DDMarlinPandora v00-12-01

* 2024-02-19 tmadlener ([PR#25](https://github.com/iLCSoft/DDMarlinPandora/pull/25))
  - Remove calls setting default encoding strings that have no effect

* 2024-02-19 tmadlener ([PR#24](https://github.com/iLCSoft/DDMarlinPandora/pull/24))
  - Switch to latest clicdp nightlies based releases
  - Add a `key4hep-build` based workflow to build against Key4hep stacks.

### KalTest v02-05-02

* 2024-02-23 tmadlener ([PR#9](https://github.com/iLCSoft/KalTest/pull/9))
  - Update CI to run on latest clicdp nightlies and use the key4hep-build action

* 2022-12-02 Thomas Madlener ([PR#8](https://github.com/iLCSoft/KalTest/pull/8))
  - Migrate CI to github actions and remove obsolete travis CI configuration
  
### DDKalTest v01-07-01

* 2024-02-15 tmadlener ([PR#16](https://github.com/iLCSoft/DDKalTest/pull/16))
  - Maintain existing functionality without emitting spurious error messages with latest versions of DD4hep. See [AIDASoft/DD4hep#1229](https://github.com/AIDASoft/DD4hep/issues/1229) for more details and related PRs.

* 2024-02-15 tmadlener ([PR#15](https://github.com/iLCSoft/DDKalTest/pull/15))
  - Update clicdp nigthles based workflows to use latest clicdp nightlies
  - Add key4hep based workflows

### Physsim v00-05

* 2023-01-12 Thomas Madlener ([PR#2](https://github.com/iLCSoft/Physsim/pull/2))
  - Update CMake configuration to use the modern target based approach of propagating dependencies and making Physsim a package that can be easily found via `find_package(Physsim)`
  - Remove duplicated headers in `src` and use the ROOT CMake macro to generate dictionaries and build the library.
  - Make examples use this functionality and in this way make it build again via the canonical iLCSoft cmake build steps.
    - Add more detailed instructions to the README
  - Add github actions based CI and remove the travis-ci configuration.

### FCalClusterer v01-00-06
* 2023-07-04 Andre Sailer ([PR#72](https://github.com/FCALSW/FCalClusterer/pull/72))
  - MarlinLumiCalClusterer: if used with SimCalorimeterHitCollection as input, the CalorimeterHitCollection will always be created correctly and stored in the event.

* 2023-03-07 Andre Sailer ([PR#71](https://github.com/FCALSW/FCalClusterer/pull/71))
  - LumiCalReco: always write out collections, even if they are empty. Needed for EDM4hep compatibility, collections always have to be present

### podio v00-99 (v01-00 pre-release)

**This is a pre-release for the first stable release of podio.** We consider the file format as well as stable and also consider the base functionality to be in place. All additional functionality should be implementable on top of the existing file format as well as existing features. We will make a few smaller fixes and remove still existing deprecated functionality before we release v01-00 in the next few weeks.

Changes wrt v00-17-04

* 2024-02-06 tmadlener ([PR#554](https://github.com/AIDASoft/podio/pull/554))
  - Bring back `vector<Data>` and `vector<Component>` into the dictionaries to allow for better interoperability with RNTuple. 
    - See [#464](https://github.com/AIDASoft/podio/issues/464) for some related discussion.

* 2024-02-06 tmadlener ([PR#552](https://github.com/AIDASoft/podio/pull/552))
  - Introduce an `operator<` to the interface types to make it possible to use them in STL containers that require that (e.g. `std::map` and `std::set`).

* 2024-02-06 tmadlener ([PR#549](https://github.com/AIDASoft/podio/pull/549))
  - Rename `{ROOT,SIO}Frame{Reader,Writer}` to `{ROOT,SIO}{Reader,Writer}` since these names are now no longer taken by the deprecated `EventStore` based ones and Frame based I/O is the default now.
    - Keep the old names around as deprecated aliases to not break everything immediately. But **plan to remove the aliases for v1.0**.

* 2024-02-02 Mateusz Jakub Fila ([PR#550](https://github.com/AIDASoft/podio/pull/550))
  - Fixed typos in tests and interface template

* 2024-01-30 tmadlener ([PR#548](https://github.com/AIDASoft/podio/pull/548))
  - Remove an unnecessary usage of the `TClass` machinery inside the `RNTupleReader` as all the necessary information is also available from metadata that we carry around in any case.

* 2024-01-30 Graeme A Stewart ([PR#544](https://github.com/AIDASoft/podio/pull/544))
  Add CMake targets for running  black and flake8 on Python source files

* 2024-01-30 tmadlener ([PR#528](https://github.com/AIDASoft/podio/pull/528))
  - Use `black` to format all python source files
  - Add a pre-commit hook for running black in CI

* 2024-01-25 jmcarcell ([PR#541](https://github.com/AIDASoft/podio/pull/541))
  - Add tool to transform between TTrees and RNTuples

* 2024-01-24 jmcarcell ([PR#543](https://github.com/AIDASoft/podio/pull/543))
  - Change ROOTNTuple{Reader,Writer} to RNTuple{Reader,Writer}

* 2024-01-22 tmadlener ([PR#516](https://github.com/AIDASoft/podio/pull/516))
  - Add a new category of types that can be generated by podio: `interfaces`. These can be used to provide a type that can be initialized from several other datatypes and offers some common functionality. These interface types can be used in `OneToOneRelation`s and in `OneToManyRelation`s.
    - `interfaces` need to provide a list of types which they interface. Other types cannot be used with them.

* 2024-01-18 Mateusz Jakub Fila ([PR#542](https://github.com/AIDASoft/podio/pull/542))
  - Fixed typos in documentation and comments, updated .gitignore

* 2024-01-18 jmcarcell ([PR#540](https://github.com/AIDASoft/podio/pull/540))
  - Add a check for the C++ standard using `ROOT_CXX_STANDARD` that was introduced yesterday in ROOT (https://github.com/root-project/root/commit/d487a42b311c5d0c7544031e3071a388c488c429)

* 2024-01-16 jmcarcell ([PR#539](https://github.com/AIDASoft/podio/pull/539))
  - Fix crash when a writer is in the global namespace by adding a class that will manage all the writers and finish them before exiting

* 2024-01-16 jmcarcell ([PR#538](https://github.com/AIDASoft/podio/pull/538))
  - Use getAvailableCollections() instead of the deprecated .collections

* 2024-01-12 jmcarcell ([PR#536](https://github.com/AIDASoft/podio/pull/536))
  - Add a `getAvailableCollections` method in python that does the same thing as in C++

* 2023-12-19 tmadlener ([PR#535](https://github.com/AIDASoft/podio/pull/535))
  - Implement the suggestions from coverity to move in places where it is easily possible.
  - Fix a small resource leak in SIO.
  - Fix a small copy-paste error in test output (only triggered in case test fails)
  - Restore ostream state after altering it for formatting.

* 2023-12-19 tmadlener ([PR#534](https://github.com/AIDASoft/podio/pull/534))
  - Update the coverity workflow to use EL9

* 2023-12-18 Andre Sailer ([PR#533](https://github.com/AIDASoft/podio/pull/533))
  - rootUtils: include sstream, fixes build on macOS 12 / 13

* 2023-12-18 tmadlener ([PR#532](https://github.com/AIDASoft/podio/pull/532))
  - Remove some benchmark utilities that became unused with the removal of the `TimedReader` and `TimedWriter` classes in #485

* 2023-12-15 tmadlener ([PR#531](https://github.com/AIDASoft/podio/pull/531))
  - Remove the last few deprecated accessors from `GenericParameters`.
  
### EDM4hep v00-10-05 (several patch version jumps below)

* 2024-02-07 jmcarcell ([PR#264](https://github.com/key4hep/EDM4hep/pull/264))
  - Delete build workflow since we have another one for key4hep that covers builds for nightlies, releases and all the operating systems we support

* 2024-02-06 jmcarcell ([PR#263](https://github.com/key4hep/EDM4hep/pull/263))
  - Change ROOTFrame{Writer,Reader} to ROOT{Writer,Reader} following https://github.com/AIDASoft/podio/pull/549

* 2024-01-22 tmadlener ([PR#253](https://github.com/key4hep/EDM4hep/pull/253))
  - Fix she-bang in README links update script.

* 2024-01-12 Mateusz Jakub Fila ([PR#250](https://github.com/key4hep/EDM4hep/pull/250))
  - Fixed doxygen excluded files and path stripping

* 2024-01-08 Mateusz Jakub Fila ([PR#249](https://github.com/key4hep/EDM4hep/pull/249))
  - Fixed formatting of components table in readme
  
* 2024-01-08 Joe Osborn ([PR#248](https://github.com/key4hep/EDM4hep/pull/248))
  - Added a Vector4f object for use as a general 4 dimensional vector with members `x`, `y`, `z` and `t`. Fixes https://github.com/key4hep/EDM4hep/issues/245

* 2023-12-12 Mateusz Jakub Fila ([PR#244](https://github.com/key4hep/EDM4hep/pull/244))
  - Fixed typos and links in documentation and doxygen

* 2023-12-06 tmadlener ([PR#243](https://github.com/key4hep/EDM4hep/pull/243))
  - Make sure that tests also work in Ubuntu 20.04 environments by running catch test discovery in correct environment.

* 2023-12-05 jmcarcell ([PR#235](https://github.com/key4hep/EDM4hep/pull/235))
  - Use `FILE_SET` to install the headers in the top folder together with the library. This also adds them in the `BUILD_INTERFACE`, something that a simple `INSTALL` doesn't do.
  - Bump the CMake version of the LCG stacks
  - Simplify finding ROOT, don't do environment variable manipulation in CMake
  
* 2023-11-14 jmcarcell ([PR#240](https://github.com/key4hep/EDM4hep/pull/240))
  - Change EventHeader to EventHeaderName; we already have an EventHeaderCollection and its elements are called EventHeader (`edm4hep::EventHeader` more precisely)

* 2023-11-14 Leonhard Reichenbach ([PR#239](https://github.com/key4hep/EDM4hep/pull/239))
  - Add a constant for the default expected EventHeader name to be used by the converters and PodioInput
  
* 2023-11-01 jmcarcell ([PR#234](https://github.com/key4hep/EDM4hep/pull/234))
  - Add a constant for CellIDEncoding. Usage:
  
  ``` cpp
  #include "edm4hep/Constants.h"
  
  std::cout << edm4hep::CellIDEncoding << std::endl;
  ```

* 2023-11-01 Juraj Smiesko ([PR#227](https://github.com/key4hep/EDM4hep/pull/227))
  - edm4hep2json now converts all EDM4hep collections, associations and Podio user data
  - added ROOT legacy support for edm4hep2json

* 2023-09-13 jmcarcell ([PR#226](https://github.com/key4hep/EDM4hep/pull/226))
  - Rename the cmake executable or target `unittests` to `unittests_edm4hep`, to avoid possible collisions since the `unittests` name is relatively common

* 2023-09-11 Wouter Deconinck ([PR#225](https://github.com/key4hep/EDM4hep/pull/225))
  - Define schema_version at top level in yaml file

* 2023-09-11 tmadlener ([PR#224](https://github.com/key4hep/EDM4hep/pull/224))
  - Add `SKIP_CATCH_DISCOVERY` option to turn of `catch_discover_tests` which may not run in the right environment in older cmake versions.

* 2023-09-05 Andre Sailer ([PR#223](https://github.com/key4hep/EDM4hep/pull/223))
  - CI: use same lcg stacks as podio
  - Test: update to Catch2 3.4.0, same as in podio, and c++20 compatible

* 2023-09-05 jmcarcell ([PR#222](https://github.com/key4hep/EDM4hep/pull/222))
  - Remove init.sh

### k4EDM4hep2LcioConv v00-08-02 (selection from several version jumps since v00-05)

* 2024-02-07 tmadlener ([PR#50](https://github.com/key4hep/k4edm4hep2lcioconv/pull/50))
  - Make it possible to keep working with MCParticle momenta based on floats for now. See https://github.com/key4hep/EDM4hep/pull/266

* 2024-02-07 tmadlener ([PR#45](https://github.com/key4hep/k4edm4hep2lcioconv/pull/45))
  - Make the upcoming renaming of `TrackerHit` -> `TrackerHit3D` transparent

* 2024-02-07 jmcarcell ([PR#48](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/48))
  - Delete build workflow since we have another one for key4hep that covers builds for nightlies, releases and all the operating systems we support

* 2024-02-07 jmcarcell ([PR#47](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/47))
  - Change ROOTFrame{Writer,Reader} to ROOT{Writer,Reader} following Remove the Frame from the default readers and writers following https://github.com/AIDASoft/podio/pull/549

* 2024-02-07 jmcarcell ([PR#46](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/46))
  - Fix compiler warnings related to double - float that appear after https://github.com/key4hep/EDM4hep/pull/237
  - Switch to non-deprecated name for `ROOTWriter` (https://github.com/AIDASoft/podio/pull/549)

* 2023-11-30 tmadlener ([PR#42](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/42))
  - Add conversion of TrackerHitPlane from EDM4hep to LCIO.
    - NOTE: The covariance matrix is not set, because there is no public setter available to do so in LCIO.

* 2023-11-14 tmadlener ([PR#38](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/38))
  - Remove compatibility with all legacy versions of EDM4hep since #34 made the minimum version 0.10.1 in any case.

* 2023-11-08 jmcarcell ([PR#34](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/34))
  - Use the new `edm4hep::CellIDEncoding` for consistency. Needs https://github.com/key4hep/EDM4hep/pull/234

* 2023-11-06 tmadlener ([PR#36](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/36))
  - Make sure to convert the full content of `edm4hep::Clusters` to LCIO clusters, including `subdetectorEnergies` and the related calorimeter hits. Set the `contribution` 1.0 because that seems to be the only value in use.
  - Add tests that cover this part of the converter.

* 2023-10-19 jmcarcell ([PR#31](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/31))
  - Do not forward declare `podio::ObjectID` since this doesn't always build
  - Add a library alias for the `k4EDM4hep2LcioConv` target
  - Add `podio` to the list of required packages (it's already there in the spack recipe)

* 2023-10-05 tmadlener ([PR#29](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/29))
  - Add the existing EDM4hep to LCIO conversion tests from MarlinWrapper
  - Fix minor issues in conversion that were uncovered during this

* 2023-10-05 tmadlener ([PR#21](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/21))
  - Generalize the conversion functionality to make it possible to use "generic maps" (i.e. `vector<tuple<K, V>>` or a proper `map<K, V>`).
    - This makes most of the conversion a template (i.e. header) library.
    - Keep the current behavior by specifying suitable defaults for all the templates.
  - This is necessary to support the introduction of a shared global map in [key4hep/k4MarlinWrapper#147](https://github.com/key4hep/k4MarlinWrapper/pull/147)

* 2023-10-04 tmadlener ([PR#28](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/28))
  - Add test setup to run the standalone converter on ILD REC and DST files with a comparison between the original and the converted file afterwards
  - Make sure to check relations in converted objects
  - Fix a bug in the relation resolution of the ReconstructedParticle that was uncovered.
  - Make `RelWithDebInfo` the default build type.

* 2023-09-12 tmadlener ([PR#27](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/27))
  - Introduce the `EDM4hep2LCIOConv` namespace for the EDM4hep to LCIO conversion functionality to avoid polluting the global namespace with too many (rather generically named) symbols.
  - Define a `EDM4HEP2LCIOCONV_NAMESPACE` preprocessor "symbol" that allows downstream users to make for a slightly smoother transition.

* 2023-07-31 jmcarcell ([PR#26](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/26))
  - `CMAKE_PROJECT_NAME` to `PROJECT_NAME` since `CMAKE_PROJECT_NAME` is the name of the top-level project and `PROJECT_NAME` is the name of the current project.

* 2023-07-31 Thomas Madlener ([PR#25](https://github.com/key4hep/k4EDM4hep2LcioConv/pull/25))
  - Make an output message less confusing
