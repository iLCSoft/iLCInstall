# iLCSoft v02-00

Production release for ILD optimization production
for the IDR.


Packages changed wrt. to v01-19-06:

## MarlinReco v01-24-01

* 2018-04-18 Ete Remi ([PR#51](https://github.com/ilcsoft/MarlinReco/pull/51))
  - RecoMCThruthLinker processor
      - Turned WARNING message to DEBUG9 to avoid log pollution
      - this warning occurs only for the SDHcal case where one SimCalorimeterHit can create more than CalorimeterHit


## MarlinReco v01-24

* 2018-04-10 Guillaume ([PR#48](https://github.com/ilcsoft/MarlinReco/pull/48))
  - SDHCAL digitizer : 
     - Switch order of the LCRelation collection between SDHCAL SimCalorimeterHits and Digitized CalorimeterHits (now from CalorimeterHit to SimCalorimeterHit)

* 2018-04-18 Carl Mikael Berggren ([PR#50](https://github.com/ilcsoft/MarlinReco/pull/50))
  - improved TrueJet processor:
       - Fixed crash due to index out-of-range
       - Remove all compiler warnings except local shadow (cheked to be OK)
       -  id of initial ColourNeutrals fixed (should be a boson (W,Z,H))
       - MCParticle collection does not need to start with the beam-particles, back-tracking now also
  gracefully stops if the first entry is reached. This should allow for usage also for the DBD-250 samples, in which the initial beam-particles are missing in the MCParticle collections.
       - nitty-gritty special cases in history fixed.
       - Now also works for higgs-samples *except for h->gluon gluon*, which will need a completely different treatment fro back-track through the parton shower, as there is no quark-line to follow...

* 2018-04-17 Frank Gaede ([PR#49](https://github.com/ilcsoft/MarlinReco/pull/49))
  - add new package TimeOfFlight
       - use TOFEstimators processor to compute TOF parameters
       - will be added as PID object to the ReconstructedParticles

## ILDPerformance v01-06

* 2018-04-12 Jakob Beyer ([PR#22](https://github.com/ilcsoft/ILDPerformance/pull/22))
  - WWZZSeparation
     - The script can now be executed with the option to run on ILCDirac (assuming the user has a certificate). Now high statistics DSTs can be produced and analyzed. (Has been tested with a total of 15k events.)
     - The output structure was changed and the README was updated.
     - Due to a new naming convention in DSTs the analysis no longer works for ilcsoft older than 01-19-06.

* 2018-04-18 Ete Remi ([PR#23](https://github.com/ilcsoft/ILDPerformance/pull/23))
  - UdsAnalysis:
     - Fixed job script to run on the NAF

* 2018-04-05 Frank Gaede ([PR#21](https://github.com/ilcsoft/ILDPerformance/pull/21))
  - in PIDTree: don't print warnings for particles that are not reconstructed


## ConformalTracking v01-07
  
* 2018-03-29 Andre Sailer ([PR#33](https://github.com/ilcsoft/ConformalTracking/pull/33))
  - combineCollections: Properly protect against empty collections, fixes #31

* 2018-04-17 Andre Sailer ([PR#34](https://github.com/ilcsoft/ConformalTracking/pull/34))
  - ConformalTracking: change setting of input collections, use collection names instead of indices, check for mistakes in processor::init

     * Drop Processorparameters: AllCollectionIndices, TrackerHitCollectionIndices
     * Add ProcessorParameters: MainTrackerHitCollectionNames, VertexBarrelHitCollectionNames, VertexEndcapHitCollectionNames
     * Automatically obtain collection indices, throw exception if there is a collection name mismatch


