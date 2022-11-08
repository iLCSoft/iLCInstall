# iLCSoft v02-03-01

Patch release for the v02-03 development series (see the [v02-03 release notes](https://github.com/iLCSoft/iLCInstall/blob/master/doc/release_notes_ilcsoft_v02-03.md) for more details about this series).

## External software versions upgrade
None

## New packages

None

## Packages changed wrt. v02-02-01

### LCIO v02-18

* 2022-11-08 Thomas Madlener ([PR#155](https://github.com/iLCSoft/LCIO/pull/155))
  - Add a previously missed function declaration to the .aid file to fix the java bindings. Fixes #154

* 2022-10-19 Thomas Madlener ([PR#153](https://github.com/iLCSoft/LCIO/pull/153))
  - Make c++17 the default and minimum c++ version for building LCIO. All "major builds" of LCIO have been using c++17 for at least a few years now, so this should not be a big issue.

* 2022-10-19 Thomas Madlener ([PR#152](https://github.com/iLCSoft/LCIO/pull/152))
  - Remove macOS workflow since github hosted runners no longer support all necessary features. See also: https://github.com/AIDASoft/run-lcg-view/pull/3
  - Update used github actions to latest available version for better caching behavior and cleaner log outputs
  - Switch to newer LCG releases for the build environments to target more recent compilers and python versions.
    - Keep one build environment that is close to the one used for the iLCSoft v02-02 to avoid accidental breaks.

* 2022-10-19 Bohdan Dudar ([PR#150](https://github.com/iLCSoft/LCIO/pull/150))
  - Added a utility function to calculate Track momentum based on its track parameters and magnetic field
  - Added methods to the LCRelationNavigator that extract the highest weight with an option to indicate weight encoding type ("track"/"cluster").
  - Added a utility function to get an index of a provided object inside a given LCCollection
  - Added a utility function to return a leading track from ReconstructedParticle in case it has multiple tracks attached.


