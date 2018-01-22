simulation_name=plume

# Adds to path.

export PATH=/home/cserv1_a/soc_pg/scdrw/Documents/nbudocuments/PhD/Nek5000/bin:$PATH

# Re-compiles genbox.

rm ../../bin/genbox
cd ../../tools; ./maketools genbox
cd ../run/$simulation_name

