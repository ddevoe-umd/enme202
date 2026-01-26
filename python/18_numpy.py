# Introduction to NumPy

"""
Topics
------
What is NumPy and Why Use It
Creating Arrays
Array Attributes
Indexing and Slicing
Array Operations and Broadcasting
Common Array Functions
Reshaping Arrays
"""

import numpy as np   # Standard convention for importing NumPy


print()
print('What is NumPy and Why Use It:')
print('---------------------------------------')

# NumPy (Numerical Python) is the fundamental package for scientific
# computing in Python. It provides support for large, multi-dimensional
# arrays and matrices, along with a collection of mathematical functions
# to operate on these arrays efficiently.

# Why use NumPy instead of Python lists?
#   -- Speed: NumPy arrays are stored more efficiently and operations
#      are implemented in C, making them much faster than Python lists.
#   -- Convenience: NumPy provides many built-in functions for mathematical
#      operations that would require loops with regular Python lists.
#   -- Memory efficiency: NumPy arrays use less memory than Python lists.

# Example: Compare adding two lists vs two NumPy arrays

# Using Python lists (requires a loop or list comprehension)
list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]
list_sum = [a + b for a, b in zip(list_a, list_b)]
print("List sum:", list_sum)

# Using NumPy arrays (element-wise operation is automatic)
arr_a = np.array([1, 2, 3, 4, 5])
arr_b = np.array([10, 20, 30, 40, 50])
arr_sum = arr_a + arr_b
print("Array sum:", arr_sum)



print()
print('Creating Arrays:')
print('---------------------------------------')

# ---------------
# np.array()
# ---------------

# The most common way to create an array is from a Python list:

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D array:", arr_1d)

# Create a 2D array (matrix) from nested lists:
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D array:\n", arr_2d)

# ---------------
# np.zeros() and np.ones()
# ---------------

# Create arrays filled with zeros or ones:
zeros_arr = np.zeros(5)           # 1D array of 5 zeros
print("Zeros:", zeros_arr)

ones_arr = np.ones((2, 3))        # 2D array of ones (2 rows, 3 columns)
print("Ones:\n", ones_arr)

# ---------------
# np.arange()
# ---------------

# Create an array with evenly spaced values (similar to Python's range())
# Syntax: np.arange(start, stop, step)

range_arr = np.arange(0, 10, 2)   # Start at 0, stop before 10, step by 2
print("Arange:", range_arr)

# ---------------
# np.linspace()
# ---------------

# Create an array with a specified number of evenly spaced values
# Syntax: np.linspace(start, stop, num)

linspace_arr = np.linspace(0, 1, 5)   # 5 values from 0 to 1 (inclusive)
print("Linspace:", linspace_arr)

# ---------------
# np.eye()
# ---------------

# Create an identity matrix (1s on diagonal, 0s elsewhere):
identity = np.eye(3)
print("Identity matrix:\n", identity)

# ---------------
# np.random
# ---------------

# Create arrays with random values:
rand_arr = np.random.rand(3)          # 3 random values between 0 and 1
print("Random (uniform):", rand_arr)

randn_arr = np.random.randn(3)        # 3 random values from standard normal distribution
print("Random (normal):", randn_arr)

randint_arr = np.random.randint(1, 10, 5)  # 5 random integers from 1 to 9
print("Random integers:", randint_arr)



print()
print('Array Attributes:')
print('---------------------------------------')

# NumPy arrays have several useful attributes that describe their structure:

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Array:\n", arr)
print("Shape (rows, cols):", arr.shape)    # Dimensions of the array
print("Number of dimensions:", arr.ndim)   # Number of axes
print("Size (total elements):", arr.size)  # Total number of elements
print("Data type:", arr.dtype)             # Data type of elements

# You can specify the data type when creating an array:
float_arr = np.array([1, 2, 3], dtype=float)
print("Float array:", float_arr)
print("Float array dtype:", float_arr.dtype)



print()
print('Indexing and Slicing:')
print('---------------------------------------')

# ---------------
# 1D Array Indexing
# ---------------

arr_1d = np.array([10, 20, 30, 40, 50])

print("Original 1D array:", arr_1d)
print("First element (index 0):", arr_1d[0])
print("Last element (index -1):", arr_1d[-1])
print("Slice [1:4]:", arr_1d[1:4])        # Elements at indices 1, 2, 3

# ---------------
# 2D Array Indexing
# ---------------

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nOriginal 2D array:\n", arr_2d)

# Access a single element: arr[row, col]
print("Element at row 0, col 2:", arr_2d[0, 2])
print("Element at row 1, col 1:", arr_2d[1, 1])

# Access an entire row or column
print("Row 0:", arr_2d[0, :])             # All columns of row 0
print("Column 1:", arr_2d[:, 1])          # All rows of column 1

# Slice a subarray
print("Subarray (rows 0-1, cols 1-2):\n", arr_2d[0:2, 1:3])

# ---------------
# Boolean Indexing
# ---------------

# Select elements based on a condition:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nOriginal array:", arr)

# Create a boolean mask
mask = arr > 5
print("Boolean mask (arr > 5):", mask)

# Use the mask to select elements
print("Elements > 5:", arr[mask])

# This can also be done in one step:
print("Elements > 5:", arr[arr > 5])
print("Even elements:", arr[arr % 2 == 0])



print()
print('Array Operations and Broadcasting:')
print('---------------------------------------')

# ---------------
# Element-wise Operations
# ---------------

# Arithmetic operations are applied element-by-element:

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("a:", a)
print("b:", b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)      # Element-wise multiplication (NOT matrix multiplication)
print("a / b:", a / b)
print("a ** 2:", a ** 2)

