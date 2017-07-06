import numpy as np #here we're importing the numpy package as np

"""
Numpy provides us with ndarrays which are objects that are similar to Python lists however they let have n-dimensions.
You can also perform mathematical operations with them.

We can use ndarrays to cover: scalars, vectors, matrices and tensors.

"""

#Creating a scalar in Numpy
s = np.array(5)
print(np.shape(s))

i = s + 3
print(i)
print(np.shape(i))

#Creating a vectors, here you pass a list
v = np.array([1,2,3])
print(np.shape(v))

print(v[1:]) #Here we're trying to access only the last two items of the one dimensional vector

#Creating a matrices, here you pass a list of lists
m = np.array([[1,2,3],[4,5,6],[6,7,8],[9,8,10]])
print(np.shape(m))

print(m[3][0]) #You get the number three in the matrices

#Creating a tensor
t = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(np.shape(t))

"""
Changing shapes of your arrays
"""

v = np.array([1,2,3,4])
print(np.shape(v))

x = v.reshape(1,4)
print(x)
print(np.shape(x))

"""
Special slicing of your array
"""
