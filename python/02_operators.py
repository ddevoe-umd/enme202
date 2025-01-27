# Python Operators

""" 
Topics
------
Arithmetic operators
Assignment operators
Comparison operators
Comparison operations using Booleans
"""


print("""
Arithmetic operators:
--------------------
+ 	addition 	
– 	subtraction
* 	multiplication
/ 	division
//	floor division
**	exponentiation
%	modulus

Assignment Operators:
--------------------
=	assignment
+=	addition assignment
–=	subtraction assignment
*=	multiplication assignment
/=	division assignment
//=	floor division assignment
**=	exponentiation assignment
%=	modulus assignment

Comparison Operators:
--------------------
==	equality
!= 	inequality
>	greater than
<	less than
>=	greater than or equal
<=	less than or equal
""")


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

5 / 2		# 2.5
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

# Assignment operators work for other arithmetic data types:

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

True + 1 	# yields 2 since True is type cast to 1
False - 1   # yields -1 since False is type case to 0

# This makes the following comparions valid:

True > False       # True since 1 > 0
True >= 2 - False  # False since 2-False yields 2-0 which is > 1


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
1. Prompt the user to enter side lengths a, b, and c of a triangle, then
   calculate and display the perimeter of the triangle.
2. Prompt the user to enter the slope (m) and y-axis intercept (b) for
   a line defined by y = m*x + b, then calculate and display the x-axis
   intercept. 

Find the length and angle of the vector from point (2, 2) to point (6,10) 


11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.


16. Find the length of the text _python_ and convert the value to float and convert it to string

17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

19. Check if type of '10' is equal to type of 10

20. Check if int('9.8') is equal to 10






"""
print(practice)






