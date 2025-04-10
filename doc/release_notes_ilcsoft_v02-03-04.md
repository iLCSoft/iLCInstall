# iLCSoft v02-03-04

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

This patch release comes with several fundamental updates:
- OS updated from CentOS7 to EL9
- Compiler updated from gcc10.3 to gcc13.1
- The c++ standard has been updated to c++20
- Python version updated from 3.9 to 3.11

## External software versions upgrade
- ROOT 6.30/04 :arrow_right: 6.32.10
- DD4hep 01-28 :arrow_right: 01-31
- Geant4 11.2.1 :arrow_right: 11.3.1
- CMake 3.28.3 :arrow_right: 3.31.6
- boost 1.84.0 :arrow_right: 1.87.0
- FastJet 3.4.2 :arrow_right: 3.4.3
- FastJet Contrib 1.054 :arrow_right: 1.056
- Qt 5.13.1 :arrow_right: 5.15.15 (from underlying LCG_106 stack)

# New packages

None

## Packages changed wrt. v02-03-03

### LCIO v02-22-04 (merged notes for several tags)

* 2025-02-03 Thomas Madlener ([PR#201](https://github.com/iLCSoft/LCIO/pull/201))
  - Make it possible to create empty subset collections during patching
    - Appending a **`*`** (star) to the collection type name (no spaces) will make this collection an empty subset collection if it is not already present.
    - Fixes [#199 ](https://github.com/iLCSoft/LCIO/issues/199)

* 2024-10-20 Valentin Volkl ([PR#197](https://github.com/iLCSoft/LCIO/pull/197))
  - Fix compilation on MacOS by adding missing include in dumpmctree-dot.cc

* 2024-09-05 tmadlener ([PR#193](https://github.com/iLCSoft/LCIO/pull/193))
  - Add functionality to `CheckCollections` that makes it possible to add missing ParticleID algorithms to ReconstructedParticle collections
    - This makes it possible to make very consistent event contents that are necessary for conversion to EDM4hep

* 2024-08-01 tmadlener ([PR#196](https://github.com/iLCSoft/LCIO/pull/196))
  - Run Key4hep CI workflows on OSs that are still supported

* 2024-08-01 tmadlener ([PR#195](https://github.com/iLCSoft/LCIO/pull/195))
  - Add a basic `.gitignore` file to avoid accidentally comitting configured / generated files

* 2024-08-01 Thomas Madlener ([PR#194](https://github.com/iLCSoft/LCIO/pull/194))
  - Make sure to require a version of SIO that is consistent with what we would use to build an internal version.
  
* 2024-06-24 jmcarcell ([PR#192](https://github.com/iLCSoft/LCIO/pull/192))
  - Fix possibly wrong behavior with `std::remove_if` with a `erase - remove` idiom

* 2024-06-24 Wouter Deconinck ([PR#191](https://github.com/iLCSoft/LCIO/pull/191))
  - fix: parentheses in SIOTrack.java

* 2024-06-07 tmadlener ([PR#189](https://github.com/iLCSoft/LCIO/pull/189))
  - Remove mentions of the removed F77 API (see [#161](https://github.com/iLCSoft/LCIO/pull/161)) from the documentation

* 2024-06-06 tmadlener ([PR#190](https://github.com/iLCSoft/LCIO/pull/190))
  - Remove the no longer used settings for the 32bit compatibility mode

* 2024-06-06 Nazar Bartosik ([PR#147](https://github.com/iLCSoft/LCIO/pull/147))
  - Add `Nholes` and and `subdetectorHoleNumbers` to the `Track` for keeping track of missing hits in a Track.

* 2024-05-08 Bohdan Dudar ([PR#170](https://github.com/iLCSoft/LCIO/pull/170))
  - Added new utility `dumpmctree` to draw the MC table of the event stored in the slcio file as the graphviz tree diagram, which represents parent-daughter relations visually in a easier way.
    - `dumpmctree` is a small wrapper script around the actual `dumpmctree-dot` executable. The latter produces a `.dot` file which is then transformed into an `.svg` file via the wrapper script and the `dot` executable.
    - The script relies on `dot` & `xdg-open` to be available on your system.

* 2024-04-15 tmadlener ([PR#188](https://github.com/iLCSoft/LCIO/pull/188))
  - Make the `PIDHandler` usable as `const` object by marking getters that do not mutate internal state as `const`

### Marlin v01-19-04 (merged notes from several tags)

* 2025-01-13 jmcarcell ([PR#62](https://github.com/iLCSoft/Marlin/pull/62))
  - Include GNUInstallDirs to set CMAKE_INSTALL_LIBDIR so that the default rpath is correct in MacOS and can be used in downstream projects, like in `k4MarlinWrapper`

* 2024-08-22 tmadlener ([PR#59](https://github.com/iLCSoft/Marlin/pull/59))
  - Make sure the `LCIO::lcio` target is also defined in packages consuming Marlin (necessary after #56)

* 2024-08-22 tmadlener ([PR#58](https://github.com/iLCSoft/Marlin/pull/58))
  - Make sure that all names that are used by `EventModifier` are forward declared
  - Add missing include to make `EventModifier` usable without having to re-order includes
  - Update the key4hep based github action workflows to use supported OSs

* 2024-08-22 jmcarcell ([PR#56](https://github.com/iLCSoft/Marlin/pull/56))
  - Change LCIO_LIBRARIES to LCIO::lcio

### MarlinReco v01-36-02 (merged notes from several tags)

* 2025-02-20 Bohdan Dudar ([PR#146](https://github.com/iLCSoft/MarlinReco/pull/146))
  - Fix a segmentation fault in RecoMCTruthLinker when an MCParticle is not found in the internal map (see [#125](https://github.com/iLCSoft/MarlinReco/issues/125))

* 2024-10-01 Bohdan Dudar ([PR#142](https://github.com/iLCSoft/MarlinReco/pull/142))
  - Fix `mismateched-new-delete` warning uncovered by gcc14 (see [#140](https://github.com/iLCSoft/MarlinReco/issues/140))

* 2024-09-09 jmcarcell ([PR#139](https://github.com/iLCSoft/MarlinReco/pull/139))
  - Add a missing `#include <algorithm>`

* 2024-09-03 Thomas Madlener ([PR#137](https://github.com/iLCSoft/MarlinReco/pull/137))
  - Remove CentOS7 from the Key4hep CI workflows

* 2024-07-30 Ulrich Einhaus ([PR#136](https://github.com/iLCSoft/MarlinReco/pull/136))
  Bug: PFOs were ignored if their MC PDG was not among signal or background PDGs. This is of minor effect, since by default all detector-stable charged particles are considered signal or background, but could lead to MC info leaking into reconstructed values in case of unintended usage.
  Solution: This effect now requires training mode to be ON, which is exclusive with inference mode.

* 2024-06-24 tmadlener ([PR#135](https://github.com/iLCSoft/MarlinReco/pull/135))
  - Add a `ReconstructedParticleParticleIDFilterProcessor` that allows to filter `ParticleID` objects from existing `ReconstructedParticle`s.

* 2024-06-24 tmadlener ([PR#132](https://github.com/iLCSoft/MarlinReco/pull/132))
  - Make the `TrueJet` processor use the `PIDHandler` to set the `ParticleIDs` for the different objects it creates. This sets the necessary metadata that is required, e.g. for the conversion to EDM4hep.

* 2024-06-19 Carl Mikael Berggren ([PR#134](https://github.com/iLCSoft/MarlinReco/pull/134))
  Reduce the size of the ParticleID vector for the final fermion-antifermion pair, since
  
  for this case, there can only be one pair. This to avoid cluttering of empty collections after transition to the EDM4HEP world. At the same time, the documentation and example steerings in the examples subdirectory have been updated. mainly for the move of TrueJet_Parser from here to MarlinUtil, but also spell-checking etc.

* 2024-06-10 Ulrich Einhaus ([PR#133](https://github.com/iLCSoft/MarlinReco/pull/133))
  - This adds the WWCategorisationProcessor to MarlinReco
  - It categorises each event by its WW decays channels. It provides a true category (only meaningful for true WW events) as well as two levels of reconstructed category. They are stored as event parameters.
  - This may serve as common coherent categorisation for any analyses using WW events.

* 2024-05-07 Bohdan Dudar ([PR#99](https://github.com/iLCSoft/MarlinReco/pull/99))
  - Fix all compiler warnings in MarlinReco, including
    - A lot of shadowed variables
    - A lot of unused parameters / variables
    - A few deprecations
    - A genuine use-after-free bug
    - A few others
  - Make at least one CI workflow use `-Werror` to make it harder to (re-)introduce new warnings

* 2024-04-16 NAKAJIMA Jurina ([PR#131](https://github.com/iLCSoft/MarlinReco/pull/131))
  - Fixed PDG code for kinks identifies as antiSigma+

### MarlinUtil v01-18-02 (merged notes from two tags)

* 2025-03-31 Thomas Madlener ([PR#49](https://github.com/iLCSoft/MarlinUtil/pull/49))
  - Make sure to fetch a Catch2 version that can actually be built with the required C++ standard.

* 2024-08-26 tmadlener ([PR#47](https://github.com/iLCSoft/MarlinUtil/pull/47))
  - Fix a potential indexing issue in `WeightedPoints3D`
  - Remove no longer supported CentOS7 from Key4hep workflows

* 2024-06-20 tmadlener ([PR#46](https://github.com/iLCSoft/MarlinUtil/pull/46))
  - Prefix currently unprefixed member variables of the `TrueJet_Parser` with an `m_` prefix.

* 2024-06-19 Ulrich Einhaus ([PR#45](https://github.com/iLCSoft/MarlinUtil/pull/45))
  - Adds SelectNthEventsProcessor.
  - This sets its own processor ReturnValue to true or false, depending on chosen parameters, which can be used in the Marlin steering file to use a particular sub-set of a sample.
  - Via the InvertSelection parameter this can be easily inverted, which is convenient for training vs. inference of ML models.

* 2024-04-29 tmadlener ([PR#44](https://github.com/iLCSoft/MarlinUtil/pull/44))
  - Update CI to use latest clicdp nightlies and central key4hep build workflows
  - Make Catch2 discovery a bit more robust and easier to use

* 2024-04-29 Bohdan Dudar ([PR#43](https://github.com/iLCSoft/MarlinUtil/pull/43))
  - Avoid the TColor warning when retrieving existing colours.

### k4geo (lcgeo) v00-21-00

* 2024-10-02 mahmoudali2 ([PR#401](https://github.com/key4hep/k4geo/pull/401))
  - IDEA_o1_v03: Moving IDEA muon system starting point in both barrel (rmin) and endcap (z-offset) 30 mm, backwards to avoid overlapping with Dual readout calorimeter.
    - The change including also updating chamber names to distinguish between muon chambers and pre shower chamber, since they are using the same uURWELL chamber.
    - Change dimensions of solenoid/endplate and move the pre-shower to avoid overlaps with dual readout calorimeter

* 2024-10-02 michaela mlynarikova ([PR#395](https://github.com/key4hep/k4geo/pull/395))
  - fix printout messages in HCal Tile barrel and Endcap three parts detector builder

* 2024-10-01 tmadlener ([PR#398](https://github.com/key4hep/k4geo/pull/398))
  - Switch the `pre-commit` action to run in a Key4hep environment
  - Add `ruff` formatting to `pre-commit`
  - Fix a few python2 style `print` statements
  - Fix format of all python files

* 2024-10-01 mahmoudali2 ([PR#397](https://github.com/key4hep/k4geo/pull/397))
  - Generalizing the muon system builder to adopt pre-shower description, the changes include:
       - Making the variable names more general, not specific only for muon system.
       - Changing the detector side's volume thicknesses in case there is only one chambers row in the side (like the pre-shower case), and it's in general it is the case for any -almost- circular shape for the detector. 
       - Disallowing the overlap rotation in case of single chamber side.
  - Overall, the changes make the builder more general to adopt different cases with different structures (polyhedron & cylinder of chambers).

* 2024-10-01 Thomas Madlener ([PR#394](https://github.com/key4hep/k4geo/pull/394))
  - Improve readability of README for FCCee MDI

* 2024-09-25 armin.ilg ([PR#396](https://github.com/key4hep/k4geo/pull/396))
  - No more warnings in silicon wrapper
  - Improvements in vertex builder printouts
  - Adding all materials of beam pipe also to material_plots_2D.py, as without having the beam pipe enabled, the vertex material budget estimation will fail.
  - Changed paths to .stl files in vertex to use https://fccsw.web.cern.ch/fccsw/filesForSimDigiReco/IDEA/IDEA_o1_v03/STL_FILES/ (still commented out due to overlaps)

* 2024-09-19 Armin Fehr ([PR#363](https://github.com/key4hep/k4geo/pull/363))
  - Update of IDEA vertex, with the ability to use the ultra-light vertex concept in-situ.
  - No overlaps in all of vertex and silicon wrapper (not including the DDCAD imported vertex support and cooling cones yet), more performant silicon wrapper (only silicon wrapper barrel sensors are simplified)

* 2024-09-18 Erich Varnes ([PR#379](https://github.com/key4hep/k4geo/pull/379))
  * ECalEndcap_Turbine_o1_v01_geo: Fix issues with printout (to allow verbosity to be controlled from run script).  
  * Add ECalEndcap_Turbine_o1_v02_geo of the "turbine" endcap geometry: which allows for more flexibility than v01 (for example, one can set different blade angles for the three wheels in v02).  As v02 is still a work in progress, the default xml points to v01.

* 2024-09-16 JEANS Daniel Thomelin Dietrich ([PR#388](https://github.com/key4hep/k4geo/pull/388))
  - For ILD models only: apply the same step limits as defined for the tracker ("Tracker_limits", currently 5mm) inside the beampipe volume and MDI region. This is important for tracking of low momentum particles  (eg beamstrahlung pairs) especially in non-uniform fields. Should have no noticeable effect in other situations.

* 2024-09-12 Andre Sailer ([PR#391](https://github.com/key4hep/k4geo/pull/391))
  - CLD_o2_v07: change LumiCal envelopes from boolean of boolean to assembly, fixes #306, speeds up overlap check (of LumiCal only) with /geometry/test/resolution 300000 down to 13s instead of 3m10s

* 2024-09-10 jmcarcell ([PR#387](https://github.com/key4hep/k4geo/pull/387))
  - Use the Key4hepConfig flag to set the standard, compiler flags and rpath magic.

* 2024-09-03 jmcarcell ([PR#386](https://github.com/key4hep/k4geo/pull/386))
  - Do not link against podio and EDM4hep dictionaries. Introduced in https://github.com/key4hep/k4geo/pull/346, I think it's never necessary to link to the dictionaries.

* 2024-09-02 Andre Sailer ([PR#385](https://github.com/key4hep/k4geo/pull/385))
  - FieldMapXYZ, FieldMapBrBz: adapt to variable rename from DD4hep, fix "OverlayedField   ERROR add: Attempt to add an unknown field type.", fixes #384

* 2024-08-29 Andre Sailer ([PR#383](https://github.com/key4hep/k4geo/pull/383))
  - CLD_o2_v07: fix overlaps related to the LumiCal, slight correction in the position of the envelopes and passive material. Fixes #376

* 2024-08-28 Leonhard Reichenbach ([PR#369](https://github.com/key4hep/k4geo/pull/369))
  - Added TrackerBarrel_o1_v06 using a stave assembly instead of directly placing the sensors into the layers
  - Added CLD_o2_v07 using the new TrackerBarrel_o1_v06

* 2024-08-28 michaela mlynarikova ([PR#350](https://github.com/key4hep/k4geo/pull/350))
  - added new HCalEndcaps_ThreeParts_TileCal_v02.xml: migrated to use FCCSWGridPhiTheta_k4geo; fixed radial dimensions, so the outer radius of all three parts is the same; renamed nModules to nsegments for number of layers in the second cylinder; uses geometry CaloThreePartsEndcap_o1_v02
  
  - added new HCalBarrel_TileCal_v02.xml which uses geometry HCalTileBarrel_o1_v01
  
  - updated ALLEGRO_o1_v03.xml to include HCalBarrel_TileCal_v02.xml and HCalEndcaps_ThreeParts_TileCal_v02.xml
  
  - added new HCalThreePartsEndcap_o1_v02_geo.cpp: added extension to store the radii of each radial layer as well as dimensions of cells. These will be used by the CellPositionsHCalPhiThetaSegTool to calculate the radii of each layer. Improved code readability and variables naming 
  
  - updated HCalTileBarrel_o1_v01_geo.cpp: added extension to store the radii of each radial layer as well as dimensions of cells. These will be used by the CellPositionsHCalPhiThetaSegTool to calculate the radii of each layer. Improved code readability and variables naming

* 2024-08-22 Victor Schwan ([PR#378](https://github.com/key4hep/k4geo/pull/378))
  - 2nd SIT barrel layer ID was corrected for `ILD_l5_v11`; the error stemmed from out-commenting 2nd out of 3 layers without adjusting hard-coded layer IDs

* 2024-08-20 BrieucF ([PR#372](https://github.com/key4hep/k4geo/pull/372))
  - [FCCeeMDI] Use absolute path to import CAD files

* 2024-08-09 jmcarcell ([PR#374](https://github.com/key4hep/k4geo/pull/374))
  - Fix a few compiler warnings

* 2024-08-09 Erich Varnes ([PR#373](https://github.com/key4hep/k4geo/pull/373))
  FCCSWEndcapTurbine_k4geo segmentation: Correct the y position for cells in the endcap on the -z side of the detector (a minus sign is needed since this detector is a mirrored copy of the +z side).

* 2024-08-09 jmcarcell ([PR#368](https://github.com/key4hep/k4geo/pull/368))
  - Clean up includes

* 2024-08-09 Alvaro Tolosa Delgado ([PR#365](https://github.com/key4hep/k4geo/pull/365))
  - IDEA_o1_v03: Dual Readout Calorimeter (DRC) is not loaded by default
     - Added Test for IDEA with DRC

* 2024-08-09 jmcarcell ([PR#353](https://github.com/key4hep/k4geo/pull/353))
  - muonSystemMuRWELL_o1_v01.cpp: Use + std::to_string to append to a string, instead of adding an integer to a string (introduced in https://github.com/key4hep/k4geo/pull/322). Adding a string and an integer cuts the string by as many characters as the value of the integer.

* 2024-08-08 BrieucF ([PR#371](https://github.com/key4hep/k4geo/pull/371))
  - Put the stl files for CAD beampipe, downloaded with cmake, at the right place

* 2024-08-06 Alvaro Tolosa Delgado ([PR#359](https://github.com/key4hep/k4geo/pull/359))
  - New CMake option `INSTALL_BEAMPIPE_STL_FILES` can be used to download the STL (CAD model) beam pipe files from the web EOS

* 2024-08-06 Sungwon Kim ([PR#346](https://github.com/key4hep/k4geo/pull/346))
  - Add DRC geometry construction code under `detector/calorimeter/dual-readout` directory
  - Add .xml compact files under `FCCee/IDEA/compact/IDEA_o1_v03` directory
  - Add custom SD action, output file, fast simulation (boosting optical photon transportation) for Monolithic fiber DRC under `plugin` directory
  - Fixed CMakeLists to compile all above

* 2024-07-30 Leonhard Reichenbach ([PR#362](https://github.com/key4hep/k4geo/pull/362))
  - TrackerEndcap_o2_v06_geo: Fixed endcap radius calculation for the event display (CED), and only the event display, fixes #355

* 2024-07-30 jmcarcell ([PR#360](https://github.com/key4hep/k4geo/pull/360))
  - Add aliases for the detectorCommon and detectorSegmentations libraries

* 2024-07-22 Giovanni Marchiori ([PR#357](https://github.com/key4hep/k4geo/pull/357))
  - [ALLEGRO_o1_v03 ECAL barrel] Get number of modules passed to readout from constant defined before in xml

* 2024-07-22 Erich Varnes ([PR#347](https://github.com/key4hep/k4geo/pull/347))
  - Added a new driver, `ECalEndcap_Turbine_o1_v01`, to build a Noble Liquid ECAL endcap with inclined blades (aka turbine geometry)
  - Added a new segmentation (`FCCSWEndcapTurbine_k4geo`) for the Noble Liquid ECAL endcap turbine geometry
  - Replaced the ALLEGRO_o1_v03 ECAL endcap made of disks perpendicular to the z axis by the turbine geometry built with `ECalEndcap_Turbine_o1_v01`

* 2024-07-19 aciarma ([PR#344](https://github.com/key4hep/k4geo/pull/344))
  - added `k4geo/FCCee/MDI` folder 
  - put the shape based beampipe in `MDI_o1_v00`
  - prepared `k4geo/FCCee/MDI/compact/MDI_o1_v01/` which will contain the CAD beampipe
  - modified the main compact files of `ALLEGRO_o1_v03` and `IDEA_o1_v03` to include the centralized beampipe and prepare them for the CAD ones
  - removed `HOMAbsorbers.xml` from ALLEGRO_o1_v03 since they are not needed with the low impedance beam pipe.

* 2024-07-16 jmcarcell ([PR#354](https://github.com/key4hep/k4geo/pull/354))
  - Rename the lcgeoTests folder to test

* 2024-07-08 mahmoudali2 ([PR#322](https://github.com/key4hep/k4geo/pull/322))
  - Define the first draft of the detailed muon system, which depend on mosaics of 50 * 50 cm^2 mRWELL chambers.
  - Define a suitable XML for the new detailed version.
  - Describe µRWELL materials.
  - Add the parameters of the muon system into the full IDEA implementation.

* 2024-07-04 Giovanni Marchiori ([PR#349](https://github.com/key4hep/k4geo/pull/349))
  - fix detector type in ALLEGRO v03 ECAL calibration scripts

* 2024-07-04 jmcarcell ([PR#348](https://github.com/key4hep/k4geo/pull/348))
  - CMake: fix printout for missing header file, by printing the actual missing file

* 2024-06-28 tmadlener ([PR#343](https://github.com/key4hep/k4geo/pull/343))
  - Make the TPC have detector ID 4 and use a consistent cellID for all tracking detectors in `ILD_l5_v11` in order to make tracking code run again

* 2024-06-19 jmcarcell ([PR#342](https://github.com/key4hep/k4geo/pull/342))
  - Remove a warning by deleting an unused string

* 2024-06-12 jmcarcell ([PR#340](https://github.com/key4hep/k4geo/pull/340))
  - Remove a CentOS7 workflow using the CLIC nightlies

* 2024-06-10 Frank Gaede ([PR#333](https://github.com/key4hep/k4geo/pull/333))
  - fix CED event display for CLIC like detectors using TrackerEndcap_o2_v0x_geo 
         -  fix nPetals in ZDiskPetalsData (for CEDViewer) to use nmodules (e.g. 48 ) rather than nrings
         -  store the number of rings in  `ZDiskPetalsData::sensorsPerPetal`

* 2024-06-06 BrieucF ([PR#339](https://github.com/key4hep/k4geo/pull/339))
  - [FCCee-ALLEGRO_o1_v03] Vertex detector and drift chamber updated to the last IDEA version
  - [FCCee-ALLEGRO_o1_v03] Added solenoidal and MDI magnetic fields
  - [FCCee-ALLEGRO_o1_v03]  Removed ALLEGRO_o1_v03_ecalonly.xml and ALLEGRO_o1_v03_trackeronly.xml to ease maintenance (they can be obtained by commenting out sub-detectors)

* 2024-05-30 BrieucF ([PR#335](https://github.com/key4hep/k4geo/pull/335))
  - Fix for the IDEA_o1_v03 solenoid position

* 2024-05-15 Alvaro Tolosa Delgado ([PR#330](https://github.com/key4hep/k4geo/pull/330))
  - Implementation of IDEA drift chamber, o1_v02. It is based on an original description. The code was redesign to be light. Standalone overlap ctest added.

* 2024-05-06 Zhibo WU ([PR#334](https://github.com/key4hep/k4geo/pull/334))
  - xtalk_neighbors_moduleThetaMergedSegmentation.cpp: change the loop variable itField from int to size_t, in order to remove a compilation warning.

* 2024-04-18 Zhibo WU ([PR#331](https://github.com/key4hep/k4geo/pull/331))
  - Add new functions related to the crosstalk neighbour finding for ALLEGRO ECAL barrel cells.

* 2024-04-16 Giovanni Marchiori ([PR#332](https://github.com/key4hep/k4geo/pull/332))
  - New version of ALLEGRO detector o1_v03 with ecal barrel with 11 layers with cell corners projective along phi. No changes to the other sub detectors.

* 2024-03-24 BrieucF ([PR#326](https://github.com/key4hep/k4geo/pull/326))
  - CLD_o2_v06: add new detector model

* 2024-03-21 Brieuc Francois ([PR#329](https://github.com/key4hep/k4geo/pull/329))
  - Add a description of CLD_o4_v05 in the FCCee README

* 2024-03-21 BrieucF ([PR#327](https://github.com/key4hep/k4geo/pull/327))
  - Add a solenoid and magnetic fields for IDEA. The solenoid has the right material budget (0.75 X0) and spacial extent but its internals should be revised by ultra-thin solenoid designers.
  - Add the endplate lead absorbers for IDEA

* 2024-03-06 Anna Zaborowska ([PR#328](https://github.com/key4hep/k4geo/pull/328))
  - Make LCIO an optional dependency. If LCIO is not found, some detectors (trackers) will not be built.

* 2024-02-25 jmcarcell ([PR#324](https://github.com/key4hep/k4geo/pull/324))
  - Remove the old key4hep build workflow since there is a newer one that builds for all the supported OSes

* 2024-02-25 jmcarcell ([PR#302](https://github.com/key4hep/k4geo/pull/302))
  - Clean up unused variables


### DDMarlinPandora v00-13 (merged from several tags)

* 2025-03-05 Archil Durglishvili ([PR#31](https://github.com/iLCSoft/DDMarlinPandora/pull/31))
  - The "DetectorName" parameter is added to the DDPandoraPFANewProcessor which allows to setup the DDGeometryCreator, DDCaloHitCreator and DDTrackCreator for the ALLEGRO detector;
  - Three new classes are created that are specific for the ALLEGRO detector: DDGeometryCreatorALLEGRO, DDCaloHitCreatorALLEGRO and DDTrackCreatorALLEGRO.

* 2024-08-28 tmadlener ([PR#30](https://github.com/iLCSoft/DDMarlinPandora/pull/30))
  - Remove the no longer supported CentOS7 builds from the Key4hep based CI workflows

* 2024-08-28 tmadlener ([PR#28](https://github.com/iLCSoft/DDMarlinPandora/pull/28))
  - Make it possible to register ECAL energy corrections with Pandora similar to what is possible for the HCAL


### MarlinTrkProcessors v02-12-07 (release notes from several tags)

* 2025-03-21 jmcarcell ([PR#73](https://github.com/iLCSoft/MarlinTrkProcessors/pull/73))
  - Set the subdetectorHitNumbers in ClonesAndSplitTracksFinder that was not being set (defaulted to 0) when `mergeSplitTracks` is false.

* 2024-08-28 Victor Schwan ([PR#72](https://github.com/iLCSoft/MarlinTrkProcessors/pull/72))
  - Remove the hardcoded (ILD) detector names from the FullLDC tracking to allow its usage with the `v11` model of ILD.
    - Keep defaults compatible with the non-hybrid ILD models

* 2024-08-23 tmadlener ([PR#70](https://github.com/iLCSoft/MarlinTrkProcessors/pull/70))
  - Add the `.clang-format` default file that is also used by other Key4hep repositories
  - Add a basic `pre-commit` configuration to run formatting checks
  - Run `clang-format` to fix all formatting issues

* 2024-08-22 tmadlener ([PR#71](https://github.com/iLCSoft/MarlinTrkProcessors/pull/71))
  - Fix warnings to make Key4hep based CI workflows pass again
  - Remove CentOS7 from Key4hep based workflows since it is no longer supported


### iLCUtil v01-07-03

* 2024-05-28 Andre Sailer ([PR#35](https://github.com/iLCSoft/iLCUtil/pull/35))
  - RPATH: set rpath to `$ORIGIN/../${CMAKE_INSTALL_LIBDIR}`

* 2024-05-02 jmcarcell ([PR#34](https://github.com/iLCSoft/iLCUtil/pull/34))
  - Write rpaths when installing. Fixes an issue introduced in https://github.com/iLCSoft/iLCUtil/pull/32 where rpaths are not being written.

* 2024-05-02 tmadlener ([PR#33](https://github.com/iLCSoft/iLCUtil/pull/33))
  - Bump the default c++ version to 17 as that is what we have been using for at least a few years now.

* 2024-04-29 Frank Gaede ([PR#32](https://github.com/iLCSoft/iLCUtil/pull/32))
  - replace `ilcsoft_default_rpath_settings.cmake` with the one from LCIO
      -  see https://github.com/iLCSoft/LCIO/pull/121 
  - this fixes the rpath settings for all iLCSoft tools using this script to work on MacOS
  - (needed to install the key4hep stack on darwin)

* 2024-04-29 Tao Lin ([PR#20](https://github.com/iLCSoft/iLCUtil/pull/20))
  - Fix the problem: the system GSL may be picked. See details in https://github.com/key4hep/k4-spack/issues/77


### GEAR v01-09-05 (merged notes from several tags)

* 2025-03-31 Thomas Madlener ([PR#21](https://github.com/iLCSoft/GEAR/pull/21))
  - Make sure that all libraries go the the same place during installation.

* 2025-03-31 Thomas Madlener ([PR#20](https://github.com/iLCSoft/GEAR/pull/20))
  - Update the Key4hep build action to the latest version to include nightlies on Ubuntu24

* 2025-03-31 jmcarcell ([PR#19](https://github.com/iLCSoft/GEAR/pull/19))
  - Add LANGUAGES CXX to the top level CMakeLists.txt to disable checks for a C compiler

* 2025-03-31 jmcarcell ([PR#18](https://github.com/iLCSoft/GEAR/pull/18))
  - Bump the minimum version of CMake to 3.5, to be able to compile with CMake 4.0

* 2025-03-10 scott snyder ([PR#17](https://github.com/iLCSoft/GEAR/pull/17))
  - Fix a few compiler warning.

* 2025-03-10 sss ([PR#16](https://github.com/iLCSoft/GEAR/pull/16))
  - Fix apparent off-by-one error in TPCParametersImpl::getNearestPad.

* 2025-01-13 Thomas Madlener ([PR#15](https://github.com/iLCSoft/GEAR/pull/15))
  - Switch to central Key4hep CI build workflows and remove clicdp nightlies based ones
  - Fix warnings that are now enabled

* 2025-01-13 jmcarcell ([PR#14](https://github.com/iLCSoft/GEAR/pull/14))
  - Add GNUInstallDirs to set CMAKE_INSTALL_LIBDIR so that the default rpath is correct and can be used in downstream projects, like in `k4MarlinWrapper`

* 2024-07-01 jmcarcell ([PR#10](https://github.com/iLCSoft/GEAR/pull/10))
  - Fix warnings about not passing exceptions by reference
  - Fix warnings about an implicit copy constructor defined
  - Fix other warnings, about fallthroughs, a weird UTF-8 character (spanish accent in comments in spanish) and unused results

### CEDViewer v01-20

* 2024-07-23 tmadlener ([PR#28](https://github.com/iLCSoft/CEDViewer/pull/28))
  - Add key4hep based CI workflows

* 2024-07-23 Leonhard Reichenbach ([PR#27](https://github.com/iLCSoft/CEDViewer/pull/27))
  - Added the processor parameter `DrawMCParticlesCreatedInSimulation` to enable drawing of the MCParticles that were created in the simulation.
  
### CED v01-10

* 2024-07-25 tmadlener ([PR#13](https://github.com/iLCSoft/CED/pull/13))
  - Make sure that all detector layers have a keyboard shortcut and that they can be properly addressed by that after [#11](https://github.com/iLCSoft/CED/pull/11)
  - Refactor the `keypressed` function and eliminate a few previously undetected clashes in available keyboard shortcuts 
    - `t`, `u`, `y`, `i` were bound twice and now exclusively used for toggling data layers

* 2024-07-23 tmadlener ([PR#14](https://github.com/iLCSoft/CED/pull/14))
  - Remove CentOS7 from the Key4hep based CI workflows

* 2024-03-27 Leonhard Reichenbach ([PR#11](https://github.com/iLCSoft/CED/pull/11))
  - Increased the number of possible detector layers to 40

### KiTrack v01-10-01

* 2024-08-22 tmadlener ([PR#4](https://github.com/iLCSoft/KiTrack/pull/4))
  - Move CI to github actions and remove travis-ci config
  - Fix c++ warnings and enable `-Werror` for CI

### PandoraPFANew v04-11-01
