# iLCSoft v02-02-01

Production release for large 250 GeV production of ILD.
Various updates and bug fixes for the 250 GeV production of ILD.

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. v02-02-01

# MarlinReco v01-31

* 2021-06-15 Thomas Madlener ([PR#92](https://github.com/iLCSoft/MarlinReco/pull/92))
  - Move the `TrueJet_Parser` utility class to MarlinUtil
    - Make it possible to use it outside of MarlinReco
    - Keep example usage and README here in MarlinReco for better discoverability

* 2021-05-07 A. Irles ([PR#91](https://github.com/iLCSoft/MarlinReco/pull/91))
  - PIDTools: 
    	- LikelihoodPID modified to be able to accept as arguments the name and type of method to run and store (allowing for versioning)
    	- AngularCorrection_dEdxProcessor created to use with DST samples generated with v02-02 and v02-02-01. The dEdx is corrected for angular effects.
    	- Compute_dEdxProcessor2021, modifictation of the default Compute_dEdxProcessor
    		- The angular correction is optional
    		- The function of this correction is a pol3(lambda)
    		- It is applied AFTER smearing
  	- Example steering files are added and can be found [here](https://github.com/iLCSoft/MarlinReco/blob/master/Analysis/PIDTools/steer/DSTcorrection_dEdx_and_LikelihoodPID.xml)


# MarlinUtil v01-16

* 2021-06-15 Thomas Madlener ([PR#18](https://github.com/iLCSoft/MarlinUtil/pull/18))
  - Move `TrueJet_Parser` utility class from MarlinReco to MarlinUtil.
    - Make it possible to use this in analysis code outside of MarlinReco

* 2021-06-09 Thomas Madlener ([PR#17](https://github.com/iLCSoft/MarlinUtil/pull/17))
  - Migrate the CI setup to use github actions instead of travis

* 2020-04-12 Frank Gaede ([PR#15](https://github.com/iLCSoft/MarlinUtil/pull/15))
  - make compatible w/ c++17 for macos/clang
        - patch provided by K.Fujii


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
