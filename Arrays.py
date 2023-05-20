import numpy as np

a = np.arange(15).reshape(3, 5)
b = np.array([6, 7, 8])
print("a = ", a)
print("b = ", b)
print("type a: ", type(a))
print("type b: ", type(b))
print("For a:")
# the number of axes (dimensions) of the array
print("number of axes: ", a.ndim)
# the dimensions of the array
print("dimension: ", a.shape)
# the total number of elements of the array
print("number of elements: ", a.size)
# the type of the elements in the array
print("type of the elements: ", a.dtype.name)
# the size in bytes of each element of the array
print("size in bytes: ", a.itemsize)
# the buffer containing the actual elements of the array
print("buffer: ", a.data)
# ---------------------------------------------------------
c1 = np.array([(1, 2, 3), (4, 5, 6)])
c2 = np.array([[1, 2, 3], [4, 5, 6]])
c3 = np.array(([1, 2, 3], [4, 5, 6]))
c4 = np.array(((1, 2, 3), [4, 5, 6]))
c5 = np.array(((1, 2, 3), (4, 5, 6)))
print(type(c1), c1)
print(type(c2), c2)
print(type(c3), c3)
print(type(c4), c4)
print(type(c5), c5)
# ---------------------------------------------------------
d1 = np.zeros([3, 4], dtype=int)
print(d1)
d2 = np.ones((3, 4), dtype=np.int16)
print(d2)
d3 = np.empty((3, 4))
print(d3)
# ---------------------------------------------------------
print(np.arange(10, 30, 5))
print(np.arange(0, 2, 0.3))
print(list(range(10, 30, 5)))
print(np.linspace(0, 2, 9))

# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)
# print(x)
# print(y)

print(np.arange(36).reshape(2, 3, 2, 3))
print(np.arange(10000).reshape(100, 100))

# import sys
# np.set_printoptions(threshold=sys.maxsize)
# print(np.arange(10000).reshape(100, 100))
