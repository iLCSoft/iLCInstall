# iLCSoft v02-02-01

Production release for large 250 GeV production of ILD.
Various updates and bug fixes for the 250 GeV production of ILD.

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. v02-02-01

# ILDPerformacne v01-10

* 2021-05-06 Ulrich Einhaus ([PR#34](https://github.com/iLCSoft/ILDPerformance/pull/34))
  Update of the dEdxAnalyser to v1.2 with new features for calibration:
  - fit poly3 to mean dE/dx vs. |lambda| -> input to AngularCorrection_dEdxProcessor
  - fit Bethe-Bloch curves mean dE/dx values -> input to LikelihoodPIDProcessor
  - these two fits and the fiducial electrons dE/dx resolution are printed on the console at the end of the Analyser

* 2021-03-16 Ulrich Einhaus ([PR#33](https://github.com/iLCSoft/ILDPerformance/pull/33))
  - Update of the dEdxAnalyser with several new features
    - optional processor parameters: cuts on momentum
    - fiducial electrons histograms for comparison with beam tests
    - optional processor parameters: properties of fiducial electrons
    - optional processor parameters: axis binning of histograms
    - hit energy histograms, will only be filled if hit info is available
    - dE/dx over |lambda| incl. fit for angular correction
