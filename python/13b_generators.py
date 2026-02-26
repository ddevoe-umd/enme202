# Generators

"""
Topics
------
Iterators and Lazy Evaluation
Generator Expressions
Generator Functions and yield
Infinite Generators
Built-In Iterators: range(), enumerate(), zip(), map(), filter()
"""


print()
print('Iterators and Lazy Evaluation:')
print('---------------------------------------')

# When Python evaluates a list comprehension, it builds the entire list
# in memory before returning it.  For large datasets this can be expensive.
#
# An _iterator_ is any object that produces values one at a time, on demand,
# rather than computing them all upfront.  This is called _lazy evaluation_.
#
# A _generator_ is a specific kind of iterator created either by a generator
# expression or a generator function (using yield).  Every generator is an
# iterator, but not every iterator is a generator -- range(), enumerate(), and
# zip() are iterators but are built-in types, not generators.
#
# You advance an iterator one step at a time using the built-in next() function:

squares_list = [x**2 for x in range(5)]   # list: all 5 values in memory at once
squares_gen  = (x**2 for x in range(5))   # generator: no values computed yet

print(type(squares_list))   # <class 'list'>
print(type(squares_gen))    # <class 'generator'>

print(next(squares_gen))    # 0  -- compute and yield the first value
print(next(squares_gen))    # 1  -- compute and yield the second value
print(next(squares_gen))    # 4  -- ...and so on

# When the generator is exhausted, next() raises StopIteration.
# A for loop handles this automatically -- it calls next() repeatedly and
# stops cleanly when StopIteration is raised:

for val in squares_gen:     # picks up where we left off (9, 16)
    print(val)

# Important: a generator can only be traversed once.  After it is exhausted,
# iterating over it again produces nothing.  A new generator object must be
# created to start over.


print()
print('Generator Expressions:')
print('---------------------------------------')

# Generator expressions use the same syntax as list comprehensions,
# but with parentheses instead of square brackets:
#
#    list:      [expression  for var in iterable  <optional if>]
#    generator: (expression  for var in iterable  <optional if>)

# Generator expressions support the same conditionals as list comprehensions:

evens_gen = (x for x in range(20) if not x % 2)

# Convert to a list to display all values at once:
print(list(evens_gen))

# Memory comparison -- a generator for 10 million values uses almost no memory:

import sys

big_list = [x**2 for x in range(10_000_000)]
big_gen  = (x**2 for x in range(10_000_000))

print(f'List size:      {sys.getsizeof(big_list):,} bytes')
print(f'Generator size: {sys.getsizeof(big_gen):,} bytes')

# The generator stores only the recipe (range object + expression), not the values.

# When passing a generator expression as the only argument to a function,
# the outer parentheses can be omitted:

total = sum(x**2 for x in range(10))   # equivalent to sum((x**2 for x in range(10)))
print(total)


print()
print('Generator Functions and yield:')
print('---------------------------------------')

# A _generator function_ uses the _yield_ keyword instead of _return_.
# Calling a generator function returns a generator object without executing
# any of the function body.  The body runs incrementally each time next()
# is called, pausing at each yield and resuming from that point on the
# next call.

def count_up(start, stop):
    n = start
    while n <= stop:
        yield n       # pause here, hand the value to the caller
        n += 1        # resume here on the next next() call

counter = count_up(3, 6)      # create a generator object (body does not run yet)
print(next(counter))          # 3
print(next(counter))          # 4

for val in counter:           # picks up at 5
    print(val)

# Contrast with a regular function: return exits the function permanently,
# discarding all local state.  yield exits temporarily, preserving all local
# variables so that execution can resume exactly where it left off.

# A generator function can yield from any iterable, or even call yield
# multiple times inside a single loop body:

def interleave(seq):
    """Yield each value flanked by dashes."""
    for item in seq:
        yield '---'
        yield item
    yield '---'

print(list(interleave(['A', 'B', 'C'])))


print()
print('Infinite Generators:')
print('---------------------------------------')

# Because a generator produces values on demand, it can describe an
# infinite sequence.  The caller is responsible for deciding when to stop.

def integers_from(n):
    """Yield every integer starting at n, forever."""
    while True:
        yield n
        n += 1

