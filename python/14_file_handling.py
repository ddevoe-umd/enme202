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
# from which the Python code was run).  Alternately, the path to the file can
# be specified in the open() function

# Use the read() method to read the contents of the file (from the current
# position, to the end) into a single _string_ including newline characters:

contents = f.read()
print(type(contents))
print(contents)

# Files should always be closed when finished with file access:
f.close()

# File content can also be read one line at a time using the
# readline() method:
f = open("myfile.txt")
for idx in range(3):
    print(f'line {idx+1}: {f.readline()}')


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
f.close()
print(contents)

# The current position in the file is set to 0 (start) when a file is first 
# opened. We can change the position using the seek() method, where
# seek(n) sets the file position to n bytes from the start of the file:
f = open("myfile.txt")
f.seek(5)              # move the current file position to the 6th byte
remainder = f.read()   # read the remainder of the file     
f.close()
print(remainder)

# The number of bytes used by each character depends on the text encoding format
# (e.g. utf-8, utf-16, ascii, etc.).  Specifying text encoding format can make 
# your code more robust:
# f = open('myfile.txt', mode = 'r', encoding = 'utf-8')


print()
print('Opening Files Using _with_:')
print('---------------------------------------')

# Python’s _with_ statement simplifies file I/O. The file will automatically close
# at end of the _with_ block, even if an exception is raised. 

with open("test.txt", 'w') as f:
    f.write("hello there")

with open("test.txt") as f:
    print(f.read())


print()
print('Files as Iterators:')
print('---------------------------------------')

# File objects are iterators, with each iteration yielding the next line in the file
# as a string.  Note that all characters from each line, including newline characters, 
# are included in the string.

with open('myfile.txt') as f:
	for line in f:
        print(line.strip())   # use strip() to remove newline characters


# Advanced: an _iterator_ is a bit different than an _iterable_. The former supports
# the __next__() method, which returns the next element. For example, we can manually 
# step through the first 3 lines of the file as follows:

with open('myfile.txt') as f:
    print(next(f))
    print(next(f))
    print(next(f))

# As an aside, an iterator can be constructed from *any* iterable using the 
# iter() function:

my_list = [1, 2, 3, 4, 5]
my_list_as_iterator = iter(my_list)
print(next(my_list_as_iterator))
print(next(my_list_as_iterator))
print(next(my_list_as_iterator))

# The __next__() method will raise a StopIteration exception if there are no 
# further elements available.

try:
    print(next(my_list_as_iterator))
    print(next(my_list_as_iterator))
    print(next(my_list_as_iterator))
except Exception as e:
    print(type(e))


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
#    objects (same as Python dictionaries, enclosed in curly braces {})
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
# JSON representation of the dictionary, since JSON object keys must be strings.

# The resulting JSON value is just a string:
print(my_dict_as_json.split(':'))

# Here is an example of a more complex dictionary converted to JSON:
my_dict = {'k_list': [1,2,3], 'k_dict': {'A':1, 'B':2}, 'k_dict_list_tuple': {'a':[4,5,6], 'b':(7,8,9)}, 'k_bool':False}
my_dict_as_json = json.dumps(my_dict)
print(my_dict_as_json)

# The result is hard to parse!  Let's make it easier to interpret by
# telling json.dumps() to show each value on a separate line, with
# indentation to show the level of each value:
 
my_dict_as_json = json.dumps(my_dict, indent=4)
print(my_dict_as_json)

# Great, now we know how to convert a dictionary to a JSON string.  How do
# we store this data in a JSON file?  We could open a file for writing, and 
# the write the string to the file, but the json.dump() method simplifies
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

# The above examples involved the use of JSON formatting to work with 
# dictionaries, but the approach can also be used to work with lists,
# which are also supported by the standard JSON data structure. 

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

with open('data.csv', 'w') as f:
    print(f.write('1,2,3\n4,5,6\n7,8,9'))

# Alternately, if we have our data in a 2D list, we can write it to
# a file using the csv.writer() method:
data_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
with open("data.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data_2d)

# The newline='' option in the open() function is prevents Python from 
# inserting extra blank lines between rows when writing to a CSV file
# (especially on Windows).

# Now go the other direction -- read data from the file into a 2D list
# using the csv.reader() method:

with open('data.csv') as f:
    array = []
    csv_reader = csv.reader(f)
    for row in csv_reader:
        array.append([row[0], row[1], row[2]])

print(array)



"""
PRACTICE PROBLEMS

1. Reading a File: Open a file named example.txt in read mode and print 
   its contents line by line.
2. Writing to a File: Create a new file named output.txt and write the 
   string "Hello, World!" to it.
3. Appending to a File: Open the file output.txt and append the string 
  "This is an additional line.".
4. File Existence Check: Write a program that checks if a file named 
   data.txt exists in the current directory.
5. Counting Lines in a File: Write a program to count the number of lines
   in a file named example.txt.
6. Reading Specific Lines: Open example.txt and print only the first 3 lines.
7. Copying a File: Write a program to copy the contents of source.txt into 
   a new file named destination.txt.
8. Word Count: Write a program that counts the number of words in example.txt.
9. File Modes: Experiment with file modes (r, w, a, r+, etc.) by opening 
   a file and observing the results of writing and reading.
10. Parsing Lines in a File: Write Python code to calculate the sum of all
    values in data.txt, which contains one numerical value on each line. 
11. Reading a File Backwards: Write a program to read and print the lines 
    of example.txt in reverse order (last line to first).
12. CSV File Handling: Use the Python csv module to write a list of 
    dictionaries [{‘name’: 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
    to a CSV file named people.csv. Then, read the CSV file and print the 
    contents.
13. JSON File Handling: Repeat the previous problem using a JSON file and 
    Python json module.
14. File Splitter: Write a program that splits a large file into smaller
    files of N lines each.
15. Word Frequency Counter: Read example.txt and count the frequency 
    of each word, ignoring case. Save the results in word_frequency.txt.
    File Searcher: Write a program that searches for a specific word in 
    example.txt and prints the line numbers where the word is found.
16. Binary File Handling: Create a program to write and read binary data to
    a file. For example, write a list of integers as binary data and read it
    back.

"""







