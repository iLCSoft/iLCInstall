#!/bin/bash

usage(){
cat << EOT
   usage: $(basename $0) CE

   example: $(basename $0)  desy.de
EOT
exit 2
}

test $# -eq 1 || usage

VO_NAME="ilc"
CE=$1

# check for grid environment
voms-proxy-info -all
test $? -eq 0 || { echo "no proxy (did you initialize your grid environment?)" ; exit 1 ; }


# generate job.jdl
cat > job.jdl <<EOF
# job.jdl
VirtualOrganisation = "$VO_NAME";
Executable = "ilc-info-job.sh";
Arguments = "";
StdOutput = "out";
StdError = "err";
InputSandbox = { "ilc-info-job.sh" };
OutputSandbox = { "out", "err" };
#OutputSandboxBaseDestURI = "gsiftp://grid-cr6.desy.de/tmp/engels-$(date +%F-%T)";
Environment = { "CE=$CE"};
#Requirements = Member( "VO-$VO_NAME-ilcsoft-v01-14-x86_64_gcc41_sl5", other.GlueHostApplicationSoftwareRunTimeEnvironment);
#Requirements = other.GlueCEInfoHostName=="$CE"; # exact match
Requirements = RegExp("$CE", other.GlueCEUniqueID);
# this should not be needed! use only if desy wms's are overloaded (lcg-infosites --vo ilc wms)
#WmProxyEndPoints = { "https://wms301.cern.ch:7443/glite_wms_wmproxy_server","https://wms302.cern.ch:7443/glite_wms_wmproxy_server","https://wms303.cern.ch:7443/glite_wms_wmproxy_server","https://ilc-wms.desy.de:7443/glite_wms_wmproxy_server" };
EOF


# submit job and clean up
glite-wms-job-submit -a -e https://ilc-wms.desy.de:7443/glite_wms_wmproxy_server -o jobs.jids job.jdl

# do not use this!
#glite-wms-job-submit -a -e https://wms301.cern.ch:7443/glite_wms_wmproxy_server -o jobs.jids job.jdl
#glite-wms-job-submit -a -e https://grid-wms13.desy.de:7443/glite_wms_wmproxy_server -o jobs.jids job.jdl
#glite-wms-job-submit -a -e https://ilc-wms.desy.de:7443/glite_wms_wmproxy_server -r grid-cr4.desy.de:8443/cream-pbs-emi -o jobs.jids job.jdl
#glite-ce-job-submit -a -r grid-cr6.desy.de:8443/cream-pbs-desy job.jdl
#glite-wms-job-list-match -a job.jdl

rm -f job.jdl
