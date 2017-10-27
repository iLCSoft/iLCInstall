# iLCSoft v01-19-05

Packages changed wrt. to v01-19-04.

## lcio v02-10-01

* 2017-10-12 Frank Gaede ([PR#40](https://github.com/ilcsoft/lcio/pull/40))
  - ensure correct version numbers in this and future releases
      - have all files that contain a version number configured by CMake
      - will allow to use tagging script for GitHub to make a new release
  - no code changes wrt. v02-10

### lcio v02-10

* 2017-07-07 Andre Sailer ([PR#36](https://github.com/ilcsoft/lcio/pull/36))
  - CellIDDecoder: use static string instead of static pointer to string for defaultEncoding

* 2017-09-28 Marko Petric ([PR#38](https://github.com/ilcsoft/lcio/pull/38))
  - Correct LCIO_MINOR_VERSION

## lcgeo v00-14

* 2017-08-09 Marko Petric ([PR#152](https://github.com/iLCSoft/lcgeo/pull/152))
  - New detector model CLIC_o3_v13
  - CLIC_o3_v13: Set the cell size in HCalEndcap, HCalRing and YokeEndcap to be read from main compact file
  - CLIC_o3_v13: Extend the support in the vertex of layer 4 to the edge of the sensitive

* 2017-10-10 Ete Remi ([PR#172](https://github.com/iLCSoft/lcgeo/pull/172))
  - Split ILD ecal segmentation selection into two values: value0 and value1 while parsing geometry for ILD_l/s5_* models. 
  - Changed both drivers and compact xml files.

* 2017-10-12 Frank Gaede ([PR#173](https://github.com/iLCSoft/lcgeo/pull/173))
  - use unbounded surfaces in the ILD TPC
      - assign surfaces only to the forward half of the TPC
      - as they are unbounded they will also be 'visible' in the backward half

* 2017-08-25 Shaojun Lu ([PR#156](https://github.com/iLCSoft/lcgeo/pull/156))
  - Fix the ILD_l4/s4_v02 Hybird Hcal RPC Anode and Cathode FloatGlass place order.
    - For the Hybird Hcal Endcaps and EndcapRing, they have been fixed inside compact file.
      - "SHcalSc04_EndcapRing_v01.xml" for both ILD_l4_v02 and ILD_s4_v02
      - "SHcalSc04_Endcaps_v01_LARGE.xml" for ILD_l4_v02
      - "SHcalSc04_Endcaps_v01_SMALL.xml" for ILD_s4_v02
    - For the Hybird Hcal Barrel, they have been fixed in both the driver and compact file
      - "SHcalSc04_Barrel_v04.xml" for both ILD_l4_v02 and ILD_s4_v02.
      - "SHcalSc04_Barrel_v04.cpp" the slices place order has been fixed to start from IP.
   - All the compact files are inside the "ILD_common_v02" folder, which are used by ILD_l5/s5_v02, too.
      - So both ILD_l5_v02 and ILD_s5_v02 have the updeted Hybird Hcal, too.

* 2017-07-28 TiborILD ([PR#150](https://github.com/iLCSoft/lcgeo/pull/150))
  - added inner box cut off for Hcal_Endcaps_SD_v01
  - added SDHCAL Barrel module with TESLA geometry

* 2017-08-30 TiborILD ([PR#157](https://github.com/iLCSoft/lcgeo/pull/157))
  - update of ILD Hcal endcap readout segmentation
          - in order to unify the readouts for all Hcal detectors  the CartesianGridXZ readout of SHCalsc04_Endcaps_v01 was changed to CartesianGridXY readout 
         - affects models ILD_l/s4_v02 and ILD_l/s5_v02

* 2017-08-30 Jan Strube ([PR#153](https://github.com/iLCSoft/lcgeo/pull/153))
  - allow to change the name of the MCParticle input collection in ddsim
          - using parameter 'mcParticleCollectionName'

* 2017-08-30 Jan Strube ([PR#153](https://github.com/iLCSoft/lcgeo/pull/153))
  /

* 2017-08-02 TiborILD ([PR#151](https://github.com/iLCSoft/lcgeo/pull/151))
  - modifications to comply with a new xml scheme in ILD_common_v02

* 2017-09-26 Daniel Jeans ([PR#167](https://github.com/iLCSoft/lcgeo/pull/167))
  - adjust parameters of hybrid ECAL model: reduce scintillator 2 -> 1.5 mm, add 0.5mm air gap
  - take hybrid ECAL segmentation from parameters (not hard-coded numbers)

* 2017-08-14 Andre Sailer ([PR#154](https://github.com/iLCSoft/lcgeo/pull/154))
  - The CommandLine information was no longer filled in the lcio runheader, it is now filled again

* 2017-09-29 Ete Remi ([PR#169](https://github.com/iLCSoft/lcgeo/pull/169))
  - Ecal (Hcal) segmentation selection variable moved from ecal(hcal)_defs.xml files to top level detector xml file
  - Added 12 new detectors for different reconstruction combination : 
    - ILD_l/s4_o1_v02 : SiWEcal + AHcal (as for standard ILD_l/s4_v02)
    - ILD_l/s4_o2_v02 : SiWEcal + SDHCAL
    - ILD_l/s5_o1_v02 : SiWEcal + AHcal (as for standard ILD_l/s5_v02)
    - ILD_l/s5_o2_v02 : SiWEcal + SDHCAL
    - ILD_l/s5_o3_v02 : ScEcal + AHcal
    - ILD_l/s5_o4_v02 : ScEcal + SDHCAL
  - One can use simulated files from i.e ILD_l4_v02 and reconstruct them with ILD_l4_o1_v02 or ILD_l4_o2_v02 models

* 2017-09-29 Frank Gaede ([PR#168](https://github.com/iLCSoft/lcgeo/pull/168))
  - adapt to changes in dd4hep::BitField64 in https://github.com/AIDASoft/DD4hep/pull/238

* 2017-07-27 Shaojun Lu ([PR#148](https://github.com/iLCSoft/lcgeo/pull/148))
  - Update ILD Documentation tools for ILD_l4/s4_v02.
        - Following the DDG4 development, and update ILD Documentation tool "extractParameters.py"
        - Following the ILD_l4/s4_v02 setup, and clean unused parameter in "ILD_envelope_parameters.txt" for the envelope parameters list.

* 2017-08-23 Daniel Jeans ([PR#155](https://github.com/iLCSoft/lcgeo/pull/155))
  - In case of multi-readout setup, give the two (or more) sensitive layers within a single calorimeter layer the same layer index

* 2017-09-14 Shaojun Lu ([PR#166](https://github.com/iLCSoft/lcgeo/pull/166))
  - Fix ILD_l4_v02 Hybird model collections key_value.
      - follow the update of the slice placement and correct the collections key_value.
      - the segmentation and collection should use the same key_value for both SDHCAL and  AHcal.

* 2017-09-06 Shaojun Lu ([PR#160](https://github.com/iLCSoft/lcgeo/pull/160))
  - Fix ILD SEcal05_ECRing for filling dd4hep::rec::LayeredCalorimeterData.
    - For the reconstruction, we fill the LayeredCalorimeterData at runtime.
    - Both side ECRings have identical layer structure, fill the one from module_num==0, and used for both.

* 2017-09-06 Shaojun Lu ([PR#159](https://github.com/iLCSoft/lcgeo/pull/159))
  - Fix ILD_l4_v02 target readout slice number for AHCAL.
    - after re-order the Hybird HCAL layers, we should also update Hcal_readout_segmentation_slice_barrel to "3" as "Hcal_readout_segmentation_slice_endcap" now.

* 2017-09-12 Daniel Jeans ([PR#165](https://github.com/iLCSoft/lcgeo/pull/165))
  Fix the filling of dd4hep::rec::LayeredCalorimeterData::Layer data for SEcal05, SEcal06 models:
  - layer.distance now defined as the distance to the *start* of a calo layer (at the start of the absorber, except in the case of the 1st layer, in which it's the start of the ECAL).
  Some additional fixes to SEcal05_ECRing: 
  - use correct absorber thickness in stack transitions (previously not guaranteed to be correct)
  - use CarbonFibre when calculating material properties for LayeredCalorimeterData (previously using air for structural material)
  - cosmetic changes: indentations, commented-out code, ...

* 2017-09-12 Shaojun Lu ([PR#164](https://github.com/iLCSoft/lcgeo/pull/164))
  - For backward consistency, update all ILD AHCAL Barrel slice placement.
      - update all ILD AHCAL Barrel drivers to place slice in the same consistent way.
      - update the slice order in all the ILD AHCAL Barrel compact files too.

* 2017-09-12 Dan Protopopescu ([PR#163](https://github.com/iLCSoft/lcgeo/pull/163))
  - Option 3 of the SiD model, with Cu absorber plates in the HCal, instead of Steel235

* 2017-09-12 Shaojun Lu ([PR#162](https://github.com/iLCSoft/lcgeo/pull/162))
  -  Fix ILD_l4_v02 Barrel MultiSegmentation slice number for different technology.
     - After change the order of slice, the segmentation slice should be updated too.
     - ILD_s4_v02 use the same compact file, should be fine.

* 2017-10-06 Andre Sailer ([PR#171](https://github.com/iLCSoft/lcgeo/pull/171))
  - Drop unused and no longer existing header includes AidaSoft/DD4hep#241

* 2017-10-05 Frank Gaede ([PR#170](https://github.com/iLCSoft/lcgeo/pull/170))
  - fill `tpcData->zMinReadout` in `TPC10_geo.cpp`
    - describing the cathode thickness

* 2017-09-11 Frank Gaede ([PR#161](https://github.com/iLCSoft/lcgeo/pull/161))
  - fix spelling of ddsim parameter:
       - rename mcParticleCollectionName to MCParticleCollectionName


## DD4hep v01-03

* 2017-10-12 Frank Gaede ([PR#244](https://github.com/AIDASoft/DD4hep/pull/244))
  - allow for unbounded surfaces in DDRec
       - add new property `SurfaceType::Unbounded`
       - if a surface is marked unbounded `Surface::insideBounds()` ignores the volume boundaries (and only checks the distance to the surface)

* 2017-09-19 Whitney Armstrong ([PR#233](https://github.com/AIDASoft/DD4hep/pull/233))
  - Added helper  `CellIDPositionConverter::cellDimensions(const CellID& cell)`

* 2017-10-09 Frank Gaede ([PR#242](https://github.com/AIDASoft/DD4hep/pull/242))
  - improve `BitFieldCoder` class
      - remove heap allocation of BitFieldElements
      - add move constructors for efficient filling of vector

* 2017-09-29 Frank Gaede ([PR#238](https://github.com/AIDASoft/DD4hep/pull/238))
  - add new threadsafe class `BitFieldCoder` as replacement for `BitField64`
  - use as `const` everywhere
  - re-implement `BitField64` using `BitFieldCoder`
    - is thread safe if used locally 
    - can be instantiated from `const BitFieldCoder*`

* 2017-09-18 Markus Frank ([PR#234](https://github.com/AIDASoft/DD4hep/pull/234))
  - Created a new example showing the CMS tracking detector
    - Get CMS going with their evaluation. Added a package DDCMS with the conversion plugins for the silicon trackers and the corresponding conversion mechanism for their `xml` structure.

* 2017-09-18 Frank Gaede ([PR#232](https://github.com/AIDASoft/DD4hep/pull/232))
  - fix reading of stdhep/lcio generator files with generator statuses not in [0,3]
  - add `G4PARTICLE_GEN_BEAM` and `G4PARTICLE_GEN_OTHER` to DDG4
    -  `G4PARTICLE_GEN_BEAM`  is generally agreed to be used for beam particles (HepMC, LCIO)
    -  all other status codes vary from generator to generator and we use OTHER
  - for stdhep or lcio input the true generator status is preserved in the lcio output, regardless of its value
  - create a vertex for every parent-less particle in LCIOEventReader
    - this allows for example to read GuineaPig files ( non-prompt pair particles) or special user created files with non-prompt particles
   - Resolves #101

* 2017-09-20 Markus Frank ([PR#235](https://github.com/AIDASoft/DD4hep/pull/235))
  - A more complete version of the CMS tracker
     - Enhanced the CMS tracker example to be more complete.
     - Stopped at some point to convert all CMS algorithms. Hence, the tracker is not complete, but the remaining work looks to be purely mechanical.

* 2017-10-02 Frank Gaede ([PR#239](https://github.com/AIDASoft/DD4hep/pull/239))
  - add cell sizes to printout of `LayeredCalorimeterData::layer`
      - used in `dumpdetector -d`

* 2017-09-14 Frank Gaede ([PR#231](https://github.com/AIDASoft/DD4hep/pull/231))
  - adapt LCIOEventReader for Pythia8 and Whizard2
    - add all parent-less particles to outgoing vertex
    - fixes #226 and closes #229 
    - also used for stdhep files

* 2017-09-07 Daniel Jeans ([PR#227](https://github.com/AIDASoft/DD4hep/pull/227))
  - Fix calculation of cell position in `MegatileLayerGridXY`
  - previously, returned position was the lower corner of the cell
  - after this bug fix, it's the cell centre

* 2017-10-05 Frank Gaede ([PR#241](https://github.com/AIDASoft/DD4hep/pull/241))
  - remove deprecated and unused classes from DDRec

* 2017-10-05 Frank Gaede ([PR#240](https://github.com/AIDASoft/DD4hep/pull/240))
  - add `dd4hep::rec::FixedPadSizeTPCData.zMinReadout`
       - needed to describe the cathode thickness

* 2017-08-21 Markus Frank ([PR#221](https://github.com/AIDASoft/DD4hep/pull/221))
  - Document several classes in doxygen notation.
     - Aim is that there are (at least) no class headers without docs.
     - See [documentation](http://test-dd4hep.web.cern.ch/test-dd4hep/doxygen/html/annotated.html)


## aidaTT v00-08

* 2017-08-21 Andre Sailer ([PR#17](https://github.com/AIDASoft/aidaTT/pull/17))
  - fixeByFiveMatrix/Vector5d: fix initialisation: Zero is a static function, previously nothing was initialised to 0. At least this fixes display of trackParameters where the covariance matrix was shown the random values from uninitialised values nstead of zeros.

* 2017-10-12 Shaojun Lu ([PR#18](https://github.com/AIDASoft/aidaTT/pull/18))
  -  Update trajectory::addMeasurement from void to bool for adding successfully.
      - the success information could be used by "MarlinTrk/src/MarlinAidaTTTrack.cc".
      - Both DDKalTest and AidaTT(GBL) may be used by  "RefitProcessor" and "FullLDCTracking_MarlinTrk" for track fitting.

## DDKalTest v01-04

* 2017-10-12 Frank Gaede ([PR#7](https://github.com/iLCSoft/DDKalTest/pull/7))
  - allow for unbounded DDCylinderMeasLayers 
     - to be used for the ILD TPC
     - if VolCylinder is marked as unbounded, we use a 'multilayer', ie.
       one layer that extends to both sides of the cathode

## MarlinTrk  v02-06

* 2017-10-12 Frank Gaede ([PR#9](https://github.com/ilcsoft/MarlinTrk/pull/9))
  - fix the re-setting of eLoss and QMS configuration parameters in TrkSysConfig

### MarlinTrk v02-05

* 2017-10-12 Shaojun Lu ([PR#8](https://github.com/iLCSoft/MarlinTrk/pull/8))
  - Fix the segmentation fault which is caused by assigning the wrong number to _indexMap.
      - Only when trajectory added measurement successfully, then to increase pointLabel by one, and assign it to _indexMap.
      - Both DDKalTest and AidaTT(GBL) may be used by  "RefitProcessor" and "FullLDCTracking_MarlinTrk" for track fitting.

* 2017-10-12 Frank Gaede ([PR#7](https://github.com/iLCSoft/MarlinTrk/pull/7))
  - add new helper class TrkSysConfig for setting the correct system configuration per event (scope)
  - reduce initial error on tanLambda in `MarlinDDKalTestTrack::initialise()`

* 2017-09-11 Frank Gaede ([PR#6](https://github.com/iLCSoft/MarlinTrk/pull/6))
  - reduce initial uncertainty for kappa/omega for track fits in
     `MarlinDDKalTestTracks::initialise(bool fitDirection)` 
        - fixes a problem in TPC track fits, when first three points define a very different curvature
        - should have no effect on Si-Tracking


## MarlinTrkProcessors v02-09-01

* 2017-10-18 Frank Gaede ([PR#31](https://github.com/iLCSoft/MarlinTrkProcessors/pull/31))
  - fix DDTPCDigiProcessor
      - allow smearing beyond cathode boundaries
  - reduce verbosity in ExtrToSIT

### MarlinTrkProcessors v02-09

* 2017-10-12 Frank Gaede ([PR#30](https://github.com/iLCSoft/MarlinTrkProcessors/pull/30))
  - set correct MarlinTrkSystem configuration for every event with `MarlinTrk::TrkSysConfig`
     in all tracking processors

* 2017-07-07 Andre Sailer ([PR#24](https://github.com/iLCSoft/MarlinTrkProcessors/pull/24))
  - SiliconTracking_MarlinTrk: initialise fastfitter in init function, fixes small memory leak if processor is not active
  
  - FPCCDFullLDCTracking_MarlinTrk: initalise helper objects in init and add cleanup in end. Fixes small memory leaks

* 2017-10-09 Frank Gaede ([PR#29](https://github.com/iLCSoft/MarlinTrkProcessors/pull/29))
  - fix DDTPCDigiProcessor
      - ensure hits are not smeared beyond cathode

* 2017-08-21 Andre Sailer ([PR#25](https://github.com/iLCSoft/MarlinTrkProcessors/pull/25))
  - RefitFinal: new processor for refitting track collections. Does not re-sort hits (like RefitProcessor), different way to setup the initial trackstate for the fit, and different MarlinTrkUtil function being called
  - DDPlanarDigi: add absolute values of u and v smearing histograms

* 2017-08-23 Emilia Leogrande ([PR#26](https://github.com/iLCSoft/MarlinTrkProcessors/pull/26))
  * TruthTrackFinder: m_maxChi2perHit changed from 1.e3 to 1.e2 for consistency with Conformal Tracking

* 2017-09-12 Shaojun Lu ([PR#27](https://github.com/iLCSoft/MarlinTrkProcessors/pull/27))
  - DDTPCDigiProcessor: Added one control for the input value of asin to avoid NAN.

* 2017-10-06 Andre Sailer ([PR#28](https://github.com/iLCSoft/MarlinTrkProcessors/pull/28))
  - Drop unused and no longer existing header includes AidaSoft/DD4hep#241



## Clupatra v01-02

* 2017-10-12 Frank Gaede ([PR#12](https://github.com/iLCSoft/Clupatra/pull/12))
  - set correct MarlinTrkSystem configuration for every event with `MarlinTrk::TrkSysConfig`


## ForwardTrackingv01-13

* 2017-10-12 Frank Gaede ([PR#9](https://github.com/iLCSoft/ForwardTracking/pull/9))
  - set correct MarlinTrkSystem configuration for every event with `MarlinTrk::TrkSysConfig`


## ConformalTracking v01-04

* 2017-09-20 Daniel Hynds ([PR#20](https://github.com/iLCSoft/ConformalTracking/pull/20))
  - Distance Of Closest Approach to the origin added, used as a cut on new seed cells in order to reduce combinatorics

* 2017-07-11 Daniel Hynds ([PR#15](https://github.com/iLCSoft/ConformalTracking/pull/15))
  - Rewrote track fit in SZ, proper phi treatment 
  - Updated track strategy including extension of hits throughout the detector
  - Utility tool added for debugging

* 2017-09-21 Andre Sailer ([PR#21](https://github.com/iLCSoft/ConformalTracking/pull/21))
  - Fix gcc compiler warnings

* 2017-08-18 Andre Sailer ([PR#19](https://github.com/iLCSoft/ConformalTracking/pull/19))
  - errors for endcaps updated and forward flag added
  - high pt track extension now uses CA (over 10 GeV/c pt)
  - strategy slightly changed for displaced tracks to stop overloading in case of high occupancy events, fixes #16

* 2017-10-02 Andre Sailer ([PR#22](https://github.com/iLCSoft/ConformalTracking/pull/22))
  - Use smart pointers to wrap objects and simplify memory management.

* 2017-07-27 Andre Sailer ([PR#17](https://github.com/iLCSoft/ConformalTracking/pull/17))
  - Added temporary workaround when a way too large number of tracks would be created. Add skipEvent flag to allow for proper cleanup before exception is thrown.

* 2017-10-06 Andre Sailer ([PR#23](https://github.com/iLCSoft/ConformalTracking/pull/23))
  - Drop unused and no longer existing header includes AidaSoft/DD4hep#241


## Marlin v01-13

* 2017-09-27 Ete Remi ([PR#20](https://github.com/iLCSoft/Marlin/pull/20))
  - Added a constants section in XMLParser parsing : 
     - Allows to write constants and refer to in processor parameter values and global parameter values
     - Makes use of ${constantName} to refer to a constant
     - Use command line argument to override a constant
     - example:
  ```xml
    <constants>
      <constant name="MCParticleCollection" value="MCParticle"/>
      <constant name="FilePath" value="../../test/testmarlin"/>
      <constant name="InputFile" value="${FilePath}/simjob.slcio"/>
    </constants>
  ```
  ```shell
  Marlin --constant.InputFile=aDifferentFile.slcio  marlin.xml
  ```

* 2017-07-10 Andre Sailer ([PR#18](https://github.com/iLCSoft/Marlin/pull/18))
  - AIDAProcessor: delete file (_tree) at the end
  - LCIOOutputProcessor: delete lcWriter at the end
  - ProcessorMgr: clear maps and list at the end; delete static instance at the end

* 2017-09-25 Ete Remi ([PR#19](https://github.com/iLCSoft/Marlin/pull/19))
  - Added <include> element feature to read external xml file and replace in main Marlin steering file
  - Added an include mechanism to the `XMLParser` class, allowing to load xml files into the main Marlin steering file. Note that :
    - Nested includes will not be processed in the current version (include of include does not work)
     - Exceptions are thrown if something goes wrong with the xml element (wrong name, no file, etc ...)
     - Includes are processed iteratively in the document inside the root element.

* 2017-10-12 YancyW ([PR#21](https://github.com/iLCSoft/Marlin/pull/21))
  - add "copy_new_Processor.sh" and "action.sh" to the example folder. The former is for copying an old processor to the new one and it can also copy the example processor to user's directory. The latter for compiling the code. 
  - change the README.md, add usage for this two scripts.

## MarlinReco v01-21

* 2017-10-26 KURATA Masakazu ([PR#26](https://github.com/ilcsoft/MarlinReco/pull/26))
  - improved PIDTools
        - added additional smearing functon for dE/dx resolution.
        - and corrected the strange behavior for PID. That is most of the muons are identified as pions.


### MarlinReco v01-20

* 2017-07-20 Andre Sailer ([PR#17](https://github.com/iLCSoft/MarlinReco/pull/17))
  - TauFinder: fix memory leak (few kB/event)

* 2017-09-13 Frank Gaede ([PR#22](https://github.com/iLCSoft/MarlinReco/pull/22))
  - add a default value for parameter inputHitCollections in RealisticCaloDigi.cc
  - create package EventShapes_Fortran, Fixes #20 
         - moved YThres from EventShapes to EventShapes_Fortran
  - build EventShapes for C++ now

* 2017-09-27 libo929 ([PR#24](https://github.com/iLCSoft/MarlinReco/pull/24))
  - improve SDHCALDigi/src/SimDigital.cc
       - Fixed the exception of unknown name y
        - add optional parameter HCALCellSize to overwrite the one from dd4hep

* 2017-07-29 libo929 ([PR#18](https://github.com/iLCSoft/MarlinReco/pull/18))
  - Updated the SimDigital processor to make it compatible with lcgeo simulation
  - Removed the digitization for ECAL 
  - Fixed the warnings

* 2017-08-14 Ete Remi ([PR#19](https://github.com/iLCSoft/MarlinReco/pull/19))
  - BruteForceEcalGapFiller : Add missing information on calo hit type

* 2017-09-15 Daniel Jeans ([PR#23](https://github.com/iLCSoft/MarlinReco/pull/23))
  - modify algorithm to fill ECAL gaps in BruteForceEcalGapFiller:
        - overall linear suppression gap hit energies [as was done in DBD]
        - additional logarithmic suppression to reduce large energy gap hits
        - separate parameters for (a) gaps between modules, and (b) gaps within modules
        - default values of new parameters seem reasonable for ILD_l4_v02 model

* 2017-10-06 Andre Sailer ([PR#25](https://github.com/iLCSoft/MarlinReco/pull/25))
  - Drop unused and no longer existing header includes AidaSoft/DD4hep#241

## DDMarlinPandora  v00-09-01

* 2017-10-18 Frank Gaede ([PR#16](https://github.com/ilcsoft/DDMarlinPandora/pull/16))
  - fix DDTrackCreatorBase::GetTrackStatesAtCalo
      - treat correctly composite spacepoints (from strip stereo layers)
      - protect against initialization error
      - fix logic for backward tracks hitting endcap
   - fixes https://github.com/iLCSoft/DDMarlinPandora/issues/15

### DDMarlinPandora v00-09

* 2017-10-14 Ete Remi ([PR#13](https://github.com/ilcsoft/DDMarlinPandora/pull/13))
  - Added separate registration function for software compensation energy correction
  - Software compensation parameters added in processor parameters 
    - SoftwareCompensationWeights : the sc weights
    - SoftwareCompensationEnergyDensityBins : the energy density bins
    - FinalEnergyDensityBin : the final energy density value

### DDMarlinPandora v00-08

* 2017-07-07 Andre Sailer ([PR#11](https://github.com/iLCSoft/DDMarlinPandora/pull/11))
  - DDCaloDigi: add cleanup of PpdDigi objects, fixes small memory leak

* 2017-09-26 Andre Sailer ([PR#12](https://github.com/iLCSoft/DDMarlinPandora/pull/12))
  - DDTrackCreator: implement passing of multiple track states to Pandora, needs PandoraPFA/LCContent#16
  - Implemented DDTrackCreatorBase::GetTrackStatesAtCalo to obtain second trackstate in the endcap
  - Added GetTrackStatesAtCalo and related code in DDTrackCreatorCLIC and DDTrackCreatorILD
  
  - DDPandoraPFANewProcessor: 
    * added *TrackStateTolerance* variable to tweak the radius until trackStates in the ECal endcap are accepted, by default only trackStates with a radius larger than EcalBarrel Inner radius are accepted
    * added *TrackSystemName* parameter to chose trackSystem (DDKalTest) to use for trackState calculation

* 2017-10-06 Frank Gaede ([PR#14](https://github.com/iLCSoft/DDMarlinPandora/pull/14))
  - rm unused and deprecated DDRec/API/Calorimeter.h 
       - (see https://github.com/AIDASoft/DD4hep/pull/241)


## CEDViewer v01-15

* 2017-09-14 Shaojun Lu ([PR#5](https://github.com/iLCSoft/CEDViewer/pull/5))
  -   Update the  ced2go template for ILD_l4_v02.
      - add the Ecal and Hcal collection names from ILD_l4_v02.
      - remove duplicated  LumiCalCollection.


## Overlay v00-19

* 2017-07-07 Andre Sailer ([PR#7](https://github.com/iLCSoft/Overlay/pull/7))
  - OverlayTiming[Generic]: clean the LCReader instance at the end

* 2017-07-24 Andre Sailer ([PR#8](https://github.com/iLCSoft/Overlay/pull/8))
  - OverlayTiming[Generic]: get random seed from eventSeeder

## FCalClusterer v00-06

* 2017-07-12 Andre Sailer ([PR#19](https://github.com/FCalSW/FCalClusterer/pull/19))
  - LumiCalClusterer: wrap decoder object in unique_ptr to guarantee cleanup, fixes memory leak

* 2017-07-17 Andre Sailer ([PR#20](https://github.com/FCalSW/FCalClusterer/pull/20))
  - LumiCalClusterer: fix memory leak if there are not enough hits to attempt clustering

* 2017-07-18 Andre Sailer ([PR#22](https://github.com/FCalSW/FCalClusterer/pull/22))
  - LumiCalReco: use lambda function in TF1 instead of string
  - BeamCalReco: GeometryDD layer starts at 0 if simulated with ddsim
  - BeamCalReco: fix infinite loop  in background subtraction if nBX = 0 (no background), fixes #21

* 2017-10-02 Andre Sailer ([PR#26](https://github.com/FCalSW/FCalClusterer/pull/26))
  - Adapt to changes in AidaSoft/DD4hep#238
  - CMake add C language to PROJECT for macs and cmake 3.3.2

* 2017-07-26 Andre Sailer ([PR#24](https://github.com/FCalSW/FCalClusterer/pull/24))
  - LumiCalReco: disable Fiducial Volume cuts, cuts on geometry should be done in later step of analysis

* 2017-07-26 Andre Sailer ([PR#23](https://github.com/FCalSW/FCalClusterer/pull/23))
  - BeamCalReco: correct the phi position of cluster reconstructed in the backward direction, which was incorrectly calculated due to the rotation of the backward BeamCal detector

* 2017-10-06 Andre Sailer ([PR#27](https://github.com/FCalSW/FCalClusterer/pull/27))
  - Drop unused and no longer existing header includes AidaSoft/DD4hep#241

