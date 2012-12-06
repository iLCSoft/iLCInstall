#! /bin/bash

set -e

package_dir=${1:-.}

url=$(svn info $package_dir| grep URL | cut -d' ' -f2)

case $url in
    https://svnsrv.desy.de/public/* ) url=$(echo $url | sed 's|/public/|/desy/|') ; echo "changed url from /public/ to /desy/" ;;
esac

echo
echo orig url: $url


subdir=$(basename $url)
#echo subdir: $subdir

base_url=$(dirname $url)
#echo base url: $base_url


if [ "$subdir" != "trunk" ] ; then

branch=$subdir

base_url=$(dirname $base_url)

tag=${branch/-pre*/}
#echo tag: $tag

echo dest url: $base_url/tags/$tag

fi

echo
echo CMakeLists.txt:
grep _VERSION_ $package_dir/CMakeLists.txt

echo
echo list lib dir:
ls $package_dir/lib

echo
echo list branches:
svn ls $base_url/branches/

echo
echo list tags:
svn ls $base_url/tags/


if [ "$subdir" != "trunk" ] ; then
echo
echo svn cp $base_url/branches/$branch $base_url/tags/$tag -m\"tagged $tag\"
echo
fi
