# User-Defined Functions

""" 
Topics
------
Function syntax
Returning multiple values
Default argument values
Passing an arbitrary number of arguments (packing & unpacking)
Documentation strings (docstrings)
Variable Scope
Lambda Functions
"""

print()
print('Function syntax:')
print('---------------------------------------')

# A function is a block of code that can be executed multiple times, and from multiple
# places, from the main program. A function can also call a function from within
# another function, or even call a function from within itself (a recursive function).

# Functions can accept one or more values as input arguments, and can return
# a single value back to the calling code.  Here "value" means the value of
# any valid Python data structure, from elemental data types (e.g. int) to
# composite structures (e.g. lists) or even custom data types that can
# be defined by the programmer.

# Here is the syntax for a user-defined function that takes no input arguments
# and returns no value

def custom_function():
    print('custom_function() called')

# Defining the function does not run the function code. To run the function code,
# we can call the function from anywhere in the main code

custom_function()

# Here is a function that takes 1 numerical argument, and displays the square 
# root of the sum of that value and 5:

def sum_sqrt(x):
    total = x + 5
    sqrt = total**(1/2)
    print(sqrt)

# Of course this function can be simplified to:

def sum_sqrt_v2(x):
    print((x+5)**(1/2))


print()
print('Returning values:')
print('---------------------------------------')

# Functions can return a single value (of any data type), allowing the 
# returned value to be accessed by the calling code:

def sum_sqrt_v3(x):
    total = x + 5
    sqrt = total**(1/2)
    return sqrt

result = sum_sqrt_v3(11)
print(result)

# Functions can include multiple _return_ statements. The function will 
# end once the first return statement is encountered. This allows
# multiple branches of a conditional to return different values:

def is_single_digit_int(x):
    if x >= 0 and x < 10 and isinstance(x, int):
        return True
    else:
        return False 

print(is_single_digit_int(2.1))   # False
print(is_single_digit_int(5))     # True
print(is_single_digit_int(-3))    # False


print()
print('Passing multiple arguments:')
print('---------------------------------------')

# A function can accept an arbitrary number of input argument values. Here is
# a function similar to sum_sqrt() above, but which takes 2 numerical arguments:

def sum_sqrt_v4(x, y):
    total = x + y
    sqrt = (total)**(1/2)
    return sqrt

print(sum_sqrt_v4(6, 3))

# Functions can accept arguments of any valid Python data type. For example,
# here is a function that takes one argument that is a list defining
# the coefficients of a quadratic expression a*x^2 + b*x + c, and a 2nd
# argument that is the value of x at which to evaluate the quadratic. The function
# returns the result.

def quad_eval(coefs, x):
    if len(coefs) != 3:
        print('improper coefficient list')
        return(None)
    (a,b,c) = coefs           # unpacking
    return(a*x**2 + b*x + c)

print(quad_eval([2,1,2], -1))

# Notice that the order in which we pass the values must be consistent with
# the order in the function definition.  However, we can avoid this limitation
# by specifying the variable names in the function call:

quad_eval(x=4, coefs=[1,2,3])

# When calling a function, we are passing _values_ not _variables_.  As long
# as an argument reduces to a value (appropriate for the data type) that
# value will be passed to the function and assigned to the given local variables:

quad_eval(list(range(3)), 6**2.5)


print()
print('Returning Multiple Values:')
print('---------------------------------------')

# Functions can only return a single value, but often we need to extract 
# multiple numbers, strings, or other data types from a function. To achieve
# this, return a composite data structure (e.g. list).
#
# Here is a function that calculates the roots of a quadratic, and
# returns both roots in a list:

def roots(coefs):
    (a,b,c) = coefs
    disc = (b**2 - 4*a*c)**(0.5)
    r1 = -b + disc/(2*a)
    r2 = -b - disc/(2*a)
    return [r1, r2]        # return a single list containing 2 numbers

print(roots([1,2,1]))      # real & repeated roots
print(roots([2,0,-2]))     # real & unique roots
print(roots([2,0,2]))      # complex conjugate roots


print()
print('Default Argument Values:')
print('---------------------------------------')

