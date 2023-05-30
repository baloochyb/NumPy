import numpy as np
import matplotlib.pyplot as plt

a = np.arange(30)
b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"
print(b.shape)

x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x, y])
print(m)
xy = np.hstack([x, y])
print(xy)

rg = np.random.default_rng(1)
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = rg.normal(mu, sigma, 10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=True)       # matplotlib version (plot)
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n)
plt.show()
