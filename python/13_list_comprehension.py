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
# List comprehension is compact, easily readable, and significantly faster 
# than using a regular loop. 

# Say we want to generate a list of numbers from another list, where the each
# value in the new list is the square of the value in the original list.  Here
# is how we might do this using a standard for loop:

vals = [1, 2, 5, 7]
print(vals)

sq_vals = []
for v in vals:
	sq_vals.append(v**2)
print(sq_vals)

# Here is the same result using list comprehension:

sq_vals = [v**2 for v in vals]
print(sq_vals)

# List comprehension can be applied to any iterable object:

print([v/2 for v in range(10)])  # range object as iterable

print([tup for tup in enumerate(range(5,10))])          # enumerate object as iterable 
                                                        # and tuples as values
print([idx%3 + x for idx, x in enumerate(range(15))])   # enumerate object as iterable, 
                                                        # using separate idx,x values

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

# Here is the same result using list comprehension:

[x*y for x in v1 for y in v2]
#    ^^^^^^^^^^^ ^^^^^^^^^^^
#         |          ^ inner loop
#         ^--- outer loop

# Another example: flatten a 2-D array:

array = [[1,2,3], [4,5,6], [7,8,9]]
print(array)
flat_array = [val for row in array for val in row]
print(flat_array)


print()
print('List Comprehension with Conditionals:')
print('---------------------------------------')

# Conditional statements can be included, allowing entry into the new list based
# on an evaluation of the iterable value.

# Example: create a list of numbers between [1,100) that are evenly dividible by 3: 
div_by_three = [x for x in range(1,100) if x%3 == 0]
print(div_by_three)


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
Easy
1. Basic List Comprehension: Write a list comprehension to create a list of 
   squares of numbers from 1 to 10.
2. Filter Even Numbers: Use a list comprehension to create a list of even 
   numbers from 1 to 20.
3. String Lengths: Given a list of words ["apple", "banana", "cherry"], 
   use a list comprehension to create a list of their lengths.
4. Uppercase Conversion: Use a list comprehension to convert the list 
   ["hello", "world"] to ["HELLO", "WORLD"].

Medium
5. Conditional Filtering: Use a list comprehension to create a list of numbers 
   from 1 to 50 that are divisible by 5.
6. Extract Initials: Given a list of names use a list comprehension to extract 
   the first letter of each name: ['JJ', 'GW', 'GO'] given the list 
   ["James Joyce", "Gene Wolfe", "George Orwell"]
7. Flatten a Nested List: Given a nested list [[1, 2], [3, 4], [5, 6]], 
   use a list comprehension to create a flat list [1, 2, 3, 4, 5, 6].
8. Generate Pairs: Use a list comprehension to create a list of all pairs 
   (x, y) where x is from [1, 2, 3] and y is from [4, 5].
9. Replace Negative Numbers: Given a list numbers = [-5, 3, -1, 2], use a list 
   comprehension to create a new list where all negative numbers are replaced by 0.
   
Hard
10. Filter Words by Length: Given a list of words ["cat", "dog", "elephant", "fox"],
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
print(practice)







