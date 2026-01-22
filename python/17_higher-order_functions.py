# Higher-Order Functions

""" 
Topics
------
Basics of Higher-Order Functions
Closures
Function Decorators
Built-in Higher Order Functions: map(), filter(), reduce()
"""


print()
print('Basics of Higher-Order Functions:')
print('---------------------------------------')

# Python functions are +first-class objects+, meaning that they can be treated 
# the same way as any other data type. Functions can be:
#     -- assigned to variables
#     -- stored in data structures
#     -- passed as arguments to other functions
#     -- returned from other functions

# Higher-order functions are functions that operate on other functions by
# taking one or more functions as arguments, returning a function, or both. 

# ---------------
# Functions as arguments
# ---------------

# A function can be passed as an argument to another function. The passed
# function can then be called within the other function:

def add_one_into_function(func, val):    # pass a function and a value
    return func(val+1)                   # return a value

# Define a pair of functions to use as argument
def square(x):
    return x**2
def cube(x):
    return x**3

# pass squared() or cubed() as an argument to add_one_into_function()
result_1 = add_one_into_function(squared, 3)
result_2 = add_one_into_function(cubed, 2)
print(result_1, result_2)



print()
print('Closure: ')
print('---------------------------------------')

# Functions can be nested, with one function defined within another 
# function, e.g.:

def outer(x):
    def inner(y):
        return y+x
    return inner(2)   # return a +numerical value+ to the calling code

print(outer(1))

# In the above example, the outer function calls the inner function, then
# returns a value to the calling code.  Nothing new here (yet)...
#
# However, if the outer function returns the inner function itself
# (rather than some other value), this is termed a _closure_.
# A closure is any function which "closes over" the environment in which
# it was defined, giving the inner function access to object names from
# the outer function that are not in the inner function's argument list.
#
# The returned function can be assigned to a variable in the calling
# code, allowing the inner function to be accessed in the main code.
#
# The power of closures lies in the ability to create different functions,
# as seen in the following closure example:

def outer(x):
    def inner(y):
        return y+x   # inner() closes over outer(), so it has access to variable x
    return inner     # return a +function+ to the calling code

add_five = outer(5)     # create a new function called add_five()
                        # with 5 assigned to x
print(add_five(1))      # 1 is assigned to y in inner(), with x = 5
print(add_five(2))      # 2 is assigned to y in inner(), with x = 5

subtract_four = outer(-4)     # create a new function called subtract_four()
                              # with -4 assigned to x
print(subtract_four(1))       # 1 is assigned to y in inner(), with x = -4
print(subtract_four(2))       # 2 is assigned to y in inner(), with x = -4


# Here is another example where new functions are created at runtime
# based on user input:

def return_a_function():
    x = float(input('Enter a value: '))
    def new_func(z):
        return x+z
    return new_func

func1 = return_a_function()    # Create a new function
func2 = return_a_function()    # Create another new function

print(func1(5))    # Output depends on value entered by user when defining func1
print(func2(5))    # Output depends on value entered by user when defining func2



print()
print('Function Decorators:')
print('---------------------------------------')

# A _decorator_ is a "design pattern" that adds new functionality to an existing
# object without modifying the object's structure. Decorators can be applied
# to functions, class methods, or entire classes.  Here we will focus on
# function decorators.

# A function decorator is a type of higher-order function that can be "applied" 
# to another function to give that function additional capabilities.  Applying
# a decorator is performed by placing the "at symbol" (@) before the decorator
# name on the line above the function to be decorated.

# Here is a simple example: 

def simple_decorator(func):
    def wrapper():
        print("Do something before calling the function.")
        func()
        print("Do something after calling the function.")
    return wrapper

@simple_decorator
def hello():
    print("Hello!")

@simple_decorator
def goodbye():
    print("See ya!")

hello()
goodbye()


# The decorator function simple_decorator() takes a function (hello() or goodbye() here)
# as an argument (func).
# 
# The decorator returns a new function, wrapper(), that includes the passed function
# plus some added functionality (simple print statements before & after the function call).
#
# The inner function is called wrapper() by convention, but this is not a requirement.
#
# @simple_decorator is the syntax that applies the decorator to the hello() and
# goodbye() functions.  When the decorated function is called, it executes the full 
# wrapper() function.


# If the function to be decorated takes an argument, the wrapper() function
# must also accept an argument to pass it along to the function:

def decorator_with_argument(func):
    def wrapper(x):
        print('passed value assiged to "x"')
        func(x)
    return wrapper

@decorator_with_argument
def display(val):
    print(val)

display(-5)


# The decorator must take the same number of arguments as any function
# to be decorated:

def decorator_with_arguments(func):
    def wrapper(x,y):
        print('passed value assiged to "x"')
        func(x,y)
    return wrapper

@decorator_with_arguments
def display(val1, val2):
    print(val1, val2)

display(5, 7)

# If a decorator will be applied to multiple functions
# that each takes a different number of arguments, the wrapper() (and the
# function call) must use _*args_ as an argument:

