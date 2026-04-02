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
Polynomial Functions
Linear Algebra (np.linalg)
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
#      are implemented in C / C++, making them much faster than Python lists.
#   -- Convenience: NumPy provides many built-in functions for mathematical
#      operations that would require loops with regular Python lists.
#   -- Memory efficiency: NumPy arrays use less memory than Python lists.

# Example: Compare adding two lists vs two NumPy arrays

# Using Python lists (requires a loop or list comprehension)
list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]
list_sum = [a + b for a, b in zip(list_a, list_b)]
print("List sum:", list_sum)

# Using NumPy arrays (element-wise operation is   )
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
print("range:", range_arr)

# ---------------
# np.linspace()
# ---------------

# Create an array with a specified number of evenly spaced values
# Syntax: np.linspace(start, stop, num_vals)

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
rand_arr = np.random.rand(3)          # 3 random floats in [0,1] uniform distribution
print("Random (uniform):", rand_arr)

randn_arr = np.random.randn(3)        # 3 random floats in [0,1] normal distribution
print("Random (normal):", randn_arr)

randint_arr = np.random.randint(1, 10, 5)  # 5 random ints in [1,9] uniform distribution
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

# Same syntax as lists

arr_1d = np.array([10, 20, 30, 40, 50])

print("Original 1D array:", arr_1d)
print("First element (index 0):", arr_1d[0])
print("Last element (index -1):", arr_1d[-1])
print("Slice [1:4]:", arr_1d[1:4])        # Elements at indices 1, 2, 3

# ---------------
# 2D Array Indexing
# ---------------

# ++Different++ syntax than list indexing and slicing!

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nOriginal 2D array:\n", arr_2d)

# Access a single element: arr[row, col]
print("Element at row 0, col 2:", arr_2d[0, 2])
print("Element at row 1, col 1:", arr_2d[1, 1])

# Slice an entire row or column
print("Row 0:", arr_2d[0, :])             # All columns of row 0
print("Column 1:", arr_2d[:, 1])          # All rows of column 1

# Rows can also be indexed using a single value:
print("Row 1:", arr_2d[1])                # Row 1

# Slice a subarray
print("Subarray (rows 0-1, cols 1-2):\n", arr_2d[0:2, 1:3])


# ---------------
# Boolean Indexing
# ---------------

# Boolean indexing is a powerful technique to pull out values from an 
# array based on conditional values.

# Comparison operators apply to each element of a numpy array, yielding
# a new array with boolean values:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = arr > 5
print("Boolean mask (arr > 5):", mask)

# Use the mask to select elements from an array
print("Elements > 5:", arr[mask])

# This can also be done in one step:
print("Elements > 5:", arr[arr > 5])
print("Even elements:", arr[arr % 2 == 0])

# More complex boolean masks can be created using bitwise operators, which
# (like comparison ops) are applied element-by-element:
mask = (arr>1) & (arr<6) | (arr%3==False)
print(arr[mask])

# Can apply numpy functions when creating masks:
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
mask = np.abs(y) > 0.9     # use a numpy function with comparison
print(y)
print(y[mask])

# Boolean masks can also be used to assign new values to selected 
# array elements:
arr[arr%2==True] = 0   # assign 0 to all even elements
print("Even values set to zero:", arr)


print()
print('Array Operations:')
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

column_vector = np.array([[100], [200], [300]])
print("Column vector:", column_vector)
print("Array + column_vector:\n", arr + column_vector)


# ---------------
# Matrix Operations
# ---------------

print()
print('Common Array Functions:')
print('---------------------------------------')

# ---------------
# Aggregation Functions: sum, mean, std, min, max
# ---------------

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

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

# Regular Python math functions can't operate with numpy arrays,
# so use the equivalent numpy functions instead:

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

# np.argmax(), argmin(), argsort():
print("\nArray:", arr)
print("Index of max value:", np.argmax(arr))   # 1st occurence only
print("Index of min value:", np.argmin(arr))   # 1st occurence only
print("Sorted indices:", np.argsort(arr))      # sort min --> max

