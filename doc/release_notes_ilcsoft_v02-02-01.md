# iLCSoft v02-02-01

Production release for large 250 GeV production of ILD.
Various updates and bug fixes for the 250 GeV production of ILD.

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. to v02-02:

# Overlay v00-22-02

* 2021-03-01 tmadlener ([PR#22](https://github.com/iLCSoft/Overlay/pull/22))
  - Migrate CI to github actions

* 2021-03-01 hegarcia ([PR#21](https://github.com/iLCSoft/Overlay/pull/21))
  - fix for merging SimCalorimeterHits in Merger.cc
        - Adding length and position to the MC Contributions for use in the SDHCALDigi.

# Overlay v00-22-01

* 2020-07-09 Placido Fernandez Declara ([PR#20](https://github.com/iLCSoft/Overlay/pull/20))
  - OverlayTiming/OverlayTimingGeneric: Fixed accessing empty file name for background file
  
# MarlinReco v01-30

* 2021-03-03 Remi Ete ([PR#83](https://github.com/iLCSoft/MarlinReco/pull/83))
  - RealisticCaloDigi: Added new option for energy/charge and time integration
    - deal with slow/fast shaper of ROC chips and time estimate
    - new processor parameters:
       - **integrationMethod**: "Standard" for old implementation (default) or "ROC" emulating the behavior of ROC chip.
       - **fastShaper**: fast shaper time, unit in ns. Only for ROC method
       - **slowShaper**: slow shaper time, unit in ns. Only for ROC method
       - **timingResolution**: optional time resolution gaussian smearing to apply, unit . Only apply is > 0. Default is 0 (no smearing)

# MarlinReco v01-29

* 2021-02-26 Bohdan Dudar ([PR#88](https://github.com/iLCSoft/MarlinReco/pull/88))
  - TOFEstimators processor: adding new algorithms to calculate the ToF, track length and momentum.
    - New output parameters:
      - TOFClosest --- based on the closest ECAL hit
      - TOFFastest --- based on the fastest ECAL hit
      - TOFCylFit --- extrapolated time from the ECAL hits within a cylinder of a shower core
      - TOFClosestFit --- extrapolated time from the ECAL hits closest to the linear continuation of the track inside the ECAL
      - FlightLength --- the helix track length based on the track parameters from the TrackState at the ECAL
      - MomAtCal --- the momentum based on the track parameters from the TrackState at the ECAL
    - New steering parameters:
      - ProcessorVersion --- changes output between the idr version (before this patch) and the dev (after this patch). Default: idr
      - CylRadius --- the radius within which to select hits for the TOFCylFit method. Default: 5 mm

* 2021-02-22 Carl Mikael Berggren ([PR#89](https://github.com/iLCSoft/MarlinReco/pull/89))
  **Heavily reworked version of TrueJet**

  From the outside, little has changed:
  New jet-type (6) for non-isr photon from the hard interaction.
  Does not require recoparticles (nor recomctruthlink), so also works
  on generator-output lcio-files.
  Boolean steering flag to indicate Whizard1 (GDE) or Whizard2 (LCC) input
  (false by default, i.e. input is Whizard2)

  Internally, heavily re-worked.

  - removed methods fix94 and fix_top
  - New method (stdhep_reader_bug_workaround) called if _whiz1 is true
  - New method - photon - added to treat the new jet type 6 (M.E. photon).
  - New boolean data-members _whiz1 (steering flag),  _higgs_to_glue_glue
  and _top_event (the latter two set at run-time event by event)
  - Handle the case if no reconstructed information (generator input).
  - In top events, define the initial colour-neutral as  the top
  - Default collectionnames changed to the mc2020 ones.

  **Changes and enhancemts to TrueJet_Parser and Use_TrueJet to go with new TrueJet**

  TrueJet_Parser.

  - added  MCPseen : LCIntExtension<MCPseen>, used to avoid
  double counting of *true* particles (decay-in-flight ...) for true-of-seen.

  - New methods: mcpjet, mcpicn,mcpfcn, recojet, recoicn and recofcn to
  returns the  corresponding jet, icn or fcn number of MCPs or PFOs.
  true_partics, to return the list of all mcps in a jet (reco_particle
  already existed).

  Use_TrueJet:

  - Gracefully handle case with no recoMCTruthLink.

  - Exercise the new methods in TrueJet_Parser.

* 2021-02-10 Yasser Radkhorrami ([PR#85](https://github.com/iLCSoft/MarlinReco/pull/85))
  Improved the `ErrorFlow` processor:
  1.  An option added to enable/disable confusion term in the jet energy error
  2. For scaling angular uncertainties of jets, CovMat of the jet is scaled by scaling factors (as processor parameters)
  3. So far, charged PFOs used to be identified by charge, so the energy of neutral PFOs with tracks was added to photons/neutral hadrons energy. Now, neutral PFOs are classified as charged PFO, since the energy and momentum are obtained from tracks.
  4. An option added to propagate confusion term to **all** covariance matrix elements.

  - New processor parameters:
        -   "EnableConfusionTerm", "Enable/disable confusion term to be added to covariance matrix"
        -   "CovMatFactorPhotons", "A correction factor to be multiplied to angular uncertainties of photons"
        -   "CovMatFactorNeutralHadrons", "A correction factor to be multiplied to angular uncertainties of Neutral Hadrons"
        -   "PropagateConfusion2Mom", "Enable/disable Propagating uncertainty due to confusion to the Momentum components/All CovMat elements"

* 2021-02-01 tmadlener ([PR#86](https://github.com/iLCSoft/MarlinReco/pull/86))
  - Migrate CI from travis to github actions

# ILDPerformance v01-09

* 2021-02-22 Kollassery Swathi Sasikumar ([PR#32](https://github.com/iLCSoft/ILDPerformance/pull/32))
  - Changes made in DDDiagnostics.cc and DDDiagnostics.h package to include the 2D plots for Tracking efficiency.
  - Two steering files are modified with different cuts as per the requirement for the 1D or 2D plots.

* 2021-02-02 tmadlener ([PR#31](https://github.com/iLCSoft/ILDPerformance/pull/31))
  - Migrate CI from travis to github actions.


# SIO v00-01

* 2021-02-08 tmadlener ([PR#15](https://github.com/iLCSoft/SIO/pull/15))
  - Export sio library as `SIO::sio` target for easier downstream usage. (For the moment `SIO_INCLUDE_DIR` and `SIO_LIBRARIES` are also still defined in a call to `find_package(SIO)` to keep some backwards compatibility).
  - Remove now obsolete cmake configuration by replacing it with more standard cmake approaches.
  - Bump minimum required cmake version to 3.12

* 2021-01-13 tmadlener ([PR#16](https://github.com/iLCSoft/SIO/pull/16))
  - Use github actions for CI and remove travis CI.

* 2021-01-05 Valentin Volkl ([PR#13](https://github.com/iLCSoft/SIO/pull/13))
  -  install cmake files under lib/cmake/SIO

# SIO v00-00-04

* 2020-11-23 Marko Petric ([PR#12](https://github.com/iLCSoft/SIO/pull/12))
  - Setup rpath for macOS and give optional flag for turning on rpath on other systems
  - Resolve correctly linker independently of OS and pass flags

* 2020-11-19 Remi Ete ([PR#11](https://github.com/iLCSoft/SIO/pull/11))
  - Fix clang warnings

# SIO v00-00-03

* 2020-10-28 Frank Gaede ([PR#4](https://github.com/ilcsoft/sio/pull/4))
  - set the default compression level to Z_DEFAULT_COMPRESSION (-1)
         - correct the documentation for `set_level()`

* 2020-09-30 tmadlener ([PR#5](https://github.com/ilcsoft/sio/pull/5))
  - Remove `sio-dump-detailed` and add a `--detailed` / `-d` flag to `sio-dump`. Slightly improve the output in case an error occurs.

* 2020-09-28 Remi Ete ([PR#8](https://github.com/ilcsoft/sio/pull/8))
  - Examples:
      - Turned example structure linked_list to normal pointer
      - Fixed buffer overflow issue
  - **Important for documentation: pointer relocation using smart pointers** (`std::shared_ptr<T>` and co) **is not supported**



# LCIO v02-16-01

* 2021-01-06 Remi Ete ([PR#129](https://github.com/iLCSoft/LCIO/pull/129))
  - Fixed skip record condition in Random Access Manager

# LCIO v02-16

* 2020-12-03 Marko Petric ([PR#127](https://github.com/ilcsoft/lcio/pull/127))
  - Fix Python3 compatibility issue with next method defined

* 2020-12-03 Frank Gaede ([PR#126](https://github.com/ilcsoft/lcio/pull/126))
  - no longer build the out-of-date lsh example

* 2020-12-03 Marko Petric ([PR#125](https://github.com/ilcsoft/lcio/pull/125))
  - Migrate CI to GitHub Actions

* 2020-12-03 Remi Ete ([PR#124](https://github.com/ilcsoft/lcio/pull/124))
  - Updated SIO sources to v00-00-04

* 2020-12-03 Frank Gaede ([PR#123](https://github.com/ilcsoft/lcio/pull/123))
  - fix some warning:
         - deprecated dynamic exception specifications in Exceptions
  - fix the build from generated C++ files

* 2020-12-03 Frank Gaede ([PR#122](https://github.com/ilcsoft/lcio/pull/122))
  - fix in `UTIL::ProcessFlag`
        - fixed const correctness and make the operator<<(ostream) inline

* 2020-11-25 Marko Petric ([PR#121](https://github.com/ilcsoft/lcio/pull/121))
  - Update compiler flag handling
  - Resolve which type of linker is used and assign proper linking flags
  - Improve RPATH handling on macOS and add flag `LCIO_SET_RPATH` default `ON`

* 2020-11-05 Frank Gaede ([PR#119](https://github.com/ilcsoft/lcio/pull/119))
  - make compatible w/ clang 12 (on MacOs)
      - remove const from map key in LCRTRelations
      - map keys are immutable anyways

* 2020-10-23 Frank Gaede ([PR#117](https://github.com/ilcsoft/lcio/pull/117))
  - fix delphes2lcio
         - replace GetEntriesFast w/ GetEntries
         - fixes #113

# LCIO v02-15-04

* 2020-10-14 Frank Gaede ([PR#115](https://github.com/ilcsoft/lcio/pull/115))
  - fix in `delphes2lcio` example
       - avoid NANs in jet 4-momenta by using zero mass hyptheses
       - NB: the mass is still set independently to the specified value (following PandoraPFA)

* 2020-09-02 Frank Gaede ([PR#111](https://github.com/ilcsoft/lcio/pull/111))
  - delphes2lcio: fix PDG in PID objects of neutral hadrons

* 2020-09-01 Frank Gaede ([PR#110](https://github.com/ilcsoft/lcio/pull/110))
  - delphes2lcio: add optional extra PFO collections
          - add by default BCalPFOs created from branch BCalPhotons

# LCIO v02-15-03

* 2020-08-26 Frank Gaede ([PR#108](https://github.com/ilcsoft/lcio/pull/108))
  - fix in UTIL::ProcessFlag::decodeMCTruthProcess
        - protection for events where nMCParticles < 10
  - fix also, independently in delphes2lcio

# LCIO v02-15-02

* 2020-08-19 Frank Gaede ([PR#107](https://github.com/ilcsoft/lcio/pull/107))
  - add optional event meta data in delphes2lcio
        - meta data like cross sections can be added via the configuration file
        - see [../examples/cpp/delphes2lcio/README.md](../examples/cpp/delphes2lcio/README.md) for details
