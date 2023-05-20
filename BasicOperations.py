import numpy as np
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10*a)
print(a < 35)
# -------------------------------------------
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
print(A * B) # elementwise product
print(A @ B) # matrix product
print(A.dot(B)) # another matrix product

rg = np.random.default_rng(1) # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)
b += a
print(b)

a = np.arange(6)
print(a)
print(a.sum(), a.min(), a.max())

b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0)) # sum of each column
print(b.min(axis=1)) # min of each row
print(b.cumsum(axis=1)) # cumulative sum along each row
