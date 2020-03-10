# iLCSoft v02-01

Developer release before 250 GeV production. 

Main upgrade is compiler version and switch to C++ 17 standard. 

All external packages have been upgraded to the latest available (see below for details).

## External software versions upgrade

- ROOT: 6.08.06, updated to 6.18.04
- Boost: 1.58.0, updated to 1.71.0
- Eigen: 3.2.9, updated to 3.3.7
- XercesC: 3.1.4, updated to 3.2.2
- Geant4: 10.03.p02, updated to 10.04.p03
- GSL: 2.1, updated to 2.6
- Qt: 4.7.4 (Qt4), updated to v5.13.1 (Qt5)
- CMake: 3.6.3, updated to 3.15.5

## New packages

### SIO v00-00-02 (base)

## Removed packages

### MarlinTPC

* Not compatible (yet) with C++17. Requires upgrade from TPC group (ongoing)

## Packages changed wrt. to v02-00-02:

### iLCUtil v01-06

* 2019-08-23 Andre Sailer ([PR#13](https://github.com/iLCSoft/iLCUtil/pull/13))
  - Pass CMAKE_CXX_STANDARD to externalproject_add to allow building packages with standards other than the compiler default or c++11

* 2018-05-08 Andre Sailer ([PR#11](https://github.com/iLCSoft/iLCUtil/pull/11))
  - MacroRootDict: fix constant re-creation of dictionary. ROOT_CINT is no longer creating *.h file but *_rdict.pcm, changing the expected output file will only recreate the dictionary when necessary
  
### CondDBMySQL_ILC-0-9-7

* 2019-11-24 Remi Ete ([PR#3](https://github.com/iLCSoft/CondDBMySQL/pull/3))
  - Removed dynamic exception specification for c++ 17

* 2019-02-08 Frank Gaede ([PR#1](https://github.com/iLCSoft/CondDBMySQL/pull/1))
  - minor fixes:
        - rm my_bool from MySQLTypes.h 
        - untrack auto generated file src/config.h

### CED v01-09-03

* 2017-07-26 Shaojun Lu ([PR#5](https://github.com/iLCSoft/CED/pull/5))
  - Fix RPATH for CVMFS (ilc.desy.de) installation
   - Do not add the system directory "/usr/lib64" into the executable files "glced" RPATH list, it will be able to find the right "libstdc++.so.6" from CERN CVMFS compiler with "LD_LIBRARY_PATH" setup.
   - It cannot have influence on sim/reco.

### Marlin v01-17

* 2019-09-04 Andre Sailer ([PR#36](https://github.com/iLCSoft/Marlin/pull/36))
  - Marlin::Processor: make setParameters and setName public functions
  - Marlin::EventSelector: moved to marlin namespace

* 2019-07-12 Remi Ete ([PR#35](https://github.com/iLCSoft/Marlin/pull/35))
  - LCIOOutputProcessor:
      - Added `CompressionLevel` processor parameter to set the compression level of the `LCWriter` instance

* 2019-03-27 Andre Sailer ([PR#34](https://github.com/iLCSoft/Marlin/pull/34))
  - XMLParser: Fix "random" crash during XML parsing. Depends on XML Steering file and memory runtime behaviour, when some freed memory is overwritten
    ```
     /Marlin/source/tinyxml/src/tinyxml.cc:377: const TiXmlNode* TiXmlNode::IterateChildren(const char*, const TiXmlNode*) const: Assertion `previous->parent == this' failed.
    ```
  - XMLParser: Fix "invalid read errors" reported by valgrind. Objects were removed before they were used again, which probably lead to the above mentioned crashs

* 2019-03-05 Andre Sailer ([PR#33](https://github.com/iLCSoft/Marlin/pull/33))
  - Marlin command line arguments: parameter names may now contain dots, solves lcfiplus/lcfiplus#3
  - LCTokenizer: add optional max parameter to limit the number of resulting tokens

* 2018-07-02 Andre Sailer ([PR#32](https://github.com/iLCSoft/Marlin/pull/32))
  - Make Doxygen documentation compatible with doxygen 1.8.8+

### DDMarlinPandora v00-11

* 2019-12-11 Ete Remi ([PR#19](https://github.com/iLCSoft/DDMarlinPandora/pull/19))
  - DDSimpleMuonDigi processor: 
     - added time computation
        - Sort MC contribution by time
        - Accumulate energy until the threshold is reached
        - Return the corresponding MC contribution time
     - added new parameter MuonTimeThreshold: the muon energy threshold for estimating the hit time

### MarlinUtil v01-15-01

* 2019-08-26 Andre Sailer ([PR#13](https://github.com/iLCSoft/MarlinUtil/pull/13))
  - MarlinUtilConfig: explicitly add DD4hep dependency so that dependent packages resolve the DD4hep::DDCore etc. libraries

* 2018-04-20 Erica Brondolin ([PR#11](https://github.com/iLCSoft/MarlinUtil/pull/11))
  - This PR is related to a detector issue discussed in: https://github.com/AIDASoft/DD4hep/issues/356
  Given that the return value of det.field().isValid() is always true for design, a different approach on the check of the geometry validity is applied.
  - This PR must be integrated with the following PR in AIDASoft/DD4hep: https://github.com/AIDASoft/DD4hep/pull/367

### MarlinReco v01-26

* 2019-12-11 Daniel Jeans ([PR#71](https://github.com/iLCSoft/MarlinReco/pull/71))
  - remove hard-coded default correction; control everything from processor parameters.
  - add getter and print functionality to PhotonCorrector class

* 2019-12-03 Daniel Jeans ([PR#70](https://github.com/iLCSoft/MarlinReco/pull/70))
  BruteForceEcalGapFiller makes new hits both within and between ECAL modules to estimate energy lost in cracks. In this update:
  - allow switching off of correction in gaps between modules by processor parameter (in fact, set it off by default)
  - Fix a couple of compiler warnings
  - add photonCorrectionProcessor to correct photon PFO energies

* 2019-10-06 Remi Ete ([PR#69](https://github.com/iLCSoft/MarlinReco/pull/69))
  - Replaced raw usage of streamlog by pre-processor macros from streamlog package

* 2019-09-03 beyerja ([PR#68](https://github.com/iLCSoft/MarlinReco/pull/68))
  - Remove compiler warnings for ErrorFlow processor (default initialization in header, using shared_ptr instead of raw pointer).
  - Add ErrorFlow processor to list of processors to be compiled by default in MarlinReco.

* 2019-08-12 Ete Remi ([PR#67](https://github.com/iLCSoft/MarlinReco/pull/67))
  - SimpleFcalDigi processor:
      - Missing cellid 1 flag in fcal output collection, causing issues in the BeamCal reconstruction

* 2019-04-08 Ete Remi ([PR#66](https://github.com/iLCSoft/MarlinReco/pull/66))
  - ReconstructedParticleImpl_CopyProcessor:
      - Added relation collection to link old PFOs to new PFOs

* 2019-03-29 Matthias Artur Weber ([PR#65](https://github.com/iLCSoft/MarlinReco/pull/65))
  - IsolatedLeptonFinder: save track and cluster information for isolated lepton candidates

* 2019-01-30 Carl Mikael Berggren ([PR#64](https://github.com/iLCSoft/MarlinReco/pull/64))
  - TrueJet: 
    - Much improved assignment of PFOs to jets, and hence of seen jet energies
    - Get rid of all -Wall warnings

* 2019-01-16 Carl Mikael Berggren ([PR#63](https://github.com/iLCSoft/MarlinReco/pull/63))
  - bug fix in TrueJet_Parser
        - fix in TrueJet_Parser::final_cn, replace math.h by cmath in Use_TrueJet

* 2019-01-15 Junping Tian ([PR#62](https://github.com/iLCSoft/MarlinReco/pull/62))
  - added fix to IsolatedLeptonfinder
       - added a new feature for supporting applications not using impact parameters
       - added corresponding weight files trained for the new feature

* 2018-12-19 Ulrich Einhaus ([PR#60](https://github.com/iLCSoft/MarlinReco/pull/60))
  - Add ReconstructedParticleImpl_CopyProcessor

* 2018-11-09 Daniel Jeans ([PR#59](https://github.com/iLCSoft/MarlinReco/pull/59))
  - add new Marlin processor DDStripSplitter, which implements the Strip Splitting Algorithm for eg a scintillator strip ECAL.

* 2018-10-29 Ete Remi ([PR#58](https://github.com/iLCSoft/MarlinReco/pull/58))
  - IsolatedLeptonTaggingProcessor processor:
     - Fixed processor logic when PFO or Vertex input collections don't exist or are empty

* 2018-10-19 Erica Brondolin ([PR#57](https://github.com/iLCSoft/MarlinReco/pull/57))
  - CLICPfoSelectorAnalysis: Fix entries of time vs pt

* 2018-10-02 Frank Gaede ([PR#55](https://github.com/iLCSoft/MarlinReco/pull/55))
  - add sub-package Analysis/GammaGammaHadronRemoval
    - first processor *TrackZVertexGrouping* implementation of track grouping based on Z0 significance
    - algorithm developed by S.Sasikumar, DESY

### PandoraPFANew v03-13-02

* See changes in https://github.com/PandoraPFA/PandoraPFA/blob/v03-13-02/ChangeLog.txt

### LCFIVertex v00-08

* 2019-10-07 Remi Ete ([PR#7](https://github.com/iLCSoft/LCFIVertex/pull/7))
  - Fixed usage of streamlog

* 2019-08-08 Frank Gaede ([PR#6](https://github.com/iLCSoft/LCFIVertex/pull/6))
  - make compatible w/ std=c++17
           - replace bool w/ char in histMaps
              as c++17 does not allow ++bool

#### CEDViewer v01-17

* 2018-11-06 Marko Petric ([PR#9](https://github.com/iLCSoft/CEDViewer/pull/9))
  - DDCEDViewer
    - Add option to color reconstructed particles by energy
      - the color range is from lowest blue to highest red, with possibility of the user to change brightens and saturation of the color pallet.
      - the color range can be fixed from a minimal energy to a maximal for all events or auto adopted event by event to span from min to max energy of a given/current event
    - Add option for scaling line thickness of helices and marker size, this is needed for good image dumps, since the displayed sizes differ from the ones in the dumped image

### Overlay v00-22

* 2019-10-07 Remi Ete ([PR#19](https://github.com/iLCSoft/Overlay/pull/19))
  - Fixed streamlog usage using pre-processor macro from streamlog
  - Fixed marlin includes inside `MARLIN_USE_AIDA` condition

* 2019-08-13 Frank Gaede ([PR#18](https://github.com/iLCSoft/Overlay/pull/18))
  - make compatible w/ c++17
      - replace std::random_shuffle w/ std::shuffle in OverlayTiming
      - use std::mt19937 rather than CLHEP::RandFlat

* 2019-05-27 Jenny List ([PR#17](https://github.com/iLCSoft/Overlay/pull/17))
  - modified `Merger::merge(LCCollection* , LCCollection* )` to be able to merge any type of collection. 
  - by default a collection is treated as tracker hits previously, namely a simple copy.

### MarlinFastJet v00-05-02

* 2019-02-19 Andre Sailer ([PR#13](https://github.com/iLCSoft/MarlinFastJet/pull/13))
  - FastJetUtil: fix memory leak when creating jetDefinition with plugin (SiSCone, Valencia), needs #12 
  - MarlinFastJet: remove support for FastJet version 2

* 2018-05-18 Lars Rickard Strom ([PR#10](https://github.com/iLCSoft/MarlinFastJet/pull/10))
  - Implemented substructure parameters commonly used for top tagging. The definition of these new variables can be adjusted from the steering file (added options to steer how to calculate the energy correlation function (energyCorrelator) and how to calculate NSubjettiness (axesMode and measureMode). Only recommended options are implemented. The beta parameter would typically be the same as used for jet clustering but can also be varied separately (beta weights the angular distances between the jet constituents compared to their pt in the calculation of the energy correlation function and subjettiness). 
  - The substructure variables are added to the file as a collection "TopTaggerSubStructure" of seven elements (order: C2, D2, C3, D3, tau1, tau2, tau3). 
  - This update is backwards compatible, with the only difference being the addition of this collection.

### LCTuple v01-12

* 2019-03-26 Ete Remi ([PR#7](https://github.com/iLCSoft/LCTuple/pull/7))
  - Jet branches: added individual particles collection indices to a new output branch `pfoori`
  - Fixed various warning, making this package warning free

* 2018-05-04 Frank Gaede ([PR#5](https://github.com/iLCSoft/LCTuple/pull/5))
  - add possibility to store arbitrary PID parameters for the ReconstructedParticle branch
      - parameter and branches need to be defined in  `PIDBranchDefinition` parameter of LCTuple
      - see [../example/lctupletof.xml](../example/lctupletof.xml) for details

### MarlinTrk v02-08

* 2019-08-23 Andre Sailer ([PR#16](https://github.com/iLCSoft/MarlinTrk/pull/16))
  - CMake: drop export of Lib dependencies, which doesn't work in cmake 3.12
  - CMake: fix CLHEP discovery, first find CLHEP then DD4hep (and implicitly geant4)

### KiTrack v01-10

* 2019-08-09 Frank Gaede ([PR#2](https://github.com/iLCSoft/KiTrack/pull/2))
  - make compatible w/ c++17
        - remove all throw() declarations
        - replace std::random_shuffle w/ std::shuffle<..., std::mt19937>

### KiTrackMarlin v01-13

* 2019-11-25 Remi Ete ([PR#5](https://github.com/iLCSoft/KiTrackMarlin/pull/5))
  - Remove dynamic exception specifier (c++17 compatibility)

### MarlinTrkProcessors v02-11

* 2019-08-21 Frank Gaede ([PR#43](https://github.com/iLCSoft/MarlinTrkProcessors/pull/43))
  - fix RefitProcessor:
         - do not drop tracks in RefitProcessor, even if the refit failed
         - ensures that the output collection has the same number of entries
            in the same order as the input collection
         - needed to identify and compare refitted tracks

* 2019-04-01 Emilia Leogrande ([PR#42](https://github.com/iLCSoft/MarlinTrkProcessors/pull/42))
  - RefitFinal: added processor parameter `MinClustersOnTrackAfterFit`
    - defines the minimum number of hits on track after the fit for the track to be accepted 
    - previously hard-coded = 3, but tracks with 3 hits are ~100% fakes
    - now implemented as in ConformalTracking ilcsoft/ConformalTracking#52

* 2019-03-20 Emilia Leogrande ([PR#41](https://github.com/iLCSoft/MarlinTrkProcessors/pull/41))
  ClonesAndSplitTracksFinder:
    - The clone treatment has been uniformized with the updated clone treatment in the seeding (conformal tracking)
    - In few cases it is just a matter of including the equal sign in the comparison
    - In few other cases, the combined length-chi2 check is replaced with a length check only: longer tracks always preferred

* 2019-02-18 Shaojun Lu ([PR#39](https://github.com/iLCSoft/MarlinTrkProcessors/pull/39))
  - Improved SiliconTracking_MarlinTrk - added two options:
       - to use simple updated triplets searching core bin,
       - to use simple "AttachHitToTrack" for merging split track segments.

* 2019-01-18 Frank Gaede ([PR#40](https://github.com/iLCSoft/MarlinTrkProcessors/pull/40))
  - fixed DDTPCDigiProcessor
      - fix B-field correction for the r-phi resolution
      - now use (4./B)^2 rather than 4./B

* 2018-04-23 Emilia Leogrande ([PR#38](https://github.com/iLCSoft/MarlinTrkProcessors/pull/38))
  - ClonesAndSplitTracksFinder: the check for toBeMerged was in the wrong place. Fixed.

* 2018-04-20 Emilia Leogrande ([PR#37](https://github.com/iLCSoft/MarlinTrkProcessors/pull/37))
  - ClonesAndSplitTracksFinder: added mergeSplitTracks parameter, that allows one to decide whether to run only the clones skimming or also the merging of split tracks
    - mergeSplitTracks = false by default
    - mergeSplitTracks = true would enable the treatment of split tracks, which is still work in progress

### ILDPerformance v01-07

* 2019-05-07 Ete Remi ([PR#28](https://github.com/iLCSoft/ILDPerformance/pull/28))
  - Added dEdX performance scripts
     - `dEdXAnalyzer` processor creates plots
     - Example steering file in `steer` directory
     - Binary `dEdxHistPlotter` to create fancy plots out of the root files produced by the processor
  - See Readme file for more information

* 2019-01-03 Jakob Beyer ([PR#27](https://github.com/iLCSoft/ILDPerformance/pull/27))
  - Add scripts to create TOF-separation plots for single particles (based on Sukees code), including config files for steering.
  - In WWZZSeparation: Remove legacy parameter in plotting script and save TH1s in plotting macro.

* 2018-11-06 Ete Remi ([PR#26](https://github.com/iLCSoft/ILDPerformance/pull/26))
  - Added `-n` option to include/exclude MC neutrino energy. 
  - Added b, c and t quarks to analysis

* 2018-10-01 Jakob Beyer ([PR#25](https://github.com/iLCSoft/ILDPerformance/pull/25))
  - Updated bash scripts, now also possible to run on already reconstructed files (DSTs).
  - Added vector boson mass lines to plots. 
  - Added another FastJet processor to the Marlin script to remove overlay which is included in new production.

### LCFIPlus v00-09

* 2020-01-29 Tomohiko Tanabe (dad78f754ee7d0db652e8b178101d3eae2b414d4)
  - Fixes bug in beam jet distance computation -- this fixed a bug introduced in 2015. The fix gives ~1% better dijet mass width for h->bb events.

### LCFIPlus v00-08

* 2019-09-04 Andre Sailer ([PR#51](https://github.com/LCFIPlus/LCFIPlus/pull/51))
  - Placeholder: add <functional> for gcc7/8, llvm5

* 2019-09-04 Frank Gaede ([PR#50](https://github.com/LCFIPlus/LCFIPlus/pull/50))
  - make compatible w/ c++17
         - replace std::bind2nd w/ std::bind
            and std::placeholders::_1 in VertexSelector.h

* 2019-03-05 Andre Sailer ([PR#46](https://github.com/LCFIPlus/LCFIPlus/pull/46))
  - LCIOStorer: fix memory leak of PIDHandler
  - LCFIPlusProcessor: clean algos and params after the end() of algos, fix memory leaks
  - Process: fix memory leak of `double *ymin`, use `std::vector<double>`
  - Process: use shared_ptr for JetFinder, fixes memory leak
  - VertexFitterSimple: fix memory leak for IP: only create it if it is used
  - VertexFinderSuehara: fix mismatch between new[] and delete (w/o []), use std::vector<double>

### LCFIPlus v00-07

* 2018-10-30 Ryo Yonamine ([PR#45](https://github.com/lcfiplus/LCFIPlus/pull/45))
  - Add initializatioin.
  - Prevent accessing a null pointer.

* 2018-10-22 Ryo Yonamine ([PR#44](https://github.com/lcfiplus/LCFIPlus/pull/44))
  - bug fix. "1" and "0" didn't work after the previous modification. now any of "true", "false", "1", "0" work.

* 2018-10-19 Ryo Yonamine ([PR#43](https://github.com/lcfiplus/LCFIPlus/pull/43))
  - too-small primary vertex postion errrors
  - problems caused due to the ip semaring
  - problem with which boolean parameters were not able to set by "true" or "false"
  
  New variables for flavor tagging introduced :(d0/z0)prob(b/c/q)2.
  These can be used istead of (d0/z0)prob(b/c/q).
  This fixs the problem that maximax exceeds 1.
  The flavor tagging performance will be slightly improved.

### ForwardTracking v01-14

* 2019-11-25 Remi Ete ([PR#10](https://github.com/iLCSoft/ForwardTracking/pull/10))
  - Remove dynamic exception specifier (c++17 compatibility)


### ConformalTracking v01-10

* 2019-10-08 Remi Ete ([PR#55](https://github.com/iLCSoft/ConformalTracking/pull/55))
  - ConformalTracking processor: Use streamlog macros instead of raw calls

* 2019-09-09 Andre Sailer ([PR#54](https://github.com/iLCSoft/ConformalTracking/pull/54))
  - Add Parameter TooManyTracks to configure what is considered too many, defaults to 5e5
  - Fix the abort logic so that after ten tries the event is actually skipped, or if retryTooManyTracks is False immediately, instead of never or until the number of created tracks is small enough

* 2019-08-22 Erica Brondolin ([PR#53](https://github.com/iLCSoft/ConformalTracking/pull/53))
  - Include cut in slope in z for CA building part to reduce number of combinatorics
    - In ConformalTrackingV2: configurable via per step parameter slopeZRange
    - Reduces CPU time
  - Change sum of chi2 from square-root of the squared sum to linear sum
  - No big changes expected in eff/fakes

### ConformalTracking v01-08

* 2019-02-07 Emilia Leogrande ([PR#49](https://github.com/iLCSoft/ConformalTracking/pull/49))
  - Clone checker: if equal length, keep the one with the better chi2
  - Debug9 prints clone checker info
  - Fix address of the track in the debug printouts among functions

* 2018-10-30 Erica Brondolin ([PR#48](https://github.com/iLCSoft/ConformalTracking/pull/48))
  - Solving bug introduced with the PR #47 : the `fitError` variable was overwritten even when the inverted fit was not better than the normal one.
  - The maximum number of track hit to try the inverted fit is now a parameter.

* 2018-10-26 Erica Brondolin ([PR#47](https://github.com/iLCSoft/ConformalTracking/pull/47))
  - If the track is too short (usually less than 7 hits correspond to a vertex track) the fit in the inverse direction is tried. If the track is longer, then it is kept as the final one.
  - This is important especially for tracks reconstructed in the very forward region where the extrapolation VTX-TRK is longer.

* 2018-10-11 Erica Brondolin ([PR#46](https://github.com/iLCSoft/ConformalTracking/pull/46))
  - Introduce `extendTracksPerLayer` function to find all the hits layer by layer
  - Filter the neighbours that are in the wrong direction of the track and that are in layers too far
  - The best candidates are inserted in the track if their chi2 is within a certain range, otherwise only the hit with the best chi2 is kept
  - Results in the bbar show improved number of hits for tracks with pT > 1 GeV and basically unchanged for tracks with pT < 1 GeV

* 2018-09-27 Emilia Leogrande ([PR#45](https://github.com/iLCSoft/ConformalTracking/pull/45))
  - ConfomalTrackingV2
      - Kalman fit direction can now be set per reconstruction step, to allow for the foreseen possibility to fit prompt tracks forward and non-prompt backward
      - added flag "KalmanFitBackward" and "KalmanFitForward" that can be parsed from steering file; if nothing is set, the default is forward
   - Kalman fit direction added as member variable of the KDTrack class, with getter/setter

* 2018-09-26 Emilia Leogrande ([PR#44](https://github.com/iLCSoft/ConformalTracking/pull/44))
  - in ConformalTracking::runStep, marking hits as used is now repositioned at the end of every step
  - implemented debug streamlog printouts to follow pattern recognition
  -- streamlog_out( DEBUG9 ) for 'main' functions: processEvent, buildNewTracks [to do: extendTracks, but function is intended to be upgraded]
  -- streamlog_out( DEBUG8 ) for 'secondary' functions: extendSeedCells, createTracksNew, getFittedTracks, getLowestChi2

* 2018-08-09 Emilia Leogrande ([PR#42](https://github.com/iLCSoft/ConformalTracking/pull/42))
  - The pt threshold to run extendHighPt is now a parameter, to be set in the steering file
    - It has effect only on the steps when extendTracks is run (buildNewTracks does not use extendHighPt)
    - Default values at the moment: 10 GeV for extending in the vertex endcap, 1 GeV for extending in the trackers

* 2018-07-24 Emilia Leogrande ([PR#41](https://github.com/iLCSoft/ConformalTracking/pull/41))
  - ConformalTrackingV2: removed the call to init()
    - init() is already done in ConformalTracking.cc
    - since in init() the step parameters are parsed, they were parsed twice, resulting in twice the number of steps in the pattern recognition chain

* 2018-06-28 Andre Sailer ([PR#40](https://github.com/iLCSoft/ConformalTracking/pull/40))
  - New processor ConformalTrackingV2, which allows complete freedom to configure the steps of the pattern recognition
    - See the README.md File
    - The ConformalTracking processor is kept for backward compatibility but should be considered deprecated
    - Refactored ConformalTracking for inheritance, loop over vector of parameters
    - Cleaned up header includes and CMakeLists

* 2018-06-25 Emilia Leogrande ([PR#39](https://github.com/iLCSoft/ConformalTracking/pull/39))
  - Conformal Tracking restructured to be run in steps with function runStep
  - runStep allows to decide which functions to run per step for the reconstruction, i.e. combineCollections, buildNewTracks, extendTracks
  - prior to runStep, the set of parameters for the reconstruction step is initialized

* 2018-05-18 Emilia Leogrande ([PR#37](https://github.com/iLCSoft/ConformalTracking/pull/37))
  - ConformalTracking: fixed two issues, one in the pattern recognition, one in the choice among clones
  - when building tracks in the combined vertex barrel + endcap, the step with looser cut must be done all at one (open the angles and increase the chi2 cut at the same time, not in two subsequent steps), otherwise tracks are made with less hits than desired
  - once increased, keep the chi2 cut the same for subsequent steps
  - in presence of clones, it is not good to prefer shorter tracks with better chi2 (the comparison is also progressive, so one can easily go from a 8 hits track to a 4 hits track). To avoid in order not to have double tracks per particle

* 2018-05-16 Emilia Leogrande ([PR#36](https://github.com/iLCSoft/ConformalTracking/pull/36))
  - new strategy: hits on the same subdetector layer are accepted (otherwise the leftover of the pairs can make a second track)
  - if hits on the same *sensor* of the same subdetector layer, only one (smaller radius) is taken
  - flag to enable tight cuts in the combined vertex endcap + barrel added as processor parameter (Temporary, will be removed in the future)

* 2018-05-09 Andre Sailer ([PR#35](https://github.com/iLCSoft/ConformalTracking/pull/35))
  - ConformalTracking.cc: [extendTracks]fix for hits from the same subdetector layers not to be accepted in the same track, when tracks are extended to vertex endcap and to trackers

### BBQ v00-01-04

- Fixed a bug in function toGlobal() in vistp.cxx; break statements were missing in switch. thus, always the same coordinate system type was used.
- Implemented bugfix suggested by Marko Petric via Frank Gaede: Pointer comparison with NULL instead of boolean false.
- copied last trunk version to this tag, as only tag-versions are incorporated into ilcsoft and, finally, the above bug led to compile errors

### GBL v02-02-00

- Composed trajectories: geometric constraint added (to kinematic)
-	Small documentation fix
-	Composed trajectories: geometric constraint added (to kinematic)
-	examples cleaned up
-	CMake for examples fixed
- Bug fix for external measurements
- examples reworked 	Diff
- Added Si tracker example, fixed down-weighted residuals
- Fixed uninitialized values (proDer, composed trajectory)
- Fixed uninitialized values (labDer)

### DD4hep v01-11

* 2019-10-23 MarkusFrankATcernch ([PR#587](https://github.com/AidaSoft/DD4hep/pull/587))
  -  Have separate compilation unit for shape utilities like `set_dimension(...)`, `dimension()`, `isA()`, `instanceOf()`... 
  - Improvements to basic shape test

* 2019-10-23 Andre Sailer ([PR#579](https://github.com/AidaSoft/DD4hep/pull/579))
  - CMake: Add possibility to build only shared libraries, fixes #493: 
    - Usage `cmake ... -D BUILD_SHARED_LIBS=OFF ...`

* 2019-10-23 Andre Sailer ([PR#575](https://github.com/AidaSoft/DD4hep/pull/575))
  * CMake: Add `DD4HEP_USE_EXISTING_DD4HEP` option which together with `DD4HEP_BUILD_PACKAGES` can be used to rebuild, for example only DDG4.
     * This creates a new Package called "DD4hepSelected" which can then be used alongside the full DD4hep Package in a third project.

* 2019-10-22 Marko Petric ([PR#586](https://github.com/AidaSoft/DD4hep/pull/586))
  - Remove deprecated rootcling flags (`-cint`, `-c`, `-p`, `-std=c++`) from dictionary creation script

* 2019-10-22 Marko Petric ([PR#585](https://github.com/AidaSoft/DD4hep/pull/585))
  - Fix bug that the c++ filesystem check is called from `${DD4hep_ROOT}`
  - Install `DD4hepConfig.cmake` only in `__prefix__/cmake` to avoid path detection confusion
  - Enable choosing examples in the `examples/CMakeLists.cmake` via cmake flag `-DDD4HEP_BUILD_EXAMPLES=OpticalSurfaces` (recommended method)
  - Make each example folder to compile standalone (not recommended method)
  - Update cmake of Segmentation example to more current state and fix resulting errors
    - include segmentation example as test
  - Resolves #582 and resolves #583

* 2019-10-21 MarkusFrankATcernch ([PR#584](https://github.com/AidaSoft/DD4hep/pull/584))
  - Add function `bool isInstance(const Handle<TGeoShape>& solid)`
     - compares types of shapes and behaves like `dynamic_cast`, similar to python's `isinstance(obj,type)`
     - remove deprecated function `instanceOf` in favour of `isInstance`. Same behavior.
   - Add function `bool isA(const Handle<TGeoShape>& solid)`
     - compares types of shapes and requires exact match, no polymorphism allowed.
  - Add Geant4 conversion for shape `TGeoCtub` -> `G4CutTube`

* 2019-10-14 Marko Petric ([PR#572](https://github.com/AidaSoft/DD4hep/pull/572))
  - Install python files in `lib/pythonX.Y/site-packages` resolves #562 
    - adapt `thisdd4hep.sh` scripts
  - Add missing RPATH to examples (basically bug fix for mac)
  - Add DDG4 tools to bin to make them more accessible to users:
    - `g4MaterialScan`, `checkGeometry`, `checkOverlaps`

* 2019-10-03 MarkusFrankATcernch ([PR#577](https://github.com/AidaSoft/DD4hep/pull/577))
  - Inhibit not allowed use of `DetectorImp.h`

* 2019-10-03 Andre Sailer ([PR#574](https://github.com/AidaSoft/DD4hep/pull/574))
  - CMake: When needing `boost::filesystem` (c++14, gcc  < 8) require at least Boost 1.56, see #567

* 2019-10-03 Markus Frank ([PR#573](https://github.com/AidaSoft/DD4hep/pull/573))
  - Fix memory leak introduced when generalizing placements to include left-handed coordinate systems.

* 2019-10-03 Markus Frank ([PR#571](https://github.com/AidaSoft/DD4hep/pull/571))
  - Add example to the volume reflection mechanism
  - Fix bug in volume reflection

* 2019-10-02 Markus Frank ([PR#569](https://github.com/AidaSoft/DD4hep/pull/569))
  - First implementation to support reflection with left-handed volumes/solids
    - Changes for volumes and solids.
    - Conversion handling of `TGeoScaledShape` in DDG4

* 2019-09-30 Andre Sailer ([PR#566](https://github.com/AidaSoft/DD4hep/pull/566))
  - PythonBindings: fix issue when source files were not available, fixes #565 
  - CMake: drop DDCores dependency on DD4hepGaudiPluginMgr
  - CMake: DD4hepConfig: use find_dependency instead of find_package

* 2019-09-24 Marko Petric ([PR#564](https://github.com/AidaSoft/DD4hep/pull/564))
  - Added test for Python3 compliance of code
  - Added test to require flake8 python code formatting

* 2019-09-13 Marko Petric ([PR#540](https://github.com/AidaSoft/DD4hep/pull/540))
  - Make python code compatible to python 2 and 3
    - add `absolute_import` and `unicode_literals` to all files
      - fix API calls and cast `unicode` to `string` when needed
    - replace print statement with logging
    - remove old octal literal
    - use future division
    - use `six`:
       - replace `dict.iteritems` with `six.iteritems`
       - replace `xrange` with `range` from `six.move`
       - replace `basestring` with `six.string_types`
       - replace `raw_input` with `input` from `six.moves`
       - added a copy of six.py named ddsix.py to DDCore
    - Replace deprecated `execfile` with call to `open`, `compile` and `exec`
    - Remove usage of `apply`
    - use `io.open` instead of standard `open`
    - convert `except a,b` to `except a as b`
    - change `dict.has_key` to `key in dict`
  - Require DD4hep Python3 CI tests to pass
  - Remove obsolete `lcdd.py`
  - Remove deprecated `SystemOfUnits.py` and replace everywhere with `g4units.py`
  - Flake8 all files

* 2019-09-02 Andre Sailer ([PR#561](https://github.com/AidaSoft/DD4hep/pull/561))
  - CMake: add option `DD4HEP_BUILD_PACKAGES` so that only individual packages can be compiled. If an incorrect selection is given cmake should fail due to missing alias libraries. The option requires a whitespace or semicolon separated list.
  - CMake add option `DD4HEP_BUILD_EXAMPLES` to enable compilation of examples together with the main DD4hep packages. Default OFF
  - CMake: add `DD4hep::` aliases for all libraries and some executables

* 2019-08-26 Andre Sailer ([PR#559](https://github.com/AidaSoft/DD4hep/pull/559))
  - DD4hepConfig: make all DD4HEP_USE variables behave as booleans

* 2019-08-22 Markus Frank ([PR#554](https://github.com/AidaSoft/DD4hep/pull/554))
  - Fix property table translation to Geant4 according to suggestions from Dong Liu
    (see issue https://github.com/AIDASoft/DD4hep/issues/440 )

* 2019-08-22 Andre Sailer ([PR#552](https://github.com/AidaSoft/DD4hep/pull/552))
  * DD4hepConfig: `DD4hepConfig.CMake` now exports `DD4hep::DDCore` `DD4hep::<Component>` targets to be consumed by users of the DD4hep package, the CMake variables `DD4hep_LIBRARIES` etc. are still being filled for backward compatibility
  
  * DD4hep CMake: Only the `dd4hep_add_plugin` and `dd4hep_add_dictionary` CMake functions are to create targets still exist, `dd4hep_add_package`/`library`/`executable` were removed and instead the cmake `default add_library`/`executable` have to be used.
  
  * PluginManager: only link against boost filesystem if the compiler and standard library do not support the filesystem library
  
  * DD4hep Requirements: Now require cmake version 3.12
  
  * DD4hep Requirements: Now require c++ standard 14

* 2019-08-21 Markus Frank ([PR#553](https://github.com/AidaSoft/DD4hep/pull/553))
  - Fix unit conversion for optical surface properties. The units of the property tables were not converted from TGeo to Geant4. See dicussion in issue https://github.com/AIDASoft/DD4hep/issues/440
  - If an external world volume is supplied, the material `Air` is deduced from this solid (only used by CMS).

* 2019-08-15 Frank Gaede ([PR#550](https://github.com/AidaSoft/DD4hep/pull/550))
  - make compatible with MacOS (10.14.6)
       - address latest developments w/ new Gaudi Plugin Manager

* 2019-08-14 Markus Frank ([PR#551](https://github.com/AidaSoft/DD4hep/pull/551))
  - Moved `setDimensions` call out of the individual dd4hep shapes into the base Solid.
  - Add `Solid::dimensions()`, `Solid::setDimension()` implementation for `PseudoTrap` and  `TruncatedTube`. The solution is not optimal, because a analytical solution tends to be ambiguous due to solutions of polynomials of degree 2 and the initial parameters had to be stored as a string.
  - Upgraded shape tests to also check the shapes (using mesh vertices) after a re-dimension using the same parameters.
  - Geant4FieldTrackingSetup: Any failure in the creation of the `G4EquationOfMotion` or the `G4MagIntegratorStepper` is now FATAL and causes an exception.

* 2019-08-12 Markus Frank ([PR#549](https://github.com/AidaSoft/DD4hep/pull/549))
  - Adopted new Gaudi plugin manager V2. V1 can be enabled using compile switch in `DD4hep/config.h`. Removed the traces from the ROOT5 Reflex based plugin service. The new plugin service depends on `Boost::file_system` and `Boost::system`. 
  - Improve GDML saving from ROOT. (requires ROOT >= 6.20)
  - Fix ROOT persistency for the volume manager.
  - Fix Geant4FieldTrackingSetup: Issue warning if the `G4MagIntegratorStepper` cannot be created.
  - Examples: based the CLICSiD example on the XML sources of DDDetectors. This ensures XML sources match C++ sources.

* 2019-08-12 Andre Sailer ([PR#548](https://github.com/AidaSoft/DD4hep/pull/548))
  - Shapes: fix conversion of `startTheta` for Sphere::setDimensions
  - Shapes::get_shape_dimension: add return value conversion for angles to internal unit (radians)

* 2019-08-12 MarkusFrankATcernch ([PR#547](https://github.com/AidaSoft/DD4hep/pull/547))
  - make compatible w/ macos (c++14)
           - replace `std::make_any` w/ make_any (defined in Any.h)
           - use `std::lock_guard<std::mutex>`

* 2019-08-07 MarkusFrankATcernch ([PR#545](https://github.com/AidaSoft/DD4hep/pull/545))
  - Fix bug in Polyhedra shape (See #544).
  - Update optical surface example (resolves #440) .

* 2019-07-16 Markus Frank ([PR#539](https://github.com/AidaSoft/DD4hep/pull/539))
  - Remove clang warnings.

* 2019-07-16 MarkusFrankATcernch ([PR#538](https://github.com/AidaSoft/DD4hep/pull/538))
  - Fix coverity errors 
  - Fix Trap shape conversion to Geant4. The theta/phi angle was not converted from degree to radians (Resolves #536).

* 2019-07-15 Marko Petric ([PR#537](https://github.com/AidaSoft/DD4hep/pull/537))
  - Add a Python 3 pipeline to the CI (currently set to `allow_failure`)

* 2019-07-13 Marko Petric ([PR#535](https://github.com/AidaSoft/DD4hep/pull/535))
  - Update CI to be based on LCG 96 (ROOT 6.18, Geant 10.5, C++17)
  - Remove `FindXercesC.cmake` since it is in CMake

* 2019-07-10 Markus Frank ([PR#533](https://github.com/AidaSoft/DD4hep/pull/533))
  - Optimize STL containers: replace insert/push with emplace. 2nd. episode.

* 2019-07-10 Marko Petric ([PR#532](https://github.com/AidaSoft/DD4hep/pull/532))
  - Remove `dd_sim` (resolves #435)

* 2019-07-10 Marko Petric ([PR#531](https://github.com/AidaSoft/DD4hep/pull/531))
  - Remove shadow warnings related to code interfacing only ROOT 6.18
  - Add `DBoost_NO_BOOST_CMAKE=ON` to examples cmake call as it is necessary now
  - Set CMP0074 policy to NEW if can be set

* 2019-07-10 Markus Frank ([PR#530](https://github.com/AidaSoft/DD4hep/pull/530))
  - Optimize STL containers: replace insert/push with emplace

* 2019-07-09 Markus Frank ([PR#528](https://github.com/AidaSoft/DD4hep/pull/528))
  * Allow for various material scan types from the root interactove prompt
  
         Examples: from DDDetectors/compact/SiD.xml
         $> materialScan file:checkout/DDDetectors/compact/SiD.xml -interactive
       
         1) Simple scan:
            root [0] gMaterialScan->print(5,5,0,5,5,400)
         2) Scan a given subdetector:
            root [0] de=gDD4hepUI->instance()->detector("LumiCal");
            root [1] gMaterialScan->setDetector(de);
            root [2] gMaterialScan->print(5,5,0,5,5,400)
         3) Scan by material:
            root [0] gMaterialScan->setMaterial("Silicon");
            root [1] gMaterialScan->print(5,5,0,5,5,400)
         4) Scan by region:
            root [0] gMaterialScan->setRegion("SiTrackerBarrelRegion");
            root [1] gMaterialScan->print(0,0,0,100,100,0)
  
  * Added copyright notices to the DDRec files.

* 2019-07-09 Marko Petric ([PR#527](https://github.com/AidaSoft/DD4hep/pull/527))
  - Update CI to macOS Mojave 10.14
  - Make `PluginService.cpp` C++17 compliant (addresses partially #525)
    - replace `ptr_fun` with `lambda`
  - Remove deprecated code that uses `auto_prt`
  - Remove deprecated `set_unexpected` from  `DetectorImp.cpp`
  - Remove code associated to `DD4HEP_DD4HEP_PTR_AUTO`

* 2019-07-08 Markus Frank ([PR#524](https://github.com/AidaSoft/DD4hep/pull/524))
  - Get the new package formally into the same shape as the other packages together with an example section.
  - Add small example to test the basic development framework

* 2019-07-04 Markus Frank ([PR#520](https://github.com/AidaSoft/DD4hep/pull/520))
  - From ROOT 6.20 onwards dd4hep shall use the Geant4 unit system (mm, nsec, MeV) instead of the TGeo units (cm, sec, keV). This commit prepares for the necessary changes.
  - A new package was created, which shall host the dd4hep digitization components.
    A small tbb based multi threaded framework was put in place. Now the real work can start.
  - The material scanner has now a switch to run in interactive mode from the ROOT prompt.
    To invoke: materialScan compact.xml  x0 y0 z0 x1 y1 z1 -interactive
    If the interactive switch is missing, the old behavior is preserved.

* 2019-06-26 Markus Frank ([PR#517](https://github.com/AidaSoft/DD4hep/pull/517))
  - Material properties use now default dd4hep units
  - Translated and updated surface example from geant4 to dd4hep
  - Added shape identification using `instanceOf operator (function)`
  - Improved handling of xml files if improperly terminated

* 2019-06-26 MarkusFrankATcernch ([PR#516](https://github.com/AidaSoft/DD4hep/pull/516))
  - CMakeLists: Changed the order in which include directories are listed when compiling, move DD4hep source paths to the front. This fixes a problem if older DD4hep installations are inadvertently in one of the include paths passed to compilers or rootcling (e.g., in LCG Views), fixes #515

* 2019-06-06 Andre Sailer ([PR#514](https://github.com/AidaSoft/DD4hep/pull/514))
  - Gean4ExtraParticles: no longer add decay process to extra particles, this is done by Geant4  resolves #513 
  - ddsim: disable physics.decays by default. This should only be enabled if completely new physics lists are created resolves #513

* 2019-05-09 Markus Frank ([PR#510](https://github.com/AidaSoft/DD4hep/pull/510))
  - Add debug printout of MEE in Geant4 material conversion

* 2019-04-29 MarkusFrankATcernch ([PR#508](https://github.com/AidaSoft/DD4hep/pull/508))
  * Geant4GDMLWriteAction:
    * Add properties to Geant4GDMLWriteAction to steer writing of regions, cuts and sensitive detectors. See github issue #507
      * Property: Export region information to the GDML: ExportRegions, default: True
      * Property: Export energy cut information to the GDML: ExportEnergyCuts, default: True
      * Property: Export sensitive detector information to the GDML: ExportSensitiveDetectors, default: True
    * **Note: The Geant4 physics list must be initialized BEFORE invoking the writer with options. Otherwise the particle definitions are missing! If you ONLY want to dump the geometry to GDML you must call**
      ```
         /run/beamOn 0
      ```
      before writing the GDML file!
      You also need to setup a minimal generation action like:
       ```py
       sid.geant4.setupGun('Gun','pi-',10*GeV,Standalone=True)
       ```

* 2019-04-29 Frank Gaede ([PR#506](https://github.com/AidaSoft/DD4hep/pull/506))
  - add utility materialBudget.cpp 
       - create plots w/ integrated radiation and interaction lengths
  - bug fix in materialScan.cpp
       - print correct endpoint

* 2019-04-17 Marko Petric ([PR#503](https://github.com/AidaSoft/DD4hep/pull/503))
  - DDG4: DDSim add option Physics.zeroTimePDG to configure ignoring particles of given PDG when their properTime is ZERO, e.g. charged leptons undergoing FSR, fixes #390 
  - DDG4: DDSim: fix parsing of rejectPDGs values from the command line

* 2019-04-12 Marko Petric ([PR#502](https://github.com/AidaSoft/DD4hep/pull/502))
  - DDSim: Add Higgs PDG code 25 to rejected codes for reading events

* 2019-04-10 MarkusFrankATcernch ([PR#501](https://github.com/AidaSoft/DD4hep/pull/501))
  - Add access to all Geant4Action derivatives to the Geant4 top level physical volume (world).
  - Add Geant4 GDML writer action accessible and configurable from the Geant4 prompt

* 2019-04-09 Mircho Rodozov ([PR#496](https://github.com/AidaSoft/DD4hep/pull/496))
  - Added powerpc macros check to include header `cxxabi.h`

* 2019-04-01 Markus Frank ([PR#494](https://github.com/AidaSoft/DD4hep/pull/494))
  -  Use shared_ptr instead of home made ref counting for ConditionUpdateCalls
  -  Implement construction parameter access for solids.  This one is a bit tricky: Some shapes (ShapeAssembly, Boolean shapes) had no such parameters. Added them as the sequence of the basic shape parameters + the corresponding matrices.
  -  Add move constructors to handles 
  -  Improve const-ness of detector object in DDG4

* 2019-03-11 Markus Frank ([PR#491](https://github.com/AidaSoft/DD4hep/pull/491))
  - Implemented basic handles to support surface objects
  - Implemented import of surface optical objects in compact to create TGeo surface objects and tabulated properties.
  - Implemented the translation from TGeo to Geant4
  - Added physics components for DDG4 handling Cerekov, Scintillation and generic optical photon physics
  - Added examples
  
  Please Note: 
  1) This is only enabled for a ROOT version > 6.17 (which is supposed to come)
  2) There are still changes in ROOT in the pipeline. The code shall have to be adapted accordingly once these changes are activated.

* 2019-03-06 ebrianne ([PR#489](https://github.com/AidaSoft/DD4hep/pull/489))
  - Added Initialization of G4EmSaturation to initialize birks coefficients - for g4 version > 10.03

* 2019-02-19 Andre Sailer ([PR#486](https://github.com/AidaSoft/DD4hep/pull/486))
  - DDRec: Surface: add accessor to DetElement member
  - DDRec: DetectorData: add Extension holding a map of String to Doubles

* 2019-02-14 Paul Gessinger ([PR#485](https://github.com/AidaSoft/DD4hep/pull/485))
  * In `DD4hepConfig.cmake`, figure out if build has compatible standard set and print error if not

* 2019-02-13 Frank Gaede ([PR#483](https://github.com/AidaSoft/DD4hep/pull/483))
  - fix drawing of surfaces for z-disks and cylinders (resolves #482)

### DD4hep v01-10

* 2019-01-31 Markus Frank ([PR#480](https://github.com/aidasoft/dd4hep/pull/480))
  - Fix bug in `geoDisplay` to allow passing the volume display depth as an argument
  - Added a static creator to the Detector class to create non-traced instances: `std::unique_ptr<Detector> Detector::make_unique(const std::string& name);` It is the users responsibility to release the allocated resources and to avoid clashed with existing `TGeoManager` instances.
  -  Allow direct access to the solid instance of the DetElements's placement.

* 2019-01-15 Markus Frank ([PR#478](https://github.com/aidasoft/dd4hep/pull/478))
  - Fix bug in `geoDisplay` see #477

* 2019-01-10 Markus Frank ([PR#476](https://github.com/aidasoft/dd4hep/pull/476))
  - Fix bug in ConditionsUserPool whan scanning DetElement conditions
  - Improve conditions handling: Allow to bind sub-class entities of ConditionObject to thew opaque data block.

* 2018-12-14 Markus Frank ([PR#475](https://github.com/aidasoft/dd4hep/pull/475))
  - Add named shape constructors (see #469)

* 2018-12-13 Markus Frank ([PR#474](https://github.com/aidasoft/dd4hep/pull/474))
  - Fix possible access violation

* 2018-12-13 MarkusFrankATcernch ([PR#473](https://github.com/aidasoft/dd4hep/pull/473))
  - Improve handling of condition dependencies ( main work item)
    - Improve logic flow in the DDCond/ConditionDependencyHandler
    - Improve the functionality of the conditions resolver accessible from the update context. Allow for the creation (and registration) of multiple conditions in one single callback.
  - Add a shape check for eight-point solids.

* 2018-12-07 Frank Gaede ([PR#470](https://github.com/aidasoft/dd4hep/pull/470))
  - add `#include <memory>` to `run_plugin.h` (needed for `std::unique_ptr` and gcc 4.9)

* 2018-12-06 Markus Frank ([PR#468](https://github.com/aidasoft/dd4hep/pull/468))
  - To fix issue #466  we had to go back to the original implementation which was actually correct (see https://github.com/AIDASoft/DD4hep/commit/36d4b01e0688f690ac2e506a62e00627bb6b798c#diff-7219d47bc4ab7516e0ca6c4f35f2602f).
  - Added an example to show how to perform scans of the volume hierarchy with user defined callback functors. See for details `examples/ClientTests/src/PlacedVolumeScannerTest.cpp`.
  
  - Added conversion between `TGeoArb8` and `G4GenericTrap`, fixes #465

* 2018-12-05 Markus Frank ([PR#467](https://github.com/aidasoft/dd4hep/pull/467))
  - Harmonize argument names in `Shapes.h` with their actual functionality. For many shapes in `DD4hep/Shapes.h` the argument names were misleading: very often deltaPhi was mentioned, whereas the code actually used instead of (phi, deltaphi) the input arguments to the ROOT constructors (startPhi,endPhi) or (phi1, phi2).  Wherever ROOT uses (startPhi,endPhi) the argument names were changed accordingly. Please note a bug was found in the legacy constructor:
    ```cpp
      /// Legacy: Constructor to create a new identifiable tube object with attribute initialization
      Tube(const std::string& nam, double rmin, double rmax, double dz, double startPhi, double endPhi)
    ```
    Here opposite to all other constructors delta_phi was used as such - in contradiction to other constructors of the same class. This was rectified.

* 2018-11-30 Andre Sailer ([PR#462](https://github.com/aidasoft/dd4hep/pull/462))
  - Introduce compile flag to minimize conditions footprint

* 2018-11-27 Markus Frank ([PR#461](https://github.com/aidasoft/dd4hep/pull/461))
  - Add shape constructor for regular trapezoids (TGeoTrd1) ( see #460). Trd2 cannot be divided the same way as Trd1 shapes. Hence the addition became necessary. Due to the imprecise name of Trapezoid the names Trd1 and Trd2 (aka old Trapezoid) are favored. The usage of Trapezoid is supported for backwards compatibility using a typedef.

* 2018-11-22 Markus Frank ([PR#459](https://github.com/aidasoft/dd4hep/pull/459))
  - Fix bug in DDCodex geometry, add debugging to VolumeBuilder

* 2018-11-14 Markus Frank ([PR#458](https://github.com/aidasoft/dd4hep/pull/458))
  - Improve ROOT persistency: flag user extensions as persistent only while saving/loading
  - Need to rename DDEve library: nameclash with ddeve executable on Apple: cmake fails to build ddeve as exe and DDEve as library. libDDEve.so is now called libDDEvePlugins.so.

* 2018-11-13 Markus Frank ([PR#457](https://github.com/aidasoft/dd4hep/pull/457))
  ## Provide support for Volume divisions.
  Since DD4hep requires Volumes (aka `TGeoVolume`) and PlacedVolumes (aka `TGeoNode`) to be enhanced with the user extension mechanism, therefore shape divisions **must** be done using the division mechanism of the DD4hep shape or the volume wrapper. Otherwise the enhancements are not added and you will get an exception when DD4hep is closing the geometry or whenever you do something with the volume, which is served by the user extension. The same argument holds when a division is made from a `Volume`. Unfortunately there is no reasonable way to intercept this call to the `TGeo` objects - except to the sub-class each of them, which is not really acceptable either.
  
  Hence: **If you use DD4hep: Never call the raw TGeo routines.**
     
  For any further documentation please see the following ROOT documentation on [TGeo](http://root.cern.ch/root/html/TGeoVolume.html)
  
  For an example see `examples/ClientTests/src/VolumeDivisionTest.cpp`
  and `examples/ClientTests/compact/VolumeDivisionTest.xml`
  
  To execute: 
  ```
  geoDisplay -input file:<path>/examples/ClientTests/compact/VolumeDivisionTest.xml
  ```

* 2018-11-13 Hadrien Grasland ([PR#438](https://github.com/aidasoft/dd4hep/pull/438))
  - Make FindPackage(DD4hep) work even if thisdd4hep.sh was not sourced

* 2018-11-09 Frank Gaede ([PR#456](https://github.com/aidasoft/dd4hep/pull/456))
  - add `#include <memory>` in `VolumeAssembly_geo.cpp` gcc 4.9 compatibility

* 2018-11-07 Markus Frank ([PR#455](https://github.com/aidasoft/dd4hep/pull/455))
  - Improve VolumeBuilder pattern matcher
  - Allow XML based volume creation based on factories.

* 2018-11-02 Markus Frank ([PR#454](https://github.com/aidasoft/dd4hep/pull/454))
  - Improve generic Volume assembly and XML volume builder

* 2018-11-01 Markus Frank ([PR#452](https://github.com/aidasoft/dd4hep/pull/452))
  - Fixed the DetElement cloning mechanism it to properly replicate DetElement trees.
    - Tested with one LHCb upgrade detector.
  - Added numeric epsilon to the default math dictionary of the expression evaluator:
    ```cpp
    int:epsilon  --> std::numeric_limits<int>::epsilon()
    long:epsilon  --> std::numeric_limits<long>::epsilon()
    float:epsilon  --> std::numeric_limits<float>::epsilon()
    double:epsilon  --> std::numeric_limits<double>::epsilon()
    ```

* 2018-10-30 Markus Frank ([PR#451](https://github.com/aidasoft/dd4hep/pull/451))
  - Add copyright notices
  - Make ddeve a program not only a ROOT script

* 2018-10-30 Markus Frank ([PR#450](https://github.com/aidasoft/dd4hep/pull/450))
  - The DDUpgrade example was removed from the main repository. Since it is only of interest for LHCb, it moved to a separate repository at CERN/gitlab.
  - Issue #449 should be fixed now.
  - The XML volume builder utility was improved.

* 2018-10-18 Markus Frank ([PR#447](https://github.com/aidasoft/dd4hep/pull/447))
  -  Fix plugin manager cmake file by removing explicit dependency on c++ standard.

### DD4hep v01-09

* 2018-10-15 Markus Frank ([PR#442](https://github.com/aidasoft/DD4hep/pull/442))
  - DDCMS: Update to support namespaces
  - DDUpgrade test example for the LHCb upgrade
  - Fix nested detectors (in fact worked only for first level parents)
  - Add VolumeBuilder XML utility to work on XML-tree patterns

* 2018-09-12 Hadrien Grasland ([PR#437](https://github.com/aidasoft/DD4hep/pull/437))
  - Remove if string equals ON/OFF in cmake IF statements and check default CMake truth values

* 2018-08-20 Oleksandr Viazlo ([PR#434](https://github.com/aidasoft/DD4hep/pull/434))
  - DD4hep_Mask_o1_v01_geo
    - allow rotation around x-axis (instead of y)
    - phi1 and phi2 cone angles configurable from the xml-file

* 2018-08-10 Markus Frank ([PR#433](https://github.com/aidasoft/DD4hep/pull/433))
  - Fix DDCMS example to use true namespace names rather than using "_"
    This should resolve issue https://github.com/AIDASoft/DD4hep/issues/421

* 2018-08-09 Markus Frank ([PR#432](https://github.com/aidasoft/DD4hep/pull/432))
  - Make the expression evaluator understand variable names with namespaces
      - Variable names containing a `:` or `::` are now accepted by the expression evaluator. This is first step towars resolving #421 
     - It has now to be seen what has to be done further. The DCMS example was not yet updated to use this feature.
  - Add new example in `examples/ClientTests` to test this functionality.

* 2018-08-09 Andre Sailer ([PR#429](https://github.com/aidasoft/DD4hep/pull/429))
  - DDG4: add possibility to simulate all events in a file by passing NumberOfEvents < 0. Fixes #237 
     * The de-facto limit is ~2 billion, which should be fine for input files.

* 2018-08-08 Markus Frank ([PR#430](https://github.com/aidasoft/DD4hep/pull/430))
  - Fix HEPMC reader for unknown generator status codes 
  - Update DDCodex example, feature imports from plain ROOT file 
  - Allow debugging Geant4VolumeManager

* 2018-08-07 Mircho Rodozov ([PR#428](https://github.com/aidasoft/DD4hep/pull/428))
  - Adapt to root interfaces changes for `TGeoMatrix::Inverse` (https://github.com/root-project/root/pull/2365), fixes #426

* 2018-08-06 Andre Sailer ([PR#424](https://github.com/aidasoft/DD4hep/pull/424))
  - CMake: Ensure proper tls flag (global-dynamic) for Geant4 build, added option DD4HEP_IGNORE_GEANT4_TLS  to override the check. Closes #419

* 2018-07-31 Andre Sailer ([PR#420](https://github.com/aidasoft/DD4hep/pull/420))
  - DDG4: Import the ddsim python program from https://github.com/iLCSoft/lcgeo
    For example:
     - `ddsim --help`
     - `ddsim --dumpSteeringFile > mySteer.py`
     - `ddsim --steeringFile=mySteer.py --compactFile myDetector.xml`

### DD4hep v01-08

* 2018-07-02 Markus Frank ([PR#418](https://github.com/aidasoft/dd4hep/pull/418))
  - Add DDCodexB in standalone mode with simulation script and basic skeleton for DDEve

* 2018-06-28 Markus Frank ([PR#417](https://github.com/aidasoft/dd4hep/pull/417))
  - Steer debug printouts in CondDB2DDDB and DDDB2Objects by parsing xml files.

* 2018-06-26 Markus Frank ([PR#416](https://github.com/aidasoft/dd4hep/pull/416))
  - Separate the hit class and add dictionary. No base class - entirely independent.
  - Allow to save the hit class to ROOT (but without MC truth)
    See MyTrackerHit.h for details.

* 2018-06-26 Markus Frank ([PR#415](https://github.com/aidasoft/dd4hep/pull/415))
  - Add small example how to specialize a new sensitive action and attach it to a detector in DDG4.

* 2018-06-26 Frank Gaede ([PR#414](https://github.com/aidasoft/dd4hep/pull/414))
  - bug fix in Geant4EventReaderGuineaPig
       - fix ignoring input lines with 'nan'

* 2018-06-26 Shaojun Lu ([PR#412](https://github.com/aidasoft/dd4hep/pull/412))
  - Added one more if statement: If the track went into new Volume, 
    - then extracted the hit in previous Volume,
    - and start a new hit in this current Volume,
      - in this current process, also allow the same following treatments for the new hit.

* 2018-06-21 Markus Frank ([PR#409](https://github.com/aidasoft/dd4hep/pull/409))
  - Support out-of-source builds of DD4hep examples.
    Comes with an expense: A new environment DD4hepExamplesINSTALL.
    has to be defined to support internal file accesses and loads.
    The builds were also checked with read-only installation directories.
    Solves issue https://github.com/AIDASoft/DD4hep/issues/382
  - Smallish improvement to the ConditionsManager.

* 2018-06-21 Andre Sailer ([PR#408](https://github.com/aidasoft/dd4hep/pull/408))
  - Cmake: fix for configuring with Geant4 with internal CLHEP, fixes #406 
  - Cmake: fix for configuring with BUILD_TESTING=OFF, fixes #407

* 2018-06-07 Markus Frank ([PR#404](https://github.com/aidasoft/dd4hep/pull/404))
  - Fix basic shape tests for PseudoTrap

* 2018-06-07 Markus Frank ([PR#403](https://github.com/aidasoft/dd4hep/pull/403))
  - patch for truncated tubes shapes.

* 2018-06-04 Markus Frank ([PR#402](https://github.com/aidasoft/dd4hep/pull/402))
  - Fix truncated tube shape

* 2018-06-04 Markus Frank ([PR#400](https://github.com/aidasoft/dd4hep/pull/400))
  - Allow for world volumes other than boxes. See `examples/ClientTests/compact/WorldVolume.xml` how to set it up. The effective thing is that the top level volume must be set to the TGeoManager before `Detector::init()`. If a top level volume is set, it is implicitly assumed to be the world volume. Otherwise the already existing mechanism (box volume) is activated.
  - Add new basic shape tests.

* 2018-06-01 Markus Frank ([PR#399](https://github.com/aidasoft/dd4hep/pull/399))
  - As discussed in issue #398 The use of TGeoUnits is inconvenient. The dd4hep units are now exposed in the python modules.
  - Basic shapes are now tested in the regular ctest executions. The mesh vertices of the shapes were 
  saved to a reference file and are compared to in subsequent runs. The reference files reside in 
  `examples/ClienTests/ref`. See `examples/ClientTests/compact/Check_Shape_*.xml` for details.
  - The ROOT UI  and some dump plugins were enhanced to expose more information.

* 2018-05-30 Markus Frank ([PR#397](https://github.com/aidasoft/dd4hep/pull/397))
  - Enable to start DDG4 using a saved detector description in a ROOT file.
     -  Added corresponding test: `Persist_CLICSiD_Geant4_LONGTEST`
  - Fix shape constructors for Trap and PseudoTrap
  - The python module `DD4hep.py` is gone as discussed in the developers meeting use `dd4hep.py` instead.
      - on masOS : your "git pull" possibly deletes both files. you may have to checkout `dd4hep.py` again, due to fact that the filesystem is case-insensitive. 
  - Add example for LHCb CODEX-b.

* 2018-05-29 Markus Frank ([PR#394](https://github.com/aidasoft/dd4hep/pull/394))
  - Consistently handle cmake command line options in case no Geant4 or no documentation should be built.

* 2018-05-28 Markus Frank ([PR#393](https://github.com/aidasoft/dd4hep/pull/393))
  - Improvements to `geoPluginRun`.
    `$> geoPluginRun -ui -interactive`
    results in DD4hep enabled ROOT prompt.
  - DD4hepUI: improvements to interact with DD4hep instance from ROOT prompt
  - DDDB improve configuration for printing and debugging
  - DDDB: allow to block certain XML branches

* 2018-05-22 Frank Gaede ([PR#389](https://github.com/aidasoft/dd4hep/pull/389))
  - fix bug in input handling, for details see discussion #387 
     - exclude leptons with zero lifetime from Geant4

* 2018-05-22 Markus Frank ([PR#388](https://github.com/aidasoft/dd4hep/pull/388))
  - Update doxygen information for some undocumented classes. 
   - Add licence header to files where not present.

* 2018-05-22 Marko Petric ([PR#380](https://github.com/aidasoft/dd4hep/pull/380))
  - Update LICENSE to LGPLv3
    - The name of the file containing the LICENSE has ben changed from LICENCE->LICENSE as all source files reference `For the licensing terms see $DD4hepINSTALL/LICENSE.`

* 2018-05-16 Markus Frank ([PR#386](https://github.com/aidasoft/dd4hep/pull/386))
  - Fix bug in variable order of `ExtrudedPolygon` (x<->y)

* 2018-05-15 Markus Frank ([PR#384](https://github.com/aidasoft/dd4hep/pull/384))
  # Implementation of non-cylindrical tracking region (resolves #371)
    -  It is possible to define volumes in a parallel world such as e.g. a tracking region. In principle any volume hierarchy may be attached to the parallel world. None of these volumes participate in the tracking as long as the "connected" attribute is set to false. The hierarchy of parallel world volumes can be accessed from the main detector object using
       ```cpp
       dd4hep::Volume parallel = dd4hep::Description::parallelWorldVolume()
       ```
    This parallel world volume is created when the geometry is opened together (and with the same dimensions) as the world volume itself.
    -  IF the NAME of the volumes is "tracking_volume" within the compact notation it is declared as the Detector's trackingVolume entity and is accessible as well:
       ```cpp
       dd4hep::Volume trackers = dd4hep::Description::trackingVolume()
       ```
    -  Although the concept is available in the DD4hep core, it's configuration from XML is only implemented for the compact notation. For details see the example `examples/ClientTests/compact/TrackingRegion.xml`.
     -  If the volume should be connected to the world:   connected="true". This is useful for debugging because  the volume can be visualized else if the volume is part of the parallelworld: connected="false". The volume is always connected to the top level. The anchor detector element defines the base transformation to place the volume within the (parallel) world.
  
  ```xml
       <parallelworld_volume name="tracking_volume" anchor="/world" material="Air" connected="true" vis="VisibleBlue">
         <shape type="BooleanShape" operation="Subtraction">
           <shape type="BooleanShape" operation="Subtraction">
             <shape type="BooleanShape" operation="Subtraction"  >
               <shape type="Tube" rmin="0*cm" rmax="100*cm" dz="100*cm"/>
               <shape type="Cone" rmin2="0*cm" rmax2="60*cm" rmin1="0*cm" rmax1="30*cm" z="40*cm"/>
               <position x="0*cm" y="0*cm" z="65*cm"/>
             </shape>
             <shape type="Cone" rmin1="0*cm" rmax1="60*cm" rmin2="0*cm" rmax2="30*cm" z="40*cm"/>
             <position x="0" y="0" z="-65*cm"/>
           </shape>
           <shape type="Cone" rmin2="0*cm" rmax2="55*cm" rmin1="0*cm" rmax1="55*cm" z="30*cm"/>
           <position x="0" y="0" z="0*cm"/>
         </shape>
         <position x="0*cm"   y="50*cm" z="0*cm"/>
         <rotation x="pi/2.0" y="0"     z="0"/>
       </parallelworld_volume>
  ```
  
  
  # Enhancement of assemblies, regions and production cuts (resolves #373)
  On request from FCC particle specific production cuts may be specified in the compact notation. These production cuts (Geant4 currently supports these for e+, e-, gammas and protons) are specified as "cut" entities in the limitset. (See the example `examples/ClientTests/compact/Assemblies.xml`).
  
    - The hierarchy of cuts being applied is:
        - If present particle specific production cuts for a region are applied.
        - else the "cut" attribute of the compact region specification is used
        - else the global Geant4 cut is automaticallly applied by Geant4.
  
  ```xml
    <limits>
      <limitset name="VXD_RegionLimitSet">
        <!--
             These are particle specific limits applied to the region
             ending in Geant4 in a G4UserLimits instance
        -->
        <limit name="step_length_max"  particles="*" value="5.0" unit="mm" />
        <limit name="track_length_max" particles="*" value="5.0" unit="mm" />
        <limit name="time_max"         particles="*" value="5.0" unit="ns" />
        <limit name="ekin_min"         particles="*" value="0.01" unit="MeV" />
        <limit name="range_min"        particles="*" value="5.0" unit="mm" />
  
        <!--
             These are particle specific production cuts applied to the region
             ending in Geant4 in a G4ProductionCuts instance
        -->
        <cut   particles="e+"          value="2.0"   unit="mm" />
        <cut   particles="e-"          value="2.0"   unit="mm" />
        <cut   particles="gamma"       value="5.0"   unit="mm" />
      </limitset>
    </limits>
  ```
  
  # SensitiveDetector types not changed by Geant4SensDetActionSequence (resolves #378)
  The sensitive detector type defined in the detector constructors is no longer changed intransparently in the back of the users. This may have side-effects for creative detector constructor writers, who invent sd types out of the sky. These obviously will not work with Geant4, because in Geant4 a mapping of these types must be applied to supported sensitive detectors. Now the mapping of a sd type (e.g. "tracker") is strict in the python setup. The default factory to create any sensitive detector instance in Geant4 (ie. an object of type G4VSensitiveDetector, G4VSDFilter, Geant4ActionSD) is a property of the Geant4Kernel  instance and defaults to:
    ```cpp
     declareProperty("DefaultSensitiveType", m_dfltSensitiveDetectorType = "Geant4SensDet");
    ```
     - Since the actual behavior is defined in the sequencer instanciated therein this default should be sufficient for 99.99 % of all cases. Otherwise the factory named "Geant4SensDet" may be overloaded.

* 2018-05-15 David Blyth ([PR#379](https://github.com/aidasoft/dd4hep/pull/379))
  - Geant4FieldTrackingConstruction now properly overrides `constructField()`

* 2018-05-03 David Blyth ([PR#377](https://github.com/aidasoft/dd4hep/pull/377))
  - Geant4Handle unhandled reference to shared actions.  This affected the destruction of shared actions.

* 2018-05-03 Markus Frank ([PR#375](https://github.com/aidasoft/dd4hep/pull/375))
  - Development of a small user example on how to do analysis in `DDG4`.
     - See `examples/DDG4/src/HitTupleAction.cpp`
     - Simply collect the energy deposits of hits and write an N-tuple with them.
     - The example shows how to access the hit collections and to extract the data in order to write other more sophisticated analyses.
  
   - This `DDG4` action is used in one of the Minitel examples: `examples/ClientTests/srcipts/MiniTelEnergyDeposits.py`

* 2018-05-02 Markus Frank ([PR#374](https://github.com/aidasoft/dd4hep/pull/374))
  - recommission the multithreaded SiD example 
     - `DDG4/examples/SiDSim_MT.py` vs. `DDG4/examples/SiDSim.py`

* 2018-04-19 Markus Frank ([PR#370](https://github.com/aidasoft/dd4hep/pull/370))
  * Allow to disable building the documentation cmake option BUILD_DOCS. By default ON and backwards compatible. If set to OFF no doc shall be built. (not everybody has biber installed)
  * Move from `DD4hep.py` to `dd4hep.py`, since `DD4hep.py` has to disappear due to conflicts on MAC.

* 2018-04-13 Markus Frank ([PR#367](https://github.com/aidasoft/dd4hep/pull/367))
  - resolves #361
    The Detector object has a state `Detector::state()` with three values:
    ```cpp
      /// The detector description states
      enum State   {
        /// The detector description object is freshly created. No geometry nothing.
        NOT_READY = 1<<0,
        /// The geometry is being created and loaded. (parsing ongoing)
        LOADING   = 1<<1,
        /// The geometry is loaded.
        READY     = 1<<2
      };
    ```
      It starts with `NOT_READY`, moves to `LOADING` once the geometry is opened and goes to `READY` once the geometry is closed. As suggested in the developers meeting: the initial field object is invalid and gets created only once the geometry is opened. As a corollary, the field may not be accessed before. Geometry parsers must take this behavior into account! 
  
  - Address some compiler warnings.
    - Mainly add override/final statements in header files.
  - Implement a module to invoke python as a DD4hep plugin:
    invoked e.g. by: `geoPluginRun -plugin DD4hep_Python -dd4hep -prompt`
    ```
    geoPluginRun -plugin DD4hep_Python -help
    Usage: -plugin <name> -arg [-arg]                                                  
       name:   factory name     DD4hep_Python                                        
       -import  <string>        import a python module, making its classes available.
       -macro   <string>        load a python script as if it were a macro.          
       -exec    <string>        execute a python statement (e.g. import ROOT.    
       -eval    <string>        evaluate a python expression (e.g. 1+1)          
       -prompt                  enter an interactive python session (exit with ^D)   
       -dd4hep                  Equivalent to -exec "import dd4hep"                
       -help                    Show this online help message.                       
  
       Note: entries can be given multiple times and are executed in exactly the     
             order specified at the command line!                      
    ```
    Implementation wise the plugin is a simple CLI wrapper for TPython.

* 2018-04-12 Marko Petric ([PR#362](https://github.com/aidasoft/dd4hep/pull/362))
  - Update DD4hepManual

* 2018-04-12 Markus Frank ([PR#360](https://github.com/aidasoft/dd4hep/pull/360))
  - Examples: only build some examples depending on the availability of dependencies.
  - DDCore: Add interface to allow URI blocking during file parsing. Default is as now.
  - DDCMS: Add conversion of new shapes.

* 2018-04-10 Markus Frank ([PR#359](https://github.com/aidasoft/dd4hep/pull/359))
  - Bunch of fixes. Mostly in `examples/DDDB`
  - Only build `examples/DDDB` if XercesC is present.
  - Only build `examples/DDCMS` if CLHEP is present

* 2018-04-09 Markus Frank ([PR#357](https://github.com/aidasoft/dd4hep/pull/357))
  - Add configuration options for loading DDDB

* 2018-04-05 Markus Frank ([PR#351](https://github.com/aidasoft/dd4hep/pull/351))
  - To avoid unwanted disappearing conditions sub pools, a conditions slice may be instructed to collect shared references to the used pools in the slice.
  - For python:
    - Move DDG4/SystemOfUnits.py to DDG4/g4units.py
      Keep SystemOfUnits.py with deprecation warning
    - move DD4hep.py to dd4hep.py. 
      import dd4hep also imports all TGeoUnit units into its namespace.
      Hence: import dd4hep; print dd4hep.m  gives: "100.0"
    - DD4hep.py is kept for backwards compatibility issuing a deprecation warning
    - DDG4.py: imports g4units    as G4Units:         DDG4.G4Units.m etc.
    - DDG4.py: imports TGeoUnit as TGeo4Units:  DDG4.TGeoUnits.m etc.
    - Some problem with replacing DD4hepUnits.h with TGeoSystemOfUnits.h
      Surface test complains. To be investigated. Keep old DD4hepUnits for the time being.

* 2018-04-05 Markus Frank ([PR#350](https://github.com/aidasoft/dd4hep/pull/350))
  - Merge `DDCMS` and `DDCMSTests` to `DDCMS`
  - Move `DDDB` to the `examples/`
  - Add tests `DDDB_DeVelo` and `DDDB_DeVelo_Gaudi` missing from #349

* 2018-04-05 Markus Frank ([PR#349](https://github.com/aidasoft/dd4hep/pull/349))
  - Resolves #339 
  - DDDB conditions had a bug when loading from file base. The IOV was not handled properly. Now the resulting IOV is configurable using properties.
  - Added Gaudi like example use case for options handling with the DeVelo detector elements.
  - Configuration improvement in DDG4 action Output2ROOT:
    - New property "DisableParticles" allows to suppress the MCParticle record from being written to the ROOT file.
    - dto. the option "DisabledCollections" allows to NOT write any hit collection.
    - Unit tests for these options are not (yet) present.
  - DDCond: allow for user defined conditions cleanup policies. Base class `dd4hep::cond::ConditionsCleanup`. Callbacks are issued to the class for IOV type pools and IOV dependent pools asking if the pools should be processed.

* 2018-04-05 Marko Petric ([PR#344](https://github.com/aidasoft/dd4hep/pull/344))
  - Move `DDCMS` into examples as it is not core functionality

### DDKalTest v01-06

* 2019-02-19 Andre Sailer ([PR#11](https://github.com/iLCSoft/DDKalTest/pull/11))
  - DDPlanarMeasLayer: use proper "height" to calculate sortingPolicy for DD4hep::Trapezoids, a.k.a. TGeoTrd2
  - DDPlanarMeasLayer: if SortingPolicy value is present in the DoubleParameters extension for the DetElement of a surface use that number, plus epsilon.
  - Requires AidaSoft/DD4hep#486 to compile, iLCSoft/lcgeo#234 with an example that sets this extension

### LCIO v02-13-01

* 2019-11-15 Frank Gaede ([PR#67](https://github.com/ilcsoft/LCIO/pull/67))
  - fix building for MacOS 10.14
      - rm superfluous `#include "/usr/include/sys/types.h"` 
         (thanks P.Mato)

* 2019-10-30 Remi Ete ([PR#66](https://github.com/ilcsoft/LCIO/pull/66))
  - Moved all stream operator overloads of EVENT class types into EVENT namespace (moved out from UTIL namespace)

### LCIO v02-13

* 2019-10-15 Marko Petric ([PR#61](https://github.com/iLCSoft/LCIO/pull/61))
  - Make pyLCIO compatible with Python3

* 2019-09-25 Frank Gaede ([PR#64](https://github.com/iLCSoft/LCIO/pull/64))
  - fix the writeEventTree test  (fixes #62)

* 2019-09-25 Marko Petric ([PR#63](https://github.com/iLCSoft/LCIO/pull/63))
  - Update CI to newer version of ROOT 6.18/04 (LCG_96b)
  - Fix issue that in the build folder the rootdicts were in the wrong location

* 2019-08-08 Frank Gaede ([PR#60](https://github.com/iLCSoft/LCIO/pull/60))
  - re-introduce `std::set_terminate` in `LCIOExceptionHandler`, which is not deprecated in c++17

* 2019-08-08 Ete Remi ([PR#54](https://github.com/iLCSoft/LCIO/pull/54))
  - Added executable to perform IO benchmarking on LCIO file reading

* 2019-07-19 Remi Ete ([PR#59](https://github.com/iLCSoft/LCIO/pull/59))
  - Added `lcio_perf` utility. Evaluate:
       - Total / mean writing time for 5000 events (sim job)
       - Total / mean reading time for 5000 events

* 2019-07-09 Marko Petric ([PR#58](https://github.com/iLCSoft/LCIO/pull/58))
  - Remove `std::set_unexpected` and `std::set_terminate` which were removed in C++17

### Gear v01-09

* 2019-08-07 Frank Gaede ([PR#5](https://github.com/iLCSoft/GEAR/pull/5))
  - make compatible with c++17:
        - remove all `throw(...)` declarations

### LCPandoraAnalysis v02-00-01

* See pull requests:
  - [PR#12](https://github.com/PandoraPFA/LCPandoraAnalysis/pull/12)
  - [PR#13](https://github.com/PandoraPFA/LCPandoraAnalysis/pull/13)
  - [PR#14](https://github.com/PandoraPFA/LCPandoraAnalysis/pull/14)
  - [PR#15](https://github.com/PandoraPFA/LCPandoraAnalysis/pull/15)

### aidaTT v00-10

* 2019-02-04 Frank Gaede ([PR#23](https://github.com/AIDAsoft/aidaTT/pull/23))
  - make example material_ntuples.cpp work w/ current DD4hep 
          - c'tor of  MaterialManager() now takes a volume ...

### FCalClusterer v01-00-01

* 2018-05-16 Shaojun Lu ([PR#59](https://github.com/fcalsw/fcalclusterer/pull/59))
  - added "FIND_PACKAGE( Doxygen REQUIRED )" for doc/CMakeLists.txt.
    - to build document with available Doxygen with "INSTALL_DOC=ON".

* 2018-05-15 Andre Sailer ([PR#58](https://github.com/fcalsw/fcalclusterer/pull/58))
  -  CI: Add build on CC7
  - CMAKE: fix linker problem on CC7 (newer ld version)

* 2018-05-15 Andre Sailer ([PR#57](https://github.com/fcalsw/fcalclusterer/pull/57))
  - Doc: add doxygen file

* 2018-05-14 Andre Sailer ([PR#56](https://github.com/fcalsw/fcalclusterer/pull/56))
  - CMAKE: use TARGET_[INCLUDE_DIRECTORIES|LINK_LIBRARIES|COMPILE_DEFINITIONS] instead of global include or linking

* 2018-05-08 Andre Sailer ([PR#55](https://github.com/fcalsw/fcalclusterer/pull/55))
  - CMake: let include directories be decided via dependencies

### lcgeo v00-16-05

* 2019-12-11 Ete Remi ([PR#240](https://github.com/iLCSoft/lcgeo/pull/240))
  - Fixed steering file for unit test. Get units from g4units.

* 2019-12-11 Daniel Jeans ([PR#239](https://github.com/iLCSoft/lcgeo/pull/239))
  - SEcal06 driver: add absorber layer thickness to layer information (this had been missing)

### lcgeo v00-16-04

* 2019-09-11 Andre Sailer ([PR#237](https://github.com/iLCSoft/lcgeo/pull/237))
  - CLIC_o4_v14: New CLIC detector model with DECal, based on CLIC_o3_v14. Ported from https://github.com/robbie-bosley/CLIC_DECAL

* 2019-05-23 Emilia Leogrande ([PR#236](https://github.com/iLCSoft/lcgeo/pull/236))
  - FCCee_o2_v01: new detector model with smaller beampipe radius (10 mm instead of 15 mm) and closer vertex subdetector

* 2019-02-20 Emilia Leogrande ([PR#235](https://github.com/iLCSoft/lcgeo/pull/235))
  - FCCee_o1_v04: Implemented changes the new sorting policy
     - Analogous of #234

* 2019-02-19 Andre Sailer ([PR#234](https://github.com/iLCSoft/lcgeo/pull/234))
  - Plugin: lcgeo_LinearSortingPolicy : new plugin to set the sorting policy for surfaces identified by placement path based on their z position and a linear function, requires AIDASoft/DD4hep#486
  - CLIC_o3_v14: add use of lcgeo_LinearSortingPolicy for TrackerEndcaps
  - TrackerEndcapSupport_o1_v01: attach support volumes to different DetElements so we can attach different extensions to them

* 2018-11-07 Marko Petric ([PR#232](https://github.com/iLCSoft/lcgeo/pull/232))
  - Add vis attribute for better visualisation of VertexEndcap_o1_v06

* 2018-11-01 Marko Petric ([PR#231](https://github.com/iLCSoft/lcgeo/pull/231))
  - Add vis attribute for better visualisation of `TrackerEndcap_o1_v02`

* 2018-08-23 Oleksandr Viazlo ([PR#229](https://github.com/iLCSoft/lcgeo/pull/229))
  - new FCCee_o1_v04 detector model: 
    - update on MDI and shielding from Anna
    - merge Materials_v01.xml and materials.xml into one file and remove unused items

* 2018-08-09 Andre Sailer ([PR#228](https://github.com/iLCSoft/lcgeo/pull/228))
  - ddsim program moved to DD4hep, AIDAsoft/DD4hep#420

* 2018-07-05 Andre Sailer ([PR#225](https://github.com/iLCSoft/lcgeo/pull/225))
  - Tests: Using other cmake variables to be able to pick up the lcgeo tests from outside of lcgeo

