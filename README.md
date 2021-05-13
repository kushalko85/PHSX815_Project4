# PHSX815_Project4
Estimation of Critical Temperature for Magnetic Phase Transitionusing 2D Ising model simulated by Monte Carlo MetropolisAlgorithm

## How to run the codes ?
# Single program
 `python3 P4.py`
The estimation of the time required for each iteration of the simulation is also displayed. 
In its existing condition it generates the plots and runs 20 MC simulations for 20 by 20 lattice size and 100000 MC sweeps.

# In the write read format:
`python3 P4_write.py` will run the simulation shows plots for the E, M and Cv. Runs multiple loops and writes the Critical Temperatures in a txt file.

Then, `python3 Project4_read.py` will read Tcs from the txt file,  perform gaussian fit, calculate the p-value for the ttest and plot it.

## Requirements:
-numpy
-scipy
-matplotlib
-rich (pip install rich)
-numba

### Numba installation for mac

`python3 -m pip install  conda`

`python3 -m pip install  cytoolz`

`python3 -m conda config --add channels conda-forge`

`python3 -m  conda install -c numba numba`
