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
