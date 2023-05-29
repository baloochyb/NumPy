import numpy as np
a = np.arange(12)**2  # the first 12 square numbers

i = np.array([1, 1, 3, 8, 5])  # an array of indices
print(a[i]) # the elements of `a` at the positions `i`
j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
print(a[j]) # the same shape as `j`

palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
print(palette[image])  # the (2, 4, 3) color image

a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
print(a[i, j]) # i and j must have equal shape
print(a[i, 2])
print(a[:, j])

l = (i, j) # equivalent to a[i, j]
a[l]

s = np.array([i, j])
print('s=', s)
print(s.shape)
v = tuple(s)
print('v=', v)
print(a[v])
print('#################################################')

time = np.linspace(20, 145, 5)  # time scale
print(time)
data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
ind = data.argmax(axis=0) # index of the maxima for each series
time_max = time[ind] # times corresponding to the maxima
print(time_max)
print(data.shape)
data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]...
print(np.all(data_max == data.max(axis=0)))

a = np.arange(5)
a[[1, 3, 4]] = 0
a[[0, 0, 2]] = [1, 2, 3]
a = np.arange(5)
a[[0, 0, 2]] += 1
print(a)
print('#################################################')

a = np.arange(12).reshape(3, 4)
b = a > 4 # `b` is a boolean with `a`'s shape
print(b)
print(a[b])  # 1d array with the selected elements
a[b] = 0  # All elements of `a` higher than 4 become 0
print('#################################################')

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])         # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection
print(a[b1, :]) # selecting rows | a[b1] is the same thing
print(a[:, b2]) # selecting columns
print(a[b1, b2])
print('#################################################')

a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax, bx, cx = np.ix_(a, b, c)
result = ax + bx * cx
print(result[3, 2, 4])
print(a[3] + b[2] * c[4])

def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity
    for v in vs:
        r = ufct(r, v)
    return r

print(ufunc_reduce(np.add, a, b, c))
