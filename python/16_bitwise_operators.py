# Bitwise Operators

""" 
Topics
------
Bitwise Operator Summary
Declaring and Displaying Binary Words
Operator Precedence
Bit Shifting
Bit Masks
"""

print()
print('Bitwise Operator Summary:')
print('---------------------------------------')

"""
Bitwise operators compare or evaluate individual bits within _binary words_
(sequences of binary values).  Unlike Boolean operators, which yield single
True/False values, bitwise operators act on multiple values within a pair
of binary words to yield a new binary word, where each bit in the new sequence
is determined by comparing the corresponding bits in the initial word pair.

Summary of bitwise operators:

x & y    AND
x | y    OR
~x       COMPLEMENT (NOT)
x ^ y    XOR (exclusive OR)
x << n   shift bits left n places (same as multiplying by 2**y)
x >> n   shift bits right n places (same as dividing by 2**y)

"""


print()
print('Declaring and Displaying Binary Words:')
print('---------------------------------------')

# Values of +all+ types are stored in the computer as binary words.
# Thus it is a misnomer to talk about "declaring" a binary value.
# Rather, we want to be able to understand how to create a value
# correspomding to a bit sequence that defines the desired binary word.

# The int() function can be used to convert values from different
# number bases to base 10, providing one option for converting between
# binary (base 2) and decimal (base 10). The function has the form:
#
#   int(value_as_string, base)
#
# Example: convert 0101 (base 2) to decimal:
x = int('0101',2)  # 0101 (b2) = 5 (b10)

# We can also directly declare binary values by preceeding a binary
# value with _0b_ as follows:
y = 0b0110         # 0110 (b2) = 6 (b10)

# Displaying either variable using print() will show a base 10 value!
# We cam display a binary word by either using the bin() function, or
# using string formatting:
print(x) # --> 5
print(bin(x)) # --> 0b101
print("{:b}".format(x))  # --> 101
print(f"{x:b}")

# Hang on...we defined x as a 4-bit word, but only 3 bits appear in 
# the output.  This is because Python does not keep track of 
# leading zeros. If we know the word length, use string formatting
# to control output appearance:

print(f"{x:04b}")  # format output 4 char long using "0" for padding.

print(f"x =     { x   :04b}") 
print(f"y =     { y   :04b}") 
print(f"x & y = { x&y :04b}") 
print(f"x | y = { x|y :04b}") 
print(f"x ^ y = { x^y :04b}") 



print()
print('Operator Precedence:')
print('---------------------------------------')

"""
Bitwise operators have precedence over both comparisons and logical 
(Boolean) operators. Operation precedence (descending order):

   **      (Exponent)
   +x, -x  (Unary addition, Unary subtraction)
   ~x      (Bitwise NOT)
   *, /, //, %  (Multiplication, Division, Floor division, Modulus)
   +, -    (Addition, Subtraction)
   <<, >>  (Bitwise shift operators)
   &       (Bitwise AND)
   ^       (Bitwise XOR)
   |       (Bitwise OR)
   ==, !=, >, >=, <, <=, is, is not, in, not in  (Comparisons, Membership)
   not     (Logical NOT)
   and     (Logical AND)
   or      (Logical OR)
"""

# As a result of precendence rules, the following statements 
# yield different results:
1>2 and 4<5
1>2 & 4<5



print()
print('Bit Shifting:')
print('---------------------------------------')

# Bit shifting "pushes" each bit either left (<<) or right (>>).
x = 0b0101
print(f"x << 1 =       { x<<1 :04b}")
print(f"x >> 2 =       { x>>2 :04b}")
print(f"x & (x << 1) = { x & (x<<1) :04b}")
print(f"x ^ (x << 1) = { x ^ (x<<1) :04b}")

# Can bit shift with the assignment operator:
x >>= 1
print(f"After x >>= 1, x = {x:04b}")

# Right bit shifting – extra bits roll off and are forgotten:
x = 0b0101
print(f"(x >> 3) << 3 =   { (x>>3) <<3 :04b}") 

# Left bit shifting – bits are remembered (word length 
# increases to retain MSB):
print(f"(x << 10) =       {  x<<10        :b}")
print(f"(x << 10) >> 10 = { (x<<10) >> 10 :b}")



print()
print('Complement Operator (Bitwise NOT):')
print('---------------------------------------')

# Now try the complement operator (~): 
print(f"x | ~x =          { x | ~x :b}")

