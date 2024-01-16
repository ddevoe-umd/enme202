// ENME 202
// 9c_composition.cpp

// Topics:
//  - composition

#include <iostream> 
#include <cmath>
using namespace std;

// Complex class from the last code file:
class Complex {  
  public: 
    float a;  // real part
    float b;  // imag part
};

// We previously extended the Complex class by inheritance,
// i.e. creating a child class that inherits from Complex
// as a base or parent class. 
//
// Another way to integrate the functionality of Complex in
// another class is by COMPOSITION. In this approach, an
// instance of Complex is included as a class attribute within
// the new class. Here is a new version of Complex2 that has the
// same functionality as our inheritance example, but using
// composition instead:

class Complex2{  
  public: 
    Complex z;    // integrate Complex by COMPOSITION
    Complex2() {  // constructor
      cout << "Real: ";
      cin >> z.a;
      cout << "Imag: ";
      cin >> z.b;
    }
    float phase() {  // class method to find phase angle
      return(atan2(z.b,z.a));
    }
};


int main(void) {

  Complex2 cval;   // Complex2 constructor queries user for values

  // Note how the values z.a and z.b are accessed:
  cout << cval.z.a << " + j(" << cval.z.b << ")" << endl;

  // The phase() method belongs to Complex2, not Complex:
  cout << "Phase angle = " << cval.phase() << endl;

  return 0;
}





