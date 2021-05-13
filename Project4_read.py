import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
import matplotlib.mlab as mlab
#from numba import jit #optimization compiler
#import random
#import time
#from rich.progress import track


#reads txt file
def read_col(fname, col=0, convert=float, sep=None):
    with open(fname) as fobj:
        return [convert(line.split(sep=sep)[col]) for line in fobj]


T_c = read_col('T_c.txt')
print(T_c)





n, bins, patches = plt.hist(T_c,15, normed = True)
t, p = stats.ttest_1samp(T_c, 2.268)
#normfit
(mu, sigma) = norm.fit(T_c)
y = mlab.normpdf(bins, mu, sigma)
x = np.linspace(1.0, 3.0, 100)
y= stats.norm.pdf(x,mu,sigma)
l = plt.plot(x, y, 'r--', linewidth=2)
#plot
plt.title(r'$\mathrm{Histogram\ of\ T_c:}\ \mu=%.3f,\ \sigma=%.3f,\ p=%.3f$' %(mu, sigma, p))
plt.xlabel('Critical Temperature)')
plt.ylabel('relative probability')
plt.grid(True)
plt.show()


print(t)
print(p)


