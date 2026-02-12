# Dictionaries

# A dicionary data structure consists of a collection of _unordered_ 
# and _mutable_ (key : value) pairs. Each key within a dictionary must be
# unique.  Dictionary values are _heterogeneous_.

"""
TOPICS
------
Dictionary Basics
Extracting Keys and Values
Copying Dictionaries
Referencing Non-Existent Keys Using get()
Removing Items from a Dictionary
Combining Dictionaries
"""

print()
print('Dictionary Basics')
print('---------------------------------------')

# Declare an empty dictionary, and add key,value pair entries
demo_dict = {}                       # declare an empty dictionary
demo_dict["words"] = "hi there"      # add a string
demo_dict["count"] = 99              # add an integer
demo_dict["list"] = ["bar", 25]      # add a list
demo_dict[4] = "foobar"              # use an integer key
print(demo_dict)
print(len(demo_dict))

# Dictionaries can also be constructed directly without starting 
# with an empty dictionary:
another_dict = {"foobar":123, "this":"that", 2:(123, 'x')}

# Add another item to the new dictionary
another_dict['new'] = 12
print(another_dict)

# Access values associated with a given key
print(demo_dict['words'])
print(demo_dict["list"])
print(demo_dict["list"][1])
print(demo_dict[4])

# Modify the value associated with a given key
demo_dict[4] = "foobar"
demo_dict['count'] = 'now I am a string'
demo_dict['list'] = True
print(demo_dict)


print()
print('Extracting Dictionary Keys and Values:')
print('---------------------------------------')

# keys()
# Return all dictionary keys as a dict_keys object -- use list() to
# convert the dict_keys object to a list if needed
k = demo_dict.keys()
print(k)
k_list = list(k)
print(k_list)

# values()
# Return all dictionary values as a dict_values object
v = demo_dict.values()
print(v)
v_list = list(v)
print(v_list)

# items()
# Return dictionary key:value pairs as a dict_items object 
# (an iterator of tuples)
it = demo_dict.items()
print(it)
it_list = list(it)
print(it_list)


print()
print('Copying Dictionaries:')
print('---------------------------------------')

# Just as with lists, the assignment operator (=) only creates a shallow copy
# of a dictionary.

shallow_copy_dict = demo_dict   # shallow copy
deep_copy_dict = demo_dict.copy()


print()
print('Referencing Non-Existent Keys:')
print('---------------------------------------')

# Referencing a dictionary key that does not exist raises an error.
# To avoid this, use the get() method which returns None (NoneType data
# type) if the key does not exist
d = {"foobar":123, "this":"that", 2:(123, 'x'), 0:1.23}
d.get("this")          # returns "that"
# d["nope"]            # this would raise an error, so instead do the following:
print(d.get('nope'))   # returns None


print()
print('Removing Items from a Dictionary:')
print('---------------------------------------')

# pop(key)
# Removes the item with the specified key, and return the value for that key
x = d.pop('foobar')
print(x)

# popitem()
# Removes the item that was last inserted into the dictionary (be careful,
# in earlier versions of Python popitem() would remove a random item)
x = d.popitem()
print(x)

# del dict[key]
# Remove an item with specified key name (nothing is returned)
del d['this']
print(d)

# clear()
# Clear the dictionary items (leaving an empty dict)
d.clear()
print(d)


print()
print('Combining Dictionaries:')
print('---------------------------------------')

# The d1.update(d2) method combines dictionaries d1 and d2. If the same key
# exists in both dictionaties, the value from d2 is used.
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d1.update(d2)
print(d1)

# Dictionaries can also be combined using the _bitwise or_ operator (|)
# which we will learn about soon.  Unlike update(), this operator
# does not modify either dictionary.

d1 | d2


"""
PRACTICE PROBLEMS

Easy
1. Create a dictionary with keys "name", "age", and "city" and corresponding values "Alice", 25, and "New York".
2. Display the value associated with the key "name" in the dictionary.
3. Add a new key-value pair "country": "USA" to the dictionary.
4. Update the value for the key "age" to 30.

Medium
5. Remove the key "city" from the dictionary.
6. Check if the key "city" exists in the dictionary without throwing an error.
7. Find the number of key-value pairs in the dictionary.
8. Merge two dictionaries: dict1 = {"a": 1, "b": 2} and dict2 = {"c": 3, "d": 4}.
9. Create a list containing all of the keys in the merged dictionary from problem 8.
10. Create a list containing all of the values in the merged dictionary from problem 8.

Hard
Given the following list of dictionaries, answer the questions below:
grades = [{"name": "Smith", "grades": {"ENME202": 100, "ENME351": 85.5}},
          {"name": "Jones", "grades": {"ENME202": 85.5, "ENME351": 99}} ]
11. Display Smith's grade in ENME202
12. In a single line of code, and assign Jones' grade for ENME202 to a variable g while also
    removing the key,value pair associated with the key "ENME202" from the dictionary for Jones.
13. Remove all key-value pairs from the dictionary for Smith.
14. Explain why the tuple (1, 2) can be a dictionary key, but the list [1, 2] cannot. Provide an example 
    of a dictionary with a tuple as a key.
"""