# np.where() returns indices where a condition is True
indices = np.where(arr > 4)
print("Indices where arr > 4:", indices[0])

# For N-dimensional arrays np.where() returns N tuples of matched indices 
# where confition is True.



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
# flatten()
# ---------------

# Convert a multi-dimensional array to 1D:
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\n2D array:\n", arr_2d)
print("Flattened:", arr_2d.flatten())


# ---------------
# Transpose (T)
# ---------------

# Swap rows and columns:
print("\nTranspose:\n", arr_2d.T)q

# Transpose only works on 2d arrays (not 1d). Need to start with a 2d array
# defned using double-brackets:
row_vector = np.array([[1,2,3]])   # note double brackets
row_vector.T

# Alternately, use reshape to convert 1d array to 2d vector:
row_vector = np.array([1,2,3])
print("Row vector:\n", row_vector)
column_vector = row_vector.reshape(-1, 1)    # transform to 2d column vector
print("Column vector\n", column_vector)



# ---------------
# concatenate()
# ---------------

# Concatenate combines arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\na:", a)
print("b:", b)
print("Concatenate:", np.concatenate([a, b]))

# For 2D arrays, specify axis:
arr1 = np.array([[1, 2], 
                 [3, 4]])
arr2 = np.array([[5, 6], 
                 [7, 8]])

print("\nVertical stack (axis=0):\n", np.concatenate([arr1, arr2], axis=0))
print("Horizontal stack (axis=1):\n", np.concatenate([arr1, arr2], axis=1))



print()
print('Polynomial Functions:')
print('---------------------------------------')

# NumPy represents polynomials as arrays of coefficients, ordered from
# the highest degree to the lowest (constant term last).
# For example, 2x^3 - 5x^2 + 3x - 7 is represented as [2, -5, 3, -7].

# ---------------
# np.polyval()
# ---------------

# Evaluate a polynomial at specific x values:
# p(x) = 2x^3 - 5x^2 + 3x - 7

coeffs = [2, -5, 3, -7]

print("Polynomial: 2x^3 - 5x^2 + 3x - 7")
print("p(0) =", np.polyval(coeffs, 0))       # Evaluate at x = 0
print("p(1) =", np.polyval(coeffs, 1))       # Evaluate at x = 1
print("p(2) =", np.polyval(coeffs, 2))       # Evaluate at x = 2

# Evaluate at multiple x values at once using an array:
x_vals = np.array([0, 1, 2, 3, 4])
print("p(x) for x = 0..4:", np.polyval(coeffs, x_vals))

# ---------------
# np.roots()
# ---------------

# Find the roots (values of x where p(x) = 0):
# p(x) = x^2 - 5x + 6  -->  factors as (x-2)(x-3)

coeffs_quad = [1, -5, 6]
r = np.roots(coeffs_quad)
print("\nPolynomial: x^2 - 5x + 6")
print("Roots:", r)               # Should be 3.0 and 2.0

# Roots can be complex numbers:
# p(x) = x^2 + 1  -->  roots are ±i
coeffs_complex = [1, 0, 1]
r_complex = np.roots(coeffs_complex)
print("\nPolynomial: x^2 + 1")
print("Roots:", r_complex)       # Should be 0+1j and 0-1j

# ---------------
# np.poly()
# ---------------

# Construct polynomial coefficients from known roots (inverse of np.roots):
# If the roots are 2 and 3, the polynomial is (x-2)(x-3) = x^2 - 5x + 6

r = [2, 3]       # roots
p = np.poly(r)   # polynomial from roots
print("\nPolynomial from roots [2, 3]:", p)    # [1, -5, 6]

r = [1, -1, 4]
p = np.poly(r)
print("Polynomial from roots [1, -1, 4]:", p)

# poly() will always create a +monic+ polynomial (coefficient on highest
# power of x will be unity):

p = [1, 5, 1]
np.poly(np.roots(p)) == p    # True since initial polynomial is monic

