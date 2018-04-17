# iLCSoft v02-00

Production release for ILD optimization production
for the IDR.


Packages changed wrt. to v01-19-06:




## ConformalTracking v01-07
  
* 2018-03-29 Andre Sailer ([PR#33](https://github.com/ilcsoft/ConformalTracking/pull/33))
  - combineCollections: Properly protect against empty collections, fixes #31

* 2018-04-17 Andre Sailer ([PR#34](https://github.com/ilcsoft/ConformalTracking/pull/34))
  - ConformalTracking: change setting of input collections, use collection names instead of indices, check for mistakes in processor::init

     * Drop Processorparameters: AllCollectionIndices, TrackerHitCollectionIndices
     * Add ProcessorParameters: MainTrackerHitCollectionNames, VertexBarrelHitCollectionNames, VertexEndcapHitCollectionNames
     * Automatically obtain collection indices, throw exception if there is a collection name mismatch


