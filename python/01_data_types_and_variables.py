# Python Data Types and Variables

""" 
Topics
------
Elemental data types
Variables and the assignment operator
User Input
"""

print()
print('Elemental data types: int, float, complex, bool, str')
print('---------------------------------------')

# Python supports 3 built-in numerical data types. We can view the type
# of any value using the built-in type() function:

print(type(4))       # integer (int)
print(type(5.27))    # floating point (float)
print(type(5 + 8j))  # complex value (complex)

# We won't work with complex values in Python, but some of the functionality
# is similar to Matlab (e.g. finding the magnitude, real part, or 
# imaginary part of a complex vector).

# Python is a ++strongly-typed++ language (intermingling of different 
# variable types is restricted), but numerical values can be 
# mixed together:

print(4 + 5.27 + (5+8j))    # yields (14.27+8j)

# Python is also a ++dynamically-typed++ language: the value type is determined 
# by context (type declarations are generally not required). 

# Unlike C-family languages, numerical data types have infinite precision!
# We don't need to worry about limits to the maximum values that can be
# represented by these data types.

# Python also supports several non-numerical data types:

print(type(True))                  # boolean (bool)
print(type('this is a string'))    # string (str)
print(type('a'))                   # single characters are also strings

# What if we want a string that contains a single quote character (')?

print("this isn't not a string")

# Alternatively, use a backslash as an _escape character_ that forces the
# next character to be included in the _string literal_:

print('that wasn\'t good grammar')

# The len() function will return the number of characters in
# the string:

print(len('let\'s count'))

# A string is not just a sequence of characters. It is a member of
# the String _class_, and is an _iterable_ object that has access to
# a number of _methods_ (functions) associated with its class 
# (we will soon learn what all of this means).



print()
print('Variables and the assignment operator:')
print('---------------------------------------')

# Variables are names used to store values in computer memory. A variable
# is actually a *reference* to a memory address where the value is stored.
#
# Python variable can only contain alpha-numeric characters (a-z, A-Z, 0-9)
# and the underscore character (_). No other characters are permitted.
#
# By convention, standard Python variables use "snake-case":
#
#   this_is_snake_case
#
# Variable names are case-sensitive (myvar, Myvar, and myVar are all
# unique names)

# The assignment operator (=) assigns a value (RHS) to variable name (LHS).
# When using the assignment operator to define the value for a new variable
# name, we say the variable is being "declared":

x = 5    # assign interger to a variable named x
this_course = "ENME202"    # assign a string
this_variable_name_is_very_short = False    # assign a bool

# Multiple variables can be defined on a single line:

x, y, z = 1.0, 9.1, 5.5
s1, s2, b = "hello", "goodbye", True

# Note that the assignment operator is *not* the mathematical "equality" 
# operator, and we cannot set up (or solve) equations using the
# assignent operator. We are simply assigning a value to a variable
# name that can later be recalled by referencing the variable.

# The print() function can control the formatting when displaying
# variables to "standard output" (the display in our case):

print('x:', x, 'y:', y, 'z', z)
print('The values of s1, s2, and b are', s1, ',', s2,', and', b)

# New values can be assigned to variables at any time:

print('x = ', x, type(x))    # initially x = 1.0 (float)
x = 10
print('x = ', x, type(x))    # now x = 10 (int)

# Because Python is a strictly-typed language, it is often necessary 
# to explicity change the variable type using the built-in functions
# int(), float(), or str(). For example, can cannot add a string and
# an int together -- the string must first be converted to an int:

print(22 + int("33"))

# Can use type converstion to "clip" values after the radix in a
# float by converting the value to an int:

print(int(123.456))

# Convert ints or floats to complex:

print(complex(7, 2.2))

# Another important elemental data type is None (NoneType). None is *not* 
# equivalent to 0, False, or an empty string. The None keyword is used to define
# a null value:

print(type(None))    # NoneType

# A variable of type NoneType tells us that no value has been assigned.


print()
print('User Input:')
print('---------------------------------------')

# Often we need to assign values to variables based on user keyboard input. 
# This can be achieved using the built-in input() function. We will talk formallt
# about functions soon, but for now the key points are that a function is a block
# of code that takes one or more "arguments" (values passed to the function), and
# returns a single value back to the point in the code where the function 
# was called. 
#
# The input() function takes a single string as an argument, and returns 
# another string equal to the user's input. Here is an example of the input() 
# function at work:

user_value = input('Enter an integer value: ')    # ask user for value
print('You entered:', user_value)                 # user_value is a string!
print('Double this value is', 2*int(user_value))  # convert to int before doing math


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
In several problems you will need to use basic mathematical operators
(+, -, *). We will talk about operators in the next code file, but 
for now just note that these operators return a value based on their
functionality that can be assigned to a variable. For example, 
"x = 10 + 1" will assign a value of 11 to the variable x.

1. Using a single line of code, declare variables called first_name and last_name by 
   assigning string values given by your first name and last name.
2. Using the len() function, declare a variable called char_count that
   holds the total number of characters contained in first_name and last_name.
3. Print the data type of char_count and first_name.
4. Using appropriate variable names, calculate the area and circumference
   of a circle with a radius of 1.0 m. Display the results (including units)
   using a single print() statement.
5. Repeat step 4, but ask the user to enter a value for the radius.
"""
print(practice)







