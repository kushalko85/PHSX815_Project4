# PHSX815_Project4
Estimation of Critical Temperature for Magnetic Phase Transitionusing 2D Ising model simulated by Monte Carlo MetropolisAlgorithm

## How to run the codes ?

 `python3 P4.py`
The estimation of the time required for each iteration of the simulation is also displayed. 
In its existing condition it generates the plots and runs 20 MC simulations for 20 by 20 lattice size and 40000 MC sweeps.

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
