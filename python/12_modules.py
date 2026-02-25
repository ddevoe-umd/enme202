# Python Modules

""" 
Topics
------
Built-in Modules
Custom Modules
config Module for Multi-File Global Variables 
"""

print()
print('Built-in Modules:')
print('---------------------------------------')

# Here is a short list of important built-in Python modules:
#
#     math        Mathematical functions and constants
#     os          Interacting with the operating system
#     sys         Accessing system-specific parameters and functions
#     random      Generating random numbers and sequences
#     datetime    Working with dates and times
#     json        Encoding and decoding JSON data
#     csv         Reading and writing CSV files
#     string      High-level string manipulation

# As engineers, you should also be familiar with several foundational
# open-source third-party modules for data manipulation and visualization:
#
#     numpy       Array/matrix processing, AI/ML development
#     scipy       Extension to numpy, data visualization
#     matplotlib  Data visualization and plotting
#     pandas      Data analysis using DataFrame objects


print()
print('Custom Modules:')
print('---------------------------------------')

# Any python code file we write can be imported into another file as a
# custom module.  When a module is imported, all code in the file is automatically
# executed as if the code was run from the command line (or the IDE run button).
# Custom modules are imported by the corresponding file name, ommitting the
# '.py' extension.  For example, if we have a module 'mymodule.py', it is
# imported as 'import mymodule'.

# Note that module names cannot start with a number (like this file!). There
# is a way around this using the importlib() function. You are not responsible
# for this detail in ENME202.

# Often we have code that should have a set of actions when run from the
# command line that are +not+ executed when being imported as a module.
# Code execution only on direct execution can be controlled is the
# __name__ variable.  __name__ is a built-in variable that evaluates to 
# "__main__"  if the current module is executed directly (rather than being 
# imported).  Here is an example:

def run():
  print("run function executed")

if __name__ == '__main__':
  run()
else:
  print("module imported")



print()
print('_config_ Module for Global Variables:')
print('---------------------------------------')

# Global variables defined within a given module retain global scope when
# importing the module into other code.  Sometimes we have globals defined
# in multiple modules that need to be accessible across all of these modules.
# One solution is to cross-import the modules, i.e. module A can import module B,
# and visa versa.  However, this can lead to unexpected behaviors and should
# be avoided!

# The canonical solution for sharing globals across multiple modules is to create
# a special module named "config.py" that contains *all* globals.  The config 
# module can then be imported into all other modules that need access to the
# globals.



"""
PRACTICE PROBLEMS

There are no practice problems for this topic, but it is recommended 
that you review the basics of working with built-in and custom Python modules
"""







