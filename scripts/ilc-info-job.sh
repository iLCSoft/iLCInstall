#!/bin/sh

##################################################
# script to get infos or tests on the grid
# @author Jan Engels - DESY
##################################################


cleanup(){
    # save exit code
    exit_code=$?

    echo

    # show time
    /bin/date -u

    echo '------------- job end -------------------------------'

    # end script
    exit $EXIT_CODE
}

# define trap to clean up stuff and remove locks
trap cleanup EXIT

echo
echo '------------- job start -----------------------------'
echo

# ----- gridtools ------------------------------------------------------------
echo "download gridtools"
curl "http://svnsrv.desy.de/viewvc/ilctools/mcprdsys/trunk/gridtools/?view=tar" -o gridtools.tgz
test $? -eq 0 || { echo "failed to download gridtools" ; exit 1 ; }
echo "unpack gridtools"
tar xzf gridtools.tgz
test $? -eq 0 || { echo "failed to untar gridtools" ; exit 1 ; }
export GRIDTOOLSDIR="$PWD/gridtools"
# ----------------------------------------------------------------------------


SW_BASEDIR=$VO_ILC_SW_DIR
SW_HOMEDIR=$SW_BASEDIR/ilcsoft

ARCH=x86_64_gcc41_sl5
SW_VER=v01-14-01


# get some debug infos and sanity tests
$GRIDTOOLSDIR/hepshlib/grid-wn-info.sh
#$GRIDTOOLSDIR/hepshlib/grid-wn-test-se.sh
echo CE: $CE
test -e $SW_BASEDIR && ls -l $SW_BASEDIR
test -e $SW_HOMEDIR && ls -l $SW_HOMEDIR
test -e $SW_HOMEDIR && ls -l $SW_HOMEDIR/$ARCH



# remove rpath from binaries/libraries
#$GRIDTOOLSDIR/$ARCH/chrpath -d $SW_HOMEDIR/$ARCH/$SW_VER/bin/*
#$GRIDTOOLSDIR/$ARCH/chrpath -d $SW_HOMEDIR/$ARCH/$SW_VER/lib/*

# remove debug symbols binaries/libraries
#strip $SW_HOMEDIR/$ARCH/$SW_VER/bin/*
#strip $SW_HOMEDIR/$ARCH/$SW_VER/lib/*

# fix sw installations for sl6
#test -e $SW_HOMEDIR && rm -vf $SW_HOMEDIR/$ARCH/extlib/{libc.so.6,libpthread.so.0}

# init sw
#. $SW_HOMEDIR/$ARCH/init_ilcsoft.sh $SW_VER

# check tools
#ldd $SW_HOMEDIR/$ARCH/SW_VER/bin/Mokka
#ldd $SW_HOMEDIR/$ARCH/SW_VER/bin/Marlin


exit 0

