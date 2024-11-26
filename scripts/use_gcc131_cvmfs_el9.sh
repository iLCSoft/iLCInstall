#!/usr/bin/env bash

# --- gcc from LCG_106
source /cvmfs/sft.cern.ch/lcg/releases/gcc/13.1.0-b3d18/x86_64-el9/setup.sh

# --- python from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/lib:/cvmfs/sft.cern.ch/lcg/releases/blas/0.3.20.openblas-c07f1/x86_64-el9-gcc13-opt/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/lib/python3.11/site-packages

# --- git from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/bin:${PATH}
export GIT_EXEC_PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/libexec/git-core

# --- use a suitable mysql (also LCG_106)
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/10.5.20-7d082/x86_64-el9-gcc13-opt

# --- pick up Qt5 from LCG release
export CMAKE_PREFIX_PATH=/cvmfs/sft.cern.ch/lcg/releases/qt5/5.15.9-c981a/x86_64-el9-gcc13-opt:${CMAKE_PREFIX_PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/qt5/5.15.9-c981a/x86_64-el9-gcc13-opt/lib:${LD_LIBRARY_PATH}
export PATH=/cvmfs/sft.cern.ch/lcg/releases/qt5/5.15.9-c981a/x86_64-el9-gcc13-opt/bin:${PATH}
export QT_PLUGIN_PATH=/cvmfs/sft.cern.ch/lcg/releases/qt5/5.15.9-c981a/x86_64-el9-gcc13-opt/plugins
export QT_QMAKE_EXECUTABLE=/cvmfs/sft.cern.ch/lcg/releases/qt5/5.15.9-c981a/x86_64-el9-gcc13-opt/bin/qmake

# --- also pick up xrootd from LCG release (as ROOT fails to build without this for whatever reason)
export PATH=/cvmfs/sft.cern.ch/lcg/releases/xrootd/5.6.9-2f3d3/x86_64-el9-gcc13-opt/bin:${PATH}
export CMAKE_PREFIX_PATH=/cvmfs/sft.cern.ch/lcg/releases/xrootd/5.6.9-2f3d3/x86_64-el9-gcc13-opt:${CMAKE_PREFIX_PATH}
export LD_PREFIX_PATH=/cvmfs/sft.cern.ch/lcg/releases/xrootd/5.6.9-2f3d3/x86_64-el9-gcc13-opt/lib64:${CMAKE_PREFIX_PATH}
