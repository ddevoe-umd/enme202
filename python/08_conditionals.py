# Conditionals and Boolean Operators

""" 
Topics
------
if Statements
if / else Statements
if / elif / else Statements
Nested if Statements
Boolean (Logical) Operators
Using Boolean Operators in if Statements

"""

print()
print('if Statements:')
print('---------------------------------------')

# Syntax:
#
# if Boolean_condition: 
#    code_block_when_True
#
# - A colon defines the start of the if statement code block
# - Indentation defines the extent of each code block

# Simple example
x = 2
if x < 5: 
    x += 10
print(x)

# Example with user input
x = float(input("Enter a number greater than 5:"))
if x <= 5: 
    print(f"{x:4.2f} is too small.") 
    print("Maybe pay more attention next time?") 
if x > 5: 
    print(f"Your number is {x:4.2f}.") 



print()
print('if / else Statements')
print('---------------------------------------')

# The _else_ statement defines actions that take place when the argument for
# an _if_ statement is False

val = int(input('Enter an integer: '))
if val > 0:
    print('The value is positive')
else:
    print('The value is negative')


print()
print('if / elif / else Statements')
print('---------------------------------------')

# The _elif_ (else if) statement allows us to add multiple conditional tests to an
# _if_ statement. Each elif statement is evaluated in sequence, and the code block 
# for the first true conditional will be executed. If all if and elif conditionals
# are False, the optional else block will be executed.
val = int(input('Enter an integer: '))
if val > 0:
    print('The value is positive')
elif val == 0:
    print('The value is zero')
else:
    print('The value is negative')


print()
print('Nested if Statements')
print('---------------------------------------')

# One or more if/elif/else blocks can be placed within another if/elif/else block, with
# arbitrary nesting depth.

val = int(input('Enter an integer: '))
if val > 0:
    print('value is positive')
    if val > 10:
        print('and greater than 10')
        if val > 1e6:
            print('also greater than one million')
        elif val > 1e3:
            print('also between one thousand and one million')
    else:
        print('but less than 10')


print()
print('Boolean (Logical) Operators')
print('---------------------------------------')

# Boolean operators are used to compare logical (True / False) values
#
# In Python, Boolean operators are written in plain English: and, or, not
x = True
y = False
x and x    # True
x and y    # False
x or y     # True
not x      # False

if not ((x > 20 and y < 50) or z < 0):
		 # do something

# There is no "exclusive or" (XOR) Boolean operator in Python.
# The caret symbol (^) is the _bitwise_ XOR (bitwise operators will be 
# discussed later), which should not be used as a Boolean operator 
# since it may give incorrect results (due to precedence rules, and 
# depending on whether the values being compared are true Booleans
# or other values). Instead, we can create XOR functionality by
# combining _not_, _and_ & _or_.

(x and not y) or (y and not x)    # XOR

# Order of precedence for Boolean operators:

not > and > or

# Build truth tables for each of the Boolean operators:

print('\n  x  | not x ')
print('-----|-----|--------')
x = 0
print(f'  {x}  |  {int(not x)}')
x = 1 
print(f'  {x}  |  {int(not x)}')


print('\n  x  |  y  | x and y')
print('-----|-----|--------')
x,y = 0, 0 
print(f'  {x}  |  {y}  |   {int(x and y)}')
x,y = 0, 1 
print(f'  {x}  |  {y}  |   {int(x and y)}')
x,y = 1, 0 
print(f'  {x}  |  {y}  |   {int(x and y)}')
x,y = 1, 1 
print(f'  {x}  |  {y}  |   {int(x and y)}')


print('\n  x  |  y  | x or y')
print('-----|-----|--------')
x,y = 0, 0 
print(f'  {x}  |  {y}  |   {int(x or y)}')
x,y = 0, 1 
print(f'  {x}  |  {y}  |   {int(x or y)}')
x,y = 1, 0 
print(f'  {x}  |  {y}  |   {int(x or y)}')
x,y = 1, 1 
print(f'  {x}  |  {y}  |   {int(x or y)}')


print('\n  x  |  y  | XOR(x,y)')
print('-----|-----|--------')
x,y = 0, 0 
print(f'  {x}  |  {y}  |   {int((x and not y) or (y and not x))}')
x,y = 0, 1 
print(f'  {x}  |  {y}  |   {int((x and not y) or (y and not x))}')
x,y = 1, 0 
print(f'  {x}  |  {y}  |   {int((x and not y) or (y and not x))}')
x,y = 1, 1 
print(f'  {x}  |  {y}  |   {int((x and not y) or (y and not x))}')



print()
print('Using Boolean Operators in if Statements')
print('---------------------------------------')

# Boolean operators can be used to construct complex logical expressions
# for use in _if_ statements (and beyond)
val = int(input('Enter an integer: '))
if val > 0 and val < 10 and val%2  == True:
    print('value is an even positive integer between 0 and 10')

# Another example
vals = input('Enter 3 words, separated by commas: ')
[w1, w2, w3] = vals.split(',')
if (len(w1) > len(w2) and len(w1) > len(w3) or (w1 == "the longest word")):
    print('The first entry is the longest word')

# Yet another example
age = 25
has_drivers_license = True
has_criminal_record = False
income = 55000
if (age > 18 and has_drivers_license) or (income > 50000 and not has_criminal_record):
    print("Eligible")
else:
    print("Not eligible")



print()
print('match / case Statements')
print('---------------------------------------')

# The match/case statement tries to match an input value to a sequence of 
# possible case values. The code block under the _first_ matching case statement
# will be executed (after which the match block ends). 

# A case value of _ will always match the input value, allowing a
# corresponding block of code to execute if all previous case values
# do not match the input value:

x = 10
match x:
    case 10:
        print("x == 10")
    case 20:
        print("x == 20")
    case _:
        print("x != 10 and x != 20")

# The match/case statement accepts composite data structures
# including iterables.

"""
PRACTICE PROBLEMS

For each problem, write your code efficiently to minimize the run time.
For example, if there are multiple conditions being checked that are
mutually exclusive, and the first condition is true, make sure that that 
the remaining conditions are _not_ checked.

1. Write code that checks if a given number is odd or even.
2. Write code to determine if a number is positive, negative, or zero.
3. Given 2 integers x and y, display integer with the larger absolute value.
4. Check if a number is divisible by both 3 and 5, either one, or neither.
5. Write code to check if three given sides lengths can form a valid triangle.
6. Check if a given character is a vowel, consonant, or numerical digit.
7. Find the largest of three numbers using nested conditionals.
8. Given the coefficients of the quadratic equation ax^2 + bx + x, write code 
   to determine the quadratic equation has real, imaginary, or equal roots. 
9. Create a simple calculator that performs addition, subtraction, 
   multiplication, or division based on user input. Each input is in the form
   of "value operator value", e.g. "12.5 * 9" or "4+5". Your code must be
   able to handle input with and without spaces between the input elements, and
   use conditionals to handle invalid inputs (like division by zero and 
   non-numerical values). You will need to think carefully about how to pull 
   out the operator and individual values from the user input!
"""







