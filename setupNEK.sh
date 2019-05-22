simulation_name=plume_v1_production

module add mpi/openmpi-x86_64

# Adds to path.

export PATH=/home/cserv1_a/soc_pg/scdrw/Documents/nbudocuments/PhD/Nek5000/bin:$PATH

# Re-compiles genbox.

rm ../../bin/genbox
cd ../../tools; ./maketools clean; ./maketools genmap; ./maketools genbox
cd ../run/$simulation_name

