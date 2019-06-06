simulation_name=geometry

module add mpi/openmpi-x86_64

# Adds to path.

export PATH=/home/cserv1_a/soc_pg/scdrw/Documents/nbudocuments/PhD/Nek5000/bin:$PATH

# Re-compiles genbox.

rm ../../bin/genbox
cd ../../tools; ./maketools clean; ./maketools all
cd ../run/$simulation_name

