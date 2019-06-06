#Link to path in which postProcess_lib is stored.
import sys
import os
sys.path.insert(1,'/home/csunix/scdrw/Documents/nbudocuments/PhD/SimNumerics/Python/postProcessingLib')
import postProcess_lib as pp

# Chooses which postprocessing script to run.
# 0 - PseudoColourPlotting
# 1 - integrateDomain
# 2 - integratePlume

switch = 0

def pseudocolour():
        pp.PseudoColourPlotting( 'plume_v1_production',
        8,      # Order 
        3,      # Dimension
        1,      # Start file
        10,      # Jump
        2000,      # Final timestep
        1,      # Number of plots
        10,     # Elements in x
        10,     # Elements in y
        10,     # Elements in z
	0.0,	# Location of slice
        1,      # Particles (0 - no, 1 - yes)
        1       # Simulation currently running (0 - no, 1 - yes)
        )
        return

def integrateDomain():
        pp.integrateDomain( 'plume_v4_LES',
        7,      # Order
        3,      # Dimension
        10,     # Jump
        100,    # Final timestep
        12,     # Elements in x
        6,     # Elements in y
        3,     # Elements in z
        -2,     # x lower boundary
        2,      # x upper boundary
        0,      # y lower boundary
        2,      # y upper boundary
        0,      # z lower boundary
        1.0,    # z upper boundary
        0.9998,   # Clustering in x
        0.9998,   # Clustering in y
        0       # Particles (0 - no, 1 - yes)
        )
        return

def integratePlume():
        pp.integratePlume( 'plume_v4_qvol',
	'./',	# File location
        8,      # Order 
        3,      # Dimension
        1,      # Start file
        20,      # Jump
        2000,      # Final timestep
        2,      # Number of plots
        40,     # Elements in x
        40,     # Elements in y
        60,     # Elements in z
        )
        return

def average_field():
        pp.average_field('plume_v9_axi',
        7,      # Order 
        3,      # Dimension
        3000,      # Start file
        5,      # Jump
        7000,      # Final timestep
        8,      # Elements in x
        30,     # Elements in y
        8      # Elements in z
        )
        return

def TKE():
        pp.TKE('plume_v9_axi',
        7,      # Order 
        3,      # Dimension
        3000,      # Start file
        5,      # Jump
        6113,      # Final timestep
        8,      # Elements in x
        30,     # Elements in y
        8      # Elements in z
        )
        return

def scatterPlume():
        pp.scatterPlume( 'plume_v4_qvol',
        './',   # File location
        8,      # Order 
        3,      # Dimension
        1,      # Start file
        10,      # Jump
        2000,      # Final timestep
        2,      # Number of plots
        40,     # Elements in x
        40,     # Elements in y
        60,     # Elements in z
        )
        return


def choose_function(argument):
        switcher = {
                0: pseudocolour,
                1: integrateDomain,
                2: integratePlume,
                3: average_field,
                4: TKE,
		5: scatterPlume,
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument)

        return func()

choose_function(switch)

