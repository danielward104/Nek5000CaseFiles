# Runs Nek5000 simulation.

# The only bits you need to change.  The variable 'simulation_name' should be the same as all the files (.par, .usr, .box) and 'num_cores' is the number of cores on which to run the simulation.  Finally, 'mesh_tolerance' is as expected, a recommended value is 0.2.
simulation_name=plume_v1_production
num_cores=8
mesh_tolerance=0.05

# Makes a temporary file for use in piping into genmap.
{
echo $simulation_name
echo $mesh_tolerance
}  > temp.txt

# Runs genmap with a mesh tolerance defined above.
cat temp.txt | genmap

# Removes temporary files.
rm temp.txt

# Creates makefile for use in simulation.
makenek $simulation_name

# Runs simulation with number of cores defined above.
nekbmpi $simulation_name $num_cores #> simulation.out

#nice -n -15 nekbmpi $simulation_name $num_cores

# Converts files for use in 'visit', 'paraview' etc.
#visnek $simulation_name
