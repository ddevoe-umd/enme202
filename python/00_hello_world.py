# Hello World

print()
print('Comments')
print('---------------------------------------')

# This is a single-line comment

"""
This is a multi-line comment between
triple double-quotes
"""

print()
print('Python shell')
print('---------------------------------------')

# This file is a Python script that can be executed to run all
# of the code contained in the file. We can also execute Python
# commands from the command line (i.e. the shell).  For example,
# typing mathematical operations into the shell will display the
# result.  Try it:

1+1
2*3*4
1/2


print()
print('The print() function')
print('---------------------------------------')

# We can control the formatting of displayed strings or other
# values using print() function.
#
# print() takes one of more _arguments_ separated
# by commas, and displays the argument values to the screen.
# If more than one argument is given, the values are displayed
# with a space between each argument. Arguments can also be combined
# (without spaces) using the addition symbol:

print("hello world")

print("hello", "world")

print("hello" + " " + "world")

# By default, the print() function adds a newline character 
# to the end of the string argument. However, sometimes
# we want multiple print lines to generate output on the
# same line. To do this, add a second "end" argument to 
# replace the default newline with a _null string_:

print("hello world...", end='')
print("and hello again ")

# The "end" value can be any valid string, such as:

print("hello", end='...and\n')
print("goodbye ")


print()
print('Code block indentation')
print('---------------------------------------')

# Indentation matters!  The following line will "throw an error"
# (if uncommented) because it is indented with 4 spaces instead
# of beling aligned with the left side of the text file:
#
#    print("fail")
#
# Each code block must use the same level of white space (tab 
# or space) indentation.  A good standard is to use 4 spaces for 
# indentation of each code block.  For example, here is a nested
# loop with 2 levels of indentation:

for i in range(2):
    print()
    for j in range(3):
        print("hello world!", end='  ')
print()
print('all done')


print()
print('Importing Modules:')
print('---------------------------------------')

# A Python module is similar to a C/C++ _library_.  Modules are Python
# code files that can be imported into other codes, giving access to
# objects (variables, functions, etc.) defined in the module. 

# Modules are imported using the _import_ keyword.  We will later learn about 
# several built-in modules, but for now let's focus on the _math_ module, which
# includes "C standard" math functions (trig functions, logarithmic functions, 
# etc.) as well as key mathematical constants (pi, e):

import math

# _import_ statements can happen anywhere in our code, but they are most commonly
# placed at the top of the code to make it easy to see which modules
# the code is dependnt on. Once a module has been imported, we can access
# objects defined in the module.  

# Try executing these lines in the Python shell:

math.pi          # pi = 3.1415...
math.e           # Euler's number, e = 2.7182...
math.sqrt(2)     # square root
math.pow(2, 3)   # same as 2**3
math.floor(9.81) # round down to nearest integer (clip after radix)
math.ceil(9.81)  # round up to nearest integer
math.log(math.e) # ln (log base e)
math.log10(100)  # log base 10
math.sin(math.pi/2)   # trig functions (sin, cos, tan)
math.asin(0.5)        # inverse trig functions (asin, acos, atan)

# hyperbolic trig functions are also available (sinh, asinh, etc.)

# If we don't want to prepend the module name ahead of each imported object,
# objects can be imported individually using the _from_ keyword, brining the
# object names into the main namespace:

from math import pi, e     # import multiple objects on a single line
pi
e

# The name of an imported module can be changed using the _as_ keyword:
import math as m
m.sqrt(9)

# Imported object names within the main namespace can be also changed using
# the _as_ keyword:

from math import log as ln
ln(e**8)

