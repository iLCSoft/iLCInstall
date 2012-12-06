#!/bin/bash

##################################################
# script for installing ilc software on the grid
# J. Engels - Desy - IT
##################################################

usage(){
cat << EOT
    usage: $(basename $0) TARBALL(S)_TO_INSTALL
    ex.:   $0 
EOT
}

# alias for ESA SW area
SW_BASEDIR=$VO_ILC_SW_DIR

# where software lives on ESA (Exp SW Area)
SW_HOMEDIR=$SW_BASEDIR/ilcsoft

# ----- BEGIN: function definitions ---------------

# define function to display error msg and exit
abort(){
    echo "Error: $1"
    exit 1;
}

create_lock(){
    lock_file=$1
    echo "creating lock $1..."
    lock_timestamp=$(date +%s)
    # -30: seconds between retries
    # -r 120: number of retries
    # -l 172800: lockfile gets invalid after 48 hours (remove zombie locks)
    lockfile -30 -r 120 -l 172800 $lock_file ; r=$?
    afterlock_timestamp=$(date +%s)
    locktime=$(( $afterlock_timestamp - $lock_timestamp ))
    if [ $r -eq 0 ]; then
        echo "lock created successfully! (waiting time: $locktime seconds)"
        lock_created=1
    else
        abort "failed to create lock after $locktime seconds!!";
    fi
}

remove_lock(){
    if [ -n "$lock_file" -a -e "$lock_file" -a ${lock_created:-0} -eq 1 ] ; then
        echo "removing lock $lock_file..."
        rm -fv $lock_file || abort "could not remove lock!!!!!"
        echo "lock removed successfully!"
    fi
}

cleanup(){
    # save exit code
    exit_code=$?

    # print usage
    test $exit_code -eq 2 && { usage ; exit $exit_code ; }

    if [ -r "$SW_HOMEDIR" ] ; then

        # give all read + execute permissions
        echo "give read + execute permissions to all users..."
        c="chmod -R a+rx $SW_HOMEDIR" ; echo "> $c"
        $c || echo "*** WARNING: failed changing user permissions"
        echo

        # give sgm group write permissions (if necessary)
        if [ $(id | cut -d' ' -f3 | sed 's/,/ /g' | wc -w) -ne 1 ] ; then
            echo "give write permissions to sgm group..."
            c="chmod -R g+w $SW_HOMEDIR" ; echo "> $c"
            $c || echo "*** WARNING: failed changing group permissions"
            echo
        fi

        c="ls -ld \$SW_HOMEDIR/*/*/*/"
        echo "+ $c" ; eval $c
        echo ; echo
    fi

    remove_lock

    echo
    exit $exit_code
}

# define trap to clean up stuff and remove locks
#trap cleanup EXIT HUP INT QUIT ABRT TERM
#trap cleanup 0 1 2 3 6 15
trap cleanup EXIT

# ----- END: function definitions -------------

# check cmd line arguments
if [ $# -lt 1 ] ; then
    exit 2
fi

# ----- gridtools ------------------------------------------------------------
wget --no-verbose "http://svnsrv.desy.de/viewvc/ilctools/mcprdsys/trunk/gridtools/?view=tar" -O ./gridtools.tgz
test $? -eq 0 || { echo "failed to download gridtools" ; exit 1 ; }
tar xzf gridtools.tgz
test $? -eq 0 || { echo "failed to untar gridtools" ; exit 65 ; }
export GRIDTOOLSDIR="$PWD/gridtools"
export PYTHONPATH="$GRIDTOOLSDIR/heppylib:$PYTHONPATH"
export PATH="$GRIDTOOLSDIR:$PATH"
export PATH="$GRIDTOOLSDIR/hepshlib:$PATH"
# ----------------------------------------------------------------------------


echo "get some worker node infos"
grid-wn-info.sh > grid-wn-info.log

echo "start installation $@"

# very ugly code :(
echo "roughly estimate available disk space on $SW_BASEDIR"
if [ "`df $SW_BASEDIR | sed '1d' | grep -o -E '^[^ ]+'`" = "AFS" ] ; then
    fs quota $SW_BASEDIR &>/dev/null && dq=`fs quota $SW_BASEDIR | cut -d'%' -f1` || dq=100
else
    dq=`df $SW_BASEDIR | sed '1d' | grep -o -E '[0-9]+%' | cut -d% -f1`
fi
# convert used space to available space
dq=`expr 100 - $dq`
echo "$dq% disk space available on $SW_BASEDIR"
echo

echo "create directory $SW_HOMEDIR ..."
c="mkdir -p $SW_HOMEDIR" ; echo "> $c"
$c || abort "could not create dir $SW_HOMEDIR";
echo

echo "do write test in $SW_HOMEDIR"
c="touch $SW_HOMEDIR/.write_test.tmp" ; echo "> $c"
$c || abort "write test in $SW_HOMEDIR failed!";
echo

echo "do delete test in $SW_HOMEDIR"
c="rm -f $SW_HOMEDIR/.write_test.tmp" ; echo "> $c"
$c || abort "delete test in $SW_HOMEDIR failed!";
echo

create_lock "$SW_BASEDIR/.install.lock"
echo

### ilcsoft
echo "will now install ilc software..."
echo

# !!! SET TO 1 TO WIPE OUT ALL ILCSOFT INSTALLATIONS !!! 
WIPEOUT=0
## CLEAN UP PREVIOUS INSTALLATIONS
if [ -d $SW_HOMEDIR ] ; then

    if [ "$WIPEOUT" = "1" ] ; then
        echo "WIPE OUT ALL PREVIOUS ILCSOFT INSTALLATIONS"
        c="rm -rf $SW_HOMEDIR" ; echo "> $c"
        $c || abort "failed trying to remove previous installations!!";
        echo
        echo "recreate directory $SW_HOMEDIR ..."
        c="mkdir -p $SW_HOMEDIR" ; echo "> $c"
        $c || abort "could not create dir $SW_HOMEDIR";
        echo
    fi
fi

for tarball_url in $* ; do

echo "installing $tarball_url ..."

# abort if there is not enough disk space
echo "check if there is enough disk space for installation..."
test $dq -gt 0 || abort "not enough disk space available on $SW_HOMEDIR"
echo "$dq% disk space available on $SW_HOMEDIR"
echo

echo "download software tarball..."
if [ "${tarball_url::4}" = "http" ] ; then
    c="wget --no-verbose \"$tarball_url\" -O ./tarball.tgz"
else
    c="grid-dl-file.py $tarball_url ./tarball.tgz"
fi
eval $c
test $? -ne 0 && abort "failed to download $tarball_url"

echo "unpack tarball to $SW_BASEDIR..."
c="tar -mxzf tarball.tgz -C $SW_BASEDIR" ; echo "> $c"
$c || abort "failed to unpack tarball"
echo

rm -vf tarball.tgz

done

#pushd $SW_BASEDIR >/dev/null
#rm -f initILCSOFT.sh  # FIXME need to remove initILCSOFT.sh from older installations
#ln -sf ilcsoft/initILCSOFT.sh
#popd >/dev/null

echo "installation finished successfully!"
echo

exit 0

