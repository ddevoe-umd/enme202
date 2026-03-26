# Bitwise Operators

""" 
Topics
------
Bitwise Operator Summary
Converting Between Base 2 and Base 10
Declaring and Displaying Binary Words (int and bin functions)
Bitwise operations
Operator Precedence
Bit Shifting
Bit Masks
Hexadecimal (Base 16)
"""

print()
print('Bitwise Operator Summary:')
print('---------------------------------------')

"""
Bitwise operators:

   x & y    AND
   x | y    OR
   ~x       COMPLEMENT (NOT)
   x ^ y    XOR (exclusive OR)
   x << n   shift bits left n places (same as multiplying by 2**n)
   x >> n   shift bits right n places (same as dividing by 2**n)

Bitwise operators compare or evaluate individual bits within _binary words_
(sequences of binary values).  Unlike Boolean operators, which yield single
True/False values, bitwise operators act on multiple values within a pair
of binary words to yield a new binary word, where each bit in the new sequence
is determined by comparing the corresponding bits in the initial word pair.

Why do we care about bitwise operators?  Bit fields, bit masks, bit flags, 
finite state machines, graphics operations, compression, encryption, 
communications, etc.

There is no standard or maximum binary word length in Python, so
binary words can be any length.
"""

print()
print('Converting Between Base 2 and Base 10:')
print('---------------------------------------')

"""
Our written system for base 10 (decimal) numbers uses 10 digits (0,1,2,...,9) to 
represent the value. To interpret a multi-digit number we learn at an early age to
evaluate each "power of 10" in the number, with the lowest power at the right end
of the number (ones column) and increasing powers going left (tens column, hundreds
column, etc.). By this convention, we interpret a decimal number like 479 as follows:

479 = 4*10^2 + 7*10^1 + 9*10^0
    = 4*100  + 7*10   + 9*1 
    = 400    + 70     + 9

This same convention applies to *any* number base, inluding base 2 (binary). 
For base 2, we only have 2 digits (0 and 1). For example, a binary value of
110110 is interpreted as a base 10 number like this:

base 2   base 10
|        |
V        V

110110 = 1*2^5 + 1*2^4 + 0*2^3 + 1*2^2 + 1*2^1 + 0*2^0
       = 1*32  + 1*16  + 0*8   + 1*4   + 1*2   + 0*1
       = 54

This approach can be applied to any number base system such as octal (base 8),
hexadecimal (base 16), etc.

"""

print()
print('int() and bin() functions:')
print('---------------------------------------')

# Values of +all+ types are stored in the computer as binary words.
# Thus it is a misnomer to talk about "declaring" a binary value.
# Rather, we want to be able to understand how to create a value
# correspomding to a particular bit sequence.

# The int() function can be used to convert values from different
# number bases to base 10, providing one option for converting between
# binary (base 2) and decimal (base 10). The function has the form:
#
#   int(value_as_string, base)
#
# Example: convert 0101 (base 2) to decimal:
x = int('0101',2)  # 0101 (b2) = 5 (b10)

# We can also directly define binary values by with a leading _0b_:
y = 0b0110         # 0110 (b2) = 6 (b10)

# Displaying either variable using print() will show a base 10 value!
# To display a binary word, either use the bin() function or apply string
# formatting:
print(x)                 # --> 5
print(bin(x))            # --> "0b101"
print("{:b}".format(x))  # --> "101"
print(f"{x:b}")          # --> "101"

# Hang on...we defined x as a 4-bit word, but only 3 bits appear in 
# the output.  This is because Python does not keep track of 
# leading zeros. If the desired word length is known, use string formatting
# to control output appearance:

print(f"{0b1010:04b}")  # format output 4 char long using "0" for padding.

x = 0b0101
y = 0b0110
print(f"x =     { x   :04b}") 
print(f"y =     { y   :04b}")



print()
print('Bitwise operations:')
print('---------------------------------------')

# Bitwise and, or, xor operating on the binary words x and y will compare
# bit values in each corresponding position within the words.  

print(f"{(0b0101 & 0b0110):04b}") 
print(f"{(0b0101 | 0b0110):04b}") 
print(f"{(0b0101 ^ 0b0110):04b}") 

# If the words have different lengths, zeros will be padded in front of the
# shorter word:

print(f"{(0b01 & 0b0110):04b}") 
print(f"{(0b1101 | 0b1):04b}") 
print(f"{(0b10 ^ 0b0110):04b}") 



print()
print('Operator Precedence:')
print('---------------------------------------')

