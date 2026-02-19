 # Exception Handling


""" 
Topics
------
try / except Blocks
else, finally Blocks
Raising Exceptions
"""

print()
print('Try / Except:')
print('---------------------------------------')

# Python exception handling is a mechanism that allows programs to 
# handle errors or unexpected conditions gracefully. Basic exception
# handling uses _try_ and _except_ blocks to manage exceptions.
# The try block contains code that might raise exceptions, and 
# the except block specifies how to handle those exceptions.  Here is
# the basic syntax:
#
#    try:
#        code where errors may occur
#    except:
#        code to run when error occurs

# Example of division by zero error:
try:
    x = 9/0
except:
    print('error occurred, setting x to default value')
    x = 1
print(x)

# Example of type mismatch error:
try:
    val = 20
    string = 'hello'
    print(val + string)
except:
    print('oops, something went wrong!')

# In these examples we know when an error has occurred, but we don't
# know what the error was!  To display the error, we can capture the
# _Exception object_ (a data element created when an error occurs)
# and print it's type and/or details:

try:
    x = 1/0
except Exception as e:  # division by zero
    print(type(e))      # check the Exception type
    print(e)            # view the error details

# Individual except blocks can be defined to handle different kinds
# of Exception values.
#
# Common Exception types, in no particular order, include:
#    Value                Raised when...
#    -----                ---------------
#    SyntaxError          parsing error (cannot catch errors in base code)
#    KeyboardInterrupt    user hits ctrl-c
#    NameError            local or global name (e.g. variable) is not found
#    IndexError           out-of-range access an index of a sequence
#    ModuleNotFoundError  cannot find a module being imported
#    ImportError          error on module import (e.g. due to code error in module)
#    AttributeError       access an attribute or method that does not exist
#    KeyError             access a dictionary key that doesn't exist
#    TypeError            operation on object(s) of inappropriate type
#    ZeroDivisionError    attempt to divide by zero
#    FileNotFoundError    attempt to read or write to a file that does not exist
#    ValueError           function receives argument of correct type but 
#                         inappropriate value, e.g. int('12a')
#
# Multiple specific Exception types can be caught and handled separately:

try:
    x = int(input('Enter a value: '))
    a = 1/x
    b = [1,2,3][x]
    c = x + 'abc'
    d = int(str(x) + 1)
except ZeroDivisionError:
    print('x cannot be zero')
except ValueError:
    print('x must be a number')
except IndexError:
    print(f'there are only 3 elements in the list')
except TypeError:
    print(f'cannot add an int to a string')
except Exception as e:
    print('something else happened...')
    print(type(e))    # check the Exception type
    print(e)          # view the error details


print()
print('Else, Finally:')
print('---------------------------------------')

# The _else_ block executes if _no_ exceptions occur.  This block only useful
# if something needs to happen *only* when the try block is successful.
#
# The _finally_ block executes _regardless_ of whether an exception was raised,
# and even if the try block terminates (for example by returning from a function call)

try:
    x = 1/0
except Exception as e:
    print('_except_ block runs only if there was an error in the _try_ block')
    print(f'Here is the error: {e}')
else:
    print('Run _else_ block only if no exception occurred in the try block')
finally:
    print('Run _finally_ block to perform clean-up operations (close files, reset')
    print('global variables, etc) regadless of whether there was an error')


print()
print('Raising Exceptions:')
print('---------------------------------------')

# Exceptions may be raised "programatically" with a custom error message 
# using the following syntax:

def check_positive(number):
    if number < 0:
        raise ValueError('The number must be positive')
    return 'The number is positive'

try:
    num = float(input("Enter a number: "))
    print(check_positive(num))
except ValueError as e:
    print(f"Error: {e}")



"""
PRACTICE PROBLEMS

1. Basic Try-Except: Write a program that attempts to divide two numbers provided 
   as inputs. Use a try-except block to catch and handle a ZeroDivisionError.
2. Catching a ValueError: Write a program that attempts to convert a string input 
   into an integer. Use a try-except block to catch and handle a ValueError.
3. File Not Found: Write a program that tries to open a file named "data.txt". 
   Use a try-except block to catch and handle a FileNotFoundError.
4. Multiple Exceptions: Write a program that attempts to divide two inputs provided
   by the user. Handle both ValueError (if the inputs are not numbers) and 
   ZeroDivisionError (if division by zero is attempted).
5. Finally Clause: Write a program that opens a file, reads its contents, and 
   closes the file in a finally block, regardless of whether an exception occurs.
6. Else Clause: Write a program that divides two numbers. Use an else block to 
   print a success message if no exception occurs.
7. Custom Error Message: Rewrite the division program to display a custom error 
   message (e.g., "Cannot divide by zero") instead of the default Python error 
   message for ZeroDivisionError.
8. KeyError Handling: Create a dictionary data = {'x': 10, 'y': 25.1}. 
   Write a program that attempts to access a key entered by the user and handles 
   a KeyError if the key is not found.
9.  Raising an Exception: Write a function check_length() that takes a string as 
    an argument. Raise a ValueError with a custom message if the length of
    the string is greater than 5.
10. Handling Multiple Exceptions in One Block: Write a program that attempts to
    divide two user-provided inputs and catch ValueError and ZeroDivisionError 
    in the same except block.
11. Nested Try-Except: Write a program that first tries to open a file and, 
    inside the try block, attempts to read and convert its first line into an 
    integer. Handle appropriate exceptions at each level.
12. Logging Errors: Write a program that uses the logging module to log errors 
    for any exceptions that occur during a user-provided division operation.
13. Custom Exception Class: Create a custom exception class NegativeNumberError 
    that inherits from Exception. Write a program that raises this exception if 
    the user provides a negative number.
14. Ignore Exceptions: Write a program that processes a list of values and 
    attempts to convert each to an integer. Use a try-except block to ignore 
    invalid values and continue processing.
15. Error Propagation: Write a function divide_numbers(a, b) that raises an
    exception if division by zero occurs. Call this function from another function 
    and handle the exception at the top level.

"""







