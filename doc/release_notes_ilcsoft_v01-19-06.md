# iLCSoft v01-19-06

Packages changed wrt. to v01-19-05.


## Garlic v03-01

* 2018-03-16 Marko Petric ([PR#1](https://github.com/iLCSoft/Garlic/pull/1))
  - Add formatting LICENCE and CI

* 2018-03-22 Marko Petric ([PR#2](https://github.com/iLCSoft/Garlic/pull/2))
  -  Fix for iLCSoft/LCIO#35

## lcio v02-12

* 2018-01-10 Frank Gaede ([PR#43](https://github.com/ilcsoft/lcio/pull/43))
  -  Remove dynamic exception specification from C++ headers

* 2018-01-12 Frank Gaede ([PR#46](https://github.com/ilcsoft/lcio/pull/46))
  - fix unused warning in test_randomaccess.cc 
  - bug fix in cmake/LCIOConfig.cmake.in (fixes DD4hep part of #45)

* 2018-01-12 Frank Gaede ([PR#44](https://github.com/ilcsoft/lcio/pull/44))
  - fix last warnings (gcc5.4)
       - dont create LCIOLibDeps.cmake (fix Policy CMP0033) 
       - fix warnings in UTIL::LCFourVector

* 2018-03-23 Frank Gaede ([PR#35](https://github.com/ilcsoft/lcio/pull/35))
  - Remove using namespace from header files


## lcgeo v00-16

* 2018-02-22 Dan Protopopescu ([PR#201](https://github.com/iLCSoft/lcgeo/pull/201))
  - Removed some unused parameters

* 2018-02-22 Daniel Jeans ([PR#200](https://github.com/iLCSoft/lcgeo/pull/200))
  - to ensure that consistent maximum step lengths are used in all models, moved their definition to common directory

* 2018-02-27 Daniel Jeans ([PR#199](https://github.com/iLCSoft/lcgeo/pull/199))
  - implement downstream magnets in ILD models:
      - thickened beampipe in regions of final focus magnets
      - should reproduce the Mokka models
      - currently verifying positions with accel. experts, so details may still change

* 2018-02-26 Andre Sailer ([PR#203](https://github.com/iLCSoft/lcgeo/pull/203))
  - DDSim: allow passing arbitrary arguments to add_argument, needed for #196 , purely behind the scenes

* 2018-02-28 Daniel Jeans ([PR#204](https://github.com/iLCSoft/lcgeo/pull/204))
  - implement step limits in SEcal06 driver (SEcal06_Helpers.cpp)
  - apply cal_limits to ECAL descriptions (barrel, endcap, ECring) in ILD_common_v02

* 2018-02-28 Ete Remi ([PR#196](https://github.com/iLCSoft/lcgeo/pull/196))
  - Added new command line parameters to ddsim
      - --eventParameters (list) to write event parameters to every output lcio events
      - --runNumberOffset (int) to offset the run number counter in lcio output file
      - --eventNumberOffset (int) to offset the event number counter in lcio output file

* 2018-02-13 Andre Sailer ([PR#197](https://github.com/iLCSoft/lcgeo/pull/197))
  - DDSim: Print the startUp and event processing time separately in addition to total runtime

* 2017-12-01 TiborILD ([PR#186](https://github.com/iLCSoft/lcgeo/pull/186))
  - update ILD models w/ SDHcal:
         - change the names of original SimCalorimeterHit collections of SDHCAL to the same ones as introduced in hybrid models, i.e. HCalBarrelRPCHits, HCalEndcapRPCHits,HCalECRingRPCHits

* 2017-11-23 Dan Protopopescu ([PR#185](https://github.com/iLCSoft/lcgeo/pull/185))
  * SiD_o2_v02: Fix BeamCal segmentation (thanks to @shaojunlu), Fixes #184

* 2017-11-23 Shaojun Lu ([PR#183](https://github.com/iLCSoft/lcgeo/pull/183))
  - Update lcgeoTests for ILD to ILD_l5_v02 and ILD_s5_v02.
      - the current models for optimisation studies, will be tested during the build.

* 2018-03-16 Frank Gaede ([PR#210](https://github.com/iLCSoft/lcgeo/pull/210))
  - improve TPCSDAction
     - enable writing of TPCSpacePoint and TPCLowPtCollections
     - TPCLowPtCollections is only written if `TPCLowPtStepLimit==true`
     - add steering properties to TPCSDAction 
     - use  in ddsim:
             `SIM.action.mapActions['tpc'] = ('TPCSDAction', {'TPCLowPtCut': 10*MeV , 'TPCLowPtStepLimit' : True })`
     - use Mokka default values:
  ```
  	Control.TPCLowPtCut = CLHEP::MeV ;
  	Control.TPCLowPtStepLimit = false ;
  	Control.TPCLowPtMaxHitSeparation = 5. * CLHEP::mm ;
  ```
    -  properly access layerID through IDDescriptor

* 2018-03-14 Daniel Jeans ([PR#209](https://github.com/iLCSoft/lcgeo/pull/209))
  - new driver for tube of square cross-section (BoxSupport_o1_v01_geo.cpp)
  - new driver for yoke endcaps with square central hole (Yoke06_Endcaps.cpp)
  - adjust description of QD0 and first extraction quad, and add its cryostat
  - remove more upstream magnets
  - include forward region support tubes: around QD0, outer tube froum outside -> LHCAL, and between ecal endcap and ring
  - update yoke design to fit with this support structure
  - implement the above in the ILD_?5_v02 models

* 2017-12-12 Dan Protopopescu ([PR#188](https://github.com/iLCSoft/lcgeo/pull/188))
  Version 3 of the SiD option 2 model (not final though). Main changes and updates:
  - cleaned up all XMLs
  - using DetIDs
  - unified segmentation and cell ID encoding
  - added type_flags where missing
  - updated plugins
  - added envelopes where missing
  - stepped design Muon calorimeters use now scintillator instead of RPCs
  - merged barrel+endcap envelopes for the Muon calorimeter
  - added or updated certain drivers
  - included alternate brass HCal 
  - added common tracker barrel+endcap envelope
  - implemented some ECal barrel driver fixes
  - checked: no overlaps
  - added test_SiD_o2_v03
  
  To check:
  - Muon caloData definitions
  - ECal towers visibility attributes
  - LumiCal and BeamCal envelopes
  
  A detailed table of changes is available in
  https://www.evernote.com/l/AJ2Q2yTuLwRGVqYpSNB8HRKx-iBxYQ6Ry0s

* 2018-03-05 Frank Gaede ([PR#207](https://github.com/iLCSoft/lcgeo/pull/207))
  -  activate G4StepLimiterPhysics in DDSim by default
      - needed to limit the steps in detector volumes and regions

* 2018-03-05 Dan Protopopescu ([PR#202](https://github.com/iLCSoft/lcgeo/pull/202))
  Minor corrections to SiD_o2_v03:
  - Corrected LumiCal grid size parameters
  - Added hole in the BeamCal (beam pipe parameters not used with the current driver)
  - Removed DetType_AUXILIARY flag from BeamCal
  - Removed some unused parameters

* 2018-03-28 Frank Gaede ([PR#214](https://github.com/iLCSoft/lcgeo/pull/214))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`

* 2017-12-11 Oleksandr Viazlo ([PR#193](https://github.com/iLCSoft/lcgeo/pull/193))
  - new FCCee_o1_v02 detector model
  - Material budget of VTX was increased for 50%
  - change of LumiCal_cell_size from 1.0 to 1.81 mm, change of LumiCall offset
  - add test for FCCee_o1_v02 model, remove test for FCCee_o1_v01

* 2017-12-04 Andre Sailer ([PR#189](https://github.com/iLCSoft/lcgeo/pull/189))
  - Add CLIC_o3_v14 with fixed LumiCal segmentation

* 2017-12-04 Frank Gaede ([PR#187](https://github.com/iLCSoft/lcgeo/pull/187))
  - Set DDSim defaults to Geant4 defaults and retain `largest_step = 10 * m` as recommended in the Geant4 manual (~ detector size). This improves simulation time for single muons approximately a factor 2 and for single pi+ for 25%

* 2018-03-27 Ete Remi ([PR#213](https://github.com/iLCSoft/lcgeo/pull/213))
  - DD4hepSimulation:
     - Fixed division by zero when no event has been processed, Fixes #208

* 2018-03-22 Oleksandr Viazlo ([PR#211](https://github.com/iLCSoft/lcgeo/pull/211))
  - create FCCee_dev detector model (extended ECAL endcap, shrinked HCAL ring, reduced magnetic field in yoke from 1.5 T to 1.0 T)
  - add test for the model

* 2018-03-23 Daniel Jeans ([PR#212](https://github.com/iLCSoft/lcgeo/pull/212))
  - writeAllILDCompactDescriptions.py: python script to create compact detector descriptions with different variations: large/small, ideal/realistic fields at 250/500 GeV, with or without anti-DID fields, different reconstruction options
  - compact descriptions all kept in one directory ILD_sl5_v02
  - each model is linked individually
  - some models are not yet functional: in particular small models with realistic fields, for which no field maps are yet available. [ ie ILD_s5_v03, v04, v05, v06 ]
  - ILD_?5_v02 models and their options should be completely unchanged


## DD4hep v01-07

* 2018-03-26 Javier Cervantes Villanueva ([PR#343](https://github.com/AIDASoft/DD4hep/pull/343))
  - Fix bug in calculating eta, introduced in #138 
    - use `magFromXYZ` instead of `radiusFromXYZ` to calculate pseudorapidity

* 2018-03-19 Frank Gaede ([PR#338](https://github.com/AIDASoft/DD4hep/pull/338))
  - Include fixes from Chris Burr for the alignments calculator.
   - Add a small study for the LHCb upgrade defining reasonable detector element conditions for the Velo pixel detector using the DDCond derived condition mechanism.
   - To be done: somehow get an example for this mechanism, which works outside Gaudi.

* 2018-03-23 Markus Frank ([PR#340](https://github.com/AIDASoft/DD4hep/pull/340))
  - Improvement for DDDB - case study to implement real-world detector elements.

* 2018-03-28 Frank Gaede ([PR#345](https://github.com/AIDASoft/DD4hep/pull/345))
  - Remove `DDSurfaces` folder as it was merged in `DDRec`

* 2018-03-28 Frank Gaede ([PR#341](https://github.com/AIDASoft/DD4hep/pull/341))
  - Remove top level `DDSegmentation` folder as it is not needed anymore


## gear v01-08

* 2018-01-12 Frank Gaede ([PR#1](https://github.com/iLCSoft/gear/pull/1))
  - fix all compiler warnings (gcc5.4)
      - uninitialized, unused, shadow, ...
      - don't create GEARLibDeps.cmake 
      - also fix warnings in tinyxml

* 2018-01-15 Frank Gaede ([PR#2](https://github.com/iLCSoft/gear/pull/2))
  - fix export of CLHEP library dependency
        - resolve location of CLHEP::CLHEP import target

* 2018-01-16 Frank Gaede ([PR#4](https://github.com/iLCSoft/gear/pull/4))
  - fix more warnings in tinyxml.h

* 2018-01-16 Frank Gaede ([PR#3](https://github.com/iLCSoft/gear/pull/3))
  - move tinyxml.h back to gearxml (for MarlinTPC) 
  - rm check for this!=0 in tinyxml.h (-Wundefined-bool-conversion warning w/ clang)


## MarlinFastJet v00-05-01

## KalTest v02-04

* 2018-01-31 Frank Gaede ([PR#2](https://github.com/iLCSoft/KalTest/pull/2))
  - fix all compiler warnings (gcc54-ub1604)

* 2017-11-30 Andre Sailer ([PR#1](https://github.com/iLCSoft/KalTest/pull/1))
  - Running profiling, replace dynamic_cast with static_cast as dynamic_cast return value is never checked, see also AIDAsoft/aidaTT#19


## KalDet v01-14-01

* 2018-01-31 Frank Gaede ([PR#2](https://github.com/iLCSoft/KalDet/pull/2))
  - silence all compiler warnings by using:
      - `"-Wno-effc++ -Wno-unused-parameter"`
      - and SYSTEM includes
  - future users/maintainers should consider to actually **fix these warnings**


## aidaTT v00-09

* 2018-01-18 Frank Gaede ([PR#21](https://github.com/AIDASoft/aidaTT/pull/21))
  - fix default initialization of reference to abstract (osx-llvm)

* 2018-01-17 Frank Gaede ([PR#20](https://github.com/AIDASoft/aidaTT/pull/20))
  -fix all warnings (gcc54-ub1604)

* 2018-03-28 Frank Gaede ([PR#22](https://github.com/AIDASoft/aidaTT/pull/22))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`

* 2017-11-30 Andre Sailer ([PR#19](https://github.com/AIDASoft/aidaTT/pull/19))
  - Performance optimisation from running profiler (Intel VTune Amplifier)


## DDKalTest v01-05

* 2018-01-19 Frank Gaede ([PR#8](https://github.com/iLCSoft/DDKalTest/pull/8))
  - fix all compiler warnings (gcc54-ub1604)
  - use const ptr for lcio::TrackerHit and dd4hep::Surface

* 2018-01-22 Frank Gaede ([PR#9](https://github.com/iLCSoft/DDKalTest/pull/9))
  - revert usage of const EVENT::TrackerHit*

* 2018-03-28 Frank Gaede ([PR#10](https://github.com/iLCSoft/DDKalTest/pull/10))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`



## MarlinTrk v02-07

* 2018-03-13 Frank Gaede ([PR#11](https://github.com/iLCSoft/MarlinTrk/pull/11))
  - Fix for iLCSoft/LCIO#35

* 2018-03-23 Frank Gaede ([PR#12](https://github.com/iLCSoft/MarlinTrk/pull/12))
  - use the origin as reference point in MarlinTrk::createPrefit() for initial helix
      - this improves the fit probability for Si-tracks (in ILD)
      - similar issues reported by CLICdp

* 2018-03-28 Frank Gaede ([PR#13](https://github.com/iLCSoft/MarlinTrk/pull/13))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`

* 2017-11-30 Andre Sailer ([PR#10](https://github.com/iLCSoft/MarlinTrk/pull/10))
  - Performance optimisation, avoiding dynamic_cast, see also  AIDAsoft/aidaTT#19
  - Fix compiler warnings for uninitialised members


## MarlinTrkProcessors v02-10

* 2018-03-02 Emilia Leogrande ([PR#34](https://github.com/iLCSoft/MarlinTrkProcessors/pull/34))
  - New Processor: ClonesAndSplitTracksFinder for running after ConformalTracking
    - This processor has a track collection as input, removes all possible clones (tracks sharing at least 2 hits), looks for split tracks (tracks in a certain space region with similar track parameters) and merges them. If more than two tracks happen to fulfil the requirements, no merging is applied at the moment.

* 2018-02-25 Ete Remi ([PR#33](https://github.com/iLCSoft/MarlinTrkProcessors/pull/33))
  - DDPlanarDigiProcessor
      - Added time information to tracker hit 
  - DDSpacePointBuilder
      - Added time information to space point as the earliest time of the two tracker hits

* 2018-03-28 Frank Gaede ([PR#36](https://github.com/iLCSoft/MarlinTrkProcessors/pull/36))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`


## Clupatra v01-03

* 2018-01-31 Frank Gaede ([PR#13](https://github.com/iLCSoft/Clupatra/pull/13))
  - fix all compiler warnings (gcc54-ub1604)
  - use private inheritance for std::list in NNClusterer 
        - add wrapper functions instead

* 2018-03-13 Frank Gaede ([PR#14](https://github.com/iLCSoft/Clupatra/pull/14))
  -  Fix for iLCSoft/LCIO#35

* 2018-03-28 Frank Gaede ([PR#15](https://github.com/iLCSoft/Clupatra/pull/15))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`


## KiTrack v01-09

* 2018-01-31 Frank Gaede ([PR#1](https://github.com/iLCSoft/KiTrack/pull/1))
  - fix all compiler warnings (gcc54-ub1604)
       - only "member initialization" from effc++

## KiTrackMarlin v01-12

* no code changes


## ConformalTracking v01-06

* 2018-03-28 Frank Gaede ([PR#31](https://github.com/iLCSoft/ConformalTracking/pull/31))
  - make compatible for other detectors, e.g. ILD
       - introduce new parameters with indices of tracker hit collections:
            - AllHitCollectionIndices
            - TrackerHitCollectionIndices
        - default values as used for CLIC
        - protect against empty collections


### ConformalTracking v01-05

* 2017-10-20 Daniel Hynds ([PR#25](https://github.com/iLCSoft/ConformalTracking/pull/25))
  - Require 5 hits/track for displaced track finding, to reduce fake rate

* 2017-10-13 Daniel Hynds ([PR#24](https://github.com/iLCSoft/ConformalTracking/pull/24))
  - Functions updated to allow tracker to vertex tracking, to allow displaced track reconstruction

* 2017-12-04 Andre Sailer ([PR#28](https://github.com/iLCSoft/ConformalTracking/pull/28))
  - Performance optimisations: avoiding temporaries, divisions, sqrts
  - protect against too many tracks

* 2017-12-12 Andre Sailer ([PR#29](https://github.com/iLCSoft/ConformalTracking/pull/29))
  - Performance optimisations: 
     - avoiding copies of `shared_ptrs`, avoiding temporary objects (use `emplace_back`, direct construction etc.)
     - move filtering of kdtree search results to before sorting
     - use `vdt::fast_atan` in `Cell:getAngle[RZ]` (enabled if ROOT provides `vdt`)
     - add option to turn off sorting of `kdtree` search results, this changes the outcome of the reconstruction, thus sorting is enabled by default

* 2017-11-27 Emilia Leogrande ([PR#26](https://github.com/iLCSoft/ConformalTracking/pull/26))
  - Parameter struct to set pattern recognition parameters
    - `_maxCellAngle`, `_maxCellAngleRZ`, `_chi2cut`, `_minClustersOnTrack`, `_maxDistance`, `_highPTfit`, `_onlyZSchi2cut`

* 2018-03-13 Frank Gaede ([PR#30](https://github.com/iLCSoft/ConformalTracking/pull/30))
  -  Fix for iLCSoft/LCIO#35


## lccd v01-05

* 2018-01-12 Frank Gaede ([PR#1](https://github.com/iLCSoft/lccd/pull/1))
  - fix all compiler warnings (gcc5.4)
      - uninitialized, copy/assignment w/ ptr members, unused, ...
      - dont create LCCDLibDeps.cmake ( CMP0033 )


## RAIDA v01-09

* 2018-01-12 Frank Gaede ([PR#3](https://github.com/iLCSoft/RAIDA/pull/3))
  - silence warnings: effc++, unused, vla 
  - fix virtual inheritance in IFunctionROOT


## MarlinUtil v01-15

* 2018-01-16 Frank Gaede 
 - export location of CLHEP::CLHEP in CMakeLists.txt


## Marlin v01-16

* 2017-12-07 Andre Sailer ([PR#28](https://github.com/iLCSoft/Marlin/pull/28))
  - XMLParsing: Replace constants in processor names: allows switching at initialisation time, e.g.:
  ```
  <processor name="BeamCalReco${BCReco}"/>
  ```
     and `Marlin --constant.BCReco=350GeV` to chose which BeamCalReco processor to run

* 2018-01-12 Frank Gaede ([PR#29](https://github.com/iLCSoft/Marlin/pull/29))
  - fix last compiler warnings in MarlinGUI and example (gcc5.4) 
  - don't create MarlinLibDeps.cmake 
  - rm Gear file from example steering and add <constants/> section 
  - rm deprecated options (-l,-f,-o) involving old steering files

* 2017-12-01 Ete Remi ([PR#27](https://github.com/iLCSoft/Marlin/pull/27))
  - Fixed warning (mostly -Weff and -Wshadow)
  - LCIOOutputProcessor: updated documentation line for LCIOWriteMode parameter

* 2018-01-29 Andre Sailer ([PR#31](https://github.com/iLCSoft/Marlin/pull/31))
  - Also count the modifyEvent function in the processor running time information


## MarlinDD4hep v00-06


## MarlinReco v01-23

* 2018-01-31 Strahinja Lukić ([PR#37](https://github.com/iLCSoft/MarlinReco/pull/37))
  Updates of SiTracker_dEdxProcessor:
  
  - Cleaned up unnecessary code.
  - Added runtime protection against failure of `TrackImpl::getTrackState()`.
  - Replaced `MarlinTrk::IMarlinTrack::propagate()` which was making the processor ~1000X slower than necessary with `MarlinTrk::IMarlinTrack::extrapolate()`.
  - Removed unnecessary parameters.
  
  Updates of AnalyseSidEdxProcessor:
  
  -   Added minor runtime protections.

* 2018-01-09 Strahinja Lukić ([PR#35](https://github.com/iLCSoft/MarlinReco/pull/35))
  - `SiTracker_dEdxProcessor` was adapted to determine the barrel/endcap type of tracker detector by checking the layering extension, rather than the type flag as before. 
  - A bug was corrected in `SiTracker_dEdxProcessor` that caused miscalculation of total sensor thickness for some of the available dEdx estimators.

* 2018-02-25 KURATA Masakazu ([PR#42](https://github.com/iLCSoft/MarlinReco/pull/42))
  - Focus on low momentum mu/pi separation
  - Correct the corresponding change for createPDF processor
   
  - update: correct bad lines:
    1. use DD4hepAPI to get b field
    2. correct array initialization
    3. prevent memory leak when using ROOT

* 2018-02-25 KURATA Masakazu ([PR#42](https://github.com/iLCSoft/MarlinReco/pull/42))
  - Thank you for writing the text to appear in the release notes. It will show up
    exactly as it appears between the two bold lines
  - ...

* 2018-02-08 Daniel Jeans ([PR#38](https://github.com/iLCSoft/MarlinReco/pull/38))
  - Change order of hit relations: now from reco/digi -> sim [to be consistent with past practice and all other processors]
  - Add to/from type info to the relation collections
  - Fix warnings from the compiler

* 2018-02-08 Andreas Alexander Maier ([PR#33](https://github.com/iLCSoft/MarlinReco/pull/33))
  - This package is an extension to the IsolatedLeptonFinderProcessor. The default functionality is untouched.
    - Optionally, it dresses leptons with close-by particles. By default it dresses electrons and muons with photons.
    - The algorithm starts with the highest energy lepton and adds all photons (and, optionally, electrons) in a cone of a given size around to it. As the original, it creates a collection with the dressed leptons and another collections with all remaining particles, except the ones that were dressed into the leptons.
    - All compiler warnings are fixed

* 2018-03-13 Frank Gaede ([PR#43](https://github.com/iLCSoft/MarlinReco/pull/43))
  -  Fix for iLCSoft/LCIO#35

* 2018-03-28 Frank Gaede ([PR#46](https://github.com/iLCSoft/MarlinReco/pull/46))
  - Fix for the removal of DDSurfaces which have been merged into DDRec 
    -  includes from `DDSurfaces` -> `DDRec`
    - namespace `DDSurfaces` -> `dd4hep::rec`

* 2017-12-12 Frank Gaede ([PR#34](https://github.com/iLCSoft/MarlinReco/pull/34))
  - Remove all warnings of type `should be initialized in the member initialization list [-Weffc++]`
  - Remove all warnings of type `unused parameter ‘run’` for `processRunHeader( LCRunHeader*  /*run*/)`
  - Remove all warnings of type `unused parameter ‘evt’` for `check( LCEvent *  /*evt*/ )`

* 2018-03-23 Ulrich Einhaus ([PR#44](https://github.com/iLCSoft/MarlinReco/pull/44))
  - Compute_dEdXProcessor:
    - geometry issue: gear to DD4hep unit adaption, fixed low momentum problem
    - added dx calculation strategies
    - added various processor options, default are all old version
    - added documentation


## ILDPerformance v01-05

* 2018-01-31 Strahinja Lukić ([PR#13](https://github.com/iLCSoft/ILDPerformance/pull/13))
  - Added TrackerHitCounter Marlin processor. This is a simple tool to count hits in the tracker elements. It reports the number of hits per run, per event and, where available, per unit area.

* 2017-12-20 Daniel Jeans ([PR#12](https://github.com/iLCSoft/ILDPerformance/pull/12))
  - simple processor to make some single photon validation plots at PFO level
  - number of PFOs, energy, energy resolution

* 2017-11-17 Shaojun Lu ([PR#7](https://github.com/iLCSoft/ILDPerformance/pull/7))
  - Tracking performance scripts for ILCSoft v01-19-05 and detector model ILD_l5_v02.
      - adapt to ILCSoft v01-19-05 and ILDConfig production.
      - in general, user could run "run_ILD_l5_v02_singleMuon.sh" for monitor track fitting.
      - in general, user could run "run_ILD_l5_v02_ttbar.sh" for the pattern recognition efficiency.
      - "README_Tracking.md" for a quick documentation.

* 2018-03-14 Jakob Beyer ([PR#15](https://github.com/iLCSoft/ILDPerformance/pull/15))
  - Adding WW/ZZ separation plots to ILDPerformance.

* 2017-12-12 Frank Gaede ([PR#9](https://github.com/iLCSoft/ILDPerformance/pull/9))
  - updated general documentation (added Usage and Sup-Packages sections)
  - updated PID package
       - updated documentation (now in README.md)
       - make all macros compatible w/ ROOT6
       - improve performance plots for PID efficiency (now all in one pdf file)
       - reduce verbosity in PIDTree.cc
       - remove all compiler warnings  for PIDTree

* 2017-12-12 Shaojun Lu ([PR#8](https://github.com/iLCSoft/ILDPerformance/pull/8))
  - Update ILD Tracking performance scripts
      - adapt to DD4hep and  use "MarlinUtil::getBzAtOrigin()" to access BField.
      - clean up all the warning for code DDDiagnostics.cc
      - improve the tracking performance scripts, to make them more user friendly.
      - remove the out-of-dated scripts for the old Mokka/Marlin
      - adapt to ILCSoft v01-19-05 and ILDConfig v01-19-05-p01 production

* 2017-12-13 Frank Gaede ([PR#10](https://github.com/iLCSoft/ILDPerformance/pull/10))
  - improve PID plots
      - create PID plots in directory of the root tree file 
         allows to create PID plots for different samples in parallel directories
      - add script `run_all.sh` to do just this

* 2018-03-28 Shaojun Lu ([PR#20](https://github.com/iLCSoft/ILDPerformance/pull/20))
  - update to the same bins as DBD for tracking efficiency plots.
  - set RunBeamCalReco=false.
  - update to next release ILCsoft v01-19-06.

* 2018-03-28 Ete Remi ([PR#19](https://github.com/iLCSoft/ILDPerformance/pull/19))
  - Added `UdsAnalysis` directory
     - Replace the old out-dated `JER` directory
     - New binary `ILDPerformance_UdsAnalysis` making plots from PfoAnalysis root files
     - Added NAF2 scripts to get JER/JES plots in a single shot

* 2018-03-26 Shaojun Lu ([PR#18](https://github.com/iLCSoft/ILDPerformance/pull/18))
  - make the scripts more generic to run for ilcsoft HEAD and release installation.
      - remove the release version "v01-19-05" information within the scripts.

* 2017-12-15 Frank Gaede ([PR#11](https://github.com/iLCSoft/ILDPerformance/pull/11))
  - fix **all compiler warnings** in ILDPerformance 
         - gcc 4.9, SL6
         - gcc 6.2, SL6
         - clang 3.9, SL6

* 2018-03-22 Shaojun Lu ([PR#16](https://github.com/iLCSoft/ILDPerformance/pull/16))
  - cleanup the massive monitoring information of tracking. 
  - cleanup the job scripts which are used on DESY NAF2 working nodes.
  - increase the statistic to 5000 single muons for each check point.
  - added RequestRuntime for expected longer runtime on DESY NAF2 working nodes
  - added FTDCollection, and count the true hits number in FTD simulation too.
  - adapt to pixel SIT, and change the name from SITSpacePoints to SITTrackerHits.
  - active minimum silicon hits number cut for MCParticles nominators.
      - count the silicon hits number from all VXD, SIT and FTD for each mcp track.

* 2018-03-23 Shaojun Lu ([PR#17](https://github.com/iLCSoft/ILDPerformance/pull/17))
  - added numberOfEvents 5000 for single Muon to fix simulation 3 events only.


## LCFIPlus v00-06-08

* 2018-03-08 Ryo Yonamine ([PR#36](https://github.com/lcfiplus/LCFIPlus/pull/36))
  - Fix vertex mass distribution problem. 
        - The corresponding line has been moved to VertexMassRecovery.cc.

* 2018-03-08 Ryo Yonamine ([PR#36](https://github.com/lcfiplus/LCFIPlus/pull/36))
  /

* 2018-01-30 Andre Sailer ([PR#34](https://github.com/lcfiplus/LCFIPlus/pull/34))
  - Add TrackHitOrdering=2 for LCFIPlusProcessor which conforms to the CLIC detector

* 2018-03-12 Frank Gaede ([PR#37](https://github.com/lcfiplus/LCFIPlus/pull/37))
  -  Fix for iLCSoft/LCIO#35


## MarlinKinfit v00-06

## MarlinKinfitProcessors v00-04

* 2017-12-15 Graham Wilson ([PR#4](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/4))
  - Add steering files for J/psi -> mu+ mu-, Higgs -> mu+ mu-, Higgs -> mu+mu-mu+mu-, K+->pi+pi-pi+
  - eta-> pi+ pi- gamma, eta-> pi+pi-pi0
  - Fix most - but not yet all - of the compiler warnings in the MassConstraintFitter related processors.

* 2017-11-29 Graham Wilson ([PR#3](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/3))
  - First commit of code of MassConstraintFitter from Justin Anguiano for 
    generalized mass-constrained fitting -- Graham. 
    Example .xml steering file is for simple use case of pi0-> gamma gamma.

* 2017-11-23 Graham Wilson ([PR#2](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/2))
  - add author

* 2017-12-20 Graham Wilson ([PR#5](https://github.com/iLCSoft/MarlinKinfitProcessors/pull/5))
  - All compiler warnings now fixed.
  - Pi0Fitter.xml now configured and tested for v01-19-05-p01 test production.
  - a) angular smearing now turned off (was work-around for photon position issues in v01-19-04)
  - b) energy scale set to 1.0
  - c) additional processor parameters in MCParticleFilter to deal with generator status differences


## DDMarlinPandora v00-10

* 2018-03-23 Ete Remi ([PR#17](https://github.com/iLCSoft/DDMarlinPandora/pull/17))
  - New class DDBFieldPlugin:
     - Returns the B field magnitude from DD4hep detector field to Pandora
  - DDPandoraPFANewProcessor:
     - Added optional registration of DDBFieldPlugin under processor parameter condition "UseDD4hepField" (default false)
  - DDCaloDigi:
     - Fixed warning



## Overlay v00-21

* 2018-01-31 Ete Remi ([PR#14](https://github.com/iLCSoft/Overlay/pull/14))
  - Overlay processor
     - Added number of overlaid events in event parameters
     - Added total number of overlaid events in event parameters
  - Fixed compiler warnings

* 2018-02-12 Ete Remi ([PR#15](https://github.com/iLCSoft/Overlay/pull/15))
  - Complete re-write of Overlay processor
     - Removed processor parameters (RunOverlay and NSkipEventsRandom)
     - Overlay of multiple files work as for a single file
     - If no collection specified in config, overlay all present collections 
     - Write in the event parameters: 
        - Overlaid run and event numbers
        - Number of overlaid events per processor and from all processors
     - Code documented and c++11 styled
     - Methods and class members cleaned-up

* 2018-03-21 Ete Remi ([PR#16](https://github.com/iLCSoft/Overlay/pull/16))
  - Overlay processor: 
     - Added new processor parameter: list of collections to avoid to overlay


## LCTuple v01-11

* 2018-03-13 Frank Gaede ([PR#4](https://github.com/iLCSoft/LCTuple/pull/4))
  -  Fix for iLCSoft/LCIO#35
********************************************************************************
INFO  - Tagger  : Committing release notes for: ilcsoft/lcio
INFO  - Tagger  : Updating version: ilcsoft/lcio to v02-12
INFO  - lcio    : Update CMakeLists.txt is to v02-12
INFO  - Tagger  : Committing release notes for: iLCSoft/lcgeo
INFO  - Tagger  : Updating version: iLCSoft/lcgeo to v00-16
INFO  - lcgeo   : Update CMakeLists.txt is to v00-16
INFO  - Tagger  : Committing release notes for: AIDASoft/DD4hep
INFO  - Tagger  : Updating version: AIDASoft/DD4hep to v01-07
INFO  - DD4hep  : Update CMakeLists.txt is to v01-07
ERROR - DD4hep  : File DDSegmentation/CMakeLists.txt not found for AIDASoft/DD4hep
ERROR - root    : Error during runtime: File not found
