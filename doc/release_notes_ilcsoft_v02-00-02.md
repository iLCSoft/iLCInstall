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


## lcgeo v00-16-03

* 2018-06-26 Frank Gaede ([PR#224](https://github.com/iLCSoft/lcgeo/pull/224)
  - make lcgeo (v00-16-03 and higher) compatible w/ DD4hep v01-17-0X releases
  -  revert https://github.com/iLCSoft/lcgeo/pull/219
       - use DD4hep rather than dd4hep in ddsim python


### lcgeo v00-16-02

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


## DD4hep v01-07-02

* 2018-06-26 Frank Gaede ([PR#413](https://github.com/AIDASoft/DD4hep/pull/413)
  - bug fix in Geant4EventReaderGuineaPig
    - fix ignoring input lines with 'nan'
    - did not work on SL6 w/ gcc


## MarlinReco v01-25

* 2018-07-05 Jakob Beyer ([PR#52](https://github.com/ilcsoft/MarlinReco/pull/52))
  - Adding new analysis toolTJjetsPFOAnalysisProcessor:
        - Combined the PFOAnalysis processor with the jet analysis power of the TrueJet/TrueJet_Parser tools to gain insight into individual jet behaviour and reconstruction.

* 2018-08-06 Erica Brondolin ([PR#54](https://github.com/ilcsoft/MarlinReco/pull/54))
  - Introduce CLICPfoSelectorAnalysis which runs on the PFO input collection and creates: a TTree with the PFO variables used in the CLICPfoSelector, cluster time vs pT graphs for each particle category and region, and PFO energy sum histos for each particle category and region
  - CLICPfoSelectorAnalysis has the possibility to detect if the PFO belongs to signal/overlay
  - CLICPfoSelectorAnalysis has the possibility to check if the track and the cluster belonging to the same PFO were produced by at least one common MCParticle

* 2018-07-18 Junping Tian ([PR#53](https://github.com/ilcsoft/MarlinReco/pull/53))
  - fixed IsolatedLeptonTagger
        - fixed the problem about track impact parameters in the new samples where interaction point is     smeared
        - some minor updates about pre-cut values and symmetric treatment for d0/z0 significance
        - new weights trained for new samples are provided



## KalTest v02-05

* 2018-08-21 Bo Li ([PR#3](https://github.com/ilcsoft/KalTest/pull/3))
  - Merged Runge-Kutta (RK) track propagation functions;
  - Added another trsansport option by using RK;
  - Cleaned the ct_nonuniform example


## CEDViewer v01-16

* 2018-08-21 Frank Gaede ([PR#7](https://github.com/ilcsoft/CEDViewer/pull/7))
  - improved CEDViewer/DDCEDViewer (also used by ced2go)
        - print run and event number at end of event
        - print only shown collections
        - added new collections ( mostly calo hits) from ILD mass production

* 2018-08-20 Akiya Miyamoto ([PR#6](https://github.com/ilcsoft/CEDViewer/pull/6))
  - Added a command line option, "-n 1".
       - If this option is specified, glced is not executed.
       - This option is useful for a case to run glced at local client and run CEDViewer at remote host.



## LCFIPlus v00-06-09

* 2018-05-14 Ryo Yonamine ([PR#38](https://github.com/lcfiplus/LCFIPlus/pull/38))
  Add daughter relation in lcfiplus::MCPartilce. This change does not affect usual reconstruction where no MCParticle is used.

* 2018-07-14 Ryo Yonamine ([PR#39](https://github.com/lcfiplus/LCFIPlus/pull/39))
  Cope with events having no vertex track candidates.
  - It tried to add a vertex even if it is a null pointer. This is confusing and caused a problem later processes in some cases.
