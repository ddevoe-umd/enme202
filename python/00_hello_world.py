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
print('The print() function')
print('---------------------------------------')

# The print() statement takes one of more _arguments_ separated
# by commas, and displays the argument values to the screen.
# If more than one argument is given, the values are displayed
# with a space between each argument:

print("hello world")

print("hello", "world")

# By default, the print() function adds a newline character 
# to the end of the string argument. However, sometimes
# we want multiple print lines to generate output on the
# same line. To do this, add a second "end" argument to 
# replace the default newline with a _null string_
# as follows:

print("hello world...", end='')
print("and hello again ")

# The "end" value can be any valid string, such as:

print("hello", end='\n...\n')
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



