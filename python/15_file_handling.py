# Overall Topic

""" 
Topics
------
File Operations
Opening Files Using with
Files as Iterators
JSON Files
CSV Files
"""


print()
print('File Operations:')
print('---------------------------------------')


# To access a file for reading, a file object must be created:

f = open("myfile.txt")

# The file must be located in the current working directory (the directory
# from which the Python code was run), or the path to the file must
# be specified in the open() function

# Use the read() method to read the contents of the file (from the current
# position to the end) into a string that including newline characters:

contents = f.read()
print(contents)

# Files should (must!) always be closed when finished with read/write operations:
f.close()

# Files can be opening for both reading and writing using one of the
# followig file opening modes:
#
#   f = open(filename, 'r')   <-- read (default, can omit ‘r’) (file must exist)
#   f = open(filename, 'w')   <-- write by overwriting file (create new if none)
#   f = open(filename, 'a')   <-- write by appending (create new if none)
#   f = open(filename, 'x')   <-- write new file only (error if existing file)
#   f = open(filename, 'r+')  <-- read + write (file must exist, content preserved)
#   f = open(filename, 'w+')  <-- read + write (overwrite, create new if none)

# Use the write() method to add a string to a file at the current position:
f = open("myfile.txt", 'w')
f.write('new text') 
f.close()

# Check to see that the text was written:
f = open("myfile.txt")
contents = f.read()
print(contents)

# The current position in the file is set to 0 when the file is opened. We can
# place the position programatically using the seek() method.
#
# seek(n) sets the file position to n bytes (n = 0 for start of file,
# 1 byte per character):
f = open("myfile.txt")
f.seek(5)              # move the current file position to the 6th byte
remainder = f.read()   # read the remainder of the file     
print(remainder)
f.close()

# Text encoding is platform-dependent (e.g. cp1252 in Windows, utf-8 for just 
# about everything else). Specifying encoding make your code more robust:
f = open('myfile.txt', mode = 'r', encoding = 'utf-8')



print()
print('Opening Files Using _with_:')
print('---------------------------------------')

# Python’s _with_ statement can be used to simplify the syntax for handling
# errors with file I/O. The file will automatically close at end of the _with_
# block _even if an exception is raised_. 

with open("test.txt", mode = 'w+') as f:
  f.write("hello there")


print()
print('Files as Iterators:')
print('---------------------------------------')

# File objects are iterators, with each iteration yielding the next line in the file
# as a string.  Note that all characters from each line, including newline characters, 
# are included in the string.

with open('myfile.txt') as f:
	for line in f:
        print(line.strip())   # use strip() to remove newlines


print()
print('JSON Files:')
print('---------------------------------------')

# JSON (JavaScript Object Notation) is a common text format used for storing
# structured data.  The _json_ module offers powerful tools for creating and 
# manipulating JSON data, including reading/writing JSON files.

import json

# The JSON structure is similar to a Python dictionary, consisting of key-value pairs
# within objects enclosed in curly braces {}. 
#
# Keys must be strings (typically in double quotes).
#
# Values can be any of:
#    objects (enclosed in curly braces {})
#    lists (enclosed in square brackets [])
#    strings
#    numbers
#    booleans (true or false)
#    null

# A Python dictionary can be converted to a JSON string using the
# json.dumps() method:

my_dict = {'A': 1, 'B': 'foo', 3: 0.192}
my_dict_as_json = json.dumps(my_dict)
print(my_dict_as_json)

# Notice that the integer key in my_dict was converted to a string in the
# JSON representation of the dictionary.

# The resulting JSON value is just a string:
print(my_dict_as_json.split(':'))

# Here is an example of a more complex dictionary converted to JSON:
my_dict = {'k_list': [1,2,3], 'k_dict': {'A':1, 'B':2}, 'k_dict_list_tuple': {'a':[4,5,6], 'b':(7,8,9)}, 'k_bool':False}
my_dict_as_json = json.dumps(my_dict,)
print(my_dict_as_json)