# x | ~x = -1 for any x
# 
# or equivalently, if x is an integer:
# 
# ~x = -(x+1) for any x
#
# Thus ~x will always invert the sign of x (when interpreting
# x as an integer).
#
# This result may not be what you were expecting.
# ~x yields "one's complement" of x, meaning each bit
# is flipped **including all leading bits** that determines
# if the value is positive or negative: Python
# represents a positive number with leading '0' values, and a 
# negative numbers with leading '1' values.
#
# Thus one's complement of a positive number will flip the
# leading zeros into leading ones (due to bit inversion),
# thus making the value negative.
#
# To make matters more confusing, values are represented
# by the computer using "two's complement", which is
# defined by taking one's complement (flipping bits) and 
# adding 1.
#
# How does Python know that 11111010 is -6 and not -3 (in other
# words, how does it inow that this bit:
#                                |
#                            11111010
# is part of the number and not just a leading 1 indicating a negative
# value)?  In languages such as C++, which have fixed-length 
# binary values, the answer would be that the system has to keep
# track of the number of relevant bits, but this is not the case
# in Python, which uses infinite-precision signed integers, and
# performs bitwise operations on actual integers, with the result
# automatically being a valid Python integer rather than a raw bit
# pattern.

# Here is an example:

print( 0b110)   #  6 base 10
print(~0b110)   # -7 base 10 via two's complement:
                #    flip bits:       001 (one complement)
                #    subtract 1:      000
                #    flip bits again: 111 = 7 (negative)

# Just remember that bitwise NOT flips all bits of a binary word, 
# but the result is interpreted using two's complement. As a result,
# when you +display+ the result using either bin() or string formatting
# it will not appear "correctly" (although it will still work the 
# way you expect "under the hood" when comparing binary words of 
# appropriate length):

print(bool(x & ~x))
print(bool(x | ~x))
print(bool(~0b1111 & 0b1111))



print()
print('Bit Masks:')
print('---------------------------------------')

# How do we get ~ to display the expected result without creating
# a negative value?  Use a bit mask to force a leading "0" bit:

x    = 0b11110000
mask = 0b11111111
print(f"x =         {  x   :08b}")
print(f"~x =        { ~x   :08b}")
print(f"mask =      { mask :08b}")
print(f"~x & mask = { ~x & mask :08b}")

# Same idea, returning to our original example:
print(f'x | (~x & mask) = { x | (~x & mask) :08b}')


"""
Bit Fields
"""

# Bit fields are used to store multiple binary values in our code such
# as system states or flags as individual bits of a binary word. 

# Suppose code is being developed to control a mechatronic device with
# the following 4 boolean flags:
#   bit 0: Power on
#   bit 1: Error
#   bit 2: Overheated
#   bit 3: Battery low

# Create bit masks (using bit shifting) to define which bit
# in the status bit field is associated with each state:
POWER        = 1 << 0  # 0b0001
ERROR        = 1 << 1  # 0b0010
OVERHEATED   = 1 << 2  # 0b0100
BATTERY_LOW  = 1 << 3  # 0b1000

# Initial status: Power ON, Error ON, Battery low ON => 0b1011
status = POWER | ERROR | BATTERY_LOW

# Bitwise AND can be used to check flag status (do you see why 
# this works?):
def check_status():
   print(f'\nCurrent status bit field: {status:04b}')
   if status & POWER:
      print('- Device is powered ON')
   else:
      print('- Device is powered OFF')

   if status & ERROR:
      print('- Error detected')
   else:
      print('- No errors detected')
   if status & OVERHEATED:
      print('- Device is overheated')
   else:
      print('- Temperature normal')

   if status & BATTERY_LOW:
      print('- Battery level is low')

check_status()

# Bitwise operators can also be applied to directly modify the flags
# without using any conditionals or other code. 

# Set a flag (turn flag on):
status |= POWER            # Set power ON
status |= ERROR            # Set error flag ON
check_status()

# Set multiple flags at the same time:
status |= POWER | ERROR # Set both power and error flags
check_status()

# Clear a flag (turn flag off):
status &= ~ERROR           # Clear error flag (turn OFF)
status &= ~POWER           # Clear power flag
check_status()

# Clear Multiple Flags at the same time:
status &= ~(POWER | ERROR)   # Clear both power and error flags
check_status()

# Toggle a flag (flip on/off):
status ^= BATTERY_LOW      # Toggle battery low flag
status ^= POWER            # Toggle power state
check_status()

# Toggle multiple flags at the same time:
status ^= POWER_ON | BATTERY_LOW 
check_status()

# Clear all flags while saving status of a selected flag:
status &= ERROR            # Turn all flags off but keep ERROR state unchanged
check_status()

# Clear all flags while saving status of multiple selected flags:
status &= (ERROR | POWER)  # Turn all flags off but keep ERROR & POWER unchanged
check_status()