"""
Bitwise operators have precedence over both logical comparisons and 
Boolean operators. Operator precedence (descending order):

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

print( 0b110)   #  6
print(~0b110)   # -7
               
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
# For example, flipping all bits of the infinite two's complement 
# representation of 6 (...00000110) gives ...11111001, which is −7.
#
# The main difference between 1′s complement and 2′s complement is 
# that 1′s complement has two representations of 0 (zero):
#   00000000, which is positive zero (+0), and
#   11111111, which is negative zero (-0)
# whereas in 2′ s complement, there is only one representation for 
# zero — 00000000 (0) because if we add 1 to 11111111 (-1), we 
# get 100000000, which is nine bits long. Since only eight bits are 
# allowed, the left-most bit is discarded (overflowed), leaving 
# 00000000 (-0) which is the same as positive zero.
#
# For this reason 2′s complement is generally used when performing
# arithmetic operations, and 1’s complement is generally used when
# performing binary inversion.


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
# without using any conditionals, and without affecting other status bits. 

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
status ^= POWER | BATTERY_LOW 
check_status()

# Clear all flags while saving status of a selected flag:
status &= ERROR            # Turn all flags off but keep ERROR state unchanged
check_status()

# Clear all flags while saving status of multiple selected flags:
status &= (ERROR | POWER)  # Turn all flags off but keep ERROR & POWER unchanged
check_status()



print()
print('Hexadecimal (Base 16):')
print('---------------------------------------')

"""
Hexadecimal (hex) is a base 16 number system that uses digits 0-9 and letters
A-F (where A=10, B=11, C=12, D=13, E=14, F=15). Hex is widely used in
programming because each hex digit maps exactly to 4 binary bits (a "nibble"),
making it a compact shorthand for binary values:

   Hex    Decimal    Binary
   ---    -------    ------
   0x0       0        0000
   0x1       1        0001
   0x2       2        0010
   0x3       3        0011
   0x4       4        0100
   0x5       5        0101
   0x6       6        0110
   0x7       7        0111
   0x8       8        1000
   0x9       9        1001
   0xA      10        1010
   0xB      11        1011
   0xC      12        1100
   0xD      13        1101
   0xE      14        1110
   0xF      15        1111

Because one hex digit = 4 bits, two hex digits = 8 bits = 1 byte. This is why
hex is the go-to notation for byte-level work. Here are common hex values you
will encounter in code and what they look like in binary:

   0xFF   = 1111 1111  (255)  -- all 8 bits set; used as an 8-bit mask
   0x80   = 1000 0000  (128)  -- only the MSB (most significant bit) set;
                                  used to test the sign bit in a byte
   0x7F   = 0111 1111  (127)  -- all bits set except MSB; max value of a
                                  signed 8-bit integer
   0x0F   = 0000 1111  (15)   -- lower nibble mask (keeps lower 4 bits)
   0xF0   = 1111 0000  (240)  -- upper nibble mask (keeps upper 4 bits)
   0xFFFF = 1111 1111 1111 1111  (65535) -- 16-bit (2-byte) mask
   0xDEAD = 1101 1110 1010 1101  (57005) -- classic debug/sentinel value
"""

# In Python, hex literals are declared with the 0x prefix (just like
# 0b for binary):
a = 0xFF
b = 0x80

print(f"0xFF in decimal: {a}")         # 255
print(f"0xFF in binary:  {a:08b}")     # 11111111
print(f"0x80 in decimal: {b}")         # 128
print(f"0x80 in binary:  {b:08b}")     # 10000000

# The hex() function converts an integer to a hex string (similar to bin()):
print(f"hex(255) = {hex(255)}")        # '0xff'
print(f"hex(128) = {hex(128)}")        # '0x80'

# String formatting can also display hex values:
print(f"{255:02x}")   # 'ff'  (lowercase)
print(f"{255:02X}")   # 'FF'  (uppercase)
print(f"{255:#04x}")  # '0xff' (with 0x prefix)

# Converting between representations -- these all refer to the same value:
print(0xFF == 0b11111111 == 255)  # True

# Practical example: extracting the upper and lower nibbles of a byte
byte_val = 0xA3  # 1010 0011
upper_nibble = (byte_val & 0xF0) >> 4  # isolate upper 4 bits, shift right
lower_nibble =  byte_val & 0x0F        # isolate lower 4 bits
print(f"Byte: 0x{byte_val:02X} = {byte_val:08b}")
print(f"  Upper nibble: 0x{upper_nibble:X} = {upper_nibble:04b}")
print(f"  Lower nibble: 0x{lower_nibble:X} = {lower_nibble:04b}")