# ---------------
# Broadcasting
# ---------------

# Broadcasting allows NumPy to perform operations on arrays of different shapes.
# When operating on two arrays, NumPy compares their shapes and automatically
# "broadcasts" the smaller array to match the larger one.

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Scalar broadcasting: operation applied to every element
print("\nOriginal array:\n", arr)
print("Array + 10:\n", arr + 10)
print("Array * 2:\n", arr * 2)

# Array broadcasting: a 1D array is broadcast across rows
row_vector = np.array([100, 200, 300])
print("Row vector:", row_vector)
print("Array + row_vector:\n", arr + row_vector)

# ---------------
# Matrix Operations
# ---------------

# For true matrix multiplication, use @ operator or np.dot():
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("A @ B (matrix multiplication):\n", A @ B)
print("A * B (element-wise multiplication):\n", A * B)



print()
print('Common Array Functions:')
print('---------------------------------------')

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:\n", arr)

# ---------------
# Aggregation Functions
# ---------------

print("\nAggregation functions:")
print("Sum of all elements:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# These functions can also operate along a specific axis:
print("\nSum along axis 0 (columns):", np.sum(arr, axis=0))
print("Sum along axis 1 (rows):", np.sum(arr, axis=1))
print("Mean along axis 0:", np.mean(arr, axis=0))

# ---------------
# Mathematical Functions
# ---------------

x = np.array([0, np.pi/4, np.pi/2, np.pi])

print("\nx:", x)
print("sin(x):", np.sin(x))
print("cos(x):", np.cos(x))

y = np.array([1, 10, 100])
print("\ny:", y)
print("log(y):", np.log(y))        # Natural log
print("log10(y):", np.log10(y))    # Base-10 log
print("exp(y):", np.exp(y))        # e^y
print("sqrt(y):", np.sqrt(y))      # Square root

# ---------------
# Finding Indices
# ---------------

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print("\nArray:", arr)
print("Index of max value:", np.argmax(arr))
print("Index of min value:", np.argmin(arr))
print("Sorted indices:", np.argsort(arr))

# np.where() returns indices where a condition is True
indices = np.where(arr > 4)
print("Indices where arr > 4:", indices[0])



print()
print('Reshaping Arrays:')
print('---------------------------------------')

# ---------------
# reshape()
# ---------------

# Change the shape of an array (total elements must remain the same):
arr = np.arange(12)
print("Original array:", arr)
print("Shape:", arr.shape)

reshaped = arr.reshape(3, 4)    # Reshape to 3 rows, 4 columns
print("\nReshaped to (3, 4):\n", reshaped)

reshaped = arr.reshape(2, 6)    # Reshape to 2 rows, 6 columns
print("Reshaped to (2, 6):\n", reshaped)

# Use -1 to let NumPy calculate one dimension automatically:
reshaped = arr.reshape(4, -1)   # 4 rows, columns calculated automatically
print("Reshaped to (4, -1):\n", reshaped)

# ---------------
# flatten() and ravel()
# ---------------

# Convert a multi-dimensional array to 1D:
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\n2D array:\n", arr_2d)
print("Flattened:", arr_2d.flatten())

# ---------------
# Transpose
# ---------------

# Swap rows and columns:
print("\nTranspose:\n", arr_2d.T)

# ---------------
# Concatenation
# ---------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\na:", a)
print("b:", b)
print("Concatenate:", np.concatenate([a, b]))

# For 2D arrays, specify axis:
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print("\nVertical stack (axis=0):\n", np.concatenate([arr1, arr2], axis=0))
print("Horizontal stack (axis=1):\n", np.concatenate([arr1, arr2], axis=1))


"""
PRACTICE PROBLEMS

Easy
1. Create Array: Create a 1D NumPy array containing the integers from 1 to 10.
2. Basic Operations: Create two arrays [1, 2, 3] and [4, 5, 6]. Add them together
   and multiply them element-wise.
3. Array Attributes: Create a 3x4 array of zeros. Print its shape, size, and dtype.
4. Indexing: Given arr = np.array([10, 20, 30, 40, 50]), extract the last 3 elements.

Medium
5. Boolean Indexing: Create an array of integers from 1 to 20. Extract all values
   that are divisible by 3.
6. Statistics: Create a 4x4 array of random integers between 1 and 100. Calculate
   the mean of each row and the sum of each column.
7. Reshaping: Create an array of 24 consecutive integers starting from 1. Reshape
   it into a 4x6 array, then into a 2x3x4 array.
8. Broadcasting: Create a 3x3 array of ones. Add the vector [10, 20, 30] to each
   row of the array.
9. Linspace: Use np.linspace to create an array of 100 evenly spaced values between
   0 and 2*pi. Calculate the sine of each value.

Hard
10. Matrix Operations: Create two 3x3 matrices with random integers. Perform matrix
    multiplication and verify the result has the correct shape.
11. Masking: Create a 5x5 array of random integers between 1 and 50. Replace all
    values greater than 25 with -1.
12. Sorting: Create a 2D array with 3 rows and 4 columns of random integers. Sort
    each row independently, then sort each column independently.
13. Finding Values: Create an array of 20 random integers between 1 and 100. Find
    the indices of the 3 largest values.
14. Combining Arrays: Create three 2x2 arrays. Stack them vertically into a 6x2
    array, then horizontally into a 2x6 array.
15. Simulation: Use NumPy to simulate rolling two dice 10,000 times. Calculate the
    probability of getting a sum of 7.
"""
