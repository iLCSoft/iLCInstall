#!/bin/bash

#Determine which OS you are using
if [ "$(uname)" == "Darwin" ]; then
    if [ $(sw_vers -productVersion | awk -F '.' '{print $1 "." $2}') == "10.12" ]; then
        OS=mac1012
        COMPILER_TYPE=clang
        COMPILER_VERSION=clang80
    else
        echo "Bootstrap only works on macOS Sierra (10.12)"
    fi
elif [ "$(uname)" == "Linux" ]; then
    if [ "$( cat /etc/*-release | grep Scientific )" ]; then
        OS=slc6
    elif [ "$( cat /etc/*-release | grep CentOS )" ]; then
        OS=centos7
    fi
else
    echo "UNKNOWN OS"
    exit 1
fi

#Determine is you have CVMFS installed
if [ ! -d "/cvmfs" ]; then
    echo "No CVMFS detected, please install it."
    exit 1
fi

if [ ! -d "/cvmfs/clicdp.cern.ch" ]; then
    echo "No clicdp CVMFS repository detected, please add it."
    exit 1
fi


#Determine which compiler to use
if [ -z ${COMPILER_TYPE} ]; then
    COMPILER_TYPE='gcc'
fi
if [ ${COMPILER_TYPE} == 'gcc' ]; then
    COMPILER_VERSION='gcc62'
fi
if [ ${COMPILER_TYPE} == 'llvm' ]; then
    COMPILER_VERSION='llvm39'
fi


#Choose build type
if [ -z ${BUILD_TYPE} ]; then
    BUILD_TYPE='opt'
fi


# General variables
CLICREPO=/cvmfs/clicdp.cern.ch
BUILD_FLAVOUR=x86_64-${OS}-${COMPILER_VERSION}-${BUILD_TYPE}

#--------------------------------------------------------------------------------
#     Compiler
#--------------------------------------------------------------------------------

if [ ${COMPILER_TYPE} == "gcc" ]; then
    source ${CLICREPO}/compilers/gcc/6.2.0/x86_64-${OS}/setup.sh
fi
if [ ${COMPILER_TYPE} == "llvm" ]; then
    source ${CLICREPO}/compilers/llvm/3.9.0/x86_64-${OS}/setup.sh
fi

#--------------------------------------------------------------------------------
#     CMake
#--------------------------------------------------------------------------------

export CMAKE_HOME=${CLICREPO}/software/CMake/3.14.3/${BUILD_FLAVOUR}
export PATH=${CMAKE_HOME}/bin:$PATH

#--------------------------------------------------------------------------------
#     MySQL
#--------------------------------------------------------------------------------

export MySQL_DIR=/cvmfs/clicdp.cern.ch/software/MySQL/5.7.16/${BUILD_FLAVOUR}

#--------------------------------------------------------------------------------
#     Python
#--------------------------------------------------------------------------------

if [ ${OS} == "slc6" ] || [ ${OS} == "centos7" ]; then
    export PYTHONDIR=${CLICREPO}/software/Python/2.7.12/${BUILD_FLAVOUR}
    export PATH=${PYTHONDIR}/bin:$PATH
    export LD_LIBRARY_PATH=${PYTHONDIR}/lib:${LD_LIBRARY_PATH}
fi