# We can define a function with arguments that can take on default values
# if the function is called without those arguments being passed:

def sum_sqrt_v4(x, y=5):
    total = x + y
    sqrt = (total)**(1/2)
    return sqrt

x1 = sum_sqrt_v4(11, 14)     # call with two arguments...
x1 = sum_sqrt_v4(11)         # or just one

# In this last example, the y is assigned the default value of 5 since a
# second argument was not passed to the function.
#
# Note that arguments with default values much come at the end of the
# argument list, otherwise Python can't know which values take default
# values with the function is called with fewer than the maximum number
# of arguments.



print()
print('Passing an Arbitrary Number of Arguments -- Packing & Unpacking:')
print('---------------------------------------')

# Sometimes we need a function that can accept an aritrary number of 
# arguments, i.e. the function can be called to different numbers of
# arguments at different points in our code.
#
# To accomplish this, place a '*' character ahead of an argument
# variable name, indicating that the resulting variable is a _tuple_
# whose elements are the values passed to the function:

def prod(*args):
    print(type(args))
    print(args)
    total = 1
    for v in args:
        total *= v 
    return total

print(prod(2, 5))
print(prod(2, 5, 2))
print(prod(2, 5, 2, 6, 9, 3))

# The * symbol denotes _packing_ or _unpacking_ of an iterable. In the above
# example we are packing a sequence of arguments into a _tuple_.

# Using _args_ as the packed argument name is convention, but not required.

# We can also _unpack_ an iterable to yield a sequence of values. For example,
# here is a function that accepts a sequence of 5 values as arguments:

def add(a,b,c,d,e):
    return(a+b+c+d+e)

# Say we want to add up the values in a list:

vals = [1, 2, 3, 4, 5]

# Passing this list to the function will result in an error, since the
# function requires 5 input values (and not just a single list value):
#
# add(vals)   <--- would result in error
#
# Instead, we can _unpack_ the list to pass each value in the list as
# a separate argument:

print(vals)          # list
print(*vals)         # individual values

print(add(*vals))    # This is valid since vals has been unpacked


# We can combine regular arguments with packed arguments by
# placing the packed argument at the end of the argument list:

def my_join(delimeter, *args):
    result = args[0]
    for s in args[1:]:        # start at 2nd string to join
        result += delimeter + s
    return(result)

print(my_join(',','one','two','three'))
print(my_join(',','a','b','c', '1', '2', '3'))


# What if we want to values to pack as elements of a _dictionary_ (which 
# contains both keys and values)?  Pass the arguments with names equal to
# the desired keys, and assigned values for each key:

def print_dict(**kwargs):
    for item in kwargs.items():
        print(f'{item[0]}: {item[1]}')

print_dict(key1='A', key2='B', key3='C', key4='D')

# As with _args_, using _kwargs_ as the name of the packed dictionary
# is convention, but not required.



print()
print('Documentation strings (docstrings):')
print('---------------------------------------')

# Here is a function that takes a single argument (a list) and returns a number.
# To make it clear what data type is passed to the function, and what type is returned
# by the function, a _docstring_ has been added to the function definition.

def average(numbers):
    """ Calculates the average of a list of numbers.
    Args:
        numbers: A list of numbers.
    Returns:
        The average of the numbers.
    """

    if not numbers:
        return 0

    total = sum(numbers)
    return total / len(numbers)

# Docstrings appear immediately after the function definition line, and are enclosed 
# in triple double quotes ("""). Docstrings should do the following:
#   1. Provide a concise description of the function's purpose.
#   2. List the arguments that the function accepts, along with their types and descriptions.
#   3. Describe the value that the function returns, including its type.
#   4. Include examples (optional)
#
# The docstring for a function can be accessed using the __doc__ attribute:

print(average.__doc__)

# Docstrings exist for most (all?) built-in functions

print(len.__doc__)
print(print.__doc__)


print()
print('Variable Scope:')
print('---------------------------------------')

# Variables declared inside a function are maintained in a _namespace_ separate
# from that of the main code. The namespace defines the mapping from names to 
# objects (variables, functions, classes, etc.), ensuring that identical names in 
# different namespaces don't interfere with each other.

