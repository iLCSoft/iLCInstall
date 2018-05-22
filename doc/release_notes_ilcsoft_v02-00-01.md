# iLCSoft v02-00-01

Patch release to production release for ILD optimization production
for the IDR.

Package changed wrt. to v02-00

## DD4hep v01-07-01

* 2018-05-17 Frank Gaede
   - exclude leptons with zero lifetime from Geant4
   - fixes issue: https://github.com/AIDASoft/DD4hep/issues/387

## lcgeo v01-16-01

* 2018-05-22 Frank Gaede ([PR#218](https://github.com/ilcsoft/lcgeo/pull/218))
  - ILD:  add 4T solenoid field map for ILD_s5_o?_v03 models

* 2018-05-18 Emilia Leogrande ([PR#217](https://github.com/ilcsoft/lcgeo/pull/217))
  - Vertex_o4_v05.xml: doubled support material in the vertex (barrel and endcap)
  - This model is made for testing purposes only

* 2018-04-26 Oleksandr Viazlo ([PR#215](https://github.com/ilcsoft/lcgeo/pull/215))
  - new FCCee_o1_v03 detector model:
    - extend ECAL endcap
    - shrink HCAL ring
    - reduce magnetic field in barrel yoke from 1.5 T to 1.0 T
    - fix in HCAL layer layout (swap steel absorber with steel wall of cassette)



## FastJet/FastJetcontrib  3.2.1/1.025
	
  -  see http://fastjet.fr/all-releases.html for details
  -  was (3.2.0/1.017)
