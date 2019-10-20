FROM ubuntu:18.04

# Possible image build arguments 
ARG COMPILE_NCORES=8
ARG ILCINSTALL_BRANCH=master
ARG ILCINSTALL_USER=iLCSoft
# LATEST or HEAD
ARG INSTALL_MODE=LASTEST
ARG DEBIAN_FRONTEND=noninteractive

# Perform the installation as root:
USER root
ENV HOME /home/ilc
WORKDIR ${HOME}
ENV ILCSOFT /home/ilc/ilcsoft

# epel-release must be installed before some other libraries
RUN apt-get -y update && \
    apt-get -y install \
    	    build-essential \
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

RUN git clone https://github.com/$ILCINSTALL_USER/iLCInstall.git --branch $ILCINSTALL_BRANCH

WORKDIR ${HOME}/iLCInstall

RUN ./ilcsoft-install -i --install-prefix ${ILCSOFT} -j $COMPILE_NCORES releases/$INSTALL_MODE/release-base.cfg

# Start the image with BASH by default
CMD ["/bin/bash"]