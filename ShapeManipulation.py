import numpy as np
rg = np.random.default_rng(1) # create instance of default random number generator
a = np.floor(10 * rg.random((3, 4)))
print(a)
print(a.shape)

print(a.ravel) # returns the array, flattened
print(a.reshape(6, 2))
print(a.T)
a.resize(2, 6)
print(a)
print(a.reshape(3, -1))
