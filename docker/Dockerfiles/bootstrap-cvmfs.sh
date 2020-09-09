#!/bin/bash                                                                                                                                                                            

sudo mkdir -p /cvmfs/sft.cern.ch
sudo mkdir -p /cvmfs/ilc.desy.de

sudo mount -t cvmfs sft.cern.ch /cvmfs/sft.cern.ch
sudo mount -t cvmfs ilc.desy.de /cvmfs/ilc.desy.de

echo 
ls /cvmfs/ilc.desy.de

bash
