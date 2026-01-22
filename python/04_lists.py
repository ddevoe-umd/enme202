# Lists

""" 
Topics
------
List Declaration
Indexing and Slicing Lists
Copying Lists
Other List Methods
"""


"""
Lists are an essential data structure in Python, allowing the coder
to reference multiple values with a single variable name.

Lists are _heterogeneous_, _ordered_, and _mutable_:
    - Heterogeneous structures can contain multiple different 
      data types (both elemental types such as ints, float, strings,
      and structured data types such as other lists)
    - In an ordered data structure, the sequence of values within
      the structure is fixed
    - Values stored in a mutable data structure may be changed at
      any time.
"""

print()
print('List Declaration')
print('---------------------------------------')

# Declare an empty list using list()
empty = list()

# Add some elements to the empty list using append(), which places each new
# value at the end of the list:
empty.append('foo')   # first element
empty.append('bar')
empty.append('123')
empty.append(123)
empty.append(32.86)
empty.append(3<1)     # last element
print(empty)

# Declare a list by directly assigning values
fruits = ['banana', 'orange', 'grape', 'blueberry', 'lemon', 'peach', 'lime']

# Print the list and it's length using len()
print(f'Fruits: {fruits}')
print(f'Number of fruits: {len(fruits)}')

# Lists are heterogeneous:
stuff = ['string', 3.1415, 10, 2+4j, ['list', 'in', 'list']]
print(f'Stuff: {stuff}')
print(f'Elements in stuff: {len(stuff)}')


print()
print('Indexing and Slicing Lists')
print('---------------------------------------')

# Indexing lists is the same as with strings, recalling that
# the first element has an index value of 0, and that we can
# index backwards from the end of the list using negative values
fruits = ['banana', 'orange', 'grape', 'blueberry', 'lemon', 'peach', 'lime']
print(fruits[0])      # banana
print(fruits[1])      # orange
print(fruits[-1])     # lime
print(fruits[-2])     # peach

# Slicing is also the same as with strings, recalling that
# the slicing indices have the format [start : end+1], and that
# we can omit the start or end values if desired
print(fruits[0:2])
print(fruits[:2])
print(fruits[3:5])
print(fruits[3:])
print(fruits[-4:])

# Slicing with steps
print(fruits[1:6:2])
print(fruits[2::2])
print(fruits[::2])

# Becauase lists are mutable (and strings are not) we can direclty
# modify indexed values
fruits[0] = 'tangerine'
print(fruits)

# Modify multiple values with slicing
fruits[1:3] = ['kiwi', 'pineapple']
print(fruits)

# Modify multiple values with stepped slicing
fruits[::3] = ['cherry', 'cranberry', 'apricot']



print()
print('in')
print('---------------------------------------')

# The _in_ keyword can be used to check if a value is present 
# in a sequence (list, string, and others we will learn about).
# The syntax "value in list" returns True if the value is in
# the list, otherwise False.
is_in_fruits = "carrot" in fruits       # False
is_in_fruits = "blueberry" in fruits    # True

val = 6
is_in_number_list = val in [2,4,6]
is_less_than_five = val in range(6)



print()
print('Copying Lists')
print('---------------------------------------')

# Copy a list using the assignment operator
x = [5, 8, 13, 4, 9]
y = x
print(x)
print(y)

# ok, it looks like we have made a copy. Now change a value in
# one list, and display both lists again
y[0] = -1
print(x)
print(y)
id(x) == id(y)        # shallow copy (same memory address)

# Uh oh...what happened? Changing one list also changed the other.
# This is because the assignment y = x simply makes both x and y
# point to the same location in memory where the original list was
# stored. As a result, changing a value in either list modifies
# the same memory location. This is called a "shallow copy".
#
# To prevent a shallow copy, use the copy() method
x = [5, 8, 13, 4, 9]
y = x.copy()
y[0] = -1
print(x)
print(y)
id(x) == id(y)        # deep copy (different memory address)

