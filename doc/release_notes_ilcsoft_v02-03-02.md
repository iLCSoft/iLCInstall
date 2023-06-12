# iLCSoft v02-03-02

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

## External software versions upgrade
- DD4hep 01-20-02 :arrow_right: 01-25-0
- ROOT 6.24/06 :arrow_right: 6.28/04
- Geant4 11.0.2 :arrow_right: 11.1.1

## New packages

None



## Packages changed wrt. v02-03-01

### iLCUtil
- [ ] TODO: merge open PR, tag

### MarlinReco
- [ ] TODO: merge open PRs, tag

### podio
- [ ] TODO: add lates tag (potentially make a new tag before)

### EDM4hep
- [ ] TODO: add latest tag

### LCIO v02-20
* 2023-05-30 Andre Sailer ([PR#168](https://github.com/iLCSoft/LCIO/pull/168))
  - Pregenerated Headers: remove self-include from some headers (breaks include-what-you-use)
  - LCIterator, LCRTRelations: remove template syntax causing errors in gcc13/c++20
  - RunEvent, LCObject, TrackStateImpl: added default copy and move constructor and assignment operator to avoid error about "'definition of implicit copy constructor for 'LCObject' is deprecated because it has a user-declared destructor'"

* 2023-05-12 tmadlener ([PR#167](https://github.com/iLCSoft/LCIO/pull/167))
  - Fix checking of collection types to make sure patching works correctly

* 2023-05-03 Thomas Madlener ([PR#166](https://github.com/iLCSoft/LCIO/pull/166))
  - Upgrade `python-lint` workflow to run on `ubuntu-lates` since `ubuntu-18.04` runners have been removed.

* 2023-05-03 Finn Johannsen ([PR#165](https://github.com/iLCSoft/LCIO/pull/165))
  - Fixes to the on the fly collection patching that are necessary for the LCIO to EDM4hep standalone conversion.
    - Make `CheckCollections` check the `FromType` and `ToType` collection parameters to figure out the involved types for `LCRelations`. Add them to the output of `CheckCollections::print`
    - Make the `CheckCollectoins::patchCollections` parse these strings back for `LCRelation` collections and set them as collection parameters for collections it creates on the fly.
    - Add a `--minimal` flag to `check_missing_cols` in order to make it possible to produce outputs that can be more easily consumbed by other programs.

* 2023-05-03 Thomas Madlener ([PR#164](https://github.com/iLCSoft/LCIO/pull/164))
  - Add Key4hep release based CI workflow
  - Fix remaining warnings to enable `-Werror`
  - Update *checkout* action to v3, since v2 is deprecated. 
  - **CLHEP >= 2.0** is now required for building the examples that use CLHEP functionality (`test_fourvector`).

* 2023-02-10 jmcarcell ([PR#162](https://github.com/iLCSoft/LCIO/pull/162))
  - Add test dependencies so that tests can run in parallel

* 2023-02-10 jmcarcell ([PR#161](https://github.com/iLCSoft/LCIO/pull/161))
  - Remove the deprecated C API and fortran bindings (c.f. [#137](https://github.com/iLCSoft/LCIO/pull/137) and [#151](https://github.com/iLCSoft/LCIO/issues/151))

### LCIO v02-19-01
* 2023-02-06 Bohdan Dudar ([PR#163](https://github.com/iLCSoft/LCIO/pull/163))
  - `getRelatedTo(From)MaxWeightObject()` and `getRelatedTo(From)MaxWeight()` now accept generic decode function of `float(float)` signature as a second argument, which specifies how to decode the weight. Default option is identity function (just compares weights as they are).
  - Helper functions to decode and encode "track"/"cluster" specific weights from PFO-MCParticle LCRelation collection are added to MarlinUtil in [MarlinUtil#36](https://github.com/iLCSoft/MarlinUtil/pull/36).

* 2023-02-03 jmcarcell ([PR#160](https://github.com/iLCSoft/LCIO/pull/160))
  - Fix a compiler warning about `strncpy` usage
  
### k4geo (lecgeo) v00-18-01

* 2023-05-26 jmcarcell ([PR#274](https://github.com/key4hep/k4geo/pull/274))
  - Change eps_min to .001 in the example steering file

* 2023-04-10 Frank Gaede ([PR#266](https://github.com/key4hep/k4geo/pull/266))
  -  add definitions of regions to the SEcal06_hybrid barrel and endcap models of ILD:
       - `EcalBarrelRegion` and `EcalEndcapRegion`
       - these can be used for fast simulation (ML generation)

* 2023-01-13 Daniel Jeans ([PR#263](https://github.com/key4hep/k4geo/pull/263))
  - deal with case when previousStep is not yet defined (could cause crash)
  - add timing information to the lowPt hits
 
### MarlinUtil v01-17-01

* 2023-05-30 Andre Sailer ([PR#40](https://github.com/iLCSoft/MarlinUtil/pull/40))
  - CMake: make sure DD4hep include directories come first

* 2023-05-30 tmadlener ([PR#38](https://github.com/iLCSoft/MarlinUtil/pull/38))
  - Add a CI workflow based on the Key4hep release and nightly builds

* 2023-05-30 Bohdan Dudar ([PR#37](https://github.com/iLCSoft/MarlinUtil/pull/37))
  - Added `DD4hep::DDRec` library as a dependency to avoid undefined reference symbol errors using `dd4hep::rec` features. Fixes #26

* 2023-02-06 Bohdan Dudar ([PR#36](https://github.com/iLCSoft/MarlinUtil/pull/36))
  - Add function to extract decoded Track and Cluster weights from encoded LCRelation collection for PFO/MCParticles.
  - Add comparator functions for these weights encodings

### RAIDA v01-10

* 2023-04-18 tmadlener ([PR#5](https://github.com/iLCSoft/RAIDA/pull/5))
  - Migrate CI to github actions and remove travis-CI based configuration.

* 2023-04-18 jmcarcell ([PR#4](https://github.com/iLCSoft/RAIDA/pull/4))
  - Link only against the ROOT libraries that are necessary to avoid downstream linker problems.

### ConformalTracking v01-11-01

* 2023-05-25 Andre Sailer ([PR#60](https://github.com/iLCSoft/ConformalTracking/pull/60))
  - ParameterParser: fix linking issue with recent versions of boost
  - ParameterParser: move to non-deprecated header file location
  
### MarlinTrkProcessors v02-12-03

* 2022-12-02 Thomas Madlener ([PR#64](https://github.com/iLCSoft/MarlinTrkProcessors/pull/64))
  - Remove the obsolote gcc8 based workflow and update github actions to the latest versions

### Overlay v00-23

* 2023-05-02 tmadlener ([PR#27](https://github.com/iLCSoft/Overlay/pull/27))
  - Remove no longer available gcc8 based workflow from CI
  - Update github actions to latest available versions

* 2023-05-02 scott snyder ([PR#26](https://github.com/iLCSoft/Overlay/pull/26))
  - OverlayTiming,OverlayTimingGeneric: Added property Start_Integration_Time to allow changing the starting integration time.  This defaults to the previously hardcoded value of -0.25, but may need to be moved earlier if vertex smearing is enabled.