def decorator_with_arguments_2(func):
    def wrapper(*args):
        print('passed value assiged to "x"')
        func(*args)
    return wrapper

@decorator_with_arguments_2
def display1(val1, val2):
    print(val1, val2)

@decorator_with_arguments_2
def display2(val1, val2, val3, val4):
    print(val1, val2, val3, val4)

display1(5, 7)
display2(5, 7, 8, 9)

# Finally, if we want the decorated function to also accept _named arguments_,
# wrapper() must accept both *args (for unnamed arguments) and
# **kwargs (for named arguments, i.e. "x=5").  This "univeral syntax"
# ensures that the decorator can be applied to any function, 
# with function calls both with and without named arguments:

def decorator_with_named_arguments(func):
    def wrapper(*args, **kwargs):
        print('passed value assiged to "x"')
        func(*args, **kwargs)
    return wrapper

@decorator_with_named_arguments
def display3(val1, val2, val3, val4):
    print(val1, val2, val3, val4)

display3(1, 2, val4=6, val3=-1)



print()
print('Built-In Python Higher Order Functions:')
print('map(), filter(), functools.reduce()')
print('---------------------------------------')

# map(), filter(), and reduce() are 3 of the most useful built-in higher-
# order functions. They each take 2 arguments, a function and
# an iterable, and return a result based on applying the function to
# the iterable.  Let's see how each of them works.

# ---------------
# map()
# ---------------

# map() applies the function to each element of the iterable, returning the
# result in a new iterable (of type map):
#
#    map(function, iterable)

# Here is a simple example using a lambda function as input:

x = [1,2,3,4,5]
xx = map(lambda x: x*x, x)
print(type(xx))     # The resulting iterable is of type map
print(list(xx))     # Convert the iterable to a list

# Of course we could have achieved the same result using list comprehension
# (can you do it?).

# ---------------
# filter()
# ---------------

# The filter() function calls the specified function which returns a bool
# for each element in the iterable. It returns a new iterable containing
# only the items for which the function returns True:
#
#    filter(function, iterable)

x = [1,2,3,4,5]
x_even = filter(lambda x: not x%2, x)
print(type(x_even))     # The resulting iterable is of type map
print(list(x_even))     # Convert the iterable to a list

# As with map(), this could have been done using list comprehension
# with an embedded conditional (can you do it?).

# ---------------
# reduce()
# ---------------

# The reduce() function is defined in the functools module.  Like map 
# and filter it takes two parameters, a function and an iterable. However,
# it returns a single value rather than another iterable.

from functools import reduce

# Example: Calculate the product of a list of numbers

vals = [2, 4, 6, 8]

def multiply(x, y):    # Function to use in reduce()
    return x * y

print(reduce(multiply, vals))

# reduce() applies the function cumulatively to the items of the 
# iterable. First, it applies the function to the first two elements: 
#     multiply(2, 4) → 8.
# Then it takes the result and applies it to the next element: 
#     multiply(8, 6) → 48.
# This process continues until all the items of the iterable are 
# exhausted: 
#    multiply(48, 8) → 384


"""
PRACTICE PROBLEMS

Easy
1. Passing Functions: Write a function apply_twice(func, x) that takes a function 
   func and a value x, and applies func to x twice.
2. Simple Closure: Write a function make_multiplier(n) that returns a new function. 
   The returned function should take a number and return it multiplied by n.
3. Built-in: map: Use the map function to square each number in the list [1, 2, 3, 4].
4. Built-in: filter: Use the filter function to extract all even numbers from the 
   list [1, 2, 3, 4, 5, 6].

Medium
5. Built-in HOF reduce(): Use functools.reduce to compute the product of all numbers in 
   the list [1, 2, 3, 4].
6. Custom Sorting: Write a function sort_by_second that sorts a list of tuples 
   based on the second element. Use the sorted function and a custom key function.
7. Decorators: Write a decorator log_function_call() that logs (prints) the name 
   of the function being called. Apply it to a sample function.
8. Stateful Closure: Write a closure counter() that returns a function. Each time 
   the returned function is called, it should increment and return the count.
9. Built-in: any(), all(): Use any() to check if any element in the list [0, 0, 1, 0] 
   is truthy, and use all() to check if all elements in [True, True, False] are truthy.

Hard
10. Higher-Order Function Factory: Write a function power_factory(n) that returns a 
    new function. The returned function should take a number x and return x ** n.
11. Memoization with Closures: Write a closure memoize_add() that caches the result 
    of adding two numbers so that the same calculation isn't repeated.
12. Decorator with Arguments: Write a decorator repeat(n) that repeats the execution 
    of a function n times.
13. Built-in: Chaining map() and filter(): Use map and filter together to find the 
    squares of all even numbers in [1, 2, 3, 4, 5, 6].
14. Decorator: Timing: Write a decorator measure_time() that measures and prints 
    the execution time of a function.
15. Lambda Expressions: Write a function apply_operation that takes a lambda 
    function and two numbers, and returns the result of applying the lambda to 
    the two numbers.
"""









