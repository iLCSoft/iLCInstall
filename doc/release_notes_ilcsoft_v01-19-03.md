
# Release notes for iLCSoft v01-19-03

Packages changed since last version: 

(*created from individual packages' release notes*)

## lcio -  v02-09

* 2017-05-08 Sebastien Binet ([PR#27](https://github.com/ilcsoft/lcio/pull/27))
  - add an example using `LCIO` from `Go`

* 2017-05-29 Marko Petric ([PR#30](https://github.com/ilcsoft/lcio/pull/30))
  - Added flag -Wheader-hygiene to warn about usage of namespace directive in global context in header


## lcgeo - v00-13-01

* 2017-07-06 Frank Gaede ([PR#131](https://github.com/iLCSoft/lcgeo/pull/131))
  - fix the pixel SIT for ILD_*_v02 models
        - add new driver SIT_Simple_Pixel_geo.cpp
        - use sit_simple_pixel_sensors_01.xml

* 2017-07-06 Shaojun Lu ([PR#130](https://github.com/iLCSoft/lcgeo/pull/130))
  - Update ILD services driver to access the ILD compact file "env_safety", and apply it in the services driver to avoid services overlap with sub-detector envelope .

## lcgeo - v00-13

* 2017-07-06 Frank Gaede ([PR#129](https://github.com/iLCSoft/lcgeo/pull/129))
  - ILD_*_v02 models: remove stereo angle in SIT ( move to pixel readout)

* 2017-07-06 Daniel Jeans ([PR#128](https://github.com/iLCSoft/lcgeo/pull/128))
  - many tweaks to ECAL dimensions in ILD_*_V02 models, referring to technical design document from H.Videau et al.
  - a couple of small bug fixes to ECAL drivers (previously ignored request for extra CF thickness in front face, if no preshower was set)
  - adjusted TPC dimensions and barrel-endcap gap to accommodate new ECAL

* 2017-07-05 Shaojun Lu ([PR#127](https://github.com/iLCSoft/lcgeo/pull/127))
  - Implement ILD HcalEndcap FrontEnd readout electronics.
  - Implement it into both ILD_common_v01 and ILD_common_v02.
  - ILD models l4/s4 will use the same services as l1/s1.

* 2017-07-05 Shaojun Lu ([PR#126](https://github.com/iLCSoft/lcgeo/pull/126))
  - Update for ILD services cables
    - Implement VXD cable cone services.
    - Implement the VXD cable services into ILD_common_v01 and ILD_common_v02.
    - Comment out the services in ILD_o1_v05.
    - Remove the ILD services reference code (not necessary).
    - The SServices00 has been updated, and used by ILD.
    - Update the ILD VXD cable configuration by expert.

* 2017-07-05 Daniel Jeans ([PR#125](https://github.com/iLCSoft/lcgeo/pull/125))
  - previously several ECAL sub-layers were combined into an averaged material to simplify simulation.
  This requires to redefine this material every time thicknesses change (quite often at the moment), which was not done consistently. 
  For the time being, separate the components to ensure correct material description. 
  (Consider recombining when sub-layer thicknesses are fixed and stable.)

* 2017-07-04 Daniel Jeans ([PR#124](https://github.com/iLCSoft/lcgeo/pull/124))
  - now use DD4hep_Beampipe_o1_v01 driver (gets rid of "deprecated" warning when using Beampipe_o1_v01)

* 2017-07-04 Shaojun Lu ([PR#123](https://github.com/iLCSoft/lcgeo/pull/123))
  - Update ILD_o1_v05 compact files for the services.
    - Change the FTD envelope shape to place SIT cable.
    - Add missing service parameters.

* 2017-07-04 Daniel Jeans ([PR#122](https://github.com/iLCSoft/lcgeo/pull/122))
  - updates to TPC in ILD_*_v02 models from Dimitra Tsionou
  - increased material in outer field cage
  - increased material in cathode plane
  - reduced thickness of outer field cage by 5mm (to accommodate thicker ECAL: final numbers to be confirmed)

* 2017-07-03 Daniel Jeans ([PR#121](https://github.com/iLCSoft/lcgeo/pull/121))
  - in ILD models, material of TPC cooling pipes is accounted for in TPC driver. They were also added in sservices00 driver, causing double counting. Solution: turn them off in SServices00.

## lcgeo - v00-12

* 2017-06-12 Daniel Jeans ([PR#110](https://github.com/iLCSoft/lcgeo/pull/110))
  - First "development" set of ILD "v02" models, with thicker ECAL and reduced TPC outer radius: Large and Small models have been implemented in "1", "2", and "4" technology options.
  - new dimensions not yet frozen, so will probably need some adjustment
  - re-organisation of code for v2 models: readout definition moved together with detector definitions (previously defined in top-level ILD_*.xml).
  - TPC services (all cooling pipes except one) removed for v02 models. Awaiting input from TPC experts on correct position/size of this pipe.
  - some change to definition of ECAL rails: move to currently favoured 2-rail design. Some update/cleanup of SServices00 driver. This also affects v01 models.

* 2017-06-28 Shaojun Lu ([PR#117](https://github.com/iLCSoft/lcgeo/pull/117))
  - Implement SITCables services for ILD detector models
  - Update the FTD envelope shape to get free space to place SITCables.
  - Add SITCables services parameters into XML files for ILD_common_v01.
  - Add SITCables services parameters into XML files for ILD_common_v02.

* 2017-06-29 Andre Sailer ([PR#119](https://github.com/iLCSoft/lcgeo/pull/119))
  - Split libraries into one without linking against Geant4 and one with Geant4 dependency. Avoid loading of Geant4 libraries in reconstruction

* 2017-06-29 Shaojun Lu ([PR#118](https://github.com/iLCSoft/lcgeo/pull/118))
  - Follow the TUBE update, and use the TUBE envelope radius to fix the services SitDisk overlaps. 
  - Define the SitDisk Rmin with TUBE_IPOuterBulge_end_envradius instead of TUBE_IPOuterBulge_end_radius.
  - Implement HcalBarrel_EndcapServices which also include the services coming from  Ecal and TPC.
  - Implement HcalBarrel_EndcapServices parameters into both ILD_comon_v01 and ILD_common_v02.
  - Add parameter 'TPC_cooling_nRings' in SServices00.xml to allow change wrt large and small ILD model for this moment.

* 2017-06-08 Daniel Jeans ([PR#107](https://github.com/iLCSoft/lcgeo/pull/107))
  - For ILD models: increase inner radius of FTD envelope, to avoid overlap with beampipe of finite thickness.

* 2017-06-16 Frank Gaede ([PR#112](https://github.com/iLCSoft/lcgeo/pull/112))
  - remove unused and deprecated (https://github.com/AIDASoft/DD4hep/pull/165 ) DDRec extensions LayeringExtension/SubdetectorExtensions from Ecal drivers

* 2017-06-15 Shaojun Lu ([PR#111](https://github.com/iLCSoft/lcgeo/pull/111))
  - Ported ILD Mokka class SServices00 line by line into a new class SServices00_v01 into lcgeo.
  - Used in ILDSServices.cpp to create services geometry for ILD_o1_v05.

* 2017-05-15 Marko Petric ([PR#102](https://github.com/iLCSoft/lcgeo/pull/102))
  - Introduce new model CLIC_o3_v11 and shift segmentation in HCal for half cell size

* 2017-05-15 Frank Gaede ([PR#101](https://github.com/iLCSoft/lcgeo/pull/101))
  - fix the logic for assigning sensitive slices in ILD Hcal drivers

* 2017-06-30 Frank Gaede ([PR#120](https://github.com/iLCSoft/lcgeo/pull/120))
  - update the ILD_(ls)(124)_v02 models
          - move the un-instrumented gaseaous volume in the TPC to the inner field cage 
          - cleaned up the use of plugins:
                 - CaloFace plugins are now in the SEcal04 drivers (in ILD_common_v02)
                 - add DD4hepVolumeManager (for consistency) and InstallSurfaceManager
                     to main compact files for all models

* 2017-06-20 Frank Gaede ([PR#114](https://github.com/iLCSoft/lcgeo/pull/114))
  -  replace DDSurfaces w/ dd4hep::rec

* 2017-06-20 Andre Sailer ([PR#113](https://github.com/iLCSoft/lcgeo/pull/113))
  - Adapt to changes in namespaces in DD4hep

* 2017-06-21 Marko Petric ([PR#115](https://github.com/iLCSoft/lcgeo/pull/115))
  - Remove using namespace from header

* 2017-06-26 Frank Gaede ([PR#116](https://github.com/iLCSoft/lcgeo/pull/116))
  - fix ILD_o4 models:
  - ILD_l4_v01:  
     - reverse order of RPC and scintillator  ( RPC first)
  - ILD_l/s4_v02:
     - reverse order of RPC and scintillator  ( RPC first)
     - add parameters for tracking volume and reconstruction geometry
     - add surface plugins for tracking

* 2017-04-28 Daniel Jeans ([PR#100](https://github.com/iLCSoft/lcgeo/pull/100))
  - Changes to HCAL endcap envelopes in ILD_l/s* models
          - in all ILD_l/s* models, reduce radial size of hcal endcap envelopes to leave space for cables. cryo-hcal endcap gap is controlled by parameter Hcal_endcap_cryostat_gap, set to 170 mm.
         - in ILD_?2 models, change SDHCAL endcap envelope shape to tube (same as other models)

* 2017-05-29 TiborILD ([PR#106](https://github.com/iLCSoft/lcgeo/pull/106))
  - updated ILD SDHcal drivers and geometry:
      - reverse ordering of slices in Barrel, Endcaps_v01
      - correction for z-cracks in Barrel
      - towers numbering from inner to outer radius (Endcaps_v02)
      - staves numbering 0-3 (Endcaps_v02)
      - removed not used variable and commented line (Endcaps_v02)

* 2017-05-30 luisaleperez ([PR#103](https://github.com/iLCSoft/lcgeo/pull/103))
  - Updated Field maps readers, FieldMapBrBz and FieldMapXYZ, to automatically get from the root file the maps parameters
    - Coordinates ranges, step size and ordering

* 2017-04-22 StrahinjaLukic ([PR#96](https://github.com/iLCSoft/lcgeo/pull/96))
  - Outgoing beam tube radius was reduced by 1 mm from "BeamCal_min_z-5*mm" to 5999*mm because the BeamCal inner radius was reduced as part of the adjustments to L*=4.1m
  - The protruding outer radius of QDEX1AFront link between tube sections was reduced to the outer radius of the larger tube.
  - The changes affect all ILD models that use ILD_common.

* 2017-04-22 Frank Gaede ([PR#95](https://github.com/iLCSoft/lcgeo/pull/95))
  - fix the creation of the DDRec::LayeredCalorimeterData data structures for the the 
    multisegmentation readout model LD_l4_v01
  - reverse the order of the slices in the HcalEndcaps and HCalEndcapRing for this model

* 2017-05-24 Frank Gaede ([PR#104](https://github.com/iLCSoft/lcgeo/pull/104))
  - set the correct DetType_ENDCAP for all ILD HcalEndcapRing models
        - was DetType_BARREL

* 2017-04-25 Marko Petric ([PR#97](https://github.com/iLCSoft/lcgeo/pull/97))
  - Introduce new model CLIC_o3_v10
  - Unify all encoding strings for ECal, HCal, Yoke with the introduction of GlobalCalorimeterReadoutID

* 2017-04-26 Daniel Jeans ([PR#98](https://github.com/iLCSoft/lcgeo/pull/98))
  - use correct LHCal01 detector setup in ILD_l1_v01

* 2017-06-09 Marko Petric ([PR#109](https://github.com/iLCSoft/lcgeo/pull/109))
  - Update the location of DD4hep Handle.inl include file to adapt to DD4hep v00.24

* 2017-06-09 Daniel Jeans ([PR#108](https://github.com/iLCSoft/lcgeo/pull/108))
  - improve SEcal05 drivers and compact description for ILD models
       - remove hard-coded numbers of carbon fiber layers (in alveolii, around absorber plates) in SEcal05* drivers: more flexible.
      - now parameterize in terms of total CF thickness, rather than thickness of one sheet multiplied by number of sheets: easier to understand, more flexible.
      - associated changes required in compact descriptions



## DD4hep -  v01-01

* 2017-07-06 Markus Frank ([PR#201](https://github.com/AIDASoft/DD4hep/pull/201))
  ### DDCore: Changes to the VolumeManager interface
  
    Recent descrepancies showed that the call to lookup a placement
    from the volume manager may have an ambiguous meaning:
    It may (as used until now) be the placement of thge closest
    detector element - a functionality used by various tests
    or be the placement of the sensitive volume itself.
    So far, since each sensitive volume in the DD4hep tests
    is represented by a DetElement structure, both
    approaches returned the same placed volume.
  
    Since there is the possibility to have sensitive volumes, which are not
    directly connected to a single DetElement structure, this call was
    split to resolve this ambiguity:
  
    /// Lookup a physical (placed) volume identified by its 64 bit hit ID
    PlacedVolume lookupVolumePlacement(VolumeID volume_id) const;
    /// Lookup a physical (placed) volume of the detector element
    /// containing a volume identified by its 64 bit hit ID
    PlacedVolume lookupDetElementPlacement(VolumeID volume_id) const;

* 2017-07-06 Andre Sailer ([PR#200](https://github.com/AIDASoft/DD4hep/pull/200))
  - Now will give a warning if multiple entities (e.g., constants) of the same name are defined in the XML

## DD4hep - v01-00-01

* 2017-07-04 Frank Gaede ([PR#199](https://github.com/AIDASoft/DD4hep/pull/199))
  - bug fix for VolumeManagerContext::toElement() and VolumeManagerContext::placement() 
        - set flag=true in VolumeManager_Populator::add_entry when 
           a ContextExtension is needed, i.e. sensitive volume is not DetElement's volume
  - fixes problems in CellIDPositionConverter


## DD4hep -  v01-00

* 2017-06-22 Marko Petric ([PR#192](https://github.com/AIDASoft/DD4hep/pull/192))
  - Move `AlignDet_Telescope_readback_xml` to later in the pipeline since it depends on the output of `AlignDet_Telescope_write_xml`

* 2017-06-22 Andre Sailer ([PR#191](https://github.com/AIDASoft/DD4hep/pull/191))
  - Surface: fix memory leak of transformation matrix
  - XML::Layering: fix memory leak of contained layers in the object

* 2017-06-23 Andre Sailer ([PR#197](https://github.com/AIDASoft/DD4hep/pull/197))
  - Fix memory leaks for Tube, EllipticalTube and Polyhedron

* 2017-06-23 Andre Sailer ([PR#196](https://github.com/AIDASoft/DD4hep/pull/196))
  - CMake: add `Project( DD4hep )`, needed to get the correct CMAKE_CXX_COMPILER_ID on macs due to CMP0025 (cmake policy)
  - CMake: fix treatment of linker flags, they are now properly set for Linux and Macs to error when undefined functions are encountered at link time
  - CMake: fix elif --> elseif when checking threading libraries

* 2017-06-23 Frank Gaede ([PR#195](https://github.com/AIDASoft/DD4hep/pull/195))
  - fix crash in `dd4hep::rec::Surface` after changes in Handle assignment (PR #193)
  - fix use of deprecated `dd4hep::rec::MaterialManager` c'tor in Surface

* 2017-06-20 Frank Gaede ([PR#185](https://github.com/AIDASoft/DD4hep/pull/185))
  - bug fix in material utilities
       - call `MaterialManager( Volume v)` with `Detector.world().volume()`

* 2017-06-20 Marko Petric ([PR#184](https://github.com/AIDASoft/DD4hep/pull/184))
  - Reinstate the full test-suite on Travis

* 2017-06-20 Markus Frank ([PR#183](https://github.com/AIDASoft/DD4hep/pull/183))
  - Unify header guards in DDCore
  - Add header to steer ignoring warnings of rootcling generated dictionaries.

* 2017-06-20 Frank Gaede ([PR#182](https://github.com/AIDASoft/DD4hep/pull/182))
  - cleanup of namespace `dd4hep::rec`
    - remove obsolete bwd compatibility for `DD4hep::DDRec`
    - re-introduce `[deprecated]` warnings for unmaintained classes in DDRec/API 
    - re-fix deprecated c'tor for `MaterialManager` in material utilities

* 2017-06-20 Markus Frank ([PR#181](https://github.com/AIDASoft/DD4hep/pull/181))
  - Attack many warnings from:
    - `-Wshadow`
    - `-Winclude-hygiene`
    - `-Woverlength-strings` (int cling dictionaries)

* 2017-06-20 Markus Frank ([PR#179](https://github.com/AIDASoft/DD4hep/pull/179))
  - Remove a bunch of shadow warnings and include-hygiene warnings.

* 2017-06-21 Marko Petric ([PR#169](https://github.com/AIDASoft/DD4hep/pull/169))
  - Make boost explicit requirement for DD4hep and drop DD4HEP_USE_BOOST

* 2017-06-21 David Blyth ([PR#168](https://github.com/AIDASoft/DD4hep/pull/168))
  - Added environment helper scripts `thisdd4hep_only.(c)sh` that only set up variables for DD4hep and not for dependencies.

* 2017-06-19 Markus Frank ([PR#178](https://github.com/AIDASoft/DD4hep/pull/178))
  - Update documentation after reorganization of namespaces (put back previous docs).

* 2017-06-19 Markus Frank ([PR#175](https://github.com/AIDASoft/DD4hep/pull/175))
  ## DD4hep namespace reorganization
  
  Re-organize namespaces according to the decisions of the DD4hep developers meeting from 16th June we have decided:
  
  1. all namespaces will be lower case and shorter
      * rename namespace `DD4hep` -> `dd4hep`
      * rename namespace `DD4hep::DDRec` -> `dd4hep::rec`
      * rename namespace `DD4hep::Simulation` -> `dd4hep::sim`
      * rename namespace `XML` -> `xml` and `JSON` -> `json`
      * rename all other namespaces according to this pattern
  2. The namespace `DD4hep::Geometry::` will be incorporated into `dd4hep::`
  3. All utilities will be moved `dd4hep::detail`
  4. `LCDD` will be renamed to `Detector` and current `Detector.h` will be renamed to `DetElement.h`
  8. Examine if `DDSegmentation` can be incorporated into `DDCore` and make it volume aware
      * If this this cannot be achieved in whole place `DDSegmentation` into the right namespace
  
    ## DDParsers
  
    DDParsers are now a separate package. This does not make it yet standalone,
    but it is at the same level as e.g. DDSeqmentation. Any librarian is
    encouraged to externialize it fully.



## MarlinFastJet -  v00-05

* 2017-05-08 Lars Rickard Strom ([PR#9](https://github.com/iLCSoft/MarlinFastJet/pull/9))
  - FastJetUtil/FastJetProcessor: Print error message if value of Inclusive minPt parameter is not specified in the steering file.
    - set default value minPt="0.0"

* 2017-05-08 Lars Rickard Strom ([PR#8](https://github.com/iLCSoft/MarlinFastJet/pull/8))
  - FastJetUtil/FastJetProcessor: Added support for running ee_genkt_algorithm with non-default exponent and inclusive clustering, using parameters ee_genkt_algorithm R p, Inclusive minPt, reproduces the results of jet-based trimming

* 2017-05-05 Lars Rickard Strom ([PR#7](https://github.com/iLCSoft/MarlinFastJet/pull/7))
  - Updated instructions on how to use FastJetUtil.h in stand-alone project.
  - Moved getRecPars to FastJetUtil to enable broader use of conversion between PseudoJet objects and ReconstructedParticle (renamed convertFromPseudoJet).
  - Added FastJet JHTopTagger implementation and made changes in other files to accommodate such tool implementations.


## aidaTT - v00-07

* 2017-06-23 Frank Gaede ([PR#15](https://github.com/AIDASoft/aidaTT/pull/15))
  -  adapt examples to recent namespace change in DD4hep
  - replace DDSurfaces with dd4hep::rec
  - fix -Winfinite-recursion in Vector5 (operator+)

* 2017-06-20 Andre Sailer ([PR#14](https://github.com/AIDASoft/aidaTT/pull/14))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-06-26 Frank Gaede ([PR#16](https://github.com/AIDASoft/aidaTT/pull/16))
  - fix some Coverity issues

* 2017-05-08 Andre Sailer ([PR#13](https://github.com/AIDASoft/aidaTT/pull/13))
  - CMake: Instead of using GENERATE_PACKAGE_CONFIG_FILES call configure_file and install directly. Macro was used from DD4hep before (and is no longer available there).


## DDKalTest - v01-03

* 2017-05-09 Andre Sailer ([PR#3](https://github.com/iLCSoft/DDKalTest/pull/3))
  - Dropped support for root version < 6

* 2017-06-20 Andre Sailer ([PR#4](https://github.com/iLCSoft/DDKalTest/pull/4))
  - Adapt to namespace changes in DD4hep

* 2017-06-29 Andre Sailer ([PR#5](https://github.com/iLCSoft/DDKalTest/pull/5))
  - CMake Configuration cleanup: Remove linking against Geant4
  - Require CMake 3.3 (same as DD4hep)


## MarlinTrk - v02-04

* 2017-06-20 Andre Sailer ([PR#4](https://github.com/iLCSoft/MarlinTrk/pull/4))
  - Adapt to namespace changes in DD4hep

* 2017-06-27 Andre Sailer ([PR#5](https://github.com/iLCSoft/MarlinTrk/pull/5))
  - Clean up of tkrSystem and DDKalDetectors at the end of lifetime

* 2017-05-17 Frank Gaede ([PR#2](https://github.com/iLCSoft/MarlinTrk/pull/2))
  - replace gear::Vector3D with DDSurfaces::Vector3D in IMarlinTrack interface
        - provide wrapper functions with old signature for backwards compatibility
        - remove all other usages of Gear
  - remove obsolete MarlinKalTest and MarlinKalTestTrack
         - from now on use only MarlinDDKalTest
  - fix all warnings seen with llvm (on mac)


## MarlinTrkProcessors - v02-08-01

* 2017-07-06 Frank Gaede ([PR#23](https://github.com/iLCSoft/MarlinTrkProcessors/pull/23))
  - fix phi0 of module rings in TPCModularEndplate


## MarlinTrkProcessors - v02-08

* 2017-06-28 Frank Gaede ([PR#21](https://github.com/iLCSoft/MarlinTrkProcessors/pull/21))
  - remove hits that are in module gaps on the TPC endplate in DDTPCDigiProcessor
        - use the following parameters to define the endplate:
        - TPCEndPlateModuleNumbers
        - TPCEndPlateModulePhi0s
        - TPCEndPlateModuleGapPhi
  - rm obsolete parameter DontEncodeSide from DDTPCDigiProcessor

* 2017-06-15 Marko Petric ([PR#14](https://github.com/iLCSoft/MarlinTrkProcessors/pull/14))
  - Replace auto_ptr with unique_ptr
  - explicitly call copy constructor of base class

* 2017-06-15 Emilia Leogrande ([PR#13](https://github.com/iLCSoft/MarlinTrkProcessors/pull/13))
  * TruthTrackFinder: hits in the same layer of the same subdetectors are now filtered. Those with higher radius are removed, then the fit is performed. In case the fit fails, those with higher z are removed and a new fit attempt is made.

* 2017-06-14 Frank Gaede ([PR#12](https://github.com/iLCSoft/MarlinTrkProcessors/pull/12))
  - remove some obsolete processors:
          - PlanarDigiProcessor
          - SpacePointBuilder
          - SimpleCylinderDigiProcessor
          - SimpleDiscDigiProcessor
          - SimplePlanarDigiProcessor.h
  - replace Gear with DD4hep/DDRec in all remaining processors

* 2017-06-30 Andre Sailer ([PR#22](https://github.com/iLCSoft/MarlinTrkProcessors/pull/22))
  - ExtrToTracker: cleanup transient collection

* 2017-06-20 Frank Gaede ([PR#17](https://github.com/iLCSoft/MarlinTrkProcessors/pull/17))
  - fix leftover namespace changes in dd4hep

* 2017-06-20 Andre Sailer ([PR#16](https://github.com/iLCSoft/MarlinTrkProcessors/pull/16))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-06-27 Andre Sailer ([PR#20](https://github.com/iLCSoft/MarlinTrkProcessors/pull/20))
  - FPCCDSiliconTracking_MarlinTrk: move object creation to init, add delete
  - DDPlanarDigiProcessor: free random number generator at the end

* 2017-06-24 Frank Gaede ([PR#19](https://github.com/iLCSoft/MarlinTrkProcessors/pull/19))
  - add DDTPCDigiProcessor and helper classes
          - adaptation of MarlinReco/TPCDigiProcessor for DD4hep

* 2017-06-23 Andre Sailer ([PR#18](https://github.com/iLCSoft/MarlinTrkProcessors/pull/18))
  - DDCellsAutomatonMV: fix duplicate parameter name 
     * MVHitsThetaDifference --> MVHitsThetaDifference_Adjacent



## Clupatra - v01-01

* 2017-06-20 Andre Sailer ([PR#11](https://github.com/iLCSoft/Clupatra/pull/11))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-05-18 Frank Gaede ([PR#10](https://github.com/iLCSoft/Clupatra/pull/10))
  - remove last leftover dependencies to Gear
  - remove any dependency on MarlinKalTest


## KiTrackMarlin - v01-11

* 2017-06-20 Andre Sailer ([PR#4](https://github.com/iLCSoft/KiTrackMarlin/pull/4))
  - Adapt to DD4hep namespace change

* 2017-05-18 Frank Gaede ([PR#3](https://github.com/iLCSoft/KiTrackMarlin/pull/3))
  - remove all references to Gear and MarlinKalTest



## ForwardTracking - v01-12

* 2017-06-20 Frank Gaede ([PR#8](https://github.com/iLCSoft/ForwardTracking/pull/8))
  - fix leftover dd4hep namespace changes

* 2017-06-20 Andre Sailer ([PR#7](https://github.com/iLCSoft/ForwardTracking/pull/7))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-03-31 Frank Gaede ([PR#5](https://github.com/iLCSoft/ForwardTracking/pull/5))
  - fix all warnings on clang, MacOS 
      - does not include -WeffC++

* 2017-03-31 Andre Sailer ([PR#4](https://github.com/iLCSoft/ForwardTracking/pull/4))
  - Rename DDForwardTracking to SiliconEndcapTracking, solves #3 
  - SiliconEndcapTracking: fix warnings
  - Ignore warnings from external headers

* 2017-03-31 Frank Gaede ([PR#2](https://github.com/iLCSoft/ForwardTracking/pull/2))
  - replace Gear with DD4hep/DDRec
      - using DD4hep::DDRec::ZDiskPetalsData as replacement for
         gear::FTDParameters
      - use DDSurfaces::Surface and DDRec::SurfaceManager as
         replacement for gear::MeasurementSurfaceStore
      - changed indentation for FTDBackgroundProcessor.cc

* 2017-05-18 Frank Gaede ([PR#6](https://github.com/iLCSoft/ForwardTracking/pull/6))
  - remove all references to Gear and MarlinKalTest



## ConformalTracking - v01-03

* 2017-06-13 Daniel Hynds ([PR#11](https://github.com/iLCSoft/ConformalTracking/pull/11))
  - Added clang-format to cmake lists and added extra target. "make format" will now format the code, and will be prepared automatically if clang-format exists.
  - Updated tracking strategy and added some improvements in terms of refitting tracks each time a hit is added, and included a maximum chi2 criteria for adding hits

* 2017-06-13 Andre Sailer ([PR#10](https://github.com/iLCSoft/ConformalTracking/pull/10))
  - ConformalTracking: Fix some memory leaks

* 2017-06-28 Andre Sailer ([PR#14](https://github.com/iLCSoft/ConformalTracking/pull/14))
  -  Add format checker as a CI check

* 2017-06-28 Andre Sailer ([PR#13](https://github.com/iLCSoft/ConformalTracking/pull/13))
  - ConformalTracking: cleanup final conformal tracks

* 2017-05-31 Andre Sailer ([PR#7](https://github.com/iLCSoft/ConformalTracking/pull/7))
  - Make all output DEBUG for now, because there is too much output for the grid to handle

* 2017-06-20 Andre Sailer ([PR#12](https://github.com/iLCSoft/ConformalTracking/pull/12))
  - Adapt to DD4hep namespace change, get BField from utility function

* 2017-06-03 Daniel Hynds ([PR#8](https://github.com/iLCSoft/ConformalTracking/pull/8))
  - Put track fit back in, accidentally missing during debugging

* 2017-05-24 Daniel Hynds ([PR#6](https://github.com/iLCSoft/ConformalTracking/pull/6))
  - Chi2 calculations completely reworked
  - Significant code cleanup
  - Code modularised to allow different tracking strategies 
  - Default state currently still vertex-only track construction



## MarlinUtil - v01-14

* 2017-05-03 Frank Gaede ([PR#3](https://github.com/iLCSoft/MarlinUtil/pull/3))
  - fix -Wabsolute-value in MarlinCED.cc

* 2017-05-03 Andre Sailer ([PR#2](https://github.com/iLCSoft/MarlinUtil/pull/2))
  - Fix all warnings in MarlinUtil for gcc and llvm, and cmake
      - use vectors instead of arrays to simplify memory handling in many classes, shadow warnings, unused parameters, unused member variables (LLVM), initialising members
  - Fix bug in copy constructor of SimpleHelix if the LCErrorMatrix argument was not NULL (https://github.com/iLCSoft/MarlinUtil/commit/4a65837e720e5ba001f3031622c1eeb6cc20be3e) the LCErrorMatrix member was never properly initialised
  - Separated ANN code into separate library to ignore all warnings, as this is exernal code (https://github.com/iLCSoft/MarlinUtil/commit/773a4d1dfd4ea7ad468d705a6c580e7a2890e165)

* 2017-05-05 Andre Sailer ([PR#4](https://github.com/iLCSoft/MarlinUtil/pull/4))
  - Add GeometryUtil file: implemented MarlinUtil::getBFieldInZ and MarlinUtil::getDetectorExtension
    - getBFieldInZ returns bfield at (0 0 0) in z direction in Tesla from GEAR or DD4hep automagically
    - getDetectorExtension returns DDRec detector extension for given flags
  - HelixClass[_double]::getDistanceToPoint, first argument is now const to allow passing return values from lcio functions. Fully backward compatible

* 2017-05-04 Andre Sailer ([PR#5](https://github.com/iLCSoft/MarlinUtil/pull/5))
  - Fixed warnings for gcc49
  - add Werror to CI configuration, no longer accepting PRs creating warnings

* 2017-06-20 Shaojun Lu ([PR#10](https://github.com/iLCSoft/MarlinUtil/pull/10))
  - Update DD4hep::DDRec::LayeredCalorimeterData to dd4hep::rec::LayeredCalorimeterData for backward compatible.
  - Adapt namespaces to changes in DD4hep

* 2017-06-03 Andre Sailer ([PR#8](https://github.com/iLCSoft/MarlinUtil/pull/8))
  - MarlinUtil::getAbsMomentum: bugfix: use `delete[]` instead of `delete` as getMomentum uses new[]

* 2017-05-29 Andre Sailer ([PR#7](https://github.com/iLCSoft/MarlinUtil/pull/7))
  - MarlinUtil::getAbsMomentum: fix memory leak
  - ClusterExtended::setHelix: use const reference instead of object as argument for function
  - HelixClass[_double]::getDistanceToHelix: fix out-of-bounds access of array
  - DDMarlinCED::*ParameterConversion: initialise isBarrel for CEDGeoTubeParams
  - DDMarlinCED:: draw: getchar returns int, value otherwise truncated
  - DDMarlinCED::kbhit: initialise fd_set

* 2017-05-22 Andre Sailer ([PR#6](https://github.com/iLCSoft/MarlinUtil/pull/6))
  - Changed `class MarlinUtil` to `namespace MarlinUtil`
  - MarlinUtilConfig: include the dependency on DD4hep and ROOT



## Marlin - v01-12

* 2017-06-29 Andre Sailer ([PR#16](https://github.com/iLCSoft/Marlin/pull/16))
  - XMLParser: cleanup member objects, make StringParameters shared pointers to simplify ownership
     Previously some were owned by the Processors, others were still owned by the XMLParser object
     adapted interfaces
  - Processors: functions using `StringParameter*` now use or return `shared_ptr<StringParameters>` instead

* 2017-06-09 Andre Sailer ([PR#12](https://github.com/iLCSoft/Marlin/pull/12))
  - EventSeeder: make event seed truly constant in space and time

* 2017-06-14 Andre Sailer ([PR#13](https://github.com/iLCSoft/Marlin/pull/13))
  - Added MemoryMonitor processor to print out memory consumption of Marlin

* 2017-06-30 Frank Gaede ([PR#17](https://github.com/iLCSoft/Marlin/pull/17))
  - adapt MarlinGUi to new usage of shared_ptr<StringParameters>
   - remove duplicate entry in ReleaseNotes.md

* 2017-05-29 Andre Sailer ([PR#11](https://github.com/iLCSoft/Marlin/pull/11))
  - Add possibility to use conditions also for eventModify processors. The processor setting the conditions must also run under modifyEvent!

* 2017-05-29 Andre Sailer ([PR#10](https://github.com/iLCSoft/Marlin/pull/10))
  - compareMarlinSteeringFiles.py: add treatment for processor groups
  - compareMarlinSteeringFiles.py: add option to compare only selected processors

* 2017-06-23 Andre Sailer ([PR#15](https://github.com/iLCSoft/Marlin/pull/15))
  - Processor: throw exception if parameter is already defined


## MarlinDD4hep - v00-05

* 2017-06-22 Andre Sailer ([PR#7](https://github.com/iLCSoft/MarlinDD4hep/pull/7))
  - Destroy Detector instance at the end to make valgrind happier

* 2017-06-20 Andre Sailer ([PR#6](https://github.com/iLCSoft/MarlinDD4hep/pull/6))
  - Adapt to namespace changes in DD4hep


## MarlinReco - v01-19-01

* 2017-07-04 Daniel Jeans ([PR#16](https://github.com/iLCSoft/MarlinReco/pull/16))
  - update resolution formula in TPC digitisation (from Dimitra Tsionou)

## MarlinReco - v01-19

* 2017-05-09 Andre Sailer ([PR#8](https://github.com/iLCSoft/MarlinReco/pull/8))
  - CLICPfoSelector: remove dependency on GEAR File; simplify calculation of TimeAtECal by using trackState at Calorimeter
  - CLICPfoSelector: fix coverity defect
  - TauFinder: fix coverity defects; use streamlog instead of cout

* 2017-06-23 Andre Sailer ([PR#13](https://github.com/iLCSoft/MarlinReco/pull/13))
  - TauFinder:: PrepareRecParticles: change second parameter with same name RecCollection --> RecCollection_Tracks
  - V0Finder: Change second parameter to its correct Name RxyCutGamma --> RxyCutLambda

* 2017-06-20 Andre Sailer ([PR#11](https://github.com/iLCSoft/MarlinReco/pull/11))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-06-20 Shaojun Lu ([PR#10](https://github.com/iLCSoft/MarlinReco/pull/10))
  - Set default from 'ON' to 'OFF' to build MarlinReco fortran sources.
  - It could be switch on in the release-ilcsoft.cfg if you want.
  - https://github.com/iLCSoft/iLCInstall/blob/master/releases/HEAD/release-ilcsoft.cfg#L116

* 2017-06-26 Andre Sailer ([PR#15](https://github.com/iLCSoft/MarlinReco/pull/15))
  - RecoMCTruthLinker: clean collections that are only created for linking. Move cleanup to end of process event instead of trackLinker so things are also cleaned up if there are no tracks. Fixes memory leaks

* 2017-06-26 Frank Gaede ([PR#14](https://github.com/iLCSoft/MarlinReco/pull/14))
  -  replace Gear with DDRec and fix warnings in
          - Compute_dEdxProcessor
          - V0Finder
          - KinkFinder
  - remove obsolete sub-packages:
         - BrahmsTracking
         - FullLDCTracking
         - SiliconTracking
         - TrackCheater
         - TrackbasedPflow
         - Wolf
         - BCalReco
         - ETDDigi
         - FTDDigi

* 2017-06-01 Matthias ([PR#9](https://github.com/iLCSoft/MarlinReco/pull/9))
  - read magnetic field from dd4hep in taufinder particle preparator
  - remove leftover condition for former printout of the taufinder, which prevents the desired increment of the iterator, and thus deletes wrong taucandidates when filling the reconstructed tau's

* 2017-04-22 Andre Sailer ([PR#7](https://github.com/iLCSoft/MarlinReco/pull/7))
  - Re-enable compilation of CLICPfoSelector, CLICDstChecker
  - Fix Warnings in  CLICPfoSelector, CLICDstChecker

* 2017-04-22 Andre Sailer ([PR#6](https://github.com/iLCSoft/MarlinReco/pull/6))
  - Added additional TauFinder processor from Astrid Munnich, see doc/TauFinder/TauFinderLCDNote.pdf for description and performance
  
  - Ignore Warnings from external headers in MarlinReco



## ILDPerformance - v01-03

* 2017-06-20 Andre Sailer ([PR#3](https://github.com/iLCSoft/ILDPerformance/pull/3))
  - ignore warnings from external header files
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-06-07 Shaojun Lu ([PR#2](https://github.com/iLCSoft/ILDPerformance/pull/2))
  - "PCut" and "PTCut" have been added as Marlin steerable parameters.
  - Update Diagnostics.xml to set 'PCut' and 'PTCut' to 0.0

* 2017-06-26 Andre Sailer ([PR#4](https://github.com/iLCSoft/ILDPerformance/pull/4))
  - Adapt to dd4hep namespace changes



## LCFIVertex - v00-07-04

* 2017-06-20 Andre Sailer ([PR#4](https://github.com/iLCSoft/LCFIVertex/pull/4))
  - Split processors into their own library as some tools are used in LCFIPlus, ilcsoft/LCFIVertex#2
  - Drop old boost tarball, rely in cvmfs/system installation of boost that is now needed elsewhere as well, ilcsoft/LCFIVertex#3
  - TState: replace usage of gear with MarlinUtil to get bfield value

* 2017-06-15 Andre Sailer ([PR#1](https://github.com/iLCSoft/LCFIVertex/pull/1))
  - Fixed warnings



## DDMarlinPandora - v00-07

* 2017-04-21 Andre Sailer ([PR#6](https://github.com/iLCSoft/DDMarlinPandora/pull/6))
  - DDSimpleMuonDigi: set ID1 bit to store cellID1 for digitized hits

* 2017-06-20 Frank Gaede ([PR#9](https://github.com/iLCSoft/DDMarlinPandora/pull/9))
  - fix order of includes to get correct tinyxml.h from PandoraPFA 
         - needed on Mac to avoid confusion with tinyxml.h from DD4hep

* 2017-06-20 Andre Sailer ([PR#8](https://github.com/iLCSoft/DDMarlinPandora/pull/8))
  - Adapt to changes in namespaces and LCDD -->  Detector

* 2017-05-10 Andre Sailer ([PR#7](https://github.com/iLCSoft/DDMarlinPandora/pull/7))
  - Add Werror to CI configuration, no more warnings allowed in DDMarlinPandora



## CEDViewer - v01-14-01

* 2017-07-06 Frank Gaede ([PR#4](https://github.com/iLCSoft/CEDViewer/pull/4))
  - add "EcalXXXCollection" to ced2go  template for drawing SimCalorimeterHits
  - fix the drawing of non-prompt neutral MCParticles in CEDViewer


## CEDViewer - v01-14

* 2017-06-20 Andre Sailer ([PR#3](https://github.com/iLCSoft/CEDViewer/pull/3))
  - Adapt to changes in namespaces and LCDD -->  Detector
  - Ignore warnings from external header files


## Overlay - v00-18

* 2017-05-29 Andre Sailer ([PR#6](https://github.com/iLCSoft/Overlay/pull/6))
  - New processor OverlayTimingGeneric: Same as OverlayTiming, but easier configuration of the collections to be merged. No more hard coding of parameters for each parameter name. 
  Shares most of the code and parameters with OverlayTiming
  To configure collections and integration times:
    ```
     <parameter name="Collection_IntegrationTimes" type="StringVec" >
        VertexBarrelCollection        10
        VertexEndcapCollection        10
  
        InnerTrackerBarrelCollection  10
        InnerTrackerEndcapCollection  10
  
        OuterTrackerBarrelCollection  10
        OuterTrackerEndcapCollection  10
  
        ECalBarrelCollection          10
        ECalEndcapCollection          10
        ECalPlugCollection            10
  
        HCalBarrelCollection          10
        HCalEndcapCollection          10
        HCalRingCollection            10
  
        YokeBarrelCollection          10
        YokeEndcapCollection          10
  
        LumiCalCollection             10
        BeamCalCollection             10
      </parameter>
    ```
  - Fix bug in OverlayTiming::cellID2long which returned the same `long long` for different cellID pairs

