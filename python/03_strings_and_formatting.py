
# Python Strings

""" 
Topics
------
String Basics
String Indexing and Slicing
String Methods
String Formatting
"""

print()
print('String Basics')
print('---------------------------------------')

# A string is a sequence of characters of any length
letter = 'a'
word = 'hello'

# Strings can be defined with single quotes or double quotes
s = "string using double quotes, isn't that nice?"
print(s)
s = 'string containing "double quote" characters'
print(s)

# Multiline Strings
s = '''Use triple-quotes to create a string
that spans multiple lines. A multi-line string can be as
long as desired.'''
print(s)

# Strings can contain spaces:
s = 'this is a string with spaces'
print(s)

# Strings can also contain non-space white characters including
# tabs and newline characters using "escape sequences":
s1 = 'start\t1 tab\t\t\t3 tabs'      # tab escape sequence: \t
s2 = 'this is a\nmultiline string'  # newline escape sequence: \n
print(s1)
print(s2)

# Strings can contain non-alphanumeric Unicode characters using
# the unicode escape sequence (\u) with the appropriate unicode
# character value, for example 03A9 for capital omega:
omega_string = 'Omega symbol: \u03A9'
print(omega_string)

# Find the number of characters in a string using len()
print(len(word))

# String Concatenation
s1 = 'combining'
s2 = 'strings'
s3 = 'together'
space = ' '
s123 = s1 + space + s2 + space + s3
print(s123)


print()
print('String input')
print('---------------------------------------')

# Remember that input(p) displays a prompt (p) to the user, and returns
# a string value given by the user's input:

name = input('Enter your name: ')
print(name)

val = input('Enter an integer value: ')
val = int(val)     # convert string to integer
print(val)


print()
print('String Indexing and Slicing')
print('---------------------------------------')

# Strings are _iterable_ data structures. One consequence is that we
# can index into a string to pull out one or more specific characters.
#
# Use square brackets for indexing
#
# Index values start at 0

word = 'Python'
first_char = word[0]
last_char = word[5]
print(first_char)
print(last_char)

# Negative index allow us to index from the *end* of a string
last_char = word[-1]
second_to_last_char = word[-2]
print(last_char)
print(second_to_last_char)

# However, we cannot "wrap around" the end of the string:
print(word[-2:2])    # yields an empty string

# Multiple characters can be accessed by "slicing" a string
# using paired index values: [start, end+1]
first_three_chars = word[0:3]
word_without_first_and_last_chars = word[1:5]
middle_of_word = word[2:3]
print(first_three_chars)
print(word_without_first_and_last_chars)
print(middle_of_word)

# Slicing with negative indices is allowed
last_two_chars = word[-2:6]
print(last_two_chars)

# If the slicing range starts or ends at the first of last character,
# that value of the range may be ommitted
first_three_chars = word[:2]
last_two_chars = word[-2:]
print(first_three_chars)
print(last_two_chars)

# Indexing with a step: [start, end+1, step]
backwards = 'zyxwvutsrq' 
print(backwards[0:6:2])
print(backwards[0:7:2])
print(backwards[0:-1:2])
print(backwards[0::2])
print(backwards[::2])

# Negative (backwards) steps also work:
print(backwards[5:1:-1])

print()
print('String Methods')
print('---------------------------------------')
"""
s.capitalize()
s.count(substr, start=.., end=..)  # start/end optional
s.lower()
s.upper()
s.strip()
s.isalpha()
s.isdecimal()
s.isspace()
s.startswith(substr)
s.endswith(substr) 
s.find(substr)
s.rfind(substr)
s.strip()
s.replace(old_str, new_str)
s.split(delimiter)
s.splitlines()
s.join(iterable)
"""

# capitalize()
# Return a new string with the first letter capitalized
welcome = "bienvenido bienvenue willkommen"
print(welcome.capitalize())

# title()
# Returns a new string with the first letters of all words capitalized
languages = "Spanish French German"
print(welcome.title())
print(languages.title())

# swapcase()
# Return a new string with lower and upper case letter swapped
print(languages.swapcase())

# count(substr, start=.., end=..)
# Return the number of occurrences of substr in s,
# optionally give the starting and ending position to test
story = 'extreme text exaggeration'
print(story.count('ex'))
print(story.count('ex', 3, -1))   # can use negative indices
print(story.count('ex', 5))       # omit ending index

# endswith(substr)
# Return True if the string ends with substr
print(story.endswith('in'))   # False
print(story.endswith('tion')) # True

# find(substr)
# Return the index of _first_ occurrence of substring
print(story.find('t'))

# rfind(substr)
# Return the index of _last_ occurrence of substring
print(story.rfind('t'))

# isalnum()
# Return True is string contains only alphanumeric characters
print('abc123'.isalnum())    # True
print('abc 123'.isalnum())   # False
print('abc+123'.isalnum())   # False

# isalpha()
# Return True if strong contains only alphanbetic characters
print('abc123'.isalpha())    # False
print('abcABC'.isalpha())    # True
print('abc ABC'.isalpha())   # False

