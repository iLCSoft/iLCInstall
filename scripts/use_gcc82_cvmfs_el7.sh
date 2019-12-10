#---- use gcc and python from SFT in cvmfs
source /cvmfs/sft.cern.ch/lcg/releases/gcc/8.2.0/x86_64-centos7/setup.sh
export PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_96/Python/2.7.16/x86_64-centos7-gcc8-opt/bin:$PATH
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_96/Python/2.7.16/x86_64-centos7-gcc8-opt/lib:$LD_LIBRARY_PATH

# --- use a suitable mysql
export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/5.7.26-c3e26/x86_64-centos7-gcc8-opt

# --- use a recent version of git
export PATH=/cvmfs/sft.cern.ch/lcg/contrib/git/2.17.0/x86_64-centos7/bin:$PATH

