import numpy as np
import matplotlib.pyplot as plt

plt.plot(range(10000), np.random.random(10000), '.')
plt.savefig('random.png')
plt.show()
