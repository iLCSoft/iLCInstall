#!/bin/bash
test $# -ne 0 && mkdir -p output

if [ $# -eq 1 -a "$1" = "-o" ] ; then
    glite-wms-job-output --dir $PWD/output `tail -n1 jobs.jids`
elif [ $# -eq 2 -a "$1" = "-o" ] ; then
    glite-wms-job-output --dir $PWD/output $2
elif [ $# -eq 2 -a "$1" = "-c" ] ; then
    glite-wms-job-status $2
else
    #glite-wms-job-status `tail -n1 jobs.jids`
    glite-wms-job-status `sed 1d jobs.jids`
    echo
    echo "get status from a certain job: $0 -c jobid"
    echo "get output from a certain job: $0 -o jobid"
    echo "get output from last job: $0 -o"
    echo
    echo
fi

