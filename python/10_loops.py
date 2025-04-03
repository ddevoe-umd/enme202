# Loops

""" 
Topics
------
for Loops
The range() Function
Nested for Loops
break, continue, else Statements
pass Statement
Structured Data Types as Loop Indices
Looping with Index Values Using enumerate()
while Loops
"""

print()
print('for Loops:')
print('---------------------------------------')

# Basic for loops syntax:

for loop_variable in iterable: 
    # Do something.
    # Never modify the iterable within the loop!

# An iterable is a data structure that can be “iterated over”. Many Python data
# structures including strings, lists, tuples, and dictionaries are iterables. 

# Let's start constructing for loops with lists as the iterable data structure.
# When used with the in keyword, Python will iterate through each element
# of the list, sequentially assigning eachlist value to the loop variable for each
# pass through the list.

my_string = 'among these barren crags'
for letter in my_string:
	print(letter, end=',')

my_list = ['cat', 'window', 'defenestrate']
for item in my_list:
    print(item, len(x))

my_dict = {'thing 1':'left', 'thing 2': 'right'}
for item in my_dict:
	print(item)

for key in my_dict.keys():
	print(my_dict[key])


print()
print('The range() Function:')
print('---------------------------------------')

# Often we need a for loop to execute a certain number of times, with a numerical 
# loop variable that increments each time through the loop. We could do this by
# creating a list with the desired values, for example:

for i in [0,1,2,3,4,5,6,7,8,9]:
	print(f'{i}^2 = {i**2}')

# What if the loop variable needs to go to 100?  1e3?  1e6?  This manual approach
# quickly becomes impractical. Instead, we can use the range() function to
# generate an iterable data structure with the desired values on the fly
#
# The range() function returns an iterable of integers, by default starting at 0,
# using the following syntax options:
#
# range(end+1)
# range(start, end+1)
# range(start, end+1, step)

for i in range(10):
	print(f'{i}^2 = {i**2}')

for idx in range(0,6):
	print(idx)

for x in range(2, 15, 3):
    print(x)

# Sometimes we want a loop to execute a certain number of times, 
# but we don't need to access the loop variable value itself.
# In this case, use a single underscore (_) to denote a
# "throwaway" variable:

for _ in range(10):
    print('.', end='')


print()
print('Nested for Loops:')
print('---------------------------------------')

# When a for loop is placed inside another for loop, the inner loop executes
# completely for each iteration of the outer loop. Nested for loops are
# typically used to iterate over multi-dimensional data structures or
# when multiple levels of iteration are needed. 

# Example -- use nested for loops to display the list structure for the
# variable _matrix_ as a 2D array:

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
for row in range(3):
    for col in range(3):
        print(matrix[row][col], end=' ')
    print()


print()
print('break, continue, else Statements:')
print('---------------------------------------')

# The break statement will stop the current loop, and continue code execution

# The continue statement will end the current loop iteration, but continue
# the loop with the next value of the loop variable

for x in range(2,6):        # outer loop, x=2,3,4,5
    for y in range(1,6):    # nested loop, y=1,2,3,4,5
        if x == y:
            continue  # go directly to next y value
        # keep going if 'continue' not called...
        print(f'{x}, {y}')
        if x + y > 5:
            break  # exit inner loop, go to next x value


# The else statement after a for loop defined a block of code that will
# execute when the loop ends (without a break statement occurring). Try
# the following with limit = 10 and limit = 5

limit = 9
for val in [1,3,6,8]:
    print(val)
    if val > limit:
        break
else:
    print('done')    # only runs when the break statement is avoided


print()
print('Pass Statememt:')
print('---------------------------------------')

# The pass statement is "syntactic filler" -- it creates a line of code when a statement
# is required, but does not do anything. It is used to avoid errors, such as in for loops
# that do not have any functional lines of code, and as a placeholder for future
# code expansion.

for val in range(100):
    pass


print()
print('Structured Data Types as Loop Indices:')
print('---------------------------------------')

# The loop variable does not need to be an int, or even a number.  Any valid
# Python object can be used as the loop variable.  Here is a simple example
# using tuples:

knights = {
  'gallahad': 'the pure', 
  'robin': 'the brave' }

for item in knights.items():          # _item_ is a tuple
  print('%s %s' % (item[0], item[1])) 

for (a, b) in knights.items():        # same idea but unpack the tuple
  print(a, b)


print()
print('Looping with Index Values Using enumerate():')
print('---------------------------------------')

# Consider a loop where we want to print the index value for each element 
# of a list that is greater than 5.  We might start by writing the following
# loop:

vals = [4, -2, 98, 2.5, 6.02]
for v in vals:
  if v > 5:
    print('uh oh')     # What do we do??  There is no loop variable to print!

# To access the index values, use the enumerate() function
#
# enumerate(iter) returns an iterator of tuples, with each tuple containing
# an (index, value) pair:

for (idx, v) in enumerate(vals):
  if v > 5:
    print(idx)

print()
print('Looping Through Paired Lists Using zip():')
print('---------------------------------------')

# zip() takes 2 iterables of equal length as arguments, and generates
# a new iterable of tuples with each tuple containing paired values from each
# of the input iterables:

letters = ['A', 'B', 'C', 'D', 'E']                    
numbers = [1, 2, 3, 4, 5]
combination = []
for letter, number in zip(letters, numbers):
    combination.append({'letter':letter, 'number':number})

print(combination)


print()
print('while Loops:')
print('---------------------------------------')

# _While_ loops are necessary when the number of loop iterations is
# not know ahead of time, but rather is defined by a condition that changes
# within the loop:

a = -10
while a <= 10:
    print(a)
    a += 1

# Infinite loops will continue indefinitely (until hitting a break statement):

while True:
    if int(input('enter number > 10 to end: ')) > 10:
        break


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
Easy
1. Print Numbers: Write a for loop to print numbers from 1 to 10.
2. Sum of Numbers: Use a while loop to calculate the sum of numbers 
   from 1 to 20.
3. Iterate Over a String: Write a for loop to print each character of the 
   string "Engineering" on a new line.
4. Countdown: Use a while loop to print a countdown from 10 to 1.

Medium
5. Factorial: Write a for loop to calculate the factorial of a given number.
6. Even Numbers: Use a while loop to print all even numbers between 1 and 50.
7. Multiplication Table: Write a for loop to display the multiplication table
   of a given number.
8. Reverse a List: Use a for loop to print the elements of a list in 
   reverse order.

Hard
9. Sum of Digits: Use a while loop to calculate the sum of the digits of 
   a given number (e.g., 123 → 6).
10. Prime Numbers: Write a for loop to print all prime numbers 
    between 1 and 100.
11. Taylor series: Use a while loop to find the first 5 terms of the 
    Taylor series expansion for sin(x), and use the result to estimate 
    sin(pi/4).
12. Repeat the previous problem, but continue taking Taylor series terms 
    until the different between successive terms is less than 1e-4
13. Pattern Printing: Write a nested for loop to print the following 
    pattern for n=4:
    *
    **
    ***
    ****
14. Multiplication table: Use nested for loops to generate a 
    multiplication table (1 to 10) in grid format. Use string formatting
    to align the table elements appropriately.
"""
print(practice)







