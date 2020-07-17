# iLCSoft v02-01-02

Developer release before 250 GeV production.
A few bug fixes before 250 GeV production

## External software versions upgrade

None

## New packages

None

## Packages changed wrt. to v02-01-01:

# Marlin v01-17-01

* 2020-07-15 Remi Ete ([PR#39](https://github.com/iLCSoft/Marlin/pull/39))
  - Set LCIO output compression to ON by default, and compression level to 6 (ZLIB default)


# LCIO v02-14-02

* 2020-07-09 Ete Remi ([PR#88](https://github.com/iLCSoft/LCIO/pull/88))
  - Fixed random access manager record reading
     - Crash observed for old files without random access record
  - Added unit test for random access record
     - Run `anajob` on a file without random access record
