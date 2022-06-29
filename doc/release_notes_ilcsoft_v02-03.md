# iLCSoft v02-03

Development release after the 250 GeV production.

Main changes wrt. v02-02 production release:
- **Upgrade from python2 to python3**, this might break some of your python scripts if you have not made them compatible with both versions.
- Switch to gcc-10.3
- All external packages are used in their latest released version

The files produced with the v02-02 series can still be read and used with this developers release, but they are potentially not fully compatible with files that are produced with the new developers release. There have been some changes in the reconstruction that break full (physics) backwards compatibility, see below for more details.

## External software versions upgrade
- gcc: 8.2.0 :arrow_right: 10.3.0
- python: 2.7.16 :arrow_right: 3.8.6
- ROOT: 6.18/04 :arrow_right: 6.26/06
- Boost: 1.71.0 :arrow_right: 1.77.0
- Eigen: 3.3.7 :arrow_right: 3.4.0
- XercesC: 3.2.2 :arrow_right: 3.2.3
- Geant4: 10.04.p03 :arrow_right: 11.0.2
- GSL: 2.6 :arrow_right: 2.7
- CMake: 3.15.5 :arrow_right: 3.23.2
- CLHEP: 2.3.4.3 :arrow_right: 2.4.5.3
- MySQL: 5.0.45 :arrow_right: 10.4.20
- DD4hep: v01-11-02 :arrow_right: v01-20-02

## New packages

