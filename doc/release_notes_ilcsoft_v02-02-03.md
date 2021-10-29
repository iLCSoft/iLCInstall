# iLCSoft v02-02-03

Production release for large 250 GeV production of ILD.
Various updates and bug fixes for the 250 GeV production of ILD

| :warning: IMPORTANT NOTE :warning: |
|:----------------------------------:|
| This patch release contains changes and fixes that affect the reconstruction. Most notably the time-of-flight estimators (TOFEstimators) and related particle identification have received some attention that makes them break backwards compatibility. **If you plan to produce private samples with this release be aware that you can most probably not use them in combination with the centrally produced 250 GeV samples.** (see below for details).|
| Since the ongoing 250 GeV production and the already produced samples are not affected by these changes we decided to release them in this patch release such that the community can profit from them. |

## External software version ugrades

## New packages

None

## Packages changed wrt. v02-02-02


# LCIO v02-17

* 2021-11-05 Frank Gaede ([PR#143](https://github.com/iLCSoft/LCIO/pull/143))
  - add support for storing double values in LCParameters
      - used in run, event and collection parameters
      - example 
  
  ```cpp
  	DoubleVec dv ;
  	dv.push_back( 1.111111111111111111111111111111111111111111111111 ) ;
  	dv.push_back( 2.222222222222222222222222222222222222222222222222 ) ;
  	dv.push_back( 3.333333333333333333333333333333333333333333333333 ) ;
  	evt->parameters().setValues( "SomeDoubleNumbers" , dv ) ;
  
  ```
  - should resolve [#138](https://github.com/iLCSoft/LCIO/issues/138)

* 2021-11-05 Bohdan Dudar ([PR#141](https://github.com/iLCSoft/LCIO/pull/141))
  - LCTrackerConf constructor now protected

* 2021-10-12 Thomas Madlener ([PR#137](https://github.com/iLCSoft/LCIO/pull/137))
  - Deprecate the C-API which is used by the fortran interface. However, since no one seems to be actively using that interface we introduce a deprecation warning for the C-API to see if that has any users outside of the internal fortran interface. **If you are seeing deprecation messages in your build outputs please let us know.**
  - Fix F77 tests and run them in the CI.
    - Degrade some compiler errors back to warnings for gcc10 as it has become more strict than previous versions.

* 2021-05-05 Thomas Madlener ([PR#136](https://github.com/iLCSoft/LCIO/pull/136))
  - Update the CI to use the cvmfs and lcg-view github actions for a more streamlined configuration. Fixes [#135](https://github.com/iLCSoft/LCIO/issues/135).
  - Make the python dictionary loading look on `LD_LIBRARY_PATH` first, before falling back to rely on the `LCIO` environment variable which has more assumptions built into it. Fixes [#134](https://github.com/iLCSoft/LCIO/issues/134)

* 2021-05-05 Andrii Verbytskyi ([PR#132](https://github.com/iLCSoft/LCIO/pull/132))
  - Replace hardcoded lib with CMAKE_INSTALL_LIBDIR when appropriate


# MarlinReco v01-32

* 2021-11-05 Bohdan Dudar ([PR#96](https://github.com/iLCSoft/MarlinReco/pull/96))
  - **Major upgrade of TOFEstimators with bug fixes and updates that are not backward compatible**
    - Track length calculation is significantly improved by refitting the track and iterating over the track states on each tracker hit
    - Fixed bugs with phi coordinate flip and wrong `abs()` instead of `std::abs()`
    - Output in the PIDHandler is changed to the minimal set of required three parameters for the PID (momentum, track length, TOF)
    - Input steering parameters adjusted
    - Removed TOFPlots processor. General clean up of the files and the code
    - Detailed documentation is added

* 2021-11-04 Thomas Madlener ([PR#101](https://github.com/iLCSoft/MarlinReco/pull/101))
  - Fix all warnings that are trivial to fix (i.e. where the fix is obvious without having to think about things). .
    - Make all Processors that have pointer members have deleted copy c'tors and assignment operators.
  - Fix a potential out ouf bounds access in `TrueJet`.
  
  **Thanks to Bohdan Dudar** (@dudarboh)

* 2021-11-01 Thomas Madlener ([PR#94](https://github.com/iLCSoft/MarlinReco/pull/94))
  - Make the IsolatedLeptonTagging processor always produce the expected output collections, even for empty input collections, i.e. if the inputs are empty:
    - the `OutputPFOsWithoutIsoLepCollection` will simply have the same content as the `InputPandoraPFOsCollection`
    -  the `OutputIsoLeptonsCollection` will be empty. 
  - On the other hand actually missing input collections will now no longer be handled as these point to a real problem (e.g. typo in the collection name). Fixes [#93](https://github.com/iLCSoft/MarlinReco/issues/93)

* 2021-09-29 Frank Gaede ([PR#98](https://github.com/iLCSoft/MarlinReco/pull/98))
  - apply the correct units for TPC parameters from DD4hep
       - fixes [#97](https://github.com/iLCSoft/MarlinReco/issues/97)
  -  apply correct units for VXD and SIT layers
       -   need cross check of efficiency for kink finding 
       -  (how could this have worked before ?)

* 2021-08-25 Andre Sailer ([PR#95](https://github.com/iLCSoft/MarlinReco/pull/95))
  - CI: build against LCG_99python2 gcc8 and LCG_100 gcc10, clang11


# MarlinTrk v02-09

* 2021-09-29 Bohdan Dudar ([PR#22](https://github.com/iLCSoft/MarlinTrk/pull/22))
  - Now checking for the intersection with the endcaps even if intersection with the barrel has been found. The closest track state to the last tracker hit is saved

* 2021-09-27 Thomas Madlener ([PR#23](https://github.com/iLCSoft/MarlinTrk/pull/23))
  - Migrate CI from travis to github actions.


# MarlinUtil v01-16-01

* 2021-09-29 Bohdan Dudar ([PR#23](https://github.com/iLCSoft/MarlinUtil/pull/23))
  - Add generic `MarlinUtil::getDetData` for getting DDRec detector extension data from dd4hep.
  - Add dedicated `getVXDData`, `getSITData`, `getFTDData`, `getTPCData`, `getSETData` in `MarlinUtil::ILD` namespace which return DDRec extensions of corresponding detector elements of the ILD detector.
  - Fix warnings about catching exceptions by value in `TrueJet_Parser`

* 2021-08-23 Andre Sailer ([PR#20](https://github.com/iLCSoft/MarlinUtil/pull/20))
  - CI: build against LCG_99python2 gcc8 and LCG_100 gcc10, clang11


# CEDViewer v01-19

* 2021-11-01 Thomas Madlener ([PR#19](https://github.com/iLCSoft/CEDViewer/pull/19))
  - Fix coverity CI workflow

* 2021-11-01 Bohdan Dudar ([PR#17](https://github.com/iLCSoft/CEDViewer/pull/17))
  - Fix position of the tracks displated by the DSTViewer (fixes [#16](https://github.com/iLCSoft/CEDViewer/issues/16))
  - Fix CEDViewer `Weff-c++` warnings

* 2021-10-29 Thomas Madlener ([PR#18](https://github.com/iLCSoft/CEDViewer/pull/18))
  - Migrate CI to github actions


# LCTuple v01-13

* 2021-08-24 Andre Sailer ([PR#12](https://github.com/iLCSoft/LCTuple/pull/12))
  - CI: build against LCG_99python2 gcc8 and LCG_100 gcc10, clang11

* 2021-08-02 Thomas Madlener ([PR#11](https://github.com/iLCSoft/LCTuple/pull/11))
  - Migrate CI to github actions and remove travis CI

* 2020-03-05 gianelle ([PR#9](https://github.com/iLCSoft/LCTuple/pull/9))
  - TrackerHitBranches: add branch to store the time of the tracker hits


# ConformalTracking v01-11

* 2021-09-27 Andre Sailer ([PR#59](https://github.com/iLCSoft/ConformalTracking/pull/59))
  - CI: Move to github actions


# MarlinTrkProcessors v02-12

* 2021-11-05 Bohdan Dudar ([PR#55](https://github.com/iLCSoft/MarlinTrkProcessors/pull/55))
  - Center of the SET strips is now properly in the middle of the sensor modules.
  - Removed unused `vertex_x`, `vertex_y`, `vertex_z` steering parameters.

* 2021-09-22 Nazar Bartosik ([PR#53](https://github.com/iLCSoft/MarlinTrkProcessors/pull/53))
  - Added time smearing to the DDPlanarDigiProcessor 
  - Introduced a time window for digitized hits in the DDPlanarDigiProcessor 
  - Introduced TOF compensation for digitized hits in the DDPlanarDigiProcessor

* 2021-09-02 Placido Fernandez Declara ([PR#49](https://github.com/iLCSoft/MarlinTrkProcessors/pull/49))
  - DDPlanarDigiProcessor:  Add setting of the fromType and toType parameters for the LCRelation collection between TrackerHit and SimTrackerHit

* 2021-08-23 Andre Sailer ([PR#51](https://github.com/iLCSoft/MarlinTrkProcessors/pull/51))
  - CI: build against LCG_99python2 gcc8 and LCG_100 gcc10, clang11

* 2020-06-02 Erica Brondolin ([PR#45](https://github.com/iLCSoft/MarlinTrkProcessors/pull/45))
  - ClonesAndSplitTracksFinder 
    - If mergeSplitTracks set to `true`, pairs of tracks above a minimum pT requirements are compared in terms of pt, theta and phi
    - For each pair of reconstructed tracks: calculate significance for each parameter, impose a cut on the significance for each parameter, remove possible common hits and sort them in r, fit the new merged track
    - Results show positive effect on both single muons and complex events, with no significant increase of the run time ([Link to the slides](https://indico.cern.ch/event/920887/))

* 2020-01-27 Erica Brondolin ([PR#44](https://github.com/iLCSoft/MarlinTrkProcessors/pull/44))
  - In case finaliseLCIOTrack fails in the RefitFinal, the track should not be saved


# Overlay v00-22-03

* 2021-08-27 Andre Sailer ([PR#24](https://github.com/iLCSoft/Overlay/pull/24))
  - CI: build against LCG_99pyhon2 gcc8 and LCG_100 gcc10, clang11

* 2021-08-02 Thomas Madlener ([PR#23](https://github.com/iLCSoft/Overlay/pull/23))
  - Add coverity scan workflow that runs daily


# DDMarlinPandora v00-12

* 2021-09-06 Placido Fernandez Declara ([PR#21](https://github.com/iLCSoft/DDMarlinPandora/pull/21))
  - DDCaloDigi: Add setting of the fromType and toType parameters for the LCRelation collection between CaloHit and SimCaloHit
  - DDSimpleMuonDigi: Add setting of the fromType and toType parameters for the LCRelation collection between CaloHit and SimCaloHit

* 2021-08-23 Andre Sailer ([PR#22](https://github.com/iLCSoft/DDMarlinPandora/pull/22))
  - CI: build against LCG_99python2 gcc8 and LCG_100 gcc10, clang11


# iLCUtil v01-06-02

* 2021-11-03 Thomas Madlener ([PR#22](https://github.com/iLCSoft/iLCUtil/pull/22))
  - Switch to the latest available nightlies in the CI workflows.
  - Remove travis-ci config

* 2021-08-16 Thomas Madlener ([PR#21](https://github.com/iLCSoft/iLCUtil/pull/21))
  - Add a working github actions based CI workflow.
  - Make it possible to use newer cmake versions for installing
    - Fix globbing for dependencies in streamlog doxygen generation, which broke with 3.17
    - Fix name mismatch warning in find_package calls for cmake > 3.17
    - Fix missing project warning in example
  - Bump the minimum required cmake version to 3.14
  - Make the INSTALL_DOC option from streamlog available from the top-level to make it possible to steer this from the outside


# lcgeo v00-16-07

* 2021-11-05 scott snyder ([PR#246](https://github.com/iLCSoft/lcgeo/pull/246))
  - Fixed XML comment syntax in SiD_o2_v03 XML files.

* 2021-09-01 Andre Sailer ([PR#247](https://github.com/iLCSoft/lcgeo/pull/247))
  - CI: Run against LCG_100, clang10, gcc10 and LCG_99python2 gcc8
  - CMake: restructure main CMake file, more use of targets
  - Remove requirement for Boost, wasn't actually used for some time (still needed by DD4hep)
  - GenericEndcapCalo: move setting of sensitive type because of error in SID simulation with newer ddsim

* 2020-09-21 Valentin Volkl ([PR#242](https://github.com/iLCSoft/lcgeo/pull/242))
  - Add standard cpp/dd4hep .gitignore

* 2020-09-18 vvolkl ([PR#244](https://github.com/iLCSoft/lcgeo/pull/244))
  - Fix print statement for python3 compatibiltiy

* 2020-05-25 Valentin Volkl ([PR#243](https://github.com/iLCSoft/lcgeo/pull/243))
  - Add INSTALL_COMPACT_FILES option (default: OFF) to copy compact files to install area


# LCFIPlus v00-10-01

* 2021-11-19 YONAMINE Ryo ([PR#61](https://github.com/lcfiplus/LCFIPlus/pull/61))
  - add dummy primary-vertex to avoid accessing null pointer unless actual one is found.

* 2020-12-09 Tomohiko Tanabe ([PR#54](https://github.com/lcfiplus/LCFIPlus/pull/54))
  - Fix typos in reading input values for the FlavorTag algorithm related to the number of VTX hits used for computing joint probabilities
