import numpy as np
import matplotlib.pyplot as plt
from numba import jit #optimization compiler
import random
import time
from rich.progress import track #estimating time it takes to run the code

# parameters 

H = 0; # Magnetic field
L = 20; # Lattice size (L * L)
s = np.random.choice([1,-1],size=(L,L)) # initialize random spin
n = 100 * L**2 # no. of MC sweeps
#n = 100000
Temperature = np.arange(1.0,3.00,0.01) # temperature range that includes critical temperature
  

#Energy calculations 
#simply the sum of interactions between spins divided by the total number of spins

#Magnetization of the configuration is the sum of all spins divided by the total number of spins

# interaction energy between spins assuming periodic boundaries is simply the difference in energy due to flipping spin i,j

@jit(nopython=True, cache=True)
def val_E(s):
    E = 0
    for i in range(L):
        for j in range(L):
            E += -dE(s,i,j)/2
    return E/L**2



@jit(nopython=True, cache=True)
def val_M(s):
    m = np.abs(s.sum())
    return m/L**2



@jit(nopython=True, cache=True)
def dE(s,i,j): # change in energy function
    #top
    if i == 0:
        t = s[L-1,j]  # boundary condition on the top part
    else:
        t = s[i-1,j]
    #bottom
    if i == L-1:
        b = s[0,j]
    else:
        b = s[i+1,j]
    #left
    if j == 0:
        l = s[i,L-1]
    else:
        l = s[i,j-1]
    #right
    if j == L-1:
        r = s[i,0]
    else:
        r = s[i,j+1]
    return 2*s[i,j]*(b+t+l+r) 

# MC sweep
@jit(nopython=True, cache=True) 
def mc(s,Temp,n):   
    for m in range(n):
        i = random.randrange(L) 
        j = random.randrange(L)  
        e_diff = dE(s,i,j)
        if e_diff <= 0: # change in energy is negative
            s[i,j] = -s[i,j]  #flip spin
        elif random.random() < np.exp(-e_diff/Temp): 
            s[i,j] = -s[i,j]
    return s

# physical quantities
@jit(nopython=True, cache=True)
def quantities(s,T,n):
    En = 0
    En2 = 0
    Mg = 0
    Mg2 = 0
    for p in range(n):
        s = mc(s,T,1)
        E = val_E(s)
        M = val_M(s)
        En += E
        Mg += M
        En2 += E*E
        Mg2 += M*M
    En_avg = En/n
    Mag = Mg/n
    Cv = (En2/n-(En/n)**2)/(T**2)
    return En_avg, Mag, Cv


Mag = np.zeros(len(Temperature))
En_avg = np.zeros(len(Temperature))
Cv = np.zeros(len(Temperature))

start = time.time()

for ind, T in enumerate(track(Temperature)):
    # Sweeps spins
    s = mc(s,T,n)
    En_avg[ind], Mag[ind], Cv[ind] = quantities(s,T,n)
end = time.time()
time = (end - start)/60




#plots
plt.plot(Temperature, En_avg, marker='.', linestyle = "None")
plt.xlabel("Temperature (T)", fontsize=14);
plt.ylabel("Energy ", fontsize=14);         #plt.axis('tight');
plt.show()


plt.plot(Temperature, abs(Mag), marker='.', linestyle = "None")
plt.xlabel("Temperature (T)", fontsize=14); 
plt.ylabel("Magnetization ", fontsize=14);   #plt.axis('tight');
plt.show()


plt.plot(Temperature, Cv, marker='.' , linestyle = "None")
plt.xlabel("Temperature (T)", fontsize=14);  
plt.ylabel("Specific Heat ", fontsize=14);   #plt.axis('tight');
plt.show()

#################################

print(Cv)

k=0

for k in range(len(Cv)):
    if (np.isclose(Cv[k],max(Cv),atol=0.001)):
        print(Cv[k],max(Cv),T[k],k)
    
