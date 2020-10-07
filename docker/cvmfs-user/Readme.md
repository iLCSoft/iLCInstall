
### CVMFS user images

We provide docker images that mounts CVMFS at startup. Having such images ensure that the compiled code of the iLCSoft installation on CVMFS are compatible with the OS.

For the time being, we provide images for:
- Scientific Linux 6: `ilcsoft/ilcsoft-cvmfs-sl6`
- Centos 7: `ilcsoft/ilcsoft-cvmfs-centos7`

#### Image creation

To regenerate these images, simply do:

```shell
# for example for sl6
docker build --file Dockerfile.cvmfs.sl6 --tag ilcsoft/ilcsoft-cvmfs-sl6 .
```

#### Pulling from Dockerhub

The CVMFS iLCSoft docker images are available at `hub.docker.com/u/ilcsoft`. For example, the sl6 image can be pulled using:

```shell
docker pull ilcsoft/ilcsoft-cvmfs-sl6
```

#### Creating a container

To create a container, run:

```shell
docker run -it --privileged ilcsoft/ilcsoft-cvmfs-sl6
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
