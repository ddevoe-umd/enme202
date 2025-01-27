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
print(t.index(2))


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """

Easy
1. Access Elements: Given the tuple numbers = (10, 20, 30, 40, 50), write a program to print the first element and the last element.
2. Tuple Length: Write a program to determine and print the length of the tuple colors = ("red", "green", "blue", "yellow").
3. Index of an Element: Find and print the index of "blue" in the tuple colors = ("red", "blue", "green").
4. Check Membership: Write a program to check if the string "apple" is in the tuple fruits = ("apple", "banana", "cherry").

Medium
5. Concatenate Tuples: Combine two tuples tuple1 = (1, 2, 3) and tuple2 = (4, 5, 6) and print the resulting tuple.
6. Tuple Slicing: Given the tuple letters = ("a", "b", "c", "d", "e"), extract and print the subtuple ("b", "c", "d").
7. Immutable Tuples: Try to change the second element of the tuple fruits = ("apple", "banana", "cherry") to "orange" and observe the error.
8. Nested Tuple Access: Access and print the value 4 from the nested tuple matrix = ((1, 2), (3, 4), (5, 6)).
9. Single-Element Tuple: Create a tuple with a single element "apple" and print its type to confirm it is a tuple.

Hard
10. Unpacking a Tuple: Given the tuple point = (4, 5), unpack its values into variables x and y in a single line of code.
11. Swap Values: Use tuple unpacking to swap the values of two variables, a = 10 and b = 20.
12. Tuple with Mixed Data Types: Create a tuple with mixed data types (e.g., ("hello", 42, 3.14)) and print each element by its position.
13. Reverse a Tuple: Reverse the tuple numbers = (1, 2, 3, 4, 5) using slicing.
14. Tuple Conversion: Convert the list numbers = [10, 20, 30] into a tuple.

"""
print(practice)



