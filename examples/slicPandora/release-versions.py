###########################################
#
# iLCSoft versions for release v01-16
#
# F.Gaede, DESY 09.12.2011
#
###########################################


# --------- ilcsoft release version ------------------------------------------
ilcsoft_release = "v00-00"
# ----------------------------------------------------------------------------


# --------- install dir ------------------------------------------------------
ilcsoft_install_prefix = "/scratch/$USER/slicPandora/"

#ilcsoft_install_prefix = "/u1/projects/slic/"
#ilcsoft_install_prefix = ilcsoft_afs_path[ arch ]
#ilcsoft_install_prefix = "/scratch/gaede/ilcsoft/"
#ilcsoft_install_prefix = "/scratch/rosem/ilcsoft/"

#ilcsoft_install_dir = os.path.join( ilcsoft_install_prefix, ilcsoft_release )
# ----------------------------------------------------------------------------

# --------- ilcsoft home -----------------------------------------------------
# python variable for referring the ILC Home directory
# used to link or use already installed packages (SL4 or SL5)
# no need to set this variable if using SL4 or SL5 with access to /afs/desy.de/
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc44_sl6'
#ilcPath = '/afs/desy.de/project/ilcsoft/sw/x86_64_gcc41_sl5'
#ilcPath = ilcsoft_afs_path[ arch ]
#fg? ilcPath = ilcsoft_install_prefix
# ----------------------------------------------------------------------------

# ======================= PACKAGE VERSIONS ===================================

# ----- java ---------------------------------------------------------
#Java_version = "1.6.0"
Java_version = "1.7.0"
#Java_path = ilcPath + "/java/" + Java_version # comment out to try auto-detect
#Java_path = "/usr/"
Java_path = "/u1/apps/jdk1.7.0_17/"

LCIO_version = "v02-03-03"

ILCUTIL_version = "v01-00"

CMake_version = "2.8.5"

PandoraPFANew_version = "v00-11"

SlicPandora_version = "HEAD"

# versions for dummy install of Marlin 
Marlin_version = "HEAD"
GEAR_version = "v01-03"
CLHEP_version = "2.1.3.1"
LCCD_version = "v01-02-01"