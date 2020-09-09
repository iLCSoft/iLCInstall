
# Docker images for iLCSoft

## Generate official Docker images

This section is meant for helping iLCSoft maintainers to (re-)generate Docker images for different OS flavors, compiler version, iLCSoft version, etc...

### Standalone images

The images are produced on a three layer basis 

- **Layer 1**: The *env* image. This defines the OS, the compiler version to use for building the iLCSoft stack. For example: `Ubuntu 18.04` and `GCC 8.3`. They are normally not often re-generated.
- **Layer 2**: The *base* installation. This uses an *env* image as base image and compiles the iLCSoft "base" stack. The base stack contains only the common software like Geant4, ROOT that we don't often re-compile. 
- **Layer 3**: The *ilcsoft* installation. Based on a "base" installation (layer 2), it compiles a specific set of iLCSoft packages. The package versions in this image are changed for each new iLCSoft version, so more often than the base. If you want to pull a docker image and run ilcsoft (ddsim , Marlin, etc...) this is what you should use.

The directory `Dockerfiles` contains a series of Dockerfiles meant to generate these images.
When the Dockerfile name contains an OS flavor, it is meant to generate a layer 1 image.
Else two other files are provided, *Dockerfile.base* to build a "base" stack image and *Dockerfile.ilcsoft* to build the final ilcsoft stack image.

Each of the layer refers to the previous one in image build process. For example, to build a "base" stack image you need to specify which "env" image to use. Same for the "ilcsoft" stack image, you must specify which "base" image to build from.

Generating an *env* image:

```shell
cd Dockerfiles
# Example for Ubuntu 18.04 and gcc 8.3
docker build \
  --file Dockerfile.ubuntu18.04-gcc8.3 \
  --tag ilcsoft/env-ubuntu18.04-gcc8.3 \ # the output image name
  .
```

The tag in command line can be any name. The one chosen here just reflects the official used in our Dockerhub repository.

Generating a *base* image:
```shell
cd Dockerfiles
# Example for Ubuntu 18.04 and gcc 8.3
docker build \
  --file Dockerfile.base \
  --tag ilcsoft/base-ubuntu18.04-gcc8.3 \ # the output image name
  --build-arg image=env-ubuntu18.04-gcc8.3 \ # the layer 1 image name
  --build-arg compile_ncores=42 \  # the number of cores to use for compilation
  --build-arg ilcinstall_version=v02-01-00 \ # the iLCInstall branch or tag to use
  --build-arg install_mode=LASTEST \ # the installation mode, either LATEST or HEAD
  .
```

Generating the final *ilcsoft* image:
```shell
cd Dockerfiles
# Example for Ubuntu 18.04 and gcc 8.3
docker build \
  --file Dockerfile.ilcsoft \
  --tag ilcsoft/ilcsoft-ubuntu18.04-gcc8.3 \ # the output image name
  --build-arg image=base-ubuntu18.04-gcc8.3 \ # the layer 1 image name
  --build-arg compile_ncores=42 \  # the number of cores to use for compilation
  --build-arg ilcinstall_version=v02-01-00 \ # the iLCInstall branch or tag to use
  --build-arg install_mode=LASTEST \ # the installation mode, either LATEST or HEAD
  .
```

**For iLCSoft maintainers only:**

Once you have produced an image, you can push it to our official docker repository.

First login on dockerhub:

```shell
docker login
# ... will ask for your docker ID and password ...
```

Your login can be either your Docker ID or your Github username if you registered in Dockerhub with your Github account.

To push an image:

```shell
docker push image:tag
```

so, if you have generated the three image above, you can use:

```shell
docker push ilcsoft/env-ubuntu18.04-gcc8.3
docker push ilcsoft/base-ubuntu18.04-gcc8.3
docker push ilcsoft/ilcsoft-ubuntu18.04-gcc8.3
```

### CVMFS images

We also provide docker images that mounts CVMFS at startup. Having such images ensure that the compiled code of the iLCSoft installation on CVMFS are compatible with the OS.

For the time being, we provide images for:
- Scientific Linux 6 (sl6)

#### Image creation

To regenerate these images, simply do:

```shell
# for example for sl6
docker build --file Dockerfile.cvmfs.sl6 --tag ilcsoft/ilcsoft-cvmfs-sl6 .
```

#### Creating a container

To create a container, run:

```
docker run -it --privileged ilcsoft/ilcsoft-cvmfs
```

**IMPORTANT**: note the `--privileged` argument here which is required because CVMFS repositories mounting requires privileged containers.

Once the container is created, any iLCSoft release can be accessed in the usual location.
For example, for sl6:

```shell
# show all version directories
ls -d /cvmfs/ilc.desy.de/sw/x86_64_*_sl6/v*
```

For GCC 8.2, iLCSoft v02-02, initialize the software as:

```shell
source /cvmfs/ilc.desy.de/sw/x86_64_gcc82_sl6/v02-02/init_ilcsoft.sh
```