# isdecimal()
# Return True if strong contains only numerical characters
print('123'.isdecimal())     # True
print('123.5'.isdecimal())   # False

# islower()
# Return True if all alphabetic characters in string are lowercase
print('abc 123'.islower())          # True
print('aBc 123'.islower())          # False
print('ABC 123'.islower())          # False

# isupper()
# Return True if all alphabetic characters in string are uppercase
print('abc 123'.isupper())          # False
print('aBc 123'.isupper())          # False
print('ABC 123'.isupper())          # True

# startswith(substr)
# Return True if string starts with substr
quote = 'Beam me up Scotty'
print(quote.startswith('Beam'))     # True
print(quote.startswith('beam'))     # False
print(quote.startswith('B'))        # True

# join()
# Add the string between each element of a list of strings, and
# return the concatenated string (we will talk more about lists
# next lecture)
questions = ['who', 'what', 'when', 'where', 'why']
phrase = ', '.join(questions)
print(phrase + ' are all questions')

# strip()
# Return a new string with leading and trailing whitespace characters
# removed
text = '   \njust some text\n\n'
print(text.strip())

# strip(substr)
# Same as strip() but remove all leading and trailing characters in 
# substr (leaving whitespace alone by default)
print(text.strip('jume\n t'))

# replace(old_str, new_str)
# Replace _all_ occurances of old_str inside the string with new_str,
# and return the result
phrase = 'live by the sword, die by the sword'
print(phrase.replace('sword', 'potato')) 

# splitlines()
# Split a string into a list of substrings based on line breaks
print('this is a\nmultiline string'.splitlines())

# split()
# Split the string into a list of substrings, with the breaks between
# substrings defined by white space in the original string
print(phrase.split())

# split(substr)
# Same as split(), but use substr to determine the break points
print(phrase.split(','))


# For methods that return a string, we can apply another string method
# on the same line as the first method
print('who,whoops,when,where,why'.replace('whoops','what').split(','))


print()
print('String Formatting')
print('---------------------------------------')

"""
Three approaches to controlling string format:
1. C-style syntax
    - basic formatting options, not recommended
2. String format() method
    - more options than C-style format control
3. f-strings 
    - compact and elegant inline formatting

For each option, let's see how to handle formatting for
float, string, and int values using the following format 
control options:
f = float
s = string
d = decimal (integer)
b = binary
e = exponent
x/X = hexadecimal (lower/upper case)

In each case, the formatted string length and numerical precision
is specified as "width.precision" where:
	width = minimum string length (adds leading spaces if needed)
	precision = # digits after the radix
"""

# float, str, and int values to use in strings:
x = 2.5
y = 'half'
z = 5

# 1. C-style syntax
s = '%2.1f is %s of %d' % (x,y,z)
print(s)

# 2. String format() method
s = '{:2.1f} is {:s} of {:d}'.format(x,y,z)
print(s)

# can use numbers in front of colons to specify argument order
print('{2:2.1f} is {1:s} of {0:d}'.format(z,y,x))

# another example comparing format options
r = 6.52
pi = 3.1415
print('Area of circle with radius {} = {}'.format(str(r), str(pi*r**2)))
print('Area of circle with radius {:2.1f} = {:2.2f}'.format(r, pi*r**2))

# 3. f-strings
#
# f-strings are _formatted string literals_
# Syntax: f'text{expression:format}'

s = f'{x:2.1f} is {y} of {z}'
print(s)


# A final point about the print() function: 
# After a print() statement is executed, Python will automatically display
# a newline character in the terminal, so that the next print() statement
# appears on the next line. Sometimes this is not the desired behavior,
# and we want successive print() statements to appear on the same
# line. To achieve this, an "end" argument can be added to print()
# to define the string that will appear after each statement instead
# of newline.

print('no',end='')
print('break')

print('now',end='\t')
print('with',end='\t')
print('tabs')


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """

Easy

1. Write a Python program to concatenate two strings, add a space between them, and print the result.
2. Write a program that takes a string input and prints its length.
3. Write a program to print the first and last characters of a given string.
4. Given a string, extract and print the substring that starts at index 2 and ends at index 5.

Medium
5. Palindrome Check: Write a function to check if a given string is a palindrome.
6. String Replacement: Replace all occurrences of the word "Python" with "Engineering" in a given string.
7. Count Substring Occurrences: Write a program that counts how many times the substring "abc" appears in a given string.
8. String Formatting: Create a formatted string using f-strings to display a name and age, given the variables name and age.
9. Vowel Count: Write a program to count the number of vowels in a given string.

Hard -- problems may require require loops and conditionals!
10. Anagram Check: Write a function to check if two strings are anagrams of each other.
11. First Non-Repeating Character: Write a program to find the first non-repeating character in a string.
12. Longest Word: Write a program that finds and prints the longest word in a given sentence.
13. String Compression: Implement a function that compresses a string using the counts of repeated characters (e.g., "aaabbc" → "a3b2c1").
14. Custom Sorting: Write a function to sort a list of strings by their last character. If two strings have the same last character, sort them by their length.


"""
print(practice)


