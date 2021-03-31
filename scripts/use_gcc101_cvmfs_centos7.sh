# --- gcc from LCG_99
source /cvmfs/sft.cern.ch/lcg/releases/gcc/10.1.0-6f386/x86_64-centos7/setup.sh

# --- python from LCG_99
export PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.8.6-3199b/x86_64-centos7-gcc10-opt/bin:${PATH}
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/Python/3.8.6-3199b/x86_64-centos7-gcc10-opt/lib:${LD_LIBRARY_PATH}
export PYTHONPATH=/cvmfs/sft.cern.ch/lcg/views/LCG_99/x86_64-centos7-gcc10-opt/lib/python3.8/site-packages

# --- git from LCG_99
export PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-e475b/x86_64-centos7-gcc10-opt/bin:${PATH}
export GIT_EXEC_PATH=/cvmfs/sft.cern.ch/lcg/releases/git/2.29.2-e475b/x86_64-centos7-gcc10-opt/libexec/git-core

# --- use a suitable mysql (also LCG_99)
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/10.4.12-8f05c/x86_64-centos7-gcc10-opt
