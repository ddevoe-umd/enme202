# Object-Oriented Programming

""" 
Topics
------
Object-Oriented Programming
Defining a Class
Object Declaration
Instance Methods
Class Methods
Method Chaining
Magic (Dunder) Methods
Class Composition
Class Inheritance
Multiple Inheritance
Method Overriding
Overriding Magic Methods
Class Attributes
Private Attributes and Methods
"""

import math  # We will use the math module in several class definitions


print()
print('Object-Oriented Programming:')
print('---------------------------------------')

# A _class_ describes a set of attributes (variables) and methods (functions) that
# are common to any variable declared as an _instance_ of the class.  Such variables
# are called _objects_ and are _members_ of the class from which they were
# instatiated.  
#
# Attributes and methods defined in a class are available to every instance of that
# class, but attribute values can differ between objects instantiated from the same class.
# In this sense, the class acts as a cookie cutter to shape multiple cookies (objects)
# which can then be "decorated" in different ways (given different attribute values).
#
# There are many advantages to object-oriented programming (OOP)!
# 1. Classes/objects abstract the code design process: 
#    - bundle together related attributes and methods.
#    - provide a more logical structure to the code.
#    - large programs become easier to plan and implement.
# 2. Classes can hide their internals from other programmers.
# 3. Classes can be extended through inheritance to create new classes with expanded
#    functionality as needs grow.
# 4. Classes are easily re-used across multiple codes.
# 5. Maintaining object-oriented code is easier than procedural code, since changes
#    are fully modular.


print()
print('Defining a Class:')
print('---------------------------------------')

# The _class_ keyword is used to create a class definition.  By convention use PascalCase
# for class names.  The basic class definition uses the following syntax:

class ClassName:
    # class attributes and class methods (if any) are defined in main block

    def __init__(self):
         # class constructor (optional)
         # instance attributes are defined in constructor
         # stuff to do when creating a new object goes here
         pass

    def __del__(self):
         # class destructor (optional)
         # stuff to do when deallocating an object from memory goes here
         pass

# The __init__ function (with double-underscores) is called the class _constructor_
# or _instantiation method_.  The constructor is run each time a new member of the
# class is declared.
#
# The __del__ function is called the class _destructor_. The destructor is run each 
# time class instance is deleted from memory.
#
# The _self_ parameter in __init__ and __del__ references the instance of the class 
# being operated on.
#
# The constructor and destructor methods are optional.

# Here is a simple class with _instance attributes_ x, y, z defining a point in 
# 3D Cartesian space.

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


print()
print('Object Declaration:')
print('---------------------------------------')

# The Point class is now a new data type available in our code. A variable
# of type Point is called an _object_ or _instance_ of the Point class.
# Let's declare a few Point objects, and change their attribute values:

p1 = Point()
print(f'{p1.x}, {p1.y}, {p1.z}')

# Attribues of a given object can be changed at any time:
p2 = Point()
p2.x = -12.5
p2.y = 0
p2.z = 7
print(f'{p2.x}, {p2.y}, {p2.z}')


# ---------------
# Assigning attribute values at instantiation
# ---------------

# The above Point class sets the default x,y,z values to 0, and forces the coder
# to manually assign each value after object instantiation.  Not very elegant!
#
# Let's re-define the Point class to accept attribute values through the 
# class constructor:

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p1 = Point(10, 4, 6)
print(f'{p1.x}, {p1.y}, {p1.z}')


# ---------------
# Default attribute values
# ---------------

# The revised Point class now +requires+ that we pass initial values for the
# instance attributes on instantiation.  Just as with any other function, we
# can provide defaut attribute values that will be assigned in the absence of
# arguments during instantiation:

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

p1 = Point(1,2,3)
print(f'{p1.x}, {p1.y}, {p1.z}')

p2 = Point()
print(f'{p2.x}, {p2.y}, {p2.z}')

p3 = Point(y=3)
print(f'{p3.x}, {p3.y}, {p3.z}')


print()
print('Instance Methods:')
print('---------------------------------------')

