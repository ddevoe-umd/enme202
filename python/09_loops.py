# Loops

""" 
Topics
------
for Loops
range()
Nested for Loops
break, continue, else Statements
pass Statement
Structured Data Types as Loop Indices
Unpacking Iterables in Loop Definition
Looping with Index Values Using enumerate()
while Loops
"""

print()
print('for Loops:')
print('---------------------------------------')

# Basic for loop syntax:

for loop_variable in iterable:
    # Loop block code here.
    # Never modify the iterable within the loop!

# An iterable is a data structure that can be “iterated over”. Many Python data
# structures including strings, lists, tuples, and dictionaries are iterables. 

# Let's start constructing for loops with lists as the iterable data structure.
# When used with the _in_ keyword (which we previously used as a membership operator),
# Python will iterate through each element of the list, sequentially assigning each
# list value to the loop variable upon each pass through the list.

my_string = 'among these barren crags'
for letter in my_string:
    print(letter, end=',')

my_list = ['cat', 'window', 'defenestrate']
for item in my_list:
    print(item, len(item))

# Any iterable can be used to assign values to the loop variable. Here is an
# example using a dictionary:

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

# If we don't need to access the loop variable itself, can use a single
# underscore (_) as a "throwaway" variable:

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

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix, '\n')

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
    print('.')


# The else statement after a for loop defines a block of code that will
# execute when the loop ends _without_ a break statement occurring. Try
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
print('Unpacking Iterables in the Loop Definition:')
print('---------------------------------------')

# An iterable can be *unpacked*, i.e. have individual values assigned to specific
# variables:

w = [1, 2, 3]
print(w)

a, b, c = w
print(a, b, c)

# Iterables used in for loops can be unpacked within the loop to assign values to
# multiple loop variables.  Here is an example using a dict_items object, which is
# an _iterator of tuples_:

knights = {
  'gallahad': 'the pure', 
  'robin': 'the brave' }
  
for (name, characteristic) in knights.items():   # unpack dict_items into tuples
  print(name, characteristic)


print()
print('Looping with Index Values -- enumerate():')
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
# enumerate(iter) returns an _iterator of tuples_, with each tuple containing
# an (index, value) pair:

for (idx, v) in enumerate(vals):
  if v > 5:
    print(idx)


print()
print('Looping Through Paired Lists Using zip():')
print('---------------------------------------')

# zip() takes 2 or more iterables of equal length as arguments, and generates
# a new iterable of tuples, with each tuple containing corresponding values 
# from each of the input iterables:

list1 = ['A', 'B', 'C', 'D', 'E']                    
list2 = [1, 2, 3, 4, 5]

for letter, number in zip(list1, list2):
    print(f'letter:{letter}, number: {number}')


# Another zip() example with 3 iterables:

vec1 = [2,4,7]
vec2 = [0,1,0]
vec3 = [1,5,9]

for (v1,v2,v3) in zip(vec1, vec2, vec3):
    print(v1 + v2 + v3)


print()
print('while Loops:')
print('---------------------------------------')

# _while_ loops iterate as long as the loop's Boolean condition remains True.  While loops
# are necessary when the number of loop iterations is unknow before entering the loop:

a = -10
while a <= 10:
    print(a)
    a += 1

# Infinite loops will continue indefinitely (until hitting a break statement).

while True:
    if int(input('enter number > 10 to end: ')) > 10:
        break

# You can also end an infinite loop manually in the IDE by hitting the stop button,
# or by pressing control-C in the shell:


"""
PRACTICE PROBLEMS

1. Use a for loop to calculate the sum of numbers from 1 to 20.
2. Use a while loop to calculate the sum of numbers from 1 to 20.
3. Use a for loop to print each character of the string "ENME202" on a new line.
4. Use a while loop to print a countdown from 10 to 1.
5. Use a for loop to calculate the factorial of 12, without using math.factorial().
6. Use a while loop to print all positive integers whose factorial is less than 1000
   (ok to use math.factorial() for this problem).
7. Use a for loop to print the list ['a','b','c',1,2,3] in reverse order (do not
   using the list reverse() method or list slicing to perform the inversion).
8. Use a while loop to calculate the sum of the digits of a given number 
   (e.g. given 123 the result is 1+2+3 = 6).
9. Use nested for loops to print all prime numbers between 1 and 100.
10. Use a for loop to find the first 5 terms of the Taylor series expansion for 
    cos(x), and use the result to estimate cos(pi/4).
11. Repeat the previous problem using a while loop to continue taking Taylor series
    terms until the different between successive terms is less than 1e-6.
12. Use nested for loops to print N lines of the following pattern:
    *
    **
    ***
    ****
    Demonstrate this for 10 lines. You _must_ use nested for loops (hint: consider
    using the loop variable from the outer loop when defining the inner loop's iterable).
13. Use nested for loops to generate a multiplication table (1 to 10) in grid format. 
    Use string formatting to align the table elements appropriately.
14. A sensor is used to measure a voltage every 0.5 s, with measured voltage values 
    stored in the following Python list:
        v = [2.41, 2.22, 2.53, 0, 3.14, 2.98, 1.66, 2.43]
    Use a for loop and the enumerate() function to display the measurement time and 
    voltage for all readings with the following example format:
        t = 0: V = 2.41
        t = 0.5: V = 2.22
        etc. 
15. A different sensor system records voltage values at random time points, and stores
    the time and voltage values in separate lists:
        t = [0.6, 1.7, 4.6, 12.2, 15.0, 31.9, 33.2, 52.6]
        v = [2.41, 2.22, 2.53, 0, 3.14, 2.98, 1.66, 2.43]
    Use a for loop and the zip() function to display these values in the same format
    as the previous problem.
16. Use a for loop and the enumerate() function to calculate the following expression:
         N
         Σ (2^i * p(i))
        i=0
    where p = [1,2,3,...] is the list of positive integers. You _must_ use enumerate()
    to generate values of i in this problem (even though there are easier ways to 
    solve this).

"""







