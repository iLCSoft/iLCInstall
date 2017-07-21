
# Release notes for iLCSoft v01-19-03.p01


## lcgeo - v00-13-04

* 2017-07-21 Shaojun Lu ([PR#147](https://github.com/iLCSoft/lcgeo/pull/147))
  - Fine tuning FTD envelope and SIT Cone cables to fix overlap that was not detected on Z-axis for ILD_l4_v02.

* 2017-07-21 Shaojun Lu ([PR#145](https://github.com/iLCSoft/lcgeo/pull/145))
  - Update lcgeoTests for ILD.
    - ILD_l4/s4_v02 are the current optimisation models.
    - Remove test of ILD_l1_v01, and added tests for ILD_l4/s4_v02.

* 2017-07-21 Shaojun Lu ([PR#144](https://github.com/iLCSoft/lcgeo/pull/144))
  - Fix VXD04 overlap by changing offset_phi - used in all ILD models

* 2017-07-20 Marko Petric ([PR#146](https://github.com/iLCSoft/lcgeo/pull/146))
  - Change starting position of inner tracker barrel to remove gaps and overlaps in CLIC_o3_v12

## lcgeo - v00-13-03

* 2017-07-19 Daniel Jeans ([PR#143](https://github.com/iLCSoft/lcgeo/pull/143))
  - introduce SEcal06 drivers, which can deal with multi-readout (requires at least DD4hep v01-01-01 for updated MegatileLayerGridXY class). Should be completely back-compatible with SEcal05 drivers.
  - defined hybrid ECAL, with both silicon and scintillator readout in each layer
  - defined large and small ILD models using such a hybrid ECAL: ILD_l5_v02 and ILD_s5_v02

* 2017-07-19 Daniel Jeans ([PR#142](https://github.com/iLCSoft/lcgeo/pull/142))
  - Hcal_readout_segmentation_slice_barrel/endcap paramters were specified in both the ILD_?v_v02.xml and hcal_defs.xml files, to inconsistent values. the values in ILD_?v_v02.xml were correct, and were used. The values in hcal_defs.xml were wrong, but were not used. 
  I have corrected values in hcal_defs.xml, removed duplicate definitions in ILD_?v_v02.xml.

* 2017-07-19 Marko Petric ([PR#141](https://github.com/iLCSoft/lcgeo/pull/141))
  - New model CLIC_o3_v12 that fixes an overlap that was considered a false positive in outer tracker barrel due to shift in z0
  - In file `OuterTracker_o2_v06_01.xml` L6 value of `OuterTracker_Barrel_half_length` change from 1264mm -> 1264.2mm

* 2017-07-19 Remi Ete ([PR#140](https://github.com/iLCSoft/lcgeo/pull/140))
  * Modified DD4hepSimulation.parseOptions() to receive argv argument, allowing user scripts to pass custom command line arguments

* 2017-07-14 Remi Ete ([PR#139](https://github.com/iLCSoft/lcgeo/pull/139))
  - CLIC_o3_v11: move HCal_cell_size constant to main file to avoid duplicate definition
  - CLIC_o3_v11: BeamCal: set correct size of incoming beampipe, only changes of absorber shape, reduce Beampipe wall thickness in beamcal by 0.02 mm to avoid overlaps


## DD4hep - v01-01-01

* 2017-07-18 Frank Gaede
    - apply changes from D.Jeans to MegatileLayerGridXY:
        - add ncellsX/Y as a "parameter", allowing it to be set in compact description.
          This change is for easier use in the case of a MultiSegmentation.
          (Only a uniform segmentation can be defined in this way: for more complex cases, must set by driver.)
        - change from array to std::vector to store ncells information