# The utility of a class can be greatly expanded by providing _instance methods_
# that can be accessed by all class instances.  The first argument of an
# instance method must be _self_, allowing the method to access attribute
# values for the particular instance calling the method.
#
# Here is an expanded Point class with 3 instance methods:
#  distance()  -- return the distance between the Point and a second Point
#  length()    -- return the distance from the origin to the Point
#  stringify() -- return Point values in a string as "(x,y,z)"

class Point:
    """3D Cartesian point class"""       # doc string
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def distance(self, p):      # distance to a second Point
        return(((self.x-p.x)**2 + (self.y-p.y)**2 + (self.z-p.z)**2)**(1/2))
    def length(self):               # distance from origin to the Point
        return(self.distance(Point(0,0,0)))
    def stringify(self):
        return(f'({self.x},{self.y},{self.z})')

p1 = Point(10, 4, 6)
print(f'length of {p1.stringify()} = {p1.length()}')

p2 = Point(-8, 7, 14)
print(f'distance between {p1.stringify()} and {p2.stringify()} = {p1.distance(p2)}')


# Remember that heterogenous built-in data types like lists can hold any valid data type,
# including custom class objects.  Here we form a list of Point values, and iterate through 
# the list to display info for each Point:

p2 = Point(-12.5, 0, 7)
p3 = Point()
p4 = Point(y=3)
points = [p1, p2, p3, p4]
for p in points:
    print(f'distance to {p.stringify()} = {p.length()}')



print()
print('Class Methods:')
print('---------------------------------------')

# Class methods apply to the class itself (rather than instances), and are denoted
# by a _decorator_ to the function as shown below. Class methods are used to access 
# or modify class-level data, such as class attributes, or to create "factory methods"
# that return class instances with specific configurations, as in this example:

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    @classmethod           # decorator
    def point123(cls):
        return cls(1,2,3)

# The _cls_ argument is the Point class itself, and the method above instantiates the
# class using values of x,y,z = 1,2,3 to create a new object:

new_point = Point.point123()



print()
print('Method Chaining:')
print('---------------------------------------')

# Method chaining allows multiple methods to be called on an object sequentially
# in a single line of code. This makes the code more concise and readable.
#
# To enable method chaining, each method must return the object itself 
# (usually _self_).

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def set_x(self, val):
        self.x = val
        return self        # need to return self for chaining
    def set_y(self, val):
        self.y = val
        return self        # need to return self for chaining
    def set_z(self, val):
        self.z = val
        return self        # need to return self for chaining

p = Point()
p.set_x(2).set_y(3).set_z(-1)
print(f'{p.x}, {p.y}, {p.z}')


print()
print('Magic (Dunder) Methods:')
print('---------------------------------------')

# All classes, including both built-in and custom classes, have a number of built-in 
# class attributes and methods called _magic attributes/methods_ (also known 
# as _dunder_ attributes/methods since they are surrounded by Double UNDERscores).

# The dir() function returns a list of all magic attributes/methods available for
# a given class:

print(dir(Point))

#    __dict__   Dictionary with class namespace
#    __doc__    Class documentation string
#    __name__   Class name
#    __module__ Module where class is defined ("__main__" or name of imported module)
#    __bases__  Tuple of all base classes the current class inherits from
#    and more...

print(Point.__dict__)
print(Point.__doc__)
print(Point.__name__)
print(Point.__module__)
print(Point.__bases__)

# Since everything in Python is an object, we can apply these attributes to other
# items including built-in data types, functions, etc:

print(int.__bases__)

print(list.__doc__)

def my_function():
    pass
print(my_function.__name__)

print(dir(dict))


# ---------------
# Classes as iterables
# ---------------

# Magic methods can give custom classes access to complex operations built into Python.
# For example, we can make class instances +iterable+ using the __iter__ method
# which, together with the iter() function, define how iterating through an object should occur.

# Here is a simple example of an iterable class:

class CountDown:
    def __init__(self, max):
        self.max = max

    def __iter__(self):  # Make the class iterable
        return iter(range(self.max, -1, -1))  # Return an iterator over the range

for val in CountDown(5):
    print(val)

# A more complex (and contrived) iterable class example:

class ListOfLists:
    def __init__(self, vals):
         self.vals = vals

    def __iter__(self):  
        # Use a generator to create an iterator to return via iter():
        second_value_list = (item[1] for item in self.vals)  
        return iter(second_value_list)

