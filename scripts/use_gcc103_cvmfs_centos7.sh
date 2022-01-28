# --- gcc from LCG_101
source /cvmfs/sft.cern.ch/lcg/releases/gcc/10.3.0/x86_64-centos7/setup.sh

# --- python from LCG_101
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.9.6-b0f98/x86_64-centos7-gcc10-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.9.6-b0f98/x86_64-centos7-gcc10-opt/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_101/x86_64-centos7-gcc10-opt/lib/python3.9/site-packages

# --- git from LCG_101
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-e475b/x86_64-centos7-gcc10-opt/bin:${PATH}
export GIT_EXEC_PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-e475b/x86_64-centos7-gcc10-opt/libexec/git-core

# --- use a suitable mysql (also LCG_101)
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/10.4.20-c0154/x86_64-centos7-gcc10-opt
