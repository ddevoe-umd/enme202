# Python Dictionaries

# A dicionary data structure consists of a collection of _unordered_ 
# and _mutable_ (key : value) pairs. Each key within a dictionary must be
# unique.  Dictionary values are _heterogeneous_.

"""
TOPICS
------
Dictionary Basics
Extracting Dictionary Keys and Values
Copying Dictionaries
Referencing Non-Existent Keys
Removing Items from a Dictionary
"""

print()
print('Dictionary Basics')
print('---------------------------------------')

# Declare an empty dictionary, and add key,value pair entries
demo_dict = {}                       # declare an empty dictionary
demo_dict["words"] = "hi there"      # add a string
demo_dict"count"] = 99              # add an integer
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
# conver the dict_keys object to a list if needed
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
d = {"foobar":123, "this":"that", 2:(123, 'x')}
# print(d['nope'])     <--- this would raise an error, so instead do the following:
print(d.get('nope'))   # None


print()
print('Removing Items from a Dictionary:')
print('---------------------------------------')

# pop(key)
# Removes the item with the specified key, and return the value for that key


# popitem()
# Removes the item that was last inserted into the dictionary (be careful,
# in earlier versions of Python popitem() would remove a random item)


# del dict[key]
# Remove an item with specified key name (nothing is returned)


# clear()
# Clear the dictionary items (leaving an empty dict)
d.clear()
print(d)


print()
print('PRACTICE PROBLEMS')
print('---------------------------------------')

practice = """
Easy
1. Create a Dictionary: Create a dictionary with keys "name", "age", and "city" and corresponding values "Alice", 25, and "New York".
2. Access a Value: Access the value associated with the key "name" in the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
3. Add a Key-Value Pair: Add a new key-value pair "country": "USA" to the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
4. Update a Value: Update the value of the key "age" to 30 in the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.

Medium
5. Remove a Key-Value Pair: Remove the key "city" from the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
6. Check for a Key: Check if the key "age" exists in the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
7. Dictionary Length: Find the number of key-value pairs in the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
8. Merge Dictionaries: Merge two dictionaries: dict1 = {"a": 1, "b": 2} and dict2 = {"c": 3, "d": 4}.
9. Default Value: Use the get() method to retrieve the value of the key "email" from the dictionary person = {"name": "Alice", "age": 25, "city": "New York"} with a default value of "Not Provided".

Hard
10. Nested Dictionary Access: Access the value "Math" from the nested dictionary student = {"name": "Alice", "grades": {"Math": 90, "English": 85}}.
11. Keys and Values: Extract the list of keys and the list of values from the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
12. Pop a Value: Use the pop() method to remove and retrieve the value of the key "age" from the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.
13. Create from Lists: Create a dictionary from two lists: keys = ["a", "b", "c"] and values = [1, 2, 3].
14. Immutable Keys: Explain why the tuple (1, 2) can be a dictionary key, but the list [1, 2] cannot. Provide an example of a dictionary with a tuple as a key.
15. Clear a Dictionary: Remove all key-value pairs from the dictionary person = {"name": "Alice", "age": 25, "city": "New York"}.

"""
print(practice)






