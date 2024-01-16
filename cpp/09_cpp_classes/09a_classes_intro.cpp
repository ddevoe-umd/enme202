// ENME 202
// 9_classes_intro.cpp
// Classes and Object-Oriented Programming (OOP)

#include <iostream> 
#include <cmath>
using namespace std;

/*
  A C++ class describes a set of attributes (variables) and 
  behaviors (methods or member functions) available to every 
  object instantiated from the class.

  Classes are identical to structs, except class attributes are
  private by default (struct variables are public by default).
  Otherwise C++ structs and classes are the same: they both support
  "inheritance", the use of "constructors", etc.

  While structs and classes are basically the same thing (in C++),
  structs are often reserved to hold simple data structurs, while
  classes are used when employing class methods, instantiation,
  and inheritance...but this is really just convention!

  Like strtucts, classes are typically named with upper 
  case, e.g. "MyClass".

  An object is an instance of a class:
  - think of a class as a "cookie-cutter" that can be used to 
    stamp out multiple cookies (objects), where each object shares
    the same "shape" but is individually customizable with unique 
    attributes.
  – Uniquely defined by the values assigned to instance variables.
  – Objects have access to the variables and methods of their class.
  – Objects typically start with lower case: myObject.

  Classes support inheritance (as do structs):
  - create new classes based on an existing class
    with expanded functionality.

  Why use classes and OOP?
  - Classes abstract the code design process and
    provide a more logical structure to your code.
  – Makes large programs easier to plan and implement.
  - Classes hide their internals from other programmers.
  - Easy to re-use classes across multiple codes.
  - Maintaining object-oriented code is easier than procedural 
    code since changes are fully modular.
*/

// Recall our Complex struct for a complex number:
// 
// struct Complex {   
//  float a;  // real part
//  float b;  // imag part
// };
//
// Let's convert this into a class:

class Complex {  
  public: 
    float a;  // real part
    float b;  // imag part
};

// The "public" keyword is needed to allow a and b to be accessed
// from outside the class. If we omitted this, the variables
// could be accessed by other code *within* the class definition
// but nowhere else.

// Now let's add a class method that will return the phase angle
// of the complex value. To do this, define a new phase() function
// using the "scope resolution operator" (::)

class Complex2 {  
  public: 
    float phase();   // declare the member function
    float a;  // real part
    float b;  // imag part
};

float Complex2::phase() {  // define the member function
  return(atan2(b,a));
}

// What if we wanted the complex value to be initialized to a0 + j*b0 
// when creating a new object? Use a constructor!  The constructor
// is automatically called whenever the class is instantiated (that
// is, when a new object is created). The constructor function is 
// declared like a regular member function, with a name matching 
// the class name and no return type:

class Complex3 {  
  public: 
    Complex3(int, int);     // constructor prototype
    float a;  // real part
    float b;  // imag part
};

Complex3::Complex3(int a0, int b0) {  // Constructor function for Complex3
  a = a0;
  b = b0;
}


// Or maybe we want the real & imaginary values to be requested
// from the user:

class Complex4 {  
  public: 
    Complex4();     // constructor prototype
    float a;  // real part
    float b;  // imag part
};

Complex4::Complex4() {  // Constructor function
  cout << "Real: ";
  cin >> a;
  cout << "Imag: ";
  cin >> b;
}


// The above methods were defined outside the class definition
// using the scope resolution operator (::), but we could
// instead have integrated them into the class directly:

class Complex5 {  

  public: 
    
    Complex5() {  // Constructor (no prototype needed)
      cout << "Real: ";
      cin >> a;
      cout << "Imag: ";
      cin >> b;
    }
    
    float a;  // real part
    float b;  // imag part

    float phase() { 
      return(atan2(b,a));
    }
};



int main(void) {

  Complex2 z;
  z.a = 1;
  z.b = -1;
  cout << "Phase angle = " << z.phase() << endl;

  Complex4 x;
  cout << x.a << " + j(" << x.b << ")" << endl;
  
  Complex5 y;
  cout << y.a << " + j(" << y.b << ")" << endl;
  cout << "Phase angle = " << y.phase() << endl;

  return 0;
}

