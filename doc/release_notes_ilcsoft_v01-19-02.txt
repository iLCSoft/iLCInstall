# Release notes for iLCSoft v01-19-02

Packages changed since last version: 

(*automatically created from individual packages' release notes - might by empty if no changes or not documented*))

## lcio - v02-08



2017-04-11 Frank Gaede ([PR#26](https://github.com/iLCSoft/LCIO/pull/26))

- fix all remaining compiler warnings from -Weffc++
  - using -Wno-non-virtual-dtor ( requires gcc 6 ) on older compilers these warnings will appear but can be safely ignored

2017-03-03 Andre Sailer ([PR#24](https://github.com/iLCSoft/LCIO/pull/24))
- LCTrackerConf: bugfix for checks of encoding string field order

2017-03-03 Marko Petric ([PR#23](https://github.com/iLCSoft/LCIO/pull/23))
- Integate CI with Coverity scan via Travis cron jobs

2017-03-01 Marko Petric ([PR#22](https://github.com/iLCSoft/LCIO/pull/22))
- Update to the CI system:
  - Install directly cvmfs on base system, which removes the need for the parrot connector 
  - Replace CernVM docker with plain docker
  - This reduces the build run time from 15 min to 5 min

2017-03-06 Andre Sailer ([PR#21](https://github.com/iLCSoft/LCIO/pull/21))
- SimTrackerHit: Add Quality bitfield


2017-03-06 Andre Sailer ([PR#19](https://github.com/iLCSoft/LCIO/pull/19))
- LCTrackerConf: allow first field to be called "system"


## lcgeo - v00-11


* 2017-04-19 Frank Gaede ([PR#94](https://github.com/iLCSoft/lcgeo/pull/94))
  - added versions of the ILD Hcal drivers (with Tesla geometry ) that allow to use multiple readout collections:
        - SHcalSc04_Barrel_v04
        - SHcalSc04_Endcaps_v01
        - SHcalSc04_EndcapRing_v01
  - use these drivers in ILD_l4_v01

* 2017-04-13 Frank Gaede ([PR#93](https://github.com/iLCSoft/lcgeo/pull/93))
  - update documentation for ILD detector models ( see ./ILD/compact/README.md )

* 2017-04-13 Shaojun Lu ([PR#92](https://github.com/iLCSoft/lcgeo/pull/92))
  - Remove this demonstration model, we have one complete ILD_l4_v01 now.

* 2017-04-13 Shaojun Lu ([PR#91](https://github.com/iLCSoft/lcgeo/pull/91))
  - Added ILD_l4_v01 as a multi-technology simulation model.
     - It use the common part of the ILD_l1_v01, and replaced the HCAL by a generic HCAL.
     - used multi-segmentation for RPCHits and SciHits.
     - and saved into two collections: HCalBarrelRPCHits/HCalBarrelSciHits,  HCalEndcapRPCHits/HCalEndcapSciHits, HCalECRingRPCHits/HCalECRingSciHits.
     - reconstruction should use them for their HCAL in this model.

* 2017-04-13 Shaojun Lu ([PR#88](https://github.com/iLCSoft/lcgeo/pull/88))
  - Replaced the ILD_o1_v05(obsolete model) with ILD_l1_v01(optimisation model) in lcgeoTests.
     - ILD will focus on  the optimisation models ILD_l1/s1, and maintain/support for optimisation studies.

* 2017-04-13 Frank Gaede ([PR#93](https://github.com/iLCSoft/lcgeo/pull/93))
  - update documentation for ILD detector models ( see ./ILD/compact/README.md )

* 2017-04-13 Shaojun Lu ([PR#92](https://github.com/iLCSoft/lcgeo/pull/92))
  - Remove this demonstration model, we have one complete ILD_l4_v01 now.

* 2017-04-13 Shaojun Lu ([PR#91](https://github.com/iLCSoft/lcgeo/pull/91))
  - Added ILD_l4_v01 as a multi-technology simulation model.
     - It use the common part of the ILD_l1_v01, and replaced the HCAL by a generic HCAL.
     - used multi-segmentation for RPCHits and SciHits.
     - and saved into two collections: HCalBarrelRPCHits/HCalBarrelSciHits,  HCalEndcapRPCHits/HCalEndcapSciHits, HCalECRingRPCHits/HCalECRingSciHits.
     - reconstruction should use them for their HCAL in this model.

* 2017-04-13 Shaojun Lu ([PR#88](https://github.com/iLCSoft/lcgeo/pull/88))
  - Replaced the ILD_o1_v05(obsolete model) with ILD_l1_v01(optimisation model) in lcgeoTests.
     - ILD will focus on  the optimisation models ILD_l1/s1, and maintain/support for optimisation studies.

* 2017-04-07 Dan Protopopescu ([PR#85](https://github.com/ilcsoft/lcgeo/pull/85))
  - Added correct tracker region to SiD models as per #81
  - Added type flags in ECalBarrel_o2_v03_00.xml
  - Updated model version for SiD test

* 2017-04-07 Shaojun Lu ([PR#80](https://github.com/ilcsoft/lcgeo/pull/80))
  - Use MutliCollections configuration to split SiEcal into preShower inside ILD_o1_v05.
     - "CaloPreShowerSDAction" is not necessary in "ddsim_steer.py"
     - The same  "ddsim_steer.py" in ILDConfig will work for all ILD modules.

* 2017-04-07 Shaojun Lu ([PR#78](https://github.com/ilcsoft/lcgeo/pull/78))
  - Added tracker region in "ILD_o4_v01.xml" to fix the MC Truth link in CED display.

* 2017-04-04 Frank Gaede ([PR#79](https://github.com/ilcsoft/lcgeo/pull/79))
  - enforce definition of tracker volume in ddsim - models need to define:
          - tracker_region_zmax
          - tracker_region_rmax
  - this is needed to ensure that the MCTruth link for hits works correctly
  - allow to enable additional DebugDumpActions with *enableDetailedHitsAndParticleInfo*

* 2017-04-04 Dan Protopopescu ([PR#70](https://github.com/ilcsoft/lcgeo/pull/70))
  * SiD: Updated to-do list

* 2017-04-05 Marko Petric ([PR#82](https://github.com/ilcsoft/lcgeo/pull/82))
  - CLIC_o3_v09_NoGaps model is same as CLIC_o3_v09 but has not gaps in calorimeters between barrel and endcap, the calorimeters endcaps have an inner radius of 1cm, therefore the beampipe and lumi and beam call are removed. Model only meant for calo efficiency study.

* 2017-04-02 bogdan ([PR#72](https://github.com/ilcsoft/lcgeo/pull/72))
  - corrections for LHCal01.xml and LHCal_o1_v01_geo.cpp fixing overlaps.
   -  Inner cutout in LHCal envelope changed from octagon to tube, as for some reasons 
      PolyhedraRegular is not subtracted - causing lack of inner cutout in envelope and overlaps 
      with beam pipe.
  -  Fix of bug in geo driver which caused  internal overlaps

* 2017-04-03 luisaleperez ([PR#77](https://github.com/ilcsoft/lcgeo/pull/77))
  - Removed line in FieldMapXYZ that set B-field to zero if point was outside field-map range.

* 2017-04-03 StrahinjaLukic ([PR#75](https://github.com/ilcsoft/lcgeo/pull/75))
  - Corrected BeamCal envelope for the new dimensions of the graphite absorber.
  - Consolidated some BeamCal parameters. Removed a redundant parameter for the incoming beam pipe radius.
  - Added clearance between BeamCal and the incoming beam pipe.

* 2017-04-03 Marko Petric ([PR#74](https://github.com/ilcsoft/lcgeo/pull/74))
  - New model of CLIC detector CLIC_o3_v09, the only change to CLIC_o3_v08 is the Polystyrene -> G4_POLYSTYRENE in the HCal barrel and endcap. This changes the density of the scintilator from 1.032 to 1.06 g/cm3.

* 2017-03-27 Daniel Jeans ([PR#61](https://github.com/ilcsoft/lcgeo/pull/61))
  - Fix bugs in barrel modules size introduced when generalising barrel symmetry
  - Exit gracefully if too many sides requested for barrel

* 2017-03-29 Frank Gaede ([PR#63](https://github.com/ilcsoft/lcgeo/pull/63))
  - add info printout if sensitive action is changed from the default

* 2017-04-08 Andre Sailer ([PR#86](https://github.com/ilcsoft/lcgeo/pull/86))
  - DDSim: Added printout of execution time at the end of simulation

* 2017-03-24 Emilia Leogrande ([PR#60](https://github.com/ilcsoft/lcgeo/pull/60))
  - Replace ILDCellID0 with LCTrackerCellID

* 2017-03-30 Shaojun Lu ([PR#69](https://github.com/ilcsoft/lcgeo/pull/69))
  - Added one option to fill act list in case that we want to use MultiSegmentation and MultiCollection.

* 2017-03-30 Shaojun Lu ([PR#68](https://github.com/ilcsoft/lcgeo/pull/68))
  - Initialise a module "ILD_o4_v01" for a combined RPC/Scintillator HcalBarrel simulation. 
     - Both RPC and Scintillator have 48 layers.
     - MarlinProcessor may access RPC from slice:3 and access Scintillator from slice:6
     - Assign different segmentations and output collections to the different sensitive type.

* 2017-03-30 Frank Gaede ([PR#67](https://github.com/ilcsoft/lcgeo/pull/67))
  - fix a bug in the field maps  FieldMapBrBz.cpp  and FieldMapXYZ.cpp  that prevented overlay
  - (fixes https://github.com/iLCSoft/lcgeo/issues/65 )

* 2017-03-31 luisaleperez ([PR#73](https://github.com/ilcsoft/lcgeo/pull/73))
  - implemented FieldMapXYZ.cpp 
       - a 3D field map defined on a grid in (x,y,z) 
  - added field maps for the ILD solenoid and anti-DID
       -  fieldmaps/ild_fieldMap_antiDID_10cm_v1_20170223.root 
       -  fieldmaps/ild_fieldMap_Solenoid3.5T_StandardYoke_10cm_v1_20170223.root 
  - added example configuration for using these maps to ILD_o1_v05


* 2017-04-12 Daniel Jeans ([PR#87](https://github.com/ilcsoft/lcgeo/pull/87))
  various updates to beampipe description:
  - inner radius of central tube reduced from 14 to 13.5mm to match DBD
  - tube thickness in conical regions corrected for the cone angle
  - second cone: now made of Be-Cu mix, and given uniform thickness of 2.7mm. this is to simulate a 2mm-thick Be beampipe with 0.7mm of Cu cables around it.


* below are release notes before PR script was introduced

Andre Sailer 2017-03-17 
  - delete NULL is a no-op, fix misleading indentation and useless setting of member variable in d'tor, initialise member pointer to NULL

Andre Sailer 2017-02-28 
  - Add Werror to CI setup

TiborILD 2017-03-22 
  - bug fixes

Dan Protopopescu 2017-03-21 
  - Unchanged from o2_v02

Marko Petric 2017-03-21 
  - Mention LICENCE in README
  - Add LICENCE
  - fix README
  - Update README.md
  - Create README.md

StrahinjaLukic 2017-03-17 
  - Adding test of the BeamCal z location for ILD detectors.
  - Adjusting indentation to surrounding code
  - Removing unneeded sliceType graphiteShielding, correcting indentation.

StrahinjaLukic 2017-03-16 
  - Minor edit in BeamCal08.xml for consistence
  - Resolving incorrect whitespace by hand
  - Correcting code.
  - Restoring another lost line.
  - Lost closing bracketwq
  - Correcting a minor error in the code
  - Removing hardcoded check of BeamCal z.
  - Another minor error...
  - Correcting a minor error in the code
  - Removing hardcoded check of BeamCal z.
  - Changes requested by Andre.

StrahinjaLukic 2017-03-15 
  - Implementing the optional outer_radius attribute for the BeamCal graphite shield as suggested by Andre
  - Changes requested by Andre.
  - Minor edit to the BeamCal driver

StrahinjaLukic 2017-03-14 
  - Adding BeamCal_LHCal.xml for testing relative position of BeamCal and LHCal. Moving BeamCal towards LHCal.
  - Updated segmentation for BeamCal. BC sensor cutout 45 deg. BC phi spanning 360deg-cutout.
  - Adding BeamCal_LHCal.xml for testing relative position of BeamCal and LHCal. Moving BeamCal towards LHCal.
  - Minor fixes and debug messages.
  - Defining top_BCal_dGraphite in top_defs_common and adjusting BeamCal envelope.
  - Updating the BeamCal inner radius and adapting the segmentation.
  - Implementing the optional outer_radius attribute for the BeamCal graphite shield as suggested by Andre
  - BCal_rGraphite has 10mm clearance from LHCal bore. Defined in fcal_defs.xml, removed elsewhere.
  - Proportional segmentation for BeamCal
  - Adding BeamCal_LHCal.xml for testing relative position of BeamCal and LHCal. Moving BeamCal towards LHCal.

StrahinjaLukic 2017-03-13 
  - Adding new parameter BCal_rGraphite to allow graphite shielding to have different outer radius than BeamCal

bogdan 2017-03-18 
  - LHCal envelope correction

bogdan 2017-03-17 
  - asymetric inner cutout, placement fix -  no x-angle rotation
  - info print modified
  - top_Lcal_z_begin set to Ecal_endcap_zmin
  -  LCal aligned with begin ECalPlug and LHCal tied to ECalPug end
  - increased number of layer to 30

Dan Protopopescu 2017-03-15 
  - Update SiTrackerBarrel_o2_v02_00.xml
  - Update SiTrackerEndcap_o2_v02_01.xml
  - Update SiD_o2_v02.xml
  - Added updated Forward Tracker

Daniel Jeans 2017-03-15 
  - add a couple of comments
  - update ECAL: allow other polyhedral barrel shapes (endcaps still octagons); configurable dead region due to slab plug (default 0)

bogdan 2017-03-14 
  -  replace LHcal.xml with new LHCal01.xml in top XML
  -  -update LHcal geometry according to info from yuno@univ.kiev.ua  -new LHCal driver centering detector at outgoing beam pipe   and building LHcal with octagonal inner bore  - new extra utility, FCAL_l1_v01.xml to build FCAL components only

TiborILD 2017-03-08 
  - detecor type flags added/corrected

TiborILD 2017-03-02 
  - correct the cell size for Hcal_EndcapRing_SD in ILD_s2_v01.xml

Frank Gaede 2017-03-03 
  - switch back to constant B-field for ILD_o1_v05

Marko Petric 2017-03-02 
  - Add sourcing of env in SensThickness tests

Marko Petric 2017-03-01 
  - Replace the tube shaped cones with actual tubes

TiborILD 2017-02-28 
  - Hcal_Endcaps_SD_v02 box geometry (as of SHalSc04)
  - Hcal_Endcaps_SD_v02 box geometry (as of SHalSc04)

TiborILD 2017-02-24 
  - Hcal_Endcaps_SD_v01.xml : cleaning & typo correction
  - some typo corrections & cleaning
  - ILD_s2_v01.xml : typo correction for HcalEndcapsCollection
  - ILD_l2_v01.xml : typo correction for HcalEndcapsCollection
  - Hcal_Endcaps_SD_v01.xml: rot_z correction & cleaning

Andre Sailer 2017-02-24 
  - Add guineapig.particlesPerEvent option, including documentation
  - Revert " add readerParameters to input readers"

Frank Gaede 2017-03-01 
  - mv Geant4EventReaderGuineaPig.cpp to DD4hep

Marko Petric 2017-02-28 
  - New driver for simple tube support
  - Keep compilation going after error

Frank Gaede 2017-02-24 
  - implment skipping to event in  GuineaPig reader
  - add parameter ParticlesPerEvent to GuineaPig reader
  -  add readerParameters to input readers
  - add component DDParsers (needed on macos)

Andre Sailer 2017-02-23 
  - TubeX01: drop register, clang warning, useless anyway
  - SServices00: comment unsed private variable (clang warning)
  - Add new/correct spelling for ROOT_INCLUDE_DIRS, root headers properly ignored now

Andre Sailer 2017-02-22 
  - LcgeoExceptions: Fix warning for llvm
  - TPCSDAction: fix shadow and unused variable warnings
  - VXD04: fix shadow and unused variable warnings
  - ECal05, plug: comment unused (Placed)Volumes, variables
  - SECal04_*: comment unsed placedvolume variable
  - SECal05_helper: delete NULL is a no-op we don't have to test before deleting
  - LumiCal_o1_v02: fix warnings for unused variables
  - ODH: static --> inline to avoid unused-function warnings
  - Fix warnings: set but not used and shadowing in detectors used by CLIC

TiborILD 2017-02-21 
  - added  Hcal_Endcaps_SD_v01.xml

Tibor Kurca 2017-02-21 
  - added  Hcal_Endcaps_SD_v01.cpp
  - added  Hcal_EndcapRing_SD_v01.cpp
  - Hcal_Barrel_SD_v01.cpp  5 modules & updates
  - ILD_s2_v01.xml modified for SDHcal
  - ILD_l2_v01.xml modified for SDHcal
  - Hcal_EndcapRing_SD_v01.xml added
  - graphite material added
  - added absorber slice, swapped epoxy/PCB slices
  - HcalSD_ extra parameters names for SDHcal

Dan Protopopescu 2017-02-21 
  - Rename detector/SiTrackerEndcap_o2_v02ext_geo.cpp to detector/tracker/SiTrackerEndcap_o2_v02ext_geo.cpp
  - Delete SiTrackerEndcap_o2_v02ext_geo.cpp

bogdanmishchenko 2017-02-17 
  - Add files via upload

bogdanmishchenko 2017-02-16 
  - Add files via upload

Dan Protopopescu 2017-02-14 
  - Updated driver after closing previous pull request

Marko Petric 2017-02-15 
  - Add the copper cables to the shell of the ourter tracker
  - Move airshell backwards
  - Remove cable from vertex

Marko Petric 2017-02-13 
  - Remove obsolete gitlab CI badge
  - Change surfaces to form a right handed system

Frank Gaede 2017-02-14 
  - split pair files into events in Geant4EventReaderGuineaPig

Frank Gaede 2017-02-13 
  - add vertex info in  Geant4EventReaderGuineaPig

Dan Protopopescu 2017-02-08 
  - Update ECalBarrel_o1_v03_geo.cpp
  - Update SiD_o2_v02.xml

Dan Protopopescu 2017-02-07 
  - Update SiD_o2_v02.xml
  - Update Solenoid_o2_v02_00.xml
  - Create ECalBarrel_o2_v03_00.xml

simoniel 2017-02-08 
  - Added region definitions for G4 material scan.

Frank Gaede 2017-02-08 
  - add ILD_s2_v01 with SDHcal from ILD_o2_v01
  - add ILD_l2_v01 with SDHcal from ILD_o2_v01

Shaojun Lu 2017-02-08 
  -  Following the update of small ILD, the HCAL radius has been reduced by ~34cm (HBU:36cm). Added one version 'SHcalSc04_Endcaps_sv01.xml' for the small AHCAL Endcaps, which has reduced one HUB at x and y, and 14 towers at x direction.(large ILD has 16 towers in endcaps from HBU.)

Andre Sailer 2017-01-27 
  - DDSim: Change default tracker action to Geant4TrackerWeightedAction

Dan Protopopescu 2017-02-01 
  - Delete SiTrackerEndcap_o2_v02_00.xml
  - Rename SiTrackerEndcap_o2_v01_01.xml to SiTrackerEndcap_o2_v02_01.xml
  - Add files via upload
  - Update SiVertexBarrel.xml
  - Rename Solenoid_o2_v01_00.xml to Solenoid_o2_v02_00.xml
  - Rename MuonEndcap_o2_v01_01.xml to MuonEndcap_o2_v02_01.xml
  - Rename MuonBarrel_o2_v01_01.xml to MuonBarrel_o2_v02_01.xml
  - Rename LumiCal_o2_v01_00.xml to LumiCal_o2_v02_00.xml
  - Rename HCalEndcap_o2_v01_01.xml to HCalEndcap_o2_v02_01.xml
  - Rename HCalBarrel_o2_v01_00.xml to HCalBarrel_o2_v02_00.xml
  - More files copied over from SiD_o2_v01_prelim
  - Delete test
  - Rename ECalEndcap_o2_v01_00.xml to ECalEndcap_o2_v02_00.xml
  - Rename ECalBarrel_o2_v01_00.xml to ECalBarrel_o2_v02_00.xml
  - Add files via upload
  - Rename SiVertexEndcap_o2_v01.xml to SiVertexEndcap_o2_v02.xml
  - Rename SiTrackerEndcap_o2_v01_00.xml to SiTrackerEndcap_o2_v02_00.xml
  - Rename SiTrackerBarrel_o2_v01_00.xml to SiTrackerBarrel_o2_v02_00.xml
  - Add files via upload
  - Add files via upload
  - Add files via upload
  - Create BeamPipe.xml
  - Create BeamCal_o2_v02_00.xml
  - Create test
  - Update SiD_o2_v02.xml
  - Update SiD_o2_v02.xml
  - Create SiD_o2_v02.xml

Frank Gaede 2017-02-02 
  - fix orientation of surface vectors in SIT, FTD

Marko Petric 2017-02-01 
  - Remove deprecated drivers to new ones
  - Add test for CLIC_o3_v08
  - Unify all tracker readout IDs with global parameter
  - Add missing materials
  - Add DD4hepVolumeManager
  - Fix the possition of the ECal surface
  - Remove regions since we do not need to go away from the global range cut
  - Fix the problem with missing outer radius for solenoid
  - The whole new tracker
  - Remove warnings from ConicalSupport
  - Fix conical support by removing a obsolete subtraction
  - This is the update of the Inner tracker
  - Update Vertex with cables and redefine materials
  - Add new drivers that read includes inside module block

Dan Protopopescu 2017-01-31 
  - Create README.md
  - Create README.md

Daniel Jeans 2017-01-27 
  - add rec geometry data to SEcal05_Endcaps.cpp driver

Daniel Jeans 2017-01-24 
  - remove SEcal04_ECRing.xml for previous driver
  - SEcal05_siw_ECRing for s1 model; fix FTD envelope definition (go to end of TPC) to avoid overlap
  - introduce SEcal05_ECRing driver: hole centered on outgoing beam; preshower status taken into account. Use this driver in ILD_(l,s)1_v01 models

Frank Gaede 2017-01-24 
  - mv sensitive  plugins; rm obsolete SDs

luisaleperez 2017-01-20 
  - Adding new guinea-pig event plugin
  - Adding new guinea-pig event plugin

luisaleperez 2017-01-19 
  - Using new field-map XYZ
  - Adding new field-map XYZ

Luis Alejandro Perez Perez 2017-01-19 
  - Adding new field-map XYZ

Frank Gaede 2017-01-18 
  - add example conversion:: guineapig_to_lcio.py

## DD4hep - v00-21


* 2017-04-03 Marko Petric ([PR#142](https://github.com/AIDASoft/DD4hep/pull/142))
  - Update to the CI system:
    - Install directly cvmfs on base system, which removes the need for the parrot connector 
    - Replace CernVM docker with plain docker
    - This reduces the build run time from 50 min to 25 min

* 2017-03-27 Shaojun Lu ([PR#134](https://github.com/AIDASoft/DD4hep/pull/134))
  - Set verbose true for G4EmSaturation to printout Birks coefficient.

* 2017-03-29 Frank Gaede ([PR#139](https://github.com/AIDASoft/DD4hep/pull/139))
  - add a utility to dump the B-field for a given Volume
          - usage: dumpBfield compact.xml x y z dx dy dz [in cm]  
          - will dump the B-field in volume [-x:x,-y:y,-z,z] with steps [dx,dy,dz]

* 2017-03-29 Joschka Lingemann ([PR#138](https://github.com/AIDASoft/DD4hep/pull/138))
  - Direct implementation that calculates eta from cartesian coordinates
  - Fix: Add registration of Phi-Eta segmentation

* 2017-03-29 Joschka Lingemann ([PR#137](https://github.com/AIDASoft/DD4hep/pull/137))
  - Adding GridRPhiEta a segmentation of equidistant size in R, Phi and Pseudorapidity
  - Adding GridPhiEta a segmentation of equidistant size in Phi and Pseudorapidity

* 2017-03-28 Markus Frank ([PR#135](https://github.com/AIDASoft/DD4hep/pull/135))
  - Accidentally the Segmentations of Joschka were added in the wrong place of the hierarchy.
     I removed them. He will later add them to the proper location.
  - Some C++ warnings concerning the C++11 standard were also fixed.

* 2017-03-24 Yorgos Voutsinas ([PR#132](https://github.com/AIDASoft/DD4hep/pull/132))
  - modifying the LayeredCalorimeterData struct in order to cope with conical shaped calorimeters

* 2017-03-31 Markus Frank ([PR#143](https://github.com/AIDASoft/DD4hep/pull/143))
  - Add new test for multi segment multi collections segmentations using a calorimeter endcap.
     See also: https://github.com/AIDASoft/DD4hep/issues/141, which is still unresolved,
     but seems not to be directly related to the Monte-Carlo truth handling.
  - Side effect: add Geant4EventActions to dump hits and particles
  - Fix a linker problem for unicode tags.

* 2017-03-31 Frank Gaede ([PR#140](https://github.com/AIDASoft/DD4hep/pull/140))
  - clarify documentation for CartesianField and implementations
  - make clear that  void fieldComponents() has to add
     the new field to the given field vector

Marko Petric 2017-03-23 
  - Convert Release notes to markdown
  - Add some text about WIP and issue tracking
  - Add CONTRIBUTING.md and PULL_REQUEST_TEMPLATE

Markus Frank 2017-03-17
 
 - Add a new input type by parsing JSON files. The basic json interpreter
    is present and offers essentially the same interface as the XML persers.
    The integration to the compact dialect however is not yet done.
    It should become however a valid alternative to parsing XML files
    with a small maintenance overhead, since the enhancement implementation
    present in XMLDimesion.h, XMLDetector.h and XMLChildValue.h is shared
    and instantiated for both.

Markus Frank 2017-03-10
 
 - New round to kill coverity deficiencies.
 - Add exception try-catch clauses around various main programs in UtilityApps
    See UtilityApps/src/main.h for details.

Markus Frank 2017-03-09
 
 - Fix issue with long volume ids exceeding 32 bits.
    Test added in examples/ClientTests
 - Fix volume manager id identical placed volumes are used in different places of the hierarchy.
    Test added in examples/ClientTests
 - Remove various svn left-overs (ID$ strings etc.)


Frank Gaede 2017-02-10
 
- allow event readers to create more than one vertex per event
     this should be possible as most generator formats allow to specify
     more than one event vertex 
  - changed signature of Geant4EventReader::readParticles(int,Vertex*, Particles&)
        to Geant4EventReader::readParticles(int,Vertices&, Particles& )
  - implement in LCIOEventReader, Geant4EventReaderHepEvt and Geant4EventReaderHepMC
  - for now still one vertex only is created using the first final state particle
        for HepEvt and LCIO

## gear - v01-07


## MarlinFastJet - v00-04


* 2017-03-29 Andre Sailer ([PR#5](https://github.com/iLCSoft/MarlinFastJet/pull/5))
  - Update CI to not allow new warnings to be merged into MarlinFastJet

* 2017-03-24 Andre Sailer ([PR#6](https://github.com/iLCSoft/MarlinFastJet/pull/6))
  - Merged the FastJetClustering processor into the MarlinFastJet package
  - Fix Warnings in FastJetClustering processor

## KalTest - v02-03



Frank Gaede 2017-04-12 
  - Updating version to v02-03
  - Release Notes for v02-03

Marko Petric 2017-04-08 
  - Coverity integration

Marko Petric 2017-03-23 
  - Add install statement to CI
  - Add CONTRIBUTING.md and PULL_REQUEST_TEMPLATE and fix test script

Frank Gaede 2017-03-21 
  - add AUTHORS file

Marko Petric 2017-03-21 
  - Update release notes
  - Enable CI and add LICENCE

## KalDet - v01-14


## aidaTT - v00-06


* 2017-04-03 Emilia Leogrande ([PR#11](https://github.com/AIDASoft/aidaTT/pull/11))
  -Replace ILDCellID0 with LCTrackerCellID

* 2017-04-12 Shaojun Lu ([PR#12](https://github.com/AIDASoft/aidaTT/pull/12))
  - Added "-DGBL_EIGEN_SUPPORT_ROOT" to allow  GBLInterface.cc still use ROOT from GBL.

## DDKalTest - v01-02


* 2017-04-07 Emilia Leogrande ([PR#2](https://github.com/iLCSoft/DDKalTest/pull/2))
  - DDKalTestConf replaced by LCTrackerConf

## MarlinTrk - v02-03


## MarlinTrkProcessors - v02-06


* 2017-04-06 Emilia Leogrande ([PR#9](https://github.com/iLCSoft/MarlinTrkProcessors/pull/9))
  - Replaced ILDCellID0 with LCTrackerCellID
  - Replaced DDKalTestConf with LCTrackerConf

* 2017-04-07 Andre Sailer ([PR#8](https://github.com/iLCSoft/MarlinTrkProcessors/pull/8))
  - Fix many warnings for gcc
  - ExtrToSIT::SelectBestCandidateLimited: remove variable shadowing pointer parameter
  - ExtrToTracker: Fix bug when using performFinalRefit where the refitted track was not used after refit

## KiTrack - v01-08



## KiTrackMarlin - v01-10



## ForwardTracking - v01-11

- moved code to GitHub

Oleksandr Viazlo 2017-03-21 
  - Replace ILDCellID0 with LCTrackerCellID

Marko Petric 2017-03-23 
  - Add install statement to CI
  - Add CONTRIBUTING.md and PULL_REQUEST_TEMPLATE and fix test script

Frank Gaede 2017-03-21 
  - add AUTHORS file

Marko Petric 2017-03-20 
  - fix markdown
  - Enable CI and add LICENCE

## ConformalTracking - v01-02


* 2017-03-29 Daniel Hynds ([PR#3](https://github.com/iLCSoft/ConformalTracking/pull/3))
  - Collections are added sequentially to the list of hits being used to make tracks, including unused hits from the previous collections. Previously hits were considered individually before this step, leading to missed hits in the interaction region.

* 2017-03-28 Andre Sailer ([PR#2](https://github.com/iLCSoft/ConformalTracking/pull/2))
  - Removed "CellIDDecoderString" parameter, not necessary by using encoding_string()

## lccd - v01-04



Marko Petric 2017-04-08
  - Coverity integration

Marko Petric 2017-03-23
  - Add install statement to CI
  - Add CONTRIBUTING.md and PULL_REQUEST_TEMPLATE and fix test script

Frank Gaede 2017-03-21
  - add AUTHORS file

Marko Petric 2017-03-20
  - Fix typo LCDD -> LCCD
  - Enable CI and add LICENCE

## RAIDA - v01-08


## MarlinUtil - v01-13


## Marlin - v01-11


* 2017-02-27 Andre Sailer ([PR#8](https://github.com/iLCSoft/Marlin/pull/8))
  - Fix warnings for GCC
  - moved tinyXML to separate library

* 2016-12-07 Marko Petric ([PR#6](https://github.com/iLCSoft/Marlin/pull/6))
  - Made CI configuration generic and usable for all packages without modifications

* 2016-12-07 Andre Sailer ([PR#4](https://github.com/iLCSoft/Marlin/pull/4))
  - Add travis configuration to repository, enable testing for PRs

* 2016-11-25 Frank Gaede ([PR#3](https://github.com/iLCSoft/Marlin/pull/3))
  - Fix warnings for clang
  - ignore warnings from external headers


* 2017-02-27 Andre Sailer ([PR#8](https://github.com/iLCSoft/Marlin/pull/8))
  - Fix warnings for GCC
  - moved tinyXML to separate library

* 2016-12-07 Marko Petric ([PR#6](https://github.com/iLCSoft/Marlin/pull/6))
  - Made CI configuration generic and usable for all packages without modifications

* 2016-12-07 Andre Sailer ([PR#4](https://github.com/iLCSoft/Marlin/pull/4))
  - Add travis configuration to repository, enable testing for PRs

* 2016-11-25 Frank Gaede ([PR#3](https://github.com/iLCSoft/Marlin/pull/3))
  - Fix warnings for clang
  - ignore warnings from external headers

## MarlinDD4hep - v00-04


* 2017-04-07 Andre Sailer ([PR#4](https://github.com/iLCSoft/MarlinDD4hep/pull/4))
  - DDKalTestConf replaced by LCTrackerConf

A.Sailer
- ignore warnings from external packages
- add parameter "EncodingStringParameter", alternate spelling of "EncodingStringParameterName" for compatibility, 
- Alternate spelling can be phased out once everyone has moved to new installation of this package
- Also change DDKaltest:DDKaltestConf instance of encoding string
- MarlinDD4hep now depends on DDKalTest until DDKalTestConf is moved to LCIO

## MarlinReco - v01-18


* 2017-03-30 Andre Sailer ([PR#4](https://github.com/iLCSoft/MarlinReco/pull/4))
  - RecoMCTruthLinker: move encoder initialisation from constructor to function body to avoid accessing encoding_string too early

* 2017-03-24 Emilia Leogrande ([PR#2](https://github.com/iLCSoft/MarlinReco/pull/2))
  - Replace ILDCellID0 to LCTrackerCellID

* 2017-04-12 Shaojun Lu ([PR#5](https://github.com/iLCSoft/MarlinReco/pull/5))
  - update to latest changes in LCIO
         - removed deprecated SimTrackerHit::setCellID
         - don't use assignment for CellIDDecoder

## ILDPerformance - v01-02





Oleksandr Viazlo 2017-03-21 
  - Replace ILDCellID0 with LCTrackerCellID

## LCFIVertex - v00-07-03



## MarlinKinfit - v00-05


## MarlinKinfitProcessors - v00-03


## DDMarlinPandora - v00-06



## CEDViewer - v01-13


## Overlay - v00-17


## LCTuple - v01-07


## Physsim - v00-04


