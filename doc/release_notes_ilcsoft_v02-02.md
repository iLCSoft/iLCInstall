# iLCSoft v02-02

Production release for large 250 GeV production of ILD.

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. to v02-01-02:

# LCIO v02-15

* 2020-08-13 Frank Gaede ([PR#102](https://github.com/ilcsoft/lcio/pull/102))
  - fix `ProcessFlag::decodeMCTruthProcess()`
        - remove ISR photons in final state for DBD 250 GeV files

* 2020-08-12 Frank Gaede ([PR#101](https://github.com/ilcsoft/lcio/pull/101))
  - make delphes2lcio compatible w/ LCIO 2.14 again
           - by not calling `ProcessFlag::decodeMCTruthProcess()`
  - add `higgsss` and `unknown` to `ProcessFlag`
  - update logic in `ProcessFlag::decodeMCTruthProcess()` (from J.List, DESY)

* 2020-08-11 Frank Gaede ([PR#100](https://github.com/ilcsoft/lcio/pull/100))
  - improve the `delphes2lcio` tool
          - changes some default collection names
                  - Electrons/ Muons/ Photons -> IsolatedElectrons / IsolatedMuons / ...
                  - MCParticle -> MCParticles
          - update all examples and Readme.md accordingly
          - add event params: crossSection and ProcessID as available in Delphes
  - add method `ProcessFlag decodeMCTruthProcess(const EVENT::LCCollection*) `
          - with first example implementation -> needs iteration
          - call this in `delphes2lcio`
  - use `const EVENT::LCCollection*` in `UTIL::LCIterator`

* 2020-08-11 Frank Gaede ([PR#99](https://github.com/ilcsoft/lcio/pull/99))
  - fix memory leak in SIOReader
       - delete previous Event and RunHeader before reading a new one
       - this restores the old expected behavior of the `IO::LCReader`
       - for parallel event reading one needs to use the `MT::LCReader` directly and
          handle the memory accordingly (e.g. via use of std::unique_ptr)
               - see [$LCIO/src/cpp/src/EXAMPLE/lcio_parallel_processing.cc](../src/cpp/src/EXAMPLE/lcio_parallel_processing.cc)
  - fixes #97 and #98

* 2020-08-07 flagarde ([PR#96](https://github.com/ilcsoft/lcio/pull/96))
  - fix some warnings w/ exceptions

* 2020-08-07 flagarde ([PR#94](https://github.com/ilcsoft/lcio/pull/94))
  - Remove FindROOT.cmake
  - Use ROOTConfig.cmake provided by ROOT
  - Change ROOT_CINT_WRAPPER to ROOT_rootcint_CMD as it's provided by ROOT 6.04.18 ROOTConfig.cmake
       - fixes #68

* 2020-08-07 flagarde ([PR#94](https://github.com/ilcsoft/lcio/pull/94))


* 2020-07-22 JennyListDESY ([PR#92](https://github.com/ilcsoft/lcio/pull/92))
  - moved . ./setup.sh upwards as part of the installation instructions

* 2020-07-22 Marko Petric ([PR#91](https://github.com/ilcsoft/lcio/pull/91))
  - fix bug in build dependency, affecting only build on large number of cores

* 2020-07-22 JennyListDESY ([PR#90](https://github.com/ilcsoft/lcio/pull/90))
  - inserted a missing cd LCIO to the instructions