# A consequence is that while variables declared in the main code can be accessed
# within a function, variables declared within the function are _local_ to the function,
# and cannot be accessed from within the main code. We say that these variables
# have _local scope_ instead of _global scope_.

def test1():
    x = -1
    print(f'Inside function: {x},{y}')   # the value of local variable x is now -1

x,y = 5, 6
test1()         # test assigns a different value to a local variable x,
print(f'Outside function: {x},{y}')      # but the value in the main code remains unchanged

# If the intent is to change the value of x in the main code, declare x inside the
# function using the _global_ keyword to ensure global scope. Note that we 
# don't need to declare y as global since the value of y is not being
# changed inside the function (we can access the global value, but cannot
# make changes to global y).

def test2():
    global x    # declare x as global
    x = -1
    print(f'Inside function: {x},{y}')  # the value of global variable x is now -1

x,y = 5, 6
test2() 
print(f'Outside function: {x},{y}')     # the value of x has been changed

# Unlike some programming languages, Python does NOT have "block-level scope". 
# This means that variables declared within if statements, for/while loops, etc., 
# are accessible outside the block.



print()
print('Lambda Functions:')
print('---------------------------------------')

# A lambda function is a small single-expression function.  Lambda functions can be
# anonymous (unnamed) when defined in-line with other code using the following syntax:
#
#    lambda bound_variables: function_body

# Here is a regular named function that adds 2 numbers, returning the result:
def add(x,y):
    return x+y
print(add(1,2))

# Here is the same function as a lambda function:
add = lambda x,y: x+y
print(add(1,2))

# Lambda functions can be returned by another function, allowing us to
# define new functions "on the fly".  

def power(x):
    return lambda n : n ** x

cube = power(3)    # create a new function called cube()
print(cube(2))

sqrt = power(1/2)  # create a new function called sqrt()
print(sqrt(81))

# This is an example of _closure_, a concept we will cover later in the
# context of _higher-order functions_. Briefly, we will see that any 
# function (not just lambda functions) can be defined within another
# function and returned by that function.


"""
PRACTICE PROBLEMS

Easy
1. Greeting Function: Define a function greet that takes a name as an argument and 
   prints "Hello, [name]!".
2. Sum of Range: Define a function sum_range that takes two integers start and 
   end, and returns the sum of all numbers between them (inclusive) using a loop.
3. Odd or Even: Define a function is_even that takes a number and returns True 
   if it is even and False if it is odd. Use a conditional statement.
4. Find Maximum: Define a function find_max that takes three numbers as arguments 
   and returns the largest using if-elif-else.

Medium
5. Factorial Calculation: Define a function factorial that takes a number and returns
   its factorial using a loop.
6. Count Vowels: Define a function count_vowels that takes a string and returns the
   number of vowels in it. Use a loop and a conditional to check for vowels.
7. Reverse String: Define a function reverse_string that takes a string and returns
   the reversed string using a loop.

8. Taylor series: write a function that will calculate the Taylor series expansion 
   for sin(x). The function must accept 2 arguments, x and n, where x is the value
   at which sin(x) is evaluated, and n is the number of terms to use in the 
   Taylor series.
9. Custom Range: Define a function custom_range that takes three arguments: 
   start, end, and step. Return a list of numbers between start and end (exclusive) 
   with the specified step.

Hard
10. Prime Number Check: Define a function is_prime that takes a number and returns 
    True if it is prime and False otherwise.
11. Palindrome Check: Define a function is_palindrome that takes a string and returns 
    True if it is a palindrome (reads the same backward and forward) and False 
    otherwise.
12. Number to Words: Define a function number_to_words that takes an integer between
    1 and 5 and returns its word representation (e.g., 1 → "One"). Use a dictionary
    and conditionals.
13. Unique Elements: Define a function unique_elements that takes a list and returns
    a new list with only the unique elements from the input list.
14. Character Frequency: Define a function char_frequency that takes a string and 
    returns a dictionary with each character as the key and its frequency as the value.
15. Find Longest Word: Define a function longest_word that takes a list of words
    and returns the longest word in the list. If there is a tie, return the first one.
"""







