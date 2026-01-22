# Python Operators

""" 
Topics
------
Arithmetic operators
Assignment operators
Comparison operators
Comparison operations using Booleans
"""

"""
Arithmetic operators:
--------------------
+   addition
–   subtraction
*   multiplication
/   division
//  floor division
**  exponentiation
%   modulus

Assignment Operators:
--------------------
=   assignment
+=  addition assignment
–=  subtraction assignment
*=  multiplication assignment
/=  division assignment
//= floor division assignment
**= exponentiation assignment
%=  modulus assignment

Comparison Operators:
--------------------
==  equality
!=  inequality
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal
"""


print()
print('Arithmetic operators')
print('---------------------------------------')

# Addition, subtraction, multiplication, division, and exponentiation
# operators work the same way as in standard mathematical expressions,
# and with the same rules of precedence:
#   1. parentheses
#   2. exponents
#   3. multiplication / division
#   4. addition / subtraction

2 + 3 * 5 - 2 / 6 ** 2  # 2 + (3*5) - (2/(6**2))

# Python understands how to perform operations on complex values:

(1 + 1j) * (1-1j)   #  2 + 0j
(1 + 2j) / (-1j)    # -2 + 1j

# Floor division returns an integer, dropping values after the radix:

5 / 2     # 2.5
5 // 2    # 2

# The molulus operator returns the remainder after division:

5 % 2    # 1
99 % 10  # 9
5 % 6    # 5

# Each arithmetic operation returns a value that can be assigned
# to a variable:

total = 2 + 5

# Note: why not call this variable "sum" instead of "total"? Becaue "sum"
# is a built-in function, and renaming this reserved word can cause
# unexpected errors!

# All operators can be applied to variables as well as raw values:
x = 3
y = x / total**2

# We can assign a value to a variable based on the current value of
# that variable:

x = x + 1   # x is now 4

print()
print('Assignment operators')
print('---------------------------------------')

# Assignment operators allow us to combine assignment and arithmetic 
# operations:

x = 8    # basic assignment operator

x += 5   # same as x = x + 5, so x is now 13
x -= 3   # same as x = x - 5 (x is now 10)
x /= 2   # same as x = x / 2 (x is now 5)
x //= 2  # same as x = x // 2 (x is now 2)
x **= 3  # same as x = x ** 2 (x is now 8)
x %= 3   # same as x = x % 3 (x is now 2)

# Assignment operators work for all arithmetic data types:

complex_val = 2 + 6j
complex_val *= -3j     # (2 + 6j) * (-3j) = 18 - 6j

float_val = 4.41
float_val += 1.02

# Assignment operators can be combined with other variables on the RHS:

x += 2*complex_val

# Addition assignment (only) also works for strings:

str1 = "foo"
str1 += "bar"

# Note that there are no increment (++) or decrement (--) operators in Python

print()
print('Comparison operators')
print('---------------------------------------')

# Comparison operators return a Boolean value (True/False) based on whether
# the comparative statement is true:

# Relative values:

3 > 2     # True
3 >= 2    # True
3 < 2     # False
2 < 3     # True
2 <= 3    # True

# Strings can be compared lexicographically (based on the alphabetical 
# order of their characters, using their Unicode values):

'a' < 'b'     # True
'abc' < 'b'   # True
'z' >= 'zz'   # False

# Equality / inequality:

3 == 2    # False
3 != 2    # True

'those' == 'these'  # False
'this' == 'this'    # True

3 == "why"          # False
'A' == '\u0041'     # True, since capital A has a unicode value of 41 (hexadecimal)
3 == len("why")     # True

print()
print('Comparison operations using Booleans')
print('---------------------------------------')

# The equality and inequality operators can be used to evaluate Boolean expressions
# (that is, expressions consisting of statements that are themselves either
# True or False:

True == True     # True
True == False    # False
False == False   # True

# These trivial examples can be extended to cases with comparisons on the LHS,
# RHS, or both (since comparisons return True or False values):

(2 > 1) == (5*2 == 10)      # True == True --> True
(1 > 10) != ('a' != 'b')    # False != True --> True

# Greater/less than operators can also be used with Boolean values, since
# Booleans are automatically type cast to int values based on the
# context. For example:

True + 1    # yields 2 since True is type cast to 1
False - 1   # yields -1 since False is type cast to 0

# This makes the following comparions valid:

True > False       # True since 1 > 0
True >= 2 - False  # False since 2-False yields 2-0 which is > 1


"""
PRACTICE PROBLEMS

Arithmetic and Assignment Operators
1. Basic Arithmetic: Compute the result of the following expressions 
   and store them in variables:
   5 + 3
   12 - 7
   4 * 6
   20 / 4
2. Floor Division: Calculate 17 // 3 and store the result in a variable.
   What is the difference between / and //?
3. Modulus: Compute the remainder when 23 is divided by 5.
4. Exponentiation: Compute 2 raised to the power of 5 using the ** operator.
5. Mixed Operations: Calculate 5 % 2 + 3 * 2 - 8 / 4**1.5, and add 
   parentheses to emphasize the correct operator precedence.
6. Assignment: Create a variable x and assign it the value 10. 
   Update its value using combined assignment and arithmetic operators to:
   Add 5
   Subtract 3 
   Multiply by 2
   Divide by 4
   Raise to the power of 0.5 (square root)

For all of the following problems, display the boolean result (True or False) for each comparison:

Comparison Operators
7. Equal and Not Equal: Write expressions to compare the following pairs 
   of values and store the results in variables:
   Is 5 equal to 5?
   Is 7 not equal to 10?
8. Greater Than and Less Than: Evaluate whether:
   15 is greater than 10.
   4 is less than 2.
9. Greater Than or Equal To: Write an expression to check if 7 is greater than or 
   equal to 7.
10. Combined Arithmetic and Comparison: Evaluate whether the result of 8 * 3 
    is greater than 25.

Boolean Operators
11. AND Operator: Evaluate whether the following two statements are both true:
    10 > 5
    8 < 12
12. OR Operator: Evaluate whether at least one of the following statements is true:
    15 < 10
    5 != 3
13. NOT Operator: Invert the following Boolean expressions:
    10 == 10
    7 < 3
14. Boolean Chain Comparison: Check if 5 < 10 < 15.
15. Combined Booleans: Assign integers to variables x and y, and write a single
    expression to evaluate if x is simultaneously greater than y, greater than 
    zero, and even, or y is both odd and less than 20. Test the expression using
    x,y = 10,13
"""






