# List Comprehension

""" 
Topics
------
List Comprehension Basics
List Comprehension with Multiple Iterables
List Comprehension with Conditionals
"""


print()
print('List Comprehension Basics:')
print('---------------------------------------')

# List comprehension is a compact syntax to create a list from any iterable sequence
# using the following syntax:
#
#    [i for i in iterable]
#
# List comprehension is compact, easily readable, and **significantly faster**
# than using a regular loop. 

# Say we want to generate a list of numbers from another list, where the each
# value in the new list is the square of the value in the original list.  Here
# is how we might do this using a standard for loop:

vals = [1, 2, 5, 7]

sq_vals = []
for v in vals:
    sq_vals.append(v**2)
print(sq_vals)

# Here is the same result using list comprehension:

sq_vals = [v**2 for v in vals]
print(sq_vals)

# From the Zen of Python: “Flat is better than nested”!

# List comprehension can be applied to any iterable object:

new_list_1 = [v/2 for v in range(10)] 

new_list_2 = [tup for tup in enumerate(range(10))]

new_list_3 = [idx%3 + x for idx, x in enumerate(range(10))] 

new_list_4 = [k.upper() for k in {'a':1, 'b':2}]

# The concept of list comprehension can also be applied to dictionaries,
# as seen below. Note how zip is required in this case to generate paired
# keys and values for the dictionary:

new_dict = {key: value for key, value in zip(['a','b','c'], range(3))}


print()
print('List Comprehension with Multiple Iterables:')
print('---------------------------------------')

# List comprehension can use more than one iterable to yield functionality
# identical to nested loops.  Consider the following nested loop designed
# to yield the cross-product of two vectors v1 and v2:

v1 = [2, 4, 8]
v2 = [4, 3, -9]
result = []
for x in v1:
    for y in v2:
        result.append(x*y)

# An aside: the result is a 1D list (rather than a 2D matrix, which is what the cross
# product should yield).  Can you think of a way to modify this code to yield
# the desired 2D data structure?

# Here is the same 1D result using list comprehension:

[x*y for x in v1 for y in v2]
#    ^^^^^^^^^^^ ^^^^^^^^^^^
#         |          ^ inner loop
#         ^--- outer loop

# Another example: flatten a 2-D array:

array = [[1,2,3], [4,5,6], [7,8,9]]
print(array)
flat_array = [val for row in array for val in row]
print(flat_array)


# Another way to work with multiple lists is using zip() (recall that zip()
# "packages" paired values from each list as tuples):

added_lists = [x+y for x,y in zip(v1, v2)]
print(added_lists)


print()
print('List Comprehension with Conditionals:')
print('---------------------------------------')

# Conditional statements can be included, allowing entry into the new list based
# on an evaluation of the iterable value.

# Case 1: use an _if_ condition to filter elements from iterable. In this case the
# _if_ statement is placed *after* the iterable.
#
# Example: create a list of numbers in [1,99] that are evenly divisible by 3: 

div_by_three = [x for x in range(1,100) if x%3 == 0]
print(div_by_three)

# Case 2: Don't filter the iterable, but use _if/else_ condition to decide
# what to do with each value. In this case the _if/else_ statements are
# placed *before* the iterable.

div_by_three = [x if x%3 == 0 else '.' for x in range(1,100)]
print(div_by_three)

# Do you see the difference? In the first case, the iterable list was filtered
# to ignore values that did not meet the _if_ condition. In the second case,
# all values from the iterable were included, but the _if/else_  condition
# allowed us to decide what to do with each value.

# Conditionals can also be nested in list comprehension. Here is an example that
# tests each list element for divisibility by different values, with different 
# entries in the final list depending on the result of each conditional:

values = list(range(1,50))  
result = [int(n/2) if n % 2 == 0 else int(n/3) if n % 3 == 0 else 'non-integer' for n in values]  
print(result)  

# Finally, conditionals can be used to both filter the iterable and decide how to process
# individual values in the same list comprehension statement:

div_by_three = [x if x%3 == 0 else '.' for x in range(1,100) if math.sin(x)>0.5]
print(div_by_three)


"""
PRACTICE PROBLEMS

1. Basic List Comprehension: Write a list comprehension to create a list of 
   squares of numbers from 1 to 10.
2. Filter Even Numbers: Use list comprehension to create a list of even 
   numbers from 1 to 20.
3. String Lengths: Given a list of words ["apple", "banana", "cherry"], 
   use a list comprehension to create a list of their lengths.
4. Uppercase Conversion: Use a list comprehension to convert the list 
   ["hello", "world"] to ["HELLO", "WORLD"].
5. Names to list: Given a list of names, use list comprehension to create a new
   list with each element being another list with 2 elements given by the first and
   last names: [["James","Joyce"], ["Gene","Wolfe"], ["George,Orwell"]] given the list 
   ["James Joyce", "Gene Wolfe", "George Orwell"]
6. Extract Initials: Given a list of names, use list comprehension to extract 
   the first letter of each name: ['JJ', 'GW', 'GO'] given the list 
   ["James Joyce", "Gene Wolfe", "George Orwell"]
7. Flatten a Nested List: Given a nested list [[1, 2], [3, 4], [5, 6]], 
   use a list comprehension to create a flat list [1, 2, 3, 4, 5, 6].
8. Generate Pairs: Use a list comprehension to create a list of all pairs 
   (x, y) where x is from [1, 2, 3] and y is from [4, 5].
9. Replace Negative Numbers: Given a list numbers = [-5, 3, -1, 2], use a list 
   comprehension to create a new list where all negative numbers are replaced by 0.
10. Filter Words by Length: Given a list of words ["cat", "dog", "elephant", "frog"],
    use a list comprehension to create a new list containing only the words with 
    more than three letters.
11. Find Common Elements: Given two lists list1 = [1, 2, 3, 4] and 
    list2 = [3, 4, 5, 6], use a list comprehension to create a list of their 
    common elements.
12. Dictionary from Lists: Given two lists keys = ["a", "b", "c"] and 
    values = [1, 2, 3], use a list comprehension to create a dictionary 
    {"a": 1, "b": 2, "c": 3}.
13. Transpose a Matrix: Given a matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]], use 
    list comprehension to transpose it (convert rows to columns).
14. Extract Digits: Use a list comprehension to extract all the digits from a 
    string, e.g., "a1b2c3" → [1, 2, 3].
15. Prime Numbers: Use a list comprehension to generate a list of all prime 
    numbers between 2 and 50. (Hint: Use nested comprehensions or a helper 
    function for the primality check.)
"""






