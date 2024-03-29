# -*- coding: utf-8 -*-
"""numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hS4R7MyZ43VAoLf65QE8hbht3wQdcUO7

**NumPy (Numerical Python)**


*   Efficient storage and manipulation of numerical arrays is absolutely fundamental to the process of doing data science.
*   Numy is a specialized tool for handling such numerical arrays.


*   NumPy arrays are like Python's built-in list type, but NumPy arrays provide much more efficient storage and data operations as the arrays grow larger in size.

*   NumPy arrays form the core of nearly the entire ecosystem of data science tools in
Python.
*   Thus, learning NumPy to use it effectively will be valuable no matter what aspect of
data science interests you.

**Import Numpy**
"""

import numpy

"""But, by convention, most of the people in Python data science world will import numpy as
np as an alias.
"""

import numpy as np

"""**Numpy Version**"""

np.__version__

"""**Creating Arrays from Python Lists**"""

#integer array:
np.array([2,4,6,8])

"""Remember that, NumPy arrays contain the same type of data. If does not match, it will
upcast if possible.
"""

# Upcast to floating point array:
np.array([2.5, 4, 6.7, 8, 10])

# Explicitly set the datatype using `dtype` keyword.
np.array([2, 4, 6, 8, 10], dtype = 'float32')

"""**Creating Arrays from Scratch**

Especially for larger arrays, it is more efficient to create arrays from scratch using
routines built into NumPy.
"""

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=np.int16)

# Create a length-10 floating point array filled with zeros
np.zeros(10, dtype=np.int64) # float64 is default size for float of this

# Create a 3x4 floating-point array filled with ones
np.ones((3,4), dtype=np.int64) # int64 is default size for int of this system (

# Create a 3x4 array filled with 2.1416
np.full((3,4), 2.1416)

# Create an array filled with a linear sequence
# using np.arange(start, end, step)
# (this is similar to the built-in range() function)
np.arange(0,20,2)

# Create an array of five values evenly spaced between 0 and 1
np.linspace(0,1,5)

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3,3))

# Create a 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
np.random.normal(0,1,(3,3))

# Create a 3x3 array of random integers in the interval [0, 10)
np.random.randint(0,10,(3,3))

# Create a 5x5 identity matrix
np.eye(5)

# Create an uninitialized array of five integers
# The values will be whatever happens to already exist at that memory location
np.empty(5)

"""**NumPy Array Attributes**"""

# seed for reproducibility
# Ensure that the same random arrays are generated each time this code is run
np.random.seed(0)

x1= np.random.randint(10, size=6) #one dimentional array
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

x1 # One-dimensional array

x2 # Two-dimensional array

x3 # Three-dimensional array

# Example of NumPy array attributes
print("x3 ndim: ", x3.ndim) #ndim (the number of dimensions)
print("x3 shape: ", x2.shape) #shape (the size of each dimension)
print("x3 size: ", x3.size) #size (the total size of the array)
print("x3 dtype: ", x3.dtype) #data type of the array 
print("x3 itemsize:", x3.itemsize, "bytes") # size (in bytes) of each array element
print("x3 nbytes:", x3.nbytes, "bytes") # total size (in bytes) of the array

"""In general, we expect that nbytes is equal to itemsize times size .

**Array Indexing**

In a one-dimensional array, the ith value (counting from zero) can be accessed by
specifying the desired index in square brackets, just as with Python lists.
"""

x1

x1[0] # first element

x1[-1] # Negative indxing, last element

"""In a multi-dimensional array, items can be accessed using a comma-separated tuple of
indices.
"""

x2

x2[0,0] # first row, first column

x2[2, -1] # 3rd row, last index

"""Values can also be modified using any of the above index notation."""

x2[1, -1] = 9
x2

"""But remember that, unlike Python lists, NumPy arrays have a fixed type. This means, for
example, that if you attempt to insert a floating-point value to an integer array, the value
will be silently truncated. Don't be caught unaware by this behavior!
"""

x1[0] = 2.1416 # this will be truncated!
x1