p = [2, 5, 1]
np.poly(np.roots(p)) == p    # False since initial polynomial not monic
2*np.poly(np.roots(p)) == p  # True (with 2x scaling applied)


# ---------------
# np.polyder()
# ---------------

# Compute the derivative of a polynomial:
# p(x) = 3x^3 + 2x^2 - x + 5
# p'(x) = 9x^2 + 4x - 1

coeffs_cubic = [3, 2, -1, 5]
deriv = np.polyder(coeffs_cubic)
print("Derivative coefficients:", deriv)       # [9, 4, -1]

# Higher-order derivatives (pass the order as the second argument):
deriv2 = np.polyder(coeffs_cubic, 2)
print("Second derivative:", deriv2)            # [18, 4]

# ---------------
# np.polyint()
# ---------------

# Compute the integral of a polynomial:
# p(x) = 9x^2 + 4x - 1
# ∫p(x)dx = 3x^3 + 2x^2 - x + C

p = [9, 4, -1]
integral = np.polyint(p)
print("Integral coefficients:", integral)      # [3, 2, -1, 0]  (C = 0 by default)

# ---------------
# np.polyadd(), np.polysub(), np.polymul()
# ---------------

# Arithmetic with polynomials:
p1 = [1, 2, 3]     # x^2 + 2x + 3
p2 = [4, 5]         # 4x + 5

print("\np1 = x^2 + 2x + 3")
print("p2 = 4x + 5")
print("p1 + p2:", np.polyadd(p1, p2))     # x^2 + 6x + 8
print("p1 - p2:", np.polysub(p1, p2))     # x^2 - 2x - 2
print("p1 * p2:", np.polymul(p1, p2))     # 4x^3 + 13x^2 + 22x + 15

# We could instead have used numpy arrays to represent the polynomials instead of
# lists, and applied normal arithmetic operators.

# ---------------
# np.polyfit()
# ---------------

# Fit a polynomial to data points (least-squares fit):

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1, 2.1, 8.9, 27.2, 64.1, 125.3])

# Fit a 3rd-degree polynomial to the data:
fit_coeffs = np.polyfit(x_data, y_data, 3)
print("\nData x:", x_data)
print("Data y:", y_data)
print("Best-fit cubic coefficients:", np.round(fit_coeffs, 2))

# Evaluate the fitted polynomial at the original x values:
y_fit = np.polyval(fit_coeffs, x_data)
print("Fitted values:", np.round(y_fit, 2))


print()
print('Linear Algebra (np.linalg):')
print('---------------------------------------')

# NumPy's linalg submodule provides standard linear algebra operations
# commonly used in engineering and science.

# ---------------
# Matrix Multiplication
# ---------------

# For true matrix multiplication (vs. element-wise mult), use @ operator
# or np.dot():
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("A @ B (matrix multiplication):\n", A @ B)
print("A * B (element-wise multiplication):\n", A * B)

# ---------------
# np.eye() — Identity Matrix
# ---------------

# np.eye() creates an identity matrix (1s on the diagonal, 0s elsewhere).
# This is defined at the top level of NumPy, not inside linalg.

I = np.eye(3)
print("3x3 Identity matrix:\n", I)

# A useful property: any matrix times the identity equals itself
A = np.array([[2, 1, 0],
              [3, 5, 2],
              [1, 0, 4]])

print("\nA:\n", A)
print("A @ I (should equal A):\n", A @ I)

# ---------------
# np.linalg.det() — Determinant
# ---------------

# The determinant is a scalar value that describes certain properties of a
# matrix. A matrix with a determinant of 0 is called singular (non-invertible).

print("\ndet(A):", np.linalg.det(A))

# Determinant of the identity matrix is always 1:
print("det(I):", np.linalg.det(I))

# A singular matrix has determinant 0:
singular = np.array([[1, 2],
                     [2, 4]])
print("det(singular):", np.linalg.det(singular))

# ---------------
# np.linalg.inv() — Matrix Inverse
# ---------------

# The inverse of a matrix A is the matrix A_inv such that A @ A_inv = I.
# Only square, non-singular matrices have an inverse.

