# iLCSoft v02-03-02

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

## External software versions upgrade
- DD4hep 01-20-02 :arrow_right: 01-25-01
- ROOT 6.24/06 :arrow_right: 6.28/04
- Geant4 11.0.2 :arrow_right: 11.1.1

## New packages

### k4EDM4hep2LcioConv (ilcsoft)
* [ ] TODO: tag
* [key4hep/k4EDM4hep2LcioConv](https://github.com/key4hep/k4EDM4hep2LcioConv)

## Packages changed wrt. v02-03-01

### MarlinReco v01-34

* 2023-07-07 tmadlener ([PR#124](https://github.com/iLCSoft/MarlinReco/pull/124))
  - Usage of new utility functionality requires a newer version of `MarlinUtil`

* 2023-07-07 yradkhorrami ([PR#123](https://github.com/iLCSoft/MarlinReco/pull/123))
  - Merge SLDCorrection to MarlinReco
  - First implementation of SLDCorrection: for the time being, done only on semi-leptonic decays of bottom hadrons in b-jets

* 2023-07-07 Leonhard Reichenbach ([PR#121](https://github.com/iLCSoft/MarlinReco/pull/121))
  - LeptonID: remove notebook output

* 2023-07-04 Ulrich Einhaus ([PR#118](https://github.com/iLCSoft/MarlinReco/pull/118))
  Comprehensive Particle Identification Processor: First beta version of CPID.
  Extracts PID-related observables from PFOs and combines them in a training model, which can be inferred afterwards to data.
  This release contains the initial version of the Marlin processor with an example steering file, the input algorithm generic class + manager along with a library of different input algorithms, corresponding to different PID observables, as well as the training model generic class + manager along with a library of predefined models for training and inference.
  The selection of algorithms and models is handled via the processor steering file.
  The managers allow to add new modules (algorithms and models), compile and use them via the steering file, without the necessity to touch any other files.
  ComprehensivePIDProcessor.h contains a ReadMe section with an explanation of all processor steering parameters.

* 2023-07-03 Bohdan Dudar ([PR#117](https://github.com/iLCSoft/MarlinReco/pull/117))
  - In case of the option to measure time-of-flight at the SET: now using raw (digitized strips) SET hits instead of simulated hits. It doesn't change anything now, but could become trouble in the future when proper time digitization is added.

* 2023-06-29 Leonhard Reichenbach ([PR#120](https://github.com/iLCSoft/MarlinReco/pull/120))
  - LeptonID: update weights

* 2023-06-13 tmadlener ([PR#115](https://github.com/iLCSoft/MarlinReco/pull/115))
  - Bump the minimal required cmake version to 3.12
  - Fix the order in which DD4hep and LCIO appear in the libraries to link against to make sure to not pick an inappropriate version from the underlying environment

* 2023-06-13 Leonhard Reichenbach ([PR#114](https://github.com/iLCSoft/MarlinReco/pull/114))
  - Added `LeptonIDProcessor` to identify electrons and muons in jets using boosted decision trees.

* 2023-06-12 tmadlener ([PR#116](https://github.com/iLCSoft/MarlinReco/pull/116))
  - Switch from `dd4hep::long64` to `dd4hep::CellID` to be compatible with DD4hep after [AIDASoft/DD4hep#1125](https://github.com/AIDASoft/DD4hep/pull/1125)

* 2023-06-07 Bohdan Dudar ([PR#113](https://github.com/iLCSoft/MarlinReco/pull/113))
  - Always use the first (before)  --> latest (now) curl in the track to get extrapolated track position at the calorimeter surface. This gives sometimes better estimate of the track position at the ECAL surface, especially for the tracks with large number of curls. Thus  new version gives better time of flight correction for the distance to the surface and thus TOF itself.
  - Minor style improvements

* 2023-06-07 Bohdan Dudar ([PR#112](https://github.com/iLCSoft/MarlinReco/pull/112))
  - Switch to the helix formula without Omega: $\ell_{i} = \frac{|z_{i+1} - z_{i}|}{|\tan{\lambda_{i}}|}\sqrt{1 +\tan^2{\lambda_{i}}}$. It shows the best performance so far.
  - Other bug fixes and consistency improvements.

* 2023-05-11 Julie Munch Torndal ([PR#110](https://github.com/iLCSoft/MarlinReco/pull/110))
  - Added `CheatedMCOverlayRemoval` processor to identify MC particles that are overlay and remove the corresponding PFOs from the collection. 
    - See under [`Analysis/OverlayRemoval/example/CheatedMCOverlayRemoval.xml`](https://github.com/iLCSoft/MarlinReco/blob/master/Analysis/OverlayRemoval/example/CheatedMCOverlayRemoval.xml) for how to run processor

* 2023-02-07 Bohdan Dudar ([PR#108](https://github.com/iLCSoft/MarlinReco/pull/108))
  - Make encoding RecoParticle relation weights more explicit with a new encode function in MarlinUtil
 

### podio v00-16-05

* 2023-05-23 tmadlener ([PR#420](https://github.com/AIDASoft/podio/pull/420))
  - Fix a version check inside the `ROOTReader` to avoid segmentation violations

* 2023-05-23 tmadlener ([PR#417](https://github.com/AIDASoft/podio/pull/417))
  - Fix an issue with reading multiple files via the `ROOTFrameReader` ([#411](https://github.com/AIDASoft/podio/issues/411))
    - Add documentation for API of opening file(s)
    - Add tests for reading multiple files

* 2023-05-22 tmadlener ([PR#418](https://github.com/AIDASoft/podio/pull/418))
  - Bring back the public templated `getMap` functionality for `podio::GenericParameters` as they are already used in DD4hep (see [AIDASoft/DD4hep#1112](https://github.com/AIDASoft/DD4hep/pull/1112)). 
    - Mark the existing `getXYZMap` as deprecated but keep them for a brief transition period.
    - These have been removed in [#415](https://github.com/AIDASoft/podio/pull/415).

* 2023-05-19 jmcarcell ([PR#416](https://github.com/AIDASoft/podio/pull/416))
  - Remove selection rules for classes that don't exist anymore

* 2023-05-15 jmcarcell ([PR#415](https://github.com/AIDASoft/podio/pull/415))
  - Remove the deprecated getters and setters from the generic parameters

* 2023-05-15 jmcarcell ([PR#410](https://github.com/AIDASoft/podio/pull/410))
  - Remove the square that is run when cmake runs

* 2023-05-09 tmadlener ([PR#414](https://github.com/AIDASoft/podio/pull/414))
  - Fix off-by-one error in `UserDataCollection::print` that caused the first element to be printed twice.

* 2023-05-09 Thomas Madlener ([PR#394](https://github.com/AIDASoft/podio/pull/394))
  - Introduce a `CollectionBufferFactory` that can create the necessary buffers from a collection type, a schema version and a subset collection flag.
    - Use this factory throughout all existing Readers
    - Remove `createBuffers` and `createSchemaEvolvableBuffers` from `podio::CollectionBase` interface
  - Make the minimum allowed `schema_version` 1 in the yaml definition files. Default to 1 if no `schema_version` is provided
  - Add a `schemaVersion` to the `DatamodelDefinition.h` header that is generated and that can be accessed via `{{ package_name }}::meta::schemaVersion`. Use this to propagate schema information to the necessary places.
  - Make `SIOBlocks` write the current schema version, such that on reading they can generate the appropriate buffers for the version on file.

* 2023-04-22 Christopher Dilks ([PR#408](https://github.com/AIDASoft/podio/pull/408))
  - fix type inconsistency between `Collection::size()` and index for const object accessors

* 2023-04-21 jmcarcell ([PR#387](https://github.com/AIDASoft/podio/pull/387))
  - Make sure that the dump model round trip tests work without `ENABLE_SIO`
  - Actually test the extension model dumping

* 2023-04-12 Thomas Madlener ([PR#400](https://github.com/AIDASoft/podio/pull/400))
  - Fix a bug in `SIOFrameData::getAvailableCollections` to also work with Frames where some of the collections have not been written and that could lead to a seg fault.
  - Add a test for this in c++ (previously only covered in python unittests of Frame).

* 2023-04-05 Thomas Madlener ([PR#399](https://github.com/AIDASoft/podio/pull/399))
  - Add `PODIO_ENABLE_SIO=1` to the public `target_compile_definitions` for `podioSioIO` so that all dependent targets automatically get it as well. This should make it easier to use SIO dependent features in dependencies. 
  - Consistently use a scope for `target_link_libraries` in tests.

* 2023-04-03 Paul Gessinger-Befurt ([PR#398](https://github.com/AIDASoft/podio/pull/398))
  - Do not reject building if ROOT was built with C++20 (instead of C++17).

* 2023-04-03 Thomas Madlener ([PR#397](https://github.com/AIDASoft/podio/pull/397))
  - Remove the `GENERATED` property from generated files in CMake to avoid inconsistent removal of headers and source files with the `clean` target. Fixes [#396](https://github.com/AIDASoft/podio/issues/396)

* 2023-03-15 Benedikt Hegner ([PR#341](https://github.com/AIDASoft/podio/pull/341))
  - Adding infrastructure for schema evolution
  - Added explicit version tracking to the metadata
  - Data model comparison tool w/ simple heuristics to identify potential omissions / mistakes (e.g. checking for the limits of the ROOT backend)
  - Changed handling of backwards compatibility for the collection info metadata

### EDM4hep v00-09

* 2023-05-03 Thomas Madlener ([PR#152](https://github.com/key4hep/EDM4hep/pull/152))
  - Add a `EDM4hepVersion.h` file that has the same basic structure and functionality as other Key4hep packages.

* 2023-05-02 jmcarcell ([PR#193](https://github.com/key4hep/EDM4hep/pull/193))
  - Add a configuration file for the new podio visualization tool

* 2023-04-28 jmcarcell ([PR#203](https://github.com/key4hep/EDM4hep/pull/203))
  - Remove root version check inside CMakeLists.txt

* 2023-04-26 jmcarcell ([PR#205](https://github.com/key4hep/EDM4hep/pull/205))
  - Add missing units to the comments

* 2023-04-23 Thomas Madlener ([PR#200](https://github.com/key4hep/EDM4hep/pull/200))
  - Add `schema_version` to YAML definition now that podio has limited support (see AIDASoft/podio#341)

### iLCUtil v01-07-01

* 2023-06-08 scott snyder ([PR#28](https://github.com/ilCSoft/iLCUtil/pull/28))
  - Fix a compilation warning in ILCTest.h.

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

### RAIDA v01-11

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

### ILDPerformance v01-12

* 2023-06-26 tmadlener ([PR#40](https://github.com/iLCSoft/ILDPerformance/pull/40))
  - Fix the CI workflow by making sure that the DD4hep headers appear early enough to have precedence over any headers that might be picked up from the underlying environment.
  - Add a workflow based on the key4hep nightly builds

* 2023-06-26 Ulrich Einhaus ([PR#39](https://github.com/iLCSoft/ILDPerformance/pull/39))
  New options:
  - lambda cut
  - PID algorithm for PDG MC-Reco plot
  - plot folder