"""
**Array Slicing**

The NumPy slicing syntax follows that of the standard Python list.
array_name[start:stop:step]
If any of these are unspecified, they default to the values start=0 , stop=size of
dimension , step=1 ."""

x = np.arange(10)
x

x[:5] # first five elements

x[5:] # elements from index 5

x[3:7] # sub-array from index 3 to 7

x[::2] # starting from 0 and step is 2

x[1::2] # starting from 1 and step is 2

"""A potentially confusing case is when the step value is negative. In this case, the
defaults for start and stop are swapped. This becomes a convenient way to reverse
an array.
"""

x[::-1] # all elements, reversed

x

x[5::-2] # reversed every other from index 5

"""Multi-dimensional slices work in the same way, with multiple slices separated by
commas.
"""

x2

x2[:2, :3] # two rows, three columns

x2[::-1, ::-1] # reversed

"""**Accessing array rows and columns**

One commonly needed routine is accessing of single rows or columns of an array. This
can be done by combining indexing and slicing, using an empty slice marked by a single
colon (:).
"""

x2

print(x2[:, 0]) # first column of x2

print(x2[0, :]) # first row of x2

"""In the case of row access, the empty slice can be omitted for a more compact syntax."""

print(x2[0]) # equivalent to x2[0, :]

"""**Subarrays as no-copy views**

NumPy array slicing differs from Python list slicing:


*   in lists, slices will be copies, and
*   in NumPy array slices return views.




"""

print(x2)

# extract a 2×2 subarray from x2 array
x2_sub = x2[:2, :2]
print(x2_sub)

# modify x2_sub subarray
x2_sub[0, 0] = 88
print(x2_sub)

"""This default behavior is useful when we work with large datasets, we can access and
process pieces of these datasets without the need to copy the underlying data buffer.

**Creating copies of arrays**

 

*   copy() method can be used to copy an array or subarray.
*   In this case if we now modify this new array or subarray, the original array is not touched/changd.



"""

x2 # original array

# copy a subarray
x2_sub_copy = x2[:2, :2].copy()
print(x2_sub_copy)

# now, modify the subarray
x2_sub_copy[0, 0] = 44
print(x2_sub_copy)

# original array x2 is not touched
print(x2)

"""
**Reshaping of Arrays**


*   Using reshape() method
*   Size of the initial array must match the size of the reshaped array



"""

# 3×3
grid = np.arange(1, 10).reshape((3,3))
print(grid)

x = np.array([1, 2, 3])
x

# row vector via reshape
x.reshape((1, 3))

# column vector via reshape
x.reshape((3, 1))

"""**Array Concatenation**

Concatenation, or joining of two arrays in NumPy, is primarily accomplished using
np.concatenate , np.vstack , and np.hstack .
"""

# Using concatenate() method
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

# More than two arrays at once
z = [99, 99, 99]
np.concatenate([x, y, z])

# concatenate two dimentional array
grid = np.array([[1, 2, 3],
[4, 5, 6]])
# concatenate along the first axis
np.concatenate([grid, grid])

# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis=1)

"""For working with arrays of mixed dimensions, it can be clearer to use the np.vstack
(vertical stack) and np.hstack (horizontal stack) functions.
"""

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
[6, 5, 4]])
# vertically stack the arrays
np.vstack([x, grid])

# horizontally stack the arrays
y = np.array([[99],
[99]])
np.hstack([grid, y])

"""**Array Splitting**


*   The opposite of concatenation is splitting, which is implemented using np.split , np.hsplit , and np.vsplit functions.
*  For each of these, we can pass a list of indices giving the split points



"""

x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print(x1, x2, x3)

"""Notice that N split-points, leads to N + 1 subarrays. The related functions
np.hsplit and np.vsplit are similar.
"""

grid = np.arange(16).reshape((4, 4))
grid

upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)

left, right = np.hsplit(grid, [2])
print(left)
print(right)

"""**Iterating Over NumPy Array**

NumPy contains an iterator object numpy.nditer , which is an efficient
multidimensional iterator object to iterate over an array.
"""

arr = np.arange(1, 10).reshape((3,3))
arr

# iterating the array, arr, using numpy.nditer()
for i in np.nditer(arr):
  print(i)