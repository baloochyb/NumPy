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

a = np.floor(10 * rg.random((2, 2)))
print(a)
b = np.floor(10 * rg.random((2, 2)))
print(b)
print(np.vstack((a, b)))
print(np.hstack((a, b)))

from numpy import newaxis
print(np.column_stack((a, b))) # with 2D arrays
a = np.array([4., 2.])
b = np.array([3., 8.])
print(np.column_stack((a, b))) # returns a 2D array
print(np.hstack((a, b))) # the result is different
print(a[:, newaxis]) # view `a` as a 2D column vector
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print(np.hstack((a[:, newaxis], b[:, newaxis]))) # the result is the same

print(np.column_stack is np.hstack)
print(np.row_stack is np.vstack)

print(np.r_[1:4, 0, 4]) # When used with arrays as arguments, r_ and c_ are similar to vstack and hstack in their default behavior

a = np.floor(10 * rg.random((2, 12)))
print(a)
print(np.hsplit(a, 3))
print(np.hsplit(a, (3, 5)))
