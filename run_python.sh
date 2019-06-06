#!/bin/bash
# Job Name
#SBATCH -J run_postProcess.job
# Number of cores
#SBATCH -n 1
# Standard output written here
#SBATCH -o run_python.sh.o%j
# Standard error written here
#SBATCH -e run_python.sh.e%j
# Slurm partition - section on which to run job
#SBATCH -p compute
# Max wallclock time
#SBATCH --time=2-00:00:00

python postProcess.py
