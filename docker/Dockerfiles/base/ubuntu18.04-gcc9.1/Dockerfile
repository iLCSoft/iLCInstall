FROM ubuntu:18.04

# Possible image build arguments 
ARG COMPILE_NCORES=8
ARG ILCINSTALL_VERSION=master
ARG ILCINSTALL_USER=iLCSoft
# LATEST or HEAD
ARG INSTALL_MODE=LASTEST
ARG DEBIAN_FRONTEND=noninteractive

# Perform the installation as root:
USER root
ENV HOME /home/ilc
WORKDIR ${HOME}
ENV ILCSOFT /home/ilc/ilcsoft

# Add recent gcc compilers repo first
RUN apt-get install software-properties-common
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test

RUN apt-get -y update && \
    apt-get -y install \
    	    build-essential \
	    gcc-9 g++-9 \
	    openssl \
	    subversion \
	    doxygen \
	    texlive \
	    ghostscript \
	    texlive-latex-extra \
	    libssl-dev \
	    libsqlite-dev \
	    zlib1g-dev \
	    wget \
	    git \
	    tree \
	    libhdf5-dev \
	    jq \
	    libbz2-dev \
	    libgdbm-dev \
	    libx11-dev \
	    libxpm-dev \
	    libxft-dev \
	    libxmu-dev \
	    libxext-dev \
	    xlibmesa-glu-dev \
	    libglew-dev \
	    libftgl-dev \
	    libncurses-dev \
	    liblzma-dev \
	    libreadline-dev \
	    uuid uuid-dev \
	    libffi-dev \
	    bash-completion \
	    tk-dev \
	    libmysqlclient-dev \
	    libxml2-dev \
	    python-dev \
	    python-pip \
	    freeglut3-dev \
	    curl \
	    emacs

RUN apt-get clean

# Default compiler is gcc 7.4.0
# We need to switch to gcc 9.1.0
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-9 50 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 100 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 50 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 100 && \
    update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-9 50 && \
    update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-7 100 && \
    update-alternatives --set gcc /usr/bin/gcc-9 && \
    update-alternatives --set g++ /usr/bin/g++-9 && \
    update-alternatives --set cpp-bin /usr/bin/cpp-9

RUN wget http://lcgpackages.web.cern.ch/lcgpackages/tarFiles/sources/Python-2.7.15.tgz && \
    tar xvf Python-2.7.15.tgz && \
    cd Python-2.7.15 && \
    ./configure --prefix=$HOME/python --enable-ipv6 --enable-shared --enable-unicode=ucs4 CXX=/usr/bin/g++ CC=/usr/bin/gcc && \
    make install -j $COMPILE_NCORES && \
    export LD_LIBRARY_PATH=$HOME/python/lib:$LD_LIBRARY_PATH && \
    export PATH=$HOME/python/bin:$PATH && \
    cd $HOME && \
    rm -rf Python-2.7.15 Python-2.7.15.tgz

RUN git clone https://github.com/$ILCINSTALL_USER/iLCInstall.git --branch $ILCINSTALL_VERSION

WORKDIR ${HOME}/iLCInstall

RUN ./ilcsoft-install -i --install-prefix ${ILCSOFT} -j $COMPILE_NCORES releases/$INSTALL_MODE/release-base.cfg

# Start the image with BASH by default
CMD ["/bin/bash"]