#!/bin/bash

####################################################################
# script to pack all shared library dependencies from a binary
# or shared library (tries to exclude any ilcsoft library)
#
# Jan Engels, Desy - IT
####################################################################


set -e # exit if any command fails
set -o errexit # exit if any command fails
set -o pipefail # exit if any command in a pipe fails

if test $# -eq 0 ; then
    echo "usage example: $0 /path/to/binary [output_dir]"
    exit 1
fi

input_file=$1
output_dir=${2:-$PWD/extlib}

mkdir -p $output_dir

#ext_libs=$(ldd $input_file | grep '=>' | grep -o '/[^ ]*' )
ext_libs=$(ldd $input_file | grep -v '/ilcsoft/' | grep '=>' | grep -o '/[^ ]*' )

echo "copy external libs..."

for i in $ext_libs ; do
    b=$(basename $i)
    #rsync -avL $i $output_dir
    test -e $output_dir/$b && echo "already copied $b" && continue
    cp -v $i $output_dir
done

