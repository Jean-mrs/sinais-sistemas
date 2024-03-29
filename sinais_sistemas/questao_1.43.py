import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 5, 0.01)
fx = 10*np.exp(-t) - 5*np.exp(-.5*t)
plt.plot(t, fx)
plt.show()

gx = 10*np.exp(-t) + 5*np.exp(-0.5*t)
plt.plot(t, gx)
plt.show()