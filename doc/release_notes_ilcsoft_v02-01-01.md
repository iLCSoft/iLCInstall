# iLCSoft v02-01

Developer release before 250 GeV production.
Main important change is the new LCIO IO layer based on 
the external version of SIO.

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. to v02-01:

### LCIO v02-14

* 2020-07-01 Frank Gaede ([PR#86](https://github.com/ilcsoft/lcio/pull/86))
  - new classes  `UTIL::EventSummary` and `UTIL::ProcessFlag`
          - used in delphes2lcio for writing event summary information and 
             encoding the generated Monte Carlo process 
  - improve delphes2lcio example
       - fill more quantities for EventSummary ( see  UTIL::EventSummary )
       - updated examples

* 2020-07-01 Remi Ete ([PR#85](https://github.com/ilcsoft/lcio/pull/85))
  - Fixed LCGenericObject collection flag IO writing
  - Fixed virtual override warning in SIOReader

* 2020-06-30 Ete Remi ([PR#79](https://github.com/ilcsoft/lcio/pull/79))
  - Externalized SIO package: https://github.com/iLCSoft/SIO
  - Use new SIO implementation:
    - Ensure thread-safety for multiple LCReader / LCWriter instance (removal of globals)
    - Possibility for adding new compression algorithm in future
    - Standard LCReader and LCWriter use the MT versions (see below) for implementation under the hood
  - Added new `MT::LCReader` and `MT::LCWriter`
     - Different interface for reading and writing events. Use smart pointers for event/run ownership
     - MT::LCWriter allows for writing concurrently event in a file from multiple threads. Event encoding and compression is standalone, so thread-safe, and I/O writing is done under a (fast) mutex.
  - Introduce new creation flag for standard LCReader: **LazyUnpacking**
     1. Reads an event from file 
     2. Move the compressed buffer inside an LCEvent object
     3. Perform un-compression and decoding only on demand when `LCEvent::getCollection()` is called
  - LCIO objects uids increment is now atomic (`AccessChecked`)
  - Introduced runtime extensions for LCEvent, accessible via `LCEvent::runtime()` method.
  - Introduced `LCIO_DEPRECATED` macro for deprecated methods in LCIODeprecated.h
  - LCIO extensions:
    - Removed global destructor mapping for each relation type, because not thread safe
    - Turned internal extension type to `std::shared_ptr<void>` to use type-safe extension destructor
  - Added example binaries:
     - `lcio_parallel_processing`: a small example to illustrates how to use the new MT classes. Implements a simple scheduling algorithm for parallel event processing
     - `lcio_parallel_read`: a small example of how to dump events and runs from multiple files at the same time in parallel
     - `lcio_performance`: printout file reading performance with and without lazy unpacking
  - Unit testing:
     - added unit test for lazy unpacking feature
     - switched back ON the unit test on RT extensions
  - Bug fixes
     - CXX standard was hardcoded to 14. Now set it to 14 if not specified via command line with i.e `-DCMAKE_CXX_STANDARD=17`  
  - Packaged builtin SIO in LCIO
     - Compile the SIO library (only) if not found on your system

* 2020-06-25 Frank Gaede ([PR#84](https://github.com/ilcsoft/lcio/pull/84))
  - improve the delphes2lcio tool
       - add configuration options for LCIO collection names and delphes branches to be used
       - the default configuration works for the ILD delphes card [https://github.com/ILDAnaSoft/ILDDelphes](https://github.com/ILDAnaSoft/ILDDelphes)
       - it can be overwritten with a simple configuration file see ./examples/delphes2lcio.cfg and *Advanced Topics* in the READM.md
       - additional jet collections can be added to the event if available in the delphes output
               - current default are *Durham2Jets-Durham6Jets*

* 2020-06-17 Frank Gaede ([PR#82](https://github.com/ilcsoft/lcio/pull/82))
  - improve delphes2lcio example
        - add an `EventSummaries` collection to a last dummy event with evtNum=-99 runNum=-99
        - add example `higgs_recoil_plots_fast.C` demonstrating the usage

* 2020-06-15 Frank Gaede ([PR#81](https://github.com/ilcsoft/lcio/pull/81))
  - fixes for delphes2lcio example:
        - fix names of isolated particle collections
        - add example for drawing higgs recoil peak

* 2020-06-12 Frank Gaede ([PR#80](https://github.com/ilcsoft/lcio/pull/80))
  - add example delphes2lcio 
        - writes LCIO mini-DSTs from a Delphes simulation
        - see [../examples/cpp/delphes2lcio/README.md](../examples/cpp/delphes2lcio/README.md) for details

* 2020-04-17 Pere Mato ([PR#77](https://github.com/ilcsoft/lcio/pull/77))
  - Fine tune the latest fix to cope with new PyROOT to use old API for versions 6.20.X