# The result is hard to parse!  Let's make it easier to interpret by
# telling json.dumps() to show each value on a separate line, with
# indentation to show the level of each value:
 
my_dict_as_json = json.dumps(my_dict, indent=4)
print(my_dict_as_json)

# Great, now we know how to convert a dictionary to a JSON string.  How do
# we store this data in a JSON file?  We could open a file for writing, and 
# the write the string to the file, but the _json.dump()_ method simplifies
# this process.  The syntax for json.dump() is:
#
#    json.dump(dict, file)

with open('datafile.json', 'w+') as f:
  json.dump(my_dict, f)
with open('datafile.json') as f:    # Display the JSON-formatted file
  print(f.read())

# If we want to JSON file to be more readible (to humans), we can add 
# indentation to json.dump() just as for json.dumps():
with open('datafile.json', 'w') as f:
  json.dump(my_dict, f, indent=4)
with open('datafile.json') as f:    # Display the JSON-formatted file
  print(f.read())

# The json.load() method can be used to read an existing JSON-formatted file
# directly into a Python dictionary:

with open('datafile.json') as f:
  new_dict = json.load(f)
print(new_dict)
print(new_dict['k_list'])
print(new_dict['k_dict_list_tuple']['b'])

# Note that we can also convert a JSON string (rather than a file) using
# the json.loads() method.



print()
print('CSV Files:')
print('---------------------------------------')

# CSV (comma-separated values) data is another common data format used 
# in many programming contexts, particularly for working with tabular
# data and in data science.
#
# The Python _csv_ module makes working with CSV-formatted files (and 
# strings) straighforward:

import csv

# The csv.reader(f) method returns a list of strings for each line in a
# CSV file, with each list entry defined by the line substrings
# separated by commas.  For example, consider a CSV file with the
# following format:

with open('data.csv', 'w+') as f:
    print(f.write('1,2,3\n4,5,6\n7,8,9'))

# Convert the data in this file into a 2D list:

with open('data.csv') as f:
    array = []
    csv_reader = csv.reader(f)
    for row in csv_reader:
        array.append([row[0], row[1], row[2]])

print(array)



print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
Easy
1. Reading a File: Open a file named example.txt in read mode and print 
   its contents line by line.
2. Writing to a File: Create a new file named output.txt and write the 
   string "Hello, World!" to it.
3. Appending to a File: Open the file output.txt and append the string 
  "This is an additional line.".
4. File Existence Check: Write a program that checks if a file named 
   data.txt exists in the current directory.

Medium
1. Counting Lines in a File: Write a program to count the number of lines
   in a file named example.txt.
2. Reading Specific Lines: Open example.txt and print only the first 3 lines.
3. Copying a File: Write a program to copy the contents of source.txt into 
   a new file named destination.txt.
4. Word Count: Write a program that counts the number of words in example.txt.
5. File Modes: Experiment with file modes (r, w, a, r+, etc.) by opening 
   a file and observing the results of writing and reading.
6. Parsing Lines in a File: Write Python code to calculate the sum of all
   values in data.txt, which contains one numerical value on each line. 

Hard
1. Reading a File Backwards: Write a program to read and print the lines 
   of example.txt in reverse order (last line to first).
2. CSV File Handling: Use the Python csv module to write a list of 
   dictionaries [{‘name’: 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
   to a CSV file named people.csv. Then, read the CSV file and print the 
   contents.
3. JSON File Handling: Repeat the previous problem using a JSON file and 
   Python json module.
4. File Splitter: Write a program that splits a large file into smaller
   files of N lines each.
5. Word Frequency Counter: Read example.txt and count the frequency 
   of each word, ignoring case. Save the results in word_frequency.txt.
   File Searcher: Write a program that searches for a specific word in 
   example.txt and prints the line numbers where the word is found.
6. Binary File Handling: Create a program to write and read binary data to
   a file. For example, write a list of integers as binary data and read it
   back.

"""
print(practice)