A_inv = np.linalg.inv(A)
print("\nA:\n", A)
print("A inverse:\n", np.round(A_inv, 4))

# Verify: A @ A_inv should give the identity matrix
product = A @ A_inv
print("A @ A_inv (should be identity):\n", np.round(product, 10))

# ---------------
# np.linalg.solve() — Solve Linear Systems
# ---------------

# Solve the system of equations Ax = b for x.
# This is more efficient and numerically stable than computing x = A_inv @ b.

# Example system:
#   2x + 1y + 0z = 5
#   3x + 5y + 2z = 15
#   1x + 0y + 4z = 8

b = np.array([5, 15, 8])
x = np.linalg.solve(A, b)
print("\nSolving Ax = b")
print("b:", b)
print("Solution x:", np.round(x, 4))

# Verify: A @ x should equal b
print("A @ x (should equal b):", np.round(A @ x, 10))

# ---------------
# np.linalg.eig() — Eigenvalues and Eigenvectors
# ---------------

# Eigenvalues (lambda) and eigenvectors (v) satisfy: A @ v = lambda * v.
# eig() returns a tuple of (eigenvalues_array, eigenvectors_matrix).

M = np.array([[4, 2],
              [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(M)
print("\nMatrix M:\n", M)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors (as columns):\n", eigenvectors)

# Verify first eigenvalue/eigenvector pair: A @ v = lambda * v
v0 = eigenvectors[:, 0]
print("\nVerification: M @ v0 =", M @ v0)
print("lambda0 * v0 =", eigenvalues[0] * v0)

# ---------------
# np.linalg.norm() — Vector and Matrix Norms
# ---------------

# The norm measures the "size" or "length" of a vector or matrix.

v = np.array([3, 4])
print("\nVector:", v)
print("L2 norm (Euclidean length):", np.linalg.norm(v))        # sqrt(3^2 + 4^2) = 5
print("L1 norm (Manhattan distance):", np.linalg.norm(v, 1))   # |3| + |4| = 7

v3d = np.array([1, 2, 2])
print("\n3D Vector:", v3d)
print("L2 norm:", np.linalg.norm(v3d))     # sqrt(1 + 4 + 4) = 3

# ---------------
# np.transpose() / .T — Transpose
# ---------------

# Transpose swaps rows and columns. For a matrix A, (A^T)_ij = A_ji.
# We saw .T earlier; np.linalg operations often use it.

B = np.array([[1, 2, 3],
              [4, 5, 6]])

print("\nB (2x3):\n", B)
print("B transposed (3x2):\n", B.T)

# A useful property: (A @ B)^T = B^T @ A^T
C = np.array([[1, 0],
              [2, 1],
              [0, 3]])

print("(B @ C)^T:\n", (B @ C).T)
print("C^T @ B^T:\n", C.T @ B.T)


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
16. Polynomial Roots: Define the polynomial p(x) = x^3 - 6x^2 + 11x - 6. Find its
    roots, and verify by evaluating p(x) at each root (results should be ~0).
17. Curve Fitting: Generate noisy data from y = 2x^2 - 3x + 1 by evaluating at
    x = np.linspace(0, 5, 20) and adding random noise with np.random.randn. Use
    np.polyfit to recover the original coefficients.
18. Derivatives: Define p(x) = x^4 - 4x^3 + 6x^2 - 4x + 1. Compute its first and
    second derivatives. Find the roots of the first derivative to locate the critical
    points.
19. Inverse Verification: Create a random 4x4 matrix using np.random.randint. Compute
    its inverse and verify that A @ A_inv is approximately the identity matrix.
20. Linear System: Solve the system:  3x + 2y - z = 1,  2x - 2y + 4z = -2,
    -x + 0.5y - z = 0.  Verify by substituting the solution back into A @ x.
21. Eigenvalues: Create a 3x3 symmetric matrix (hint: A = B + B^T for any B).
    Compute its eigenvalues and verify they are all real numbers.
"""
