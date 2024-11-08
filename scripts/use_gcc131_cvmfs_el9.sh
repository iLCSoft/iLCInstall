#!/usr/bin/env bash

# --- gcc from LCG_106
source /cvmfs/sft.cern.ch/lcg/releases/gcc/13.1.0-b3d18/x86_64-el9/setup.sh

# --- python from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.11.9-2924c/x86_64-el9-gcc13-opt/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_106/x86_64-el9-gcc13-opt/lib/python3.11/site-packages

# --- git from LCG_106
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/bin:${PATH}
export GIT_EXEC_PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-daa17/x86_64-el9-gcc13-opt/libexec/git-core

# --- use a suitable mysql (also LCG_106)
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/10.5.20-7d082/x86_64-el9-gcc13-opt
