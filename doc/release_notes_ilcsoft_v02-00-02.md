# iLCSoft v02-00-02

Patch release to production release for ILD optimization production
for the IDR.

Package changed wrt. to v02-00-01


## lcio v02-12-01
  
* 2018-06-21 Frank Gaede ([PR#48](https://github.com/ilcsoft/lcio/pull/48))
  - protect against invalid ParticleID objects in `LCTOOLS::printReconstructedParticles()`
           - these where added as a nasty side effect in `PIDHandler::getParticleID()`
  - fix `PIDHandler::getParticleID()` accordingly
  - fixes #47


## lcgeo v00-16-02

* 2018-06-25 Frank Gaede ([PR#223](https://github.com/ilcsoft/lcgeo/pull/223))
  - fix travis CI: use wget --no-check-certificate

* 2018-06-25 Daniel Jeans ([PR#222](https://github.com/ilcsoft/lcgeo/pull/222))
  - apply anti-DID field map to small ILD models. (assume same anti-DID field as for large models)

* 2018-05-23 Dan Protopopescu ([PR#216](https://github.com/ilcsoft/lcgeo/pull/216))
  - Added separate GlobalForwardCaloReadoutID for LumiCal and BeamCal and reverted the XMLs to use the DD4hep drivers from o2_v02
  - Deleted now unused driver CylCalEndcap_o1_v01_geo.cpp
  - Reverted to 'systemID=20' in plugin definition of the Barrel ECal

* 2018-06-21 Daniel Jeans ([PR#220](https://github.com/ilcsoft/lcgeo/pull/220))
  - QD0 and QDEX1A magnet strengths for 1 TeV
  - new models
    ILD_(sl)5_v07 : 1 TeV fwd magnets, solenoid field map, no anti-DID
    ILD_(sl)5_v08 : 1 TeV fwd magnets, solenoid field map + with anti-DID

* 2018-06-01 Marko Petric ([PR#219](https://github.com/ilcsoft/lcgeo/pull/219))
  - Accommodate AIDASoft/DD4hep#397 - `DD4hep.py` was dropped in favor of `dd4hep.py`