data = [(1, 'a', 9, 'x'), (2, 'b'), (3, 'c', 7)]
my_list = ListOfLists(data)
for entry in my_list:
    print(entry)

# Note that in the above example, "(item[1] for item in self.vals)" looks like
# list comprehension, but this is actually a _generator_, which is similar
# to list comprehension but is more memory-efficient for cases where we don't need
# to store the entire list in memory at once.


# ---------------
# Classes as iterators
# ---------------

# Instead of making an _iterable_, which uses iter() to return an iterator, the class 
# itself can instatiate _iterators_ that support the use of next() to manually
# iterate through the data elements.
#
# Redo CountDown as an iterator:

class CountDown:
    def __init__(self, max):
        self.current = max

    def __iter__(self):
        return self      # iterators should return themselves

    def __next__(self):  
    # _next__ makes the class an _iterator_, defining the next value to be returned at
    # each iteration, and raising a StopIteration exception when there are no more values
        if self.current <0:
            raise StopIteration
        self.current -= 1
        return self.current+1

# Use as iterable (recall that all iterators are also iterables):
counter = CountDown(5)
for number in counter:
    print(number)

# Use as iterator:
counter = CountDown(5)
print('first value: ', end='')
print(next(counter))
print('second value: ', end='')
print(next(counter))


print()
print('Class Composition:')
print('---------------------------------------')

# Composition: "has a"
# Composition involves defining classes that contain instances of other classes, 
# thereby extending the new class by giving access to attributes and methods 
# from the other class.

# Here is a new Triangle class that contains 3 Point objects, thereby extending
# the Point class by composition:

class Triangle:
    def __init__(self, p1=(0,0), p2=(0,0), p3=(0,0)):
        self.p1 = Point(p1[0],p1[1])
        self.p2 = Point(p2[0],p2[1])
        self.p3 = Point(p3[0],p3[1])
    def perimeter(self):
        side12 = math.sqrt((self.p2.y-self.p1.y)**2 + (self.p2.x-self.p1.x)**2)
        side23 = math.sqrt((self.p3.y-self.p2.y)**2 + (self.p3.x-self.p2.x)**2)
        side31 = math.sqrt((self.p1.y-self.p3.y)**2 + (self.p1.x-self.p3.x)**2)
        return side12 + side23 + side31

tri = Triangle((-2,-5), (-3,3), (0,10))
print(tri.perimeter())


print()
print('Class Inheritance:')
print('---------------------------------------')

# Inheritance: “is a”
# Inheritance involves derived a new class from an existing base class
# to extend base class functionality by inheriting the base class interface
# and implementation.
#
# Classes that inherit from another are termed _derived classes_,
# _child classes_, or _subclasses_.
#
# Classes from which other classes are derived are called _base classes_,
# _parent classes_, or _super classes_.
#
# A derived class _inherits_ or _extends_ a base class.
#
# When one class is derived from another, the derived class inherits:
#    The base class _interface_ (methods, properties, and attributes)
#    The base class _implementation_ (code that implements the class interface)
#
# The super() function gives access to methods and attributes of the parent class.

class Vector:
    """n-dimensional vector"""
    def __init__(self, *args):      # pack all argument values into a tuple
        self.coordinates = args
    def magnitude(self):
        return math.sqrt((sum(c**2 for c in self.coordinates)))

class Vector3d(Vector):
    """3-dimensional vector"""
    def __init__(self, x, y, z):
        super().__init__(x,y,z)     # access parent constructor
    def prism_volume(self):
        [x,y,z] = self.coordinates
        return(x*y*z)

class Vector2d(Vector):
    """2-dimensional vector"""
    def __init__(self, x, y):
        super().__init__(x,y)       # access parent constructor
    def rectangle_area(self):
        [x,y] = self.coordinates
        return(x*y)
    def xy_angle(self):
        [x,y] = self.coordinates
        return math.atan(y/x)

v = Vector(5,2,6,8,3)
v3d = Vector3d(1,2,3)
v2d = Vector2d(1,2)

print(v.magnitude())
print(v3d.magnitude())
print(v2d.magnitude())

print(v3d.prism_volume())

print(v2d.rectangle_area())
print(v2d.xy_angle())



