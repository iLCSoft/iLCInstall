#!/bin/bash

#######################################################
# sends an installation job which gets a tarball and
# unpacks it into the ESA
# J. Engels, Desy - IT
#######################################################

usage(){
cat << EOT
   usage: $(basename $0) CE TARBALL_URL

   example: $(basename $0)  desy.de http://ilcsoft.desy.de/ilcsoft-bin-releases/ilcsoft-v01-14-x86_64_gcc41_sl5-full.tar.gz
   example: $(basename $0)  desy.de /grid/ilc/ilcsoft/ilcsoft-v01-14-x86_64_gcc41_sl5-full.tar.gz
EOT
exit 2
}

test $# -eq 2 || usage

VO_NAME="ilc"
CE=$1
TARBALL_URL="$2"


# check for grid environment
voms-proxy-info -all | grep -q lcgadmin
test $? -eq 0 || { echo "no sgm proxy (did you initialize your grid environment?)" ; exit 1 ; }


# generate job.jdl
cat > job.jdl <<EOF
# job.jdl
VirtualOrganisation = "$VO_NAME";
Executable = "ilc-install-job.sh";
Arguments = "$TARBALL_URL";
StdOutput = "out";
StdError = "err";
InputSandbox = { "ilc-install-job.sh" };
OutputSandbox = { "out", "err" };
Environment = { "CE=$CE"};
Requirements = RegExp("$CE", other.GlueCEUniqueID);
EOF


# submit job and clean up
glite-wms-job-submit -a -e https://ilc-wms.desy.de:7443/glite_wms_wmproxy_server -o jobs.jids job.jdl

rm -f job.jdl

