# Tuples

""" 
Topics
------
Tuple Declaration
Indexing and Slicing Tuples
Converting Tuples to Lists
Copying Tuples
Deleting Tuples
Tuple Methods
"""

# Tuples are similar to lists, but they are _immutable_.  Once a tuple
# has been defined, the values in the tuple cannot be changed.  As a
# result, there are no add, insert, or remove methods for tuples. 

print()
print('Tuple Declaration')
print('---------------------------------------')

# Declare an empty tuple (rarely used, but can serve as a placeholder)
empty = ()

# Declare a tuple with a single value by following the value with a comma
# (it is not sufficient to enclose a single value in parentheses)
one_val = ('foo',)

# Declare a tuple with 2+ values
t = (4, 6.5, 'bar', False, 2+4j)
print(f'Tuple: {t}')
print(f'Number of elements: {len(t)}')


print()
print('Indexing and Slicing Tuples')
print('---------------------------------------')

# Indexing and slicing is identical for tuples and lists, with the
# exception that we cannot slice into a tuple to change values 
# since they are immutable

print(t[0])
print(t[:4])
print(t[0:2:2])


print()
print('in')
print('---------------------------------------')

# The _in_ keyword operates just as for lists.
is_in_tuple = "bar" in t          # True
is_in_tuple = "ba" in t           # False
is_in_tuple = 2+4j in t           # True


print()
print('Converting Tuples to Lists')
print('---------------------------------------')

# A tuple can be converted to a list using the list() function, which
# returns a new list containing the values in the tuple (in the same order).
# The original tuple is not modified by the function.

t_as_list = list(t)
print(t_as_list)


print()
print('Copying Tuples')
print('---------------------------------------')

# There is no copy() method for tuples. We can assign a tuple to
# another variable, but this also does not copy the tuple (it
# simply makes a new variable name pointing to the same block of
# memory). Since tuples are immutable, there is no point in ever
# making a copy!


print()
print('Joining tuples')
print('---------------------------------------')

# The addition operator will return a new tuple combining the
# elements in the tuples used in the operation
t1 = ('this', 'that')
t2 = ('these', 'those')
t3 = t1 + t2
print(t3)

print()
print('Deleting Tuples')
print('---------------------------------------')

# Individual tuple elements cannot be deleted, but an entire
# tuple can be deleted
del t3    # remove the tuple from memory


print()
print('Tuple Methods')
print('---------------------------------------')

# The few available tuple methods work the same way as for lists

# count(val)
# Count the number of occurences of val in tuple
t = (5, 2, 6, 8, 5, 5, 2, 0)
print(t.count(5))   

# index(val)
# Return the first index of tuple element with value equal to val
print(t.index(6))


"""
PRACTICE PROBLEMS

1. Immutable Tuples: Try to change the second element of the tuple fruits = ("apple", "banana", "cherry")
   to "orange" and observe the error.
2. Single-Element Tuple: Create a tuple with a single value "x", and print its type to confirm it is a tuple.
3. Given the tuple point = (4, 5), use "iterable unpacking" to assign the tuple values to variables 
   x and y in a single line of code (google "iterable unpacking" if you don't know how to do this).
4. Convert the tuple n = (10, 20, 30) into a list.
5. Convert the list n = [1, 2, 3] into a tuple.

"""



