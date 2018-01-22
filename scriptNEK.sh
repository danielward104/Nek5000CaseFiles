# Runs Nek5000 simulation.

# The only bits you need to change.  The variable 'simulation_name' should be the same as all the files (.par, .usr, .box) and 'num_cores' is the number of cores on which to run the simulation.  Finally, 'mesh_tolerance' is as expected, a recommended value is 0.2.
simulation_name=plume
num_cores=6
mesh_tolerance=0.2

# Pipes the simulation into genbox to build the mesh.
echo $simulation_name.box | genbox

# Renames files created by genbox such that they're used for the simulation.
mv ./box.re2 ./$simulation_name.re2
mv ./box.tmp ./$simulation_name.tmp

# Makes a temporary file for use in piping into genmap.
{
echo $simulation_name
echo $mesh_tolerance
}  > temp.txt

# Creates makefile for use in simulation.
makenek $simulation_name

# Runs genmap with a mesh tolerance defined above.
cat temp.txt | genmap

# Removes temporary file.
rm temp.txt

# Runs simulation with number of cores defined above.
nekbmpi $simulation_name $num_cores #> simulation.out

# Converts files for use in 'visit', 'paraview' etc.
#visnek $simulation_name
