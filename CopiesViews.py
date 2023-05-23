import numpy as np

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
b = a
print(b is a) #No Copy at All and in a
print(id(a)) # id is a unique identifier of an object
print(id(b))
# Python passes mutable objects as references, so function calls make no copy.
"""
print(a)
print(b)
b = b.reshape((2, 6))
print(a)
print(b)
# b[0, 4] = 1234
b = 10
print(a)
print(b)
"""
c = a.view()
print(c is a) #No Copy at All and in a
print(id(a)) # id is a unique identifier of an object
print(id(c))
print(c.base)
print(a.base)
print(c.base is a)
print(c.flags.owndata)
print(a.flags.owndata)

c = c.reshape((2, 6))  # a's shape doesn't change
print(c.shape)
print(a.shape)
print(c)
c[0, 4] = 1234         # a's data changes
print(c)
print(a)

s = a[:, 1:3] # Slicing an array returns a view of it
s[:] = 10 # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
print(s)
print(a)
del s, c, b
print(a)

d = a.copy()  # a new array object with new data is created
print(d is a)
print(d.base is a)  # d doesn't share anything with a
d[0, 0] = 9999
print(a)

a = np.arange(int(1e8))
print(a)
b = a[:100].copy()
print(b)
del a
# If b = a[:100] is used instead, a is referenced by b and will persist in memory even if del a is executed.