counter = integers_from(0)
print(next(counter))   # 0
print(next(counter))   # 1
print(next(counter))   # 2

# Use break to stop consuming an infinite generator:

counter = integers_from(1)
for val in counter:
    if val > 5:
        break
    print(val)

# Engineering use case: simulate a sensor stream.
# In practice the data would come from hardware; here we use random noise.

import random

def sensor_stream(mean, noise):
    """Yield simulated sensor readings indefinitely."""
    while True:
        yield mean + random.gauss(0, noise)

stream = sensor_stream(mean=5.0, noise=0.1)

readings = [next(stream) for _ in range(6)]   # collect 6 readings
print([f'{v:.3f}' for v in readings])


print()
print('Built-In Iterators: range(), enumerate(), zip(), map(), filter():')
print('---------------------------------------')

# Several built-in functions you have already used return iterators, not lists.
# These are NOT generators (they are built-in types that implement the iterator
# protocol directly), but they behave the same way: values are produced lazily,
# one at a time.  That is why wrapping them in list() is needed to display all values.

# range() -- generates integers on demand (does not store the full sequence):
r = range(5)
print(type(r))          # <class 'range'>
print(next(iter(r)))    # 0  (must call iter() first to get an iterator from range)

# enumerate() -- yields (index, value) tuples one at a time:
e = enumerate(['a', 'b', 'c'])
print(type(e))          # <class 'enumerate'>
print(next(e))          # (0, 'a')

# zip() -- yields paired tuples one at a time:
z = zip([1, 2, 3], ['x', 'y', 'z'])
print(type(z))          # <class 'zip'>
print(next(z))          # (1, 'x')

# map() and filter() (from 17_higher-order_functions.py) also return iterators:
m = map(lambda x: x**2, range(5))
print(type(m))          # <class 'map'>
print(list(m))          # [0, 1, 4, 9, 16]

f = filter(lambda x: not x % 2, range(10))
print(type(f))          # <class 'filter'>
print(list(f))          # [0, 2, 4, 6, 8]

# The key insight: these built-ins are all lazy.  They compute each value
# only when requested, which is why they are memory-efficient for large sequences.


"""
PRACTICE PROBLEMS

Easy
1. Generator Expression -- Cubes: Write a generator expression that yields
   the cube of each number from 1 to 10.  Convert it to a list to display
   the result.
2. Generator Expression -- Filter: Write a generator expression that yields
   only the odd numbers from range(1, 20).  Print each value using a for loop.
3. next(): Create a generator from the expression (x**2 for x in range(5)).
   Use next() to manually retrieve the first three values.

Medium
4. Generator Function -- Countdown: Write a generator function countdown(n)
   that yields integers from n down to 1.
5. Generator Function -- Running Total: Write a generator function
   running_total(values) that takes a list of numbers and yields the cumulative
   sum after each element.  For example, given [1, 2, 3] it should yield 1, 3, 6.
6. Memory Comparison: Create both a list comprehension and a generator expression
   for x**2 where x is in range(1_000_000).  Use sys.getsizeof() to compare
   their sizes.
7. Generator Function -- Fibonacci: Write a generator function fibonacci() that
   yields Fibonacci numbers indefinitely.  Use it with a for loop and break to
   print all Fibonacci numbers less than 1000.

Hard
8. Generator Pipeline: Write two generator functions:
       evens(n)   -- yields even numbers from 0 up to n
       squared(g) -- takes a generator and yields the square of each value
   Chain them so that squared(evens(20)) yields the squares of all even
   numbers up to 20.
9. Sensor Threshold Alert: Write an infinite generator function
   sensor_stream(mean, noise) (as in the lecture notes).  Then write a
   function first_above(stream, threshold) that consumes the stream using
   next() in a while loop and returns the first reading that exceeds
   the threshold.  Test it with mean=5.0, noise=0.5, threshold=6.0.
10. Sliding Window: Write a generator function window(seq, n) that yields
    every contiguous sub-list of length n from seq.  For example,
    window([1,2,3,4,5], 3) should yield [1,2,3], [2,3,4], [3,4,5].
    Use it to compute a 3-point moving average of [1, 4, 2, 8, 5, 7].
"""