### podio v00-14-03 (ilcsoft)
* [AIDASoft/podio](https://github.com/AIDASoft/podio)

### EDM4hep v00-05 (ilcsoft)
* [key4hep/EDM4hep](https://github.com/key4hep/EDM4hep)

## Packages changed wrt. v02-02-03

### CED v01-09-04

* 2022-03-18 Thomas Madlener ([PR#10](https://github.com/iLCSoft/CED/pull/10))
  - Make sure to link against GLUT libraries

* 2022-03-18 Thomas Madlener ([PR#9](https://github.com/iLCSoft/CED/pull/9))
  - Migrate CI to github actions.

### MarlinFastJet v00-05-03

* 2022-06-29 Andre Sailer ([PR#21](https://github.com/iLCSoft/MarlinFastJet/pull/21))
  - FastJetUtil: fix memory leak in clusterJets function. Change signature of this function to include the clusterSequence, fixes #20 
  - FastJetProcessor: fix issue for kt algorithm ,fixes #15

* 2021-12-03 Thomas Madlener ([PR#18](https://github.com/iLCSoft/MarlinFastJet/pull/18))
  - Migrate CI to github actions.

* 2021-12-03 Frank Gaede ([PR#17](https://github.com/iLCSoft/MarlinFastJet/pull/17))
  - fix order of fastjet libraries at linking step - needed on Ubuntu systems
  -  fixes https://github.com/iLCSoft/iLCInstall/issues/128

* 2021-12-03 Frank Gaede ([PR#16](https://github.com/iLCSoft/MarlinFastJet/pull/16))
  - minor fix of source paths in cmake file (for newer cmake versions, eg. 3.17)

### MarlinReco v01-33

* 2022-04-19 Bohdan Dudar ([PR#104](https://github.com/iLCSoft/MarlinReco/pull/104))
  - Migrated track length and  mean harmonic momentum code from `TOFEstimators` into separate `TrackLengthProcessor` to save CPU computing time. 
  - **NOTE: If you have been using these processors outside of the standard reconstruction chain you will have to update your steering files** (see [iLCSoft/ILDConfig#133](https://github.com/iLCSoft/ILDConfig/pull/133) for the necessary changes)
  
### lcgeo v00-16-08

* 2022-06-14 Valentin Volkl ([PR#253](https://github.com/iLCSoft/lcgeo/pull/253))
  - Move SiD_o2_v04 beampipe constants to global list to fix an error in key4hep builds

* 2022-06-09 Dan Protopopescu ([PR#252](https://github.com/iLCSoft/lcgeo/pull/252))
  - Added SiD_o2_v04, which is an updated version of o2_v03, containing a few fixes, among which
      - correct size and position of ECal layer 0 via new driver ECalBarrel_o2_v04_geo.cpp
      - new beam pipe by Chris Potter
      - removed brass HCal option

* 2022-03-19 Valentin Volkl ([PR#251](https://github.com/iLCSoft/lcgeo/pull/251))
  - Fix more hyphens in xml comments

* 2022-03-09 Andre Sailer ([PR#249](https://github.com/iLCSoft/lcgeo/pull/249))
  - Rebrand LCGEO as Lepton Collider GEOmetry, Fix #248
 
### CEDViewer v01-19-01

* 2022-06-22 Thomas Madlener ([PR#23](https://github.com/iLCSoft/CEDViewer/pull/23))
  - Make sure that `ced2go` can be run without the `-n` argument even if `CED_HOST` is set. Fixes #21
  - Remove some compatibility code for python < 2.4

* 2022-03-11 Bohdan Dudar ([PR#20](https://github.com/iLCSoft/CEDViewer/pull/20))
  - Fix typo bug in the ced2go local host argument option

### KalTest v02-05-01

* 2022-06-27 Daniel Jeans ([PR#5](https://github.com/iLCSoft/KalTest/pull/5))
  - add missing factor 0.5 to density term of Bethe-Bloch parameterisation

* 2020-04-12 Frank Gaede ([PR#4](https://github.com/iLCSoft/KalTest/pull/4))
  - fix issue w/ c++17 
        - this caused KalTest to return a “filtered” state as its “smoothed” or “inverse-filtered” state
        - patch provided by K.Fujii
        
### DDKalTest v01-07

* 2022-06-24 Daniel Jeans ([PR#13](https://github.com/iLCSoft/DDKalTest/pull/13))
  - - add missing factor 0.5 to density term of Bethe-Bloch parameterisation

* 2022-06-17 Thomas Madlener ([PR#14](https://github.com/iLCSoft/DDKalTest/pull/14))
  - Make CI use github actions instead of travis-CI

### LCIO v02-17-01

* 2022-05-09 Thomas Madlener ([PR#146](https://github.com/iLCSoft/LCIO/pull/146))
  - Install all the necessary headers to make the python bindings work, even if the sources are removed after installation. Fixes #106
  
### MarlinKinfitProcessors v00-05

* 2022-06-28 Thomas Madlener ([PR#18](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/18))
  - Make doxygen cmake config work with newer cmakes (>= 3.17)

* 2022-05-17 JennyListDESY ([PR#17](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/17))
  - bug fix in ZHllqq5CFit for usage of fixed JER

* 2022-04-20 Jenny List ([PR#16](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/16))
  - preparations towards a MarlinKinfit tutorial:
      - fixing CMakeLists.txt to include MarlinUtil
      - adding an ee->ZH->llqq example with up-to-date ErrorFlow, based on work from Yasser Radkhorrami and Julie Torndal
  - example steering still assumes availability of two private processors, which are yet to be made available in a next step.

* 2022-04-04 Thomas Madlener ([PR#15](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/15))
  - Migrate CI to github actions and remove travis CI setup

### LCCD v01-05-01

* 2022-06-28 Thomas Madlener ([PR#5](https://github.com/iLCSoft/LCCD/pull/5))
  - Fix bug in coverity config to point to the right repo

* 2022-06-28 Thomas Madlener ([PR#4](https://github.com/iLCSoft/LCCD/pull/4))
  - Migrate CI to github actions and remove travis CI configuration

* 2022-06-28 Thomas Madlener ([PR#3](https://github.com/iLCSoft/LCCD/pull/3))
  - Replace the implicit globbing for the doxygen target with an explicit cmake glob expression in order for working documentation generation with cmake >= 3.17

* 2020-04-10 Frank Gaede ([PR#2](https://github.com/iLCSoft/LCCD/pull/2))
  - make compatible w/ c++17 for macos/clang
        - patch provided by K.Fujii

### GEAR v01-09-01

* 2022-06-28 Thomas Madlener ([PR#8](https://github.com/iLCSoft/GEAR/pull/8))
  - Fix cmake doxygen configuration to work with CMake >= 3.17

* 2022-06-28 Thomas Madlener ([PR#7](https://github.com/iLCSoft/GEAR/pull/7))
  - Migrate CI to use github actions and remove travis CI

* 2020-09-07 Valentin Volkl ([PR#6](https://github.com/iLCSoft/GEAR/pull/6))
  - put more tests under the scope of BUILD_TESTING. Also fixes a build issue with spack https://github.com/key4hep/k4-spack/pull/33
 
  
### LCTuple v01-14

* 2022-06-29 Kollassery Swathi Sasikumar ([PR#10](https://github.com/iLCSoft/LCTuple/pull/10))
  - Changed the names of parameter in the event header to the names that are used in MC2020

* 2022-06-28 Thomas Madlener ([PR#13](https://github.com/iLCSoft/LCTuple/pull/13))
  - Make doxygen cmake config work with newer cmake versions (>= 3.17)

### Physsim v00-04-02

* 2021-08-16 Valentin Volkl ([PR#1](https://github.com/iLCSoft/Physsim/pull/1))
  - Add explicit include for TString.h to avoid build failure with ROOT v6.24
  
### ILDConfig v02-03

* 2022-06-29 Gerald Grenier ([PR#131](https://github.com/iLCSoft/ILDConfig/pull/131))
  - Add Calibration files to be able to run standard Marlin reconstruction on ILD simulation with Videau geometry.
  - For this first pass, files are only link to current ILD option 2 model from hybrid TESLA geometry.
  - Verification that Marlin runs on both small and large ILD Videau geometry have been done.

* 2022-04-20 Bohdan Dudar ([PR#133](https://github.com/iLCSoft/ILDConfig/pull/133))
  - Added TrackLength processor in the HighLevelReco chain.

* 2022-03-14 Bohdan Dudar ([PR#132](https://github.com/iLCSoft/ILDConfig/pull/132))
  - All steering parameters of `TOFEstimators` are explicitly specified in the steering file w/o any modification to the behaviour


## CMake fixes and CI migrations
The following packages have received a bump in their version numbers due to same fix in the cmake configuration that has been applied to all of them. The fix was necessary to make the doxygen generation work with the newer CMake versions (>= 3.17). Additionally, some of these packages were not yet migrated to the github actions CI, which has also been done for these packages. Instead of repeating the same release notes over and over again, here we simply provide the links to the corresponding pull requests

* MarlinDD4hep v00-06-01
  - [PR#8](https://github.com/iLCSoft/MarlinDD4hep/pull/8) 
* MarlinUtil v01-16-02
  - [PR#27](https://github.com/iLCSoft/MarlinUtil/pull/27)
* MarlinTrk v02-09-01
  - [PR#24](https://github.com/iLCSoft/MarlinTrk/pull/24)
* MarlinTrkProcessors v02-12-02
  - [PR#61](https://github.com/iLCSoft/MarlinTrkProcessors/pull/61)
* MarlinKinfit v00-06-01
  - [PR#2](https://github.com/iLCSoft/MarlinKinfit/pull/2)
* Overlay v00-22-04
  - [PR#25](https://github.com/iLCSoft/Overlay/pull/25)
* KiTrackMarlin v01-13-01
  - [PR#6](https://github.com/iLCSoft/KiTrackMarlin/pull/6)
* ForwardTracing v01-14-01
  - [PR#14](https://github.com/iLCSoft/ForwardTracking/pull/14)
