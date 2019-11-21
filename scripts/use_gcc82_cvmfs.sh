#---- use gcc and python from SFT in cvmfs
source /cvmfs/sft.cern.ch/lcg/releases/gcc/8.2.0/x86_64-slc6/setup.sh
export PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_96/Python/2.7.16/x86_64-slc6-gcc8-opt/bin:$PATH
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/LCG_96/Python/2.7.16/x86_64-slc6-gcc8-opt/lib:$LD_LIBRARY_PATH

# --- use correct tbb for ROOT
export LD_LIBRARY_PATH=/cvmfs/sft.cern.ch/lcg/releases/tbb/2019_U1-5939b/x86_64-slc6-gcc8-opt/lib/:$LD_LIBRARY_PATH 


# --- use a suitable mysql

export MYSQL_DIR=/cvmfs/sft.cern.ch/lcg/releases/mysql/5.7.26-c3e26/x86_64-slc6-gcc8-opt


# --- use a recent version of cmake 
export PATH=/afs/desy.de/project/ilcsoft/sw/x86_64_gcc82_sl6/CMake/3.15.1/bin:$PATH

