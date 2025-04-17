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
(sequences of binary values).  In other words, while boolean operators
work with single True/False values, bitwise operators can be applied to
multiple boolean values within binary words.  

Here is a summary of bitwise operators in Python:

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
# with the desired bit sequence for a given binary word.

# Declare a binary word using int():
x = int('0101',2)  # 4-bit base-2 word: 0101 (b2) = 5 (b10)

# Declare a binary word using 0b syntax:
y = 0b0110         # 0110 (b2) = 6 (b10)

# How to display a binary word?
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
Operation precedence (descending order):
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

print(f"x << 1 =       { x<<1 :04b}")
print(f"x >> 2 =       { x>>2 :04b}")
print(f"x & (x << 1) = { x & (x<<1) :04b}")
print(f"x ^ (x << 1) = { x ^ (x<<1) :04b}")

# Can bit shift with the assignment operator:
x >>= 1
print(f"After x >>= 1, x = {x:04b}")

# Reset x...
x = 0b0101
print(f"x = { x :04b}") 

# Right bit shifting – extra bits roll off and are forgotten:
print(f"(x >> 3) << 3 =   { (x>>3) <<3 :04b}") 

# Left bit shifting – bits are remembered (word length 
# increases to retain MSB):
print(f"(x << 10) =       {  x<<10        :b}")
print(f"(x << 10) >> 10 = { (x<<10) >> 10 :b}")

# Now try the complement operator (~): 
print(f"x | ~x =          { x | ~x :b}")

# x | ~x = -1 for any x
#
# This result may not be what you were expecting.
# ~x yields "one's complement" of x, meaning each bit
# is flipped **including the leading bit** that determines
# if the value is positive or negative: the computer 
# represents a positive number with a leading '0', and a 
# negative number with a leading '1'.
#
# Thus one's complement of a positive number will flip the
# leading zero into a leading 1 (due to bit inversion),
# thus making the value negative.

# To make matters more confusing, values are represented
# by the computer using "two's complement", which is
# defined by inverting all bits and then adding 1:

print( 0b100)   # 0000100
print(~0b100)   # 1111011 <-- but this is -5 via two's complement
                #             (5 = 0b0000101, flip bits, add 1...)

# Note that ~x will always invert the sign of x: ~x = -(x+1)
#
# Just remember that ~ simply flips the bits
# of a binary word, but the result is interpreted using
# two's complement so that when you try to **display** the
# result it will not appear "correctly" (although
# it will still work the way you expect "under the hood"
# when comparing binary words of appropriate length):

print(bool(x & ~x))
print(bool(x | ~x))
print(bool(~0b1111 & 0b1111))


print()
print('Bit Masks:')
print('---------------------------------------')

# How do we get ~ to display the expected result
# without creating a negative value?  Use a bit mask to 
# force a leading "0" bit:

x    = 0b11110000
mask = 0b11111111
print(f"x =         {  x   :08b}")
print(f"~x =        { ~x   :08b}")
print(f"mask =      { mask :08b}")
print(f"~x & mask = { ~x & mask :08b}")

# Same idea, returning to our original example:
print(f'x | (~x & mask) = { x | (~x & mask) :08b}')


# Bit mask example: state tracking

# Say x is a "bit field" with 5 states we want to track:
x = 0b00000  

# Let mask1 and mask2 be bitmasks used to manipulate the field:
mask1 = 0b00110
mask2 = 0b10001

# Turn bit 2 and 3 on:
x |= mask1
print(f'x = { x :05b}')

# Turn bit 1 and 5 on: 
x |= mask2
print(f'x = { x :05b}')

# Flip state of bit 5:
x ^= 1<<4
print(f'x = { x :05b}')

# Turn bit 2 off: 
x &= 0b11101
print(f'x = { x :05b}')

# Turn bit 2 and 3 off:
x &= ~mask1
print(f'x = { x :05b}')

# Flip states of bits 1 and 2:
x ^= 0b00011
print(f'x = { x :05b}')

# Check each state in sequence by shifting
# a single bit to probe each state:
for i in range(5):
    print(f"State {i} = {+bool(x & 1<<i)}")
    # unary addition used to convert bool to int
