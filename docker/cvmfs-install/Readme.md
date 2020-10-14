

# CVMFS installation with docker images

CVMFS is one of the main deployment solution for the iLCSoft stack. CVMFS provides servers to software teams to install and publish their packages.
Setting up such servers requires some effort and are not always available for all OS flavors that are supported in the different labs.

Here at DESY, the main OSs that are supported are SL6 (end of life in November 2020), Centos7 and Ubuntu 18.04. Only one CVMFS server is available for our deployment. To be able to install the iLCSoft stack on all possible OS flavors, we provide Docker images for these OS flavors within which the iLCSoft stack is compiled and then deployed later on our CVMFS server.

As of today, the available images are:
- centos7: `ilcsoft/ilcsoft-cvmfs-install-centos7`

## Generating a docker image

The Dockerfiles available in this directory are meant for updating or re-generating images for a CVMFS deployment.
These images are generally already available on Dockerhub, so this step is not required.

If you need to create or re-generate an image, simply pickup a Dockerfile and e.g run:

```shell
# Build an image
docker build -f Dockerfile.cvmfs-install.centos7 --tag ilcsoft/ilcsoft-cvmfs-install-centos7 .
# Push the image on Dockerhub, if you have the permission dude!
docker push ilcsoft/ilcsoft-cvmfs-install-centos7
```

## Compiling the stack

For example here, we assume that you are using the centos7 image. The installation must be performed on a machine where the stack can be uploaded later on to the CVMFS server (using `rsync`, see below). At DESY, any NAF machine is suitable. Please, also ensure you have enough disk space before starting the installation. Depending on the machine, docker might or not be available. The NAF machines at DESY currently do not support `docker` but have `singularity` installed.

It is not possible to install directly the stack on CVMFS via the NAF machine, because CVMFS is read-only. It is also not possible to install the stack on any other location and then move directories because all paths will be wrongly hardcoded. The trick is to create a directory on your local machine (the NAF machine in our case) that will temporarily store the installation, but that actually points to the target CVMFS repository in the container.

Start by creating a local directory (remember, disk space..). At DESY, we have created a dedicated space on dust with a UNIX group (`ilc-cvmfs`) at `/nfs/dust/ilc/group/cvmfs_ilc` for all our installations.

The target CVMFS repository for our deployment is `/cvmfs/ilc.desy.de/`. For our example, the stack will be deployed in `/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7`. We need to mimic this path in our local directory. On `dust` you will then find the directory `/nfs/dust/ilc/group/cvmfs_ilc/sw/x86_64_gcc82_centos7`. This directory will be mounted in the container as `/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7`.

Also, the iLCSoft installation requires the `sft.cern.ch` CVMFS repository, mainly for compilers and corresponding python installation. This CVMFS repository will also be mounted in the container at startup.

With docker:

```shell
docker run -it \
    -v /cvmfs/sft.cern.ch:/cvmfs/sft.cern.ch \
    -v /nfs/dust/ilc/group/cvmfs_ilc/sw/x86_64_gcc82_centos7:/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7 \
    ilcsoft/ilcsoft-cvmfs-install-centos7
```

With singularity:

**IMPORTANT:** before running it the first time, create a home directory (not in *afs*) for using with this container, e.g:
```sh
mkdir -p /nfs/dust/ilc/user/$USER/singularity/homedir
```

```shell
# Mandatory step before running singularity - change to the
# home directory created above:
cd /nfs/dust/ilc/user/$USER/singularity/homedir

singularity shell -H $PWD \
    --bind /cvmfs/sft.cern.ch:/cvmfs/sft.cern.ch \
    --bind /nfs/dust/ilc/group/cvmfs_ilc/sw/x86_64_gcc82_centos7:/cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7 \
    docker://ilcsoft/ilcsoft-cvmfs-install-centos7
```

Inside the container, "git-clone" the `ILCInstall` package with your favorite version:

```shell
git clone https://github.com/iLCSoft/ILInstall.git --branch v02-02 # v02-02, only if v02-02 is your favorite version...
cd ILCInstall
```

Then, install the full stack:

```shell
# don't forget to initialize compiler, python, etc... from CERN CVMFS repo
source ./script/use_gcc82_cvmfs_el7.sh
# Install the base stack if needed
./ilcsoft-install -i -j 42 --install-prefix /cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7 releases/LATEST/release-base.cfg
# Install the ilcsoft specific stack
./ilcsoft-install -i -j 42 --install-prefix /cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7 releases/LATEST/release-ilcsoft.cfg
```

Don't forget to remove un-necessary build directories:

```shell
find /cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7 -type d -name build -exec rm -rf {} \;
# special commands for ROOT and geant4, if needed
rm -rf /cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/root/build-*
rm -rf /cvmfs/ilc.desy.de/sw/x86_64_gcc82_centos7/geant4/build-*
```

## CVMFS deployment

From your local (NAF) machine, log into the CVMFs server:

```shell
# requires permissions of course!
ssh  ilccv@ilc-cvmfs
```

Start a CVMFS transaction:

```shell
cvmfs_server transaction
```

And synchronize your (NAF) copy:

```shell
cd /cvmfs/ilc.desy.de/sw
# Only if the directory doesn't exists
mkdir x86_64_gcc82_centos7
# Synchronize directories, this takes a lot of time
# Make sure you grabbed a coffee before hitting the enter key!
# Replace <username> by your (NAF) local machine account and <local-machine> by the server name
# on which the files have been created
rsync -avz <username>@<local-machine>:/nfs/dust/ilc/group/cvmfs_ilc/sw/x86_64_gcc82_centos7 .
# Example: rsync -avz toto@naf-ilc.desy.de:/nfs/dust/ilc/group/cvmfs_ilc/sw/x86_64_gcc82_centos7 .
# Exit the /cvmfs/ilc.desy.de repository to finalize the transaction
cd $HOME
# Publish the new release.
# For a meaningful release name and commit message, you can list available tags:
cvmfs_server tag
# This takes even longer than rsync.
# Don't abuse with coffee: https://www.caffeineinformer.com/harmful-effects-of-caffeine
# You can go and annoy your colleagues for some time if you want instead
cvmfs_server publish -a release-name -m "Commit message"
```

**Congratulations!**

It's Friday, 10pm. You can wait for maybe 30 minutes for your new release to be visible on CVMFS or you can go home and recall yourself to have a social life.
