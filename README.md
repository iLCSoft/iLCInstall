# iLCInstall

Installation script that enable a fully automated installation of iLCSoft with minimal user intervention.

iLCInstall is distributed under the [GPLv3 License](http://www.gnu.org/licenses/gpl-3.0.en.html)

[![License](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Usage

The script can be called with the following syntax:
```
ilcsoft-install install.cfg [ -p, -i ]
```
options description:
* -p to preview installation environment
* -i to install the software

If called without options a summary of the installation is displayed. Examples of configuration files can be found under releases.



## Usage Examples:



### Install the full ilc software tools + external dependencies on your local disk 

* note that boost, mysql, java and cernlib installations are not supported in ilcinstall
*  this packages need to be installed on your system. Please change the paths to this packages in
* the file releases/v01-17-07/release-versions.py

* for debian/ubuntu distributions you may need to install a few packages beforehand such as:
* apt-get install build-essential cmake subversion libmysqlclient-dev freeglut3-dev zlib1g-dev libqt4-dev cernlib-core-dev 
* default-jdk libxpm-dev libxmu-dev lesstif2-dev doxygen latex2html


### Step 1:  install the external packages  (geant4, root, GSL,....)
you can skip this step, if you want to use external tools from afs or cvmfs - see below

**NB: you have to use a compiler that is compatible w/ c++11**
for SL6 you can use gcc4.8 provided by CERN SFT
see comment in release-versions.py on how to set this up 
```
ilcsoft_install_prefix = "/scratch/ilcsoft/"    
```
note: no version suffix is added to this path here as the external tools are rather independent of the ilcsoft version

possibly edit releases/v01-17-07/release-base.cfg and comment out any unneeded packages:
* e.g. those that are already installed on your system no need to comment out packages that are already installed in the correct place, ilcinstall will simply use them

run:
```
./ilcsoft-install releases/v01-17-07/release-base.cfg [-p]
```
check the output carefully w.r.t. to paths used, then install:
```
./ilcsoft-install releases/v01-17-07/release-base.cfg -i       
```

### Step 2:  install the actual ilcsoft release   

* no need to edit `releases/v01-17-07/release-versions.py` 
* assuming you have set `ilcsoft_install_prefix` already in Step 1
* Note: the release version will be automatically appended to the install path !


* if you have skipped Step 0 and want to use the external tools installed in afs or cvmfs:

* set the ilcPath accordingly (see below for pathes), e.g:
```
ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6
```
or
```
ilcPath = '/cvmfs/ilc.desy.de/sw/x86_64_gcc48_sl6
```

can be set to any other directory that contains all the needed external tools

* possibly edit releases/v01-17-07/release-ilcsoft.cfg and comment out any unneeded packages. Run:
```
./ilcsoft-install releases/v01-17-07/release-ilcsoft.cfg [-p]
```
check the output carefully w.r.t. to pathes used, then install:
```
./ilcsoft-install releases/v01-17-07/release-ilcsoft.cfg -i
```

## License and Copyright
Copyright (C), iLCInstall Authors

iLCInstall is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License long with this program.  If not, see <http://www.gnu.org/licenses/>.