print()
print('Multiple Inheritance:')
print('---------------------------------------')

# Multiple inheritance is the ability to derive a class from multiple base classes,
# allowing simultaneous access to the interfaces of each base class in the new 
# derived class. 
#
# We will not cover this topic in ENME202 beyond recognizing that multiple 
# inheritance is supported by Python.


print()
print('Method Overriding:')
print('---------------------------------------')

# Method overriding allows a child class to provide a specific 
# implementation of a method that is already defined in its parent class,
# allowing the behavior of inherited methods in child classes to
# be customized.
#
# The parent class method can still be accessed using the super() function.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):     # override the Animal.speak() method
        print("Woof!")

class Cat(Animal):
    def speak(self):     # override the Animal.speak() method
        super().speak()  # access parent method via super()
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()


print()
print('Overriding Magic Methods:')
print('---------------------------------------')

# Certain magic methods define how objects are processed by various built-in
# operators.  For example:
#
# __str__     Defines what is sent to standard output by print()
# __add__     Defines what is returned by the addition operator (+)
# __float__   Defines what is returned by type conversion using float()
#
# ...and many more!
#
# We can override magic methods using custom instance methods, allowing us to 
# control how each operator processes our objects:

class Vector:
    """n-dimensional vector"""
    def __init__(self, *args):
        self.coordinates = args     

    def __add__(self, other):
        # Make sure both objects are Vectors:
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to another Vector")
        # Make sure Vectors are the same length:
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must be of the same length")
        
        # If there was no error, we can now add the Vectors by first
        # making a list containing our desired result:
        result = [x + y for x, y in zip(self.coordinates, other.coordinates)]

        # Declare a new Vector object holding the result.  Note that we 
        # must unpack the list (*result) to generate the individual arguments
        # to be sent to the constructor:
        return Vector(*result)    

    def __str__(self):
        return f'Vector: {self.coordinates}'

# First test the raising of exceptions when adding:
v1 = Vector(1,2,3)
v2 = Vector(4,5)
try:
    v3 = v1 + v2    # unmatched lengths (ValueError)
    v3 = v1 + 1     # wrong type of 2nd argument (TypeError)
except Exception as e:
    print(e)

# Now demonstrate adding & displaying vectors:
v1 = Vector(1,12,4,7,3)
v2 = Vector(-9,0,6,6,0)
print(v1 + v2)


# What if we want to add a Vector and a float (interpreted as
# adding the float to each element of the Vector)?

class Vector:
    def __init__(self, *args):
        self.coordinates = args
    def __add__(self, other):
        if isinstance(other, Vector):
            result = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        elif isinstance(other, float) or isinstance(other, int):
            result = [x + other for x in self.coordinates]
        else:
            raise TypeError("Values must be Vector + Vector or Vector + float")
        return Vector(*result)    
    def __str__(self):
        return f'Vector: {self.coordinates}'

v = Vector(1,12,4,7)
print(v + 20)

# Now trigger an exception:

try:
    v + 'x'
except Exception as e:
    print(e)


# Because the arguments in __add__ are ordered as (self, other), this implementation
# will work for Vector + float, but not for float + Vector.  To handle both
# cases, the __add__ method must be supplemented with the +reverse add+ method,
# __radd__:

class Vector:
    def __init__(self, *args):
        self.coordinates = args
    def __add__(self, other):
        if isinstance(other, Vector):
            result = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        elif isinstance(other, float) or isinstance(other, int):
            result = [x + other for x in self.coordinates]
        return Vector(*result)    
    
    # Handle reserved order of addition (number + Vector): 
    def __radd__(self,other):
        if isinstance(other, float) or isinstance(other, int):
            result = [x + other for x in self.coordinates]
        return Vector(*result)

    def __str__(self):
        return f'Vector: {self.coordinates}'

v = Vector(1,12,4,7)
print(v + 20)
print(20 + v)

# Similar "reverse order" methods exist for all other arithmetic and
# bitwise operators. 


print()
print('Destructors:')
print('---------------------------------------')

