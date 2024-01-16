#include <iostream>
#include <cmath>
#include <bitset>
using namespace std;

// Number systems
//
// Our normal system for counting is the decimal (base 10) number system.
// The "base" is the number of digits that are available to represent a single
// unique value, so for base 10 we have: 0,1,2,3,4,5,6,7,8,9.  After 9 we
// need to add a second digit to represent higher numbers: 10, 11, 12, etc., and
// after 99 a third digit is needed: 100, 101, etc.  This notation is called
// the "positional system", or place-value notation, and can be applied to
// any base we like.  
//
// Consider the binary (base 2) system, which only has 2 unique values for a 
// single digit, namely 0 and 1. Let's count to 7 in binary:
//
// base 10    base 2
//    0         000
//    1         001
//    2         010
//    3         011
//    4         100
//    5         101
//    6         110
//    7         111
//
// In base 2, each 0 or 1 value is called a "BInary digiT" or bit.  A 
// sequence of bits is called a "binary word", and an 8-bit word is a 
// byte.  The left-most bit in a binary word is the 
// Most Significant Bit (MSB), and the right-most is called
// the Least Significant Bit (LSB).  The value of a binary word can be
// represented in base 10 by multiplying the value of each bit (0 or 1) 
// times 2 to the power of the bit's column, starting with the LSB as 
// column 0.  
//
// Using this approach, 101 in base 2 is converted as follows:
//
// 101 = 1*2^2 + 0*2^1 + 1*2^0 = 1*4 + 0*2 + 1*1 = 5 in base 10
//
// Here the caret symbol means exponentiation (just remember C++ does
// not interpret "^" the same way).


int main(void) {
  
  // We can define a binary word in C++ by placing "0b" in front of a
  // binary value (containing only 0s and 1s):

  int a = 0b100;
  cout << a << endl;

  cout << 0b11111111 << endl;  // max 8-bit word value = 2^8-1 = 255

  // Similarly, hexadecimal (base 16) numbers can be defined by 
  // placing "0x" in front of a hexadecimal value (containing the
  // numbers 0-9 and letters A-F):

  cout << 0x80 << endl;

  // C++ does not distinguish between different number system, so when
  // we display a value defined using binary or hexadecimal notation, 
  // it appears as a base 10 integer. 

  // To display a binary value directly, we can use the bitset
  // library:

  cout << bitset<8>(0b1111) << endl; 

  // Now let's focus on how we can manipulate binary words,
  // using bitwise operators:
  //
  //    x & y bitwise AND
  //    x | y bitwise OR
  //    x ^ y bitwise XOR (exclusive OR)
  //    ~x  bitwise COMPLEMENT (returns the complement of x, same as -x-1)
  //        (note this is not the same as logical NOT operator: "!")
  //    x << n shift bits to the left by n places (same as multiplying by 2**y)
  //    x >> n shift bits to the right by n places (same as dividing by 2**y)

  int x = 0b1001;
  int y = 0b1110;
  cout << bitset<4>(x & y) << endl;   // AND
  cout << bitset<4>(x | y) << endl;   // OR
  cout << bitset<4>(x ^ y) << endl;   // XOR
  
  // Now try the complement operator (~): 

  cout << bitset<4>(~x) << endl;      // COMPLEMENT (inverse)
  cout << bitset<4>(x | ~x) << endl;

  // x | ~x = -1 for any x.
  // This result may not be what you were expecting.
  // ~x yields the complement of x, meaning the value of x
  // represented using "two's complement".
  // 
  // To find two's complement of x: invert all bits, and add 1. 
  // Note that ~x will always invert the sign of x: ~x = -(x+1)
  // 
  // Just remember that ~ simply flips the bits
  // of a binary word, but the result is represented using
  // two's complement so that when you try to display the result
  // it will not appear the way you expect.  To verify this,
  // consider the following:

  x = 0b11110000;
  int mask = 0b11111111;
  cout << bitset<8>(~x & mask) << endl;

  // Bit shifting
  //
  
  x = 0b0110;

  cout << endl;
  cout << "x =      ";
  cout << bitset<4>(x) << endl;

  cout << "x << 1 = ";
  cout << bitset<4>(x << 1) << endl;

  // Right bit shifting – extra bits roll off and are forgotten:
  cout << "(x >> 3) << 3 = ";
  cout << bitset<4>((x >> 3) << 3) << endl;

  // Left bit shifting – bits are remembered (word length 
  // increases to retain MSB):
  cout << "(x << 10) >> 10 = ";
  cout << bitset<4>((x << 10) >> 10) << endl;


  // Bit fields + bit masks
  //
  // Say x is a "bit field" with 5 states we want to track:
  
  x = 0b00000;    // we could just say x = 0...

  // Let mask1 and mask2 be bitmasks to manipulate the field:
  int mask1 = 0b01010;
  int mask2 = 0b10001;

  // Turn 2nd and 4th bits on:
  x |= mask1;
  cout << bitset<5>(x) << endl;

  // Turn 1st and 5th bits on: 
  x |= mask2;
  cout << bitset<5>(x) << endl;

  // Flip state of 5th bit:
  x ^= 1<<4;
  cout << bitset<5>(x) << endl;

  // Turn 2nd bit off: 
  x &= 0b11101;
  cout << bitset<5>(x) << endl;

  // Use a mask to turn off 2nd and 4th bits:
  x &= ~mask1;

  // Flip states of 2nd and 4th bits:
  x ^= mask1;
  cout << bitset<5>(x) << endl;

  // use bit shifting to check each state in sequence:
  for (int i=0; i<5; i++) {
    cout << "State " << i << " = " << (bool)(x & 1<<i) << endl;
  }


}