# Warning: if the list contains another list as an element, copy() 
# will yield a shallow copy of the internal list!  To avoid this,
# there is another function called deepcopy() that is part of the
# _copy_ module, which must be manually imported into the code.
# We will not cover the use of deepcopy() in ENME202, but be aware
# of this issue for the future.


print()
print('Other List Methods')
print('---------------------------------------')

# We have already seen how the append() and copy() methods work.
# Here let's consider some other useful list methods.

# insert(idx, val)
# Insert a single value into the list at index = idx
fruits.insert(2, 'apple')
print(fruits) 

# You might want to insert multiple values into the list using the
# following syntax, but this will instead insert a single element 
# given by the 2-element list
fruits.insert(3, ['guava', 'fig'])
print(fruits)

# remove(val)
# Remove the first occurance of val from the list
fruits.remove('banana')
print(fruits)
fruits.remove(['guava', 'fig'])
print(fruits)

# pop(idx=0)
# Remove a single value at index idx, and return the value (if no
# argument is given the index defaults to 0)
x = fruits.pop()
print(x)
print(fruits)
y = fruits.pop(2)
print(y)
print(fruits)

# clear()
# Remove all elements from a list, yielding an empty list
fruits.clear()     
print(fruits)       # []

# del index[slice]
# Delete one or more elements from a list
fruits = ['banana', 'orange', 'grape', 'blueberry', 'lemon', 'peach', 'lime']
del fruits[0]     
print(fruits)

del fruits[1:3]     # remove elements at index 1 and 2
print(fruits)

del fruits          # remove entire list from memory and delete the list name

# extend(newlist)
# Add newlist to the end of list (nothing is returned)
even = [0, 2, 4, 6, 8]
odd =  [1, 3, 5, 7, 9]
even.extend(odd)
print(even)

# we can also join lists using the addition operator, just as we did
# with strings, returing a new list
neg = [-1, -2, -3, -4, -5]
vals = odd + neg
print(vals)

# count(val)
# Count the number of occurences of val in list
print(even.count(6))   
print(fruits.count('grape'))

# index(val)
# Return the first index of list element with value equal to val
print(even.index(2))
print(fruits.index('orange'))

# reverse()
# Reverse the order of the list sequence (nothing is returned)
print(fruits)  
fruits.reverse()
print(fruits)  

# sort(reverse=False, key_function)
# Sort the list in ascending order based on the numerical value (numbers)
# or length (strings) of the elements. The order can be changed to
# descending by passing True as a first argument. The sort rule can
# be defined by the user by passing a sorting function as a second
# argument (we will cover functions shortly). Nothing is returned.
print(fruits)
fruits.sort()
print(fruits)

print(even) 
even.sort(reverse=True)
print(even) 

# Note that there is also a sorted() function available that will return a 
# sorted list without modifying the original list.


"""
PRACTICE PROBLEMS

Easy
1. Given the list n = [10, 20, 30, 40, 50], write code to print the first element and the last element.
2. Print the number of elements in the list from problem 1.
3. Change the second element of the list from problem 1 to "apple".
4. Concatenate list1 = [1, 2, 3] and list2 = [4, 5, 6] into a single list.

Medium
Given letters = ["a", "b", "c", "d", "e"], do the following:
5. Slicing: extract ["b", "c", "d"] as a new list.
6. Check Membership: Write a program to check if "x" is in the original list.
7. Append Element: Add the string "z" to the original list so that it is the 3rd element in the new list.
8. Remove Element: Remove the element "b" from the original list.
9. Find the index of "d" in the original list.

Hard
Given v = [[1, 2, 5], [3, [0, 4, 0]], [5, 6]]:
10. Nested List Access: Print "4" by indexing into v.
11. Create a deep copy of v assigned to a new variable v_copy.
12. Replace [5,6] in v with a new value of -1.
13. Reverse the order of the elements in v.
14. Find Maximum: display the largest value in the list n = [10, 50, 20, 40].

"""