# We can manually deallocate memory for any variable by using the _del_ 
# command, which will run the __del__() method before releasing the memory.
#
# Destructors are used to perform cleanup activities before an object is 
# deallocated from memory. This can include closing files, releasing network
# connections, or freeing up other resources.
#
# Python's garbage collector automatically handles memory management, but 
# the exact timing of destructor execution is not guaranteed, as it is 
# managed by the garbage collector. 

class Cow:
    def __init__(self):
        print("...")
    def __del__(self):
        print("Goodby cold cruel world")
    def speak(self):
        print("Moo")

a = Cow()
a.speak()
del a


print()
print('Class Attributes:')
print('---------------------------------------')

# Class Attributes are variables that belong to the class itself, rather than
# a specific instance.  They are shared among +all+ instances of the class.
# Class Attributes are directly within the class body, outside of any methods.

class Cow:
    herd_size = 0         # declare a class attribute
    def __init__(self):
        Cow.herd_size += 1
        if Cow.herd_size == 1:
            print('The first cow has joined the herd')
        else:
            print('Another cow has joined')
    def __del__(self):
        Cow.herd_size -= 1
        print('We lost a cow')
        if Cow.herd_size <= 0:
            print('The herd is gone')
    def speak(self):
        print("Moo")

c1 = Cow()
c2 = Cow()
print(f'The herd size is {Cow.herd_size}')
del c1
print(f'The herd size is {Cow.herd_size}')
del c2


print()
print('Private Attributes and Methods:')
print('---------------------------------------')

# Python does not have true private attributes or methods.  However, you can use
# naming conventions to indicate that an attribute or method should not be 
# accessed directly from outside the class using a single leading underscore 
# (_attribute_name or _method_name) to indicate that it is intended for internal
# use within the class only.



"""
PRACTICE PROBLEMS

1. Defining a Class and Object Declaration: Define a class Car with an attribute 
   color. Create an object of this class and set its color to "red".
2. Instance Method: Add an instance method drive to the Car class that prints 
   "The car is driving". Call this method using an object of the class.
3. Magic Method: __str__: Modify the Car class to include a __str__ method that 
   returns the car’s color when the object is printed.
4. Class Attribute: Define a class Circle with a class attribute pi = 3.14. 
   Create an object and access the pi attribute through both the object and the class.
5. Class Composition: Create a class Engine with a method start that prints 
   "Engine started". Create another class Car that contains an Engine object as an 
   attribute and call the start method through the Car object.
6. Class Inheritance: Create a base class Vehicle an instance attribute max_speed 
   (set during initialization) and a method describe() that prints "Maximum 
   speed = {max_speed} km/h". Then create two subclasses:
   Car: Add an attribute num_doors and override the describe method to include 
        the number of doors (e.g., "maximum speed = 200 km/h, 4 doors").
    Motorcycle: Add an attribute has_sidecar (boolean) and override the describe
    method to include whether it has a sidecar (e.g., "maximum speed = 150 km/h, 
    no sidecar").
7. Method Overriding: Create a class Person with a method introduce() that prints 
   "Hello, I'm a person". Create a subclass Engineer that inherits from Person but
   overrides the introduce() method to print "Hello, I'm an engineer".
8. Constructors and Destructors: Create a class FileHandler with a constructor 
   that takes a file name as an argument, opens the file in write mode, and prints
   "File {filename} opened.", and a destructor that closes the file and prints 
   "File {filename} closed.".
9. Custom Magic Method: __add__: Modify the Point class so that the + operator
   can be used to add two Point objects. The result should be a new Point with 
   the sum of the x and y values.
10. Class Attribute vs Instance Attribute: Create a class Book with a class 
    attribute library_name = "Central Library" and an instance attribute title. 
   Create two book objects and demonstrate the difference between class and instance
    attributes.
11. Dynamic Attribute Addition: Create a class Student and an object of the 
    class. Dynamically add an attribute grade to the object and set its value to "A".
12. Method Chaining: Create a class Builder with methods set_height, set_width, 
    and set_color. Each method should return the object itself to allow method 
    chaining.
13. Composition with Multiple Components: Create a class House that contains objects
    of classes Room, Door, and Window. Define appropriate methods in each class and 
    show how the House class interacts with these components. Include appropriate
    class attributes and constructor / destructor code that will keep track of the 
    number of Room, Door, and Window objects as they are declared and deleted.
"""







