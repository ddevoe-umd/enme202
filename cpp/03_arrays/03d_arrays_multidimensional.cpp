// ENME 202
// 3d_arrays_multidimensional.cpp
// MULTIDIMENSIONAL ARRAYS

#include <iostream>
using namespace std;

int main(void) {

  // C++ supports 2D arrays, for example:
  int r = 3;
  int c = 5;
  int badArray[r][c];  

  // ^^ This is a bad example!!!
  //
  // In C++ the array size must be known at "compile time", 
  // preventing us from using variables like r and c above 
  // as size values.  
  //
  // Instead, use #define declarations to create constant values.  
  // The C++ preprocessor will replace all instances of
  // ROWS or COLS with the values in these #define statements:
  
  #define ROWS 5
  #define COLS 3
  int myArray[ROWS][COLS];     // poroperly create a 3x5 array  


  // Recall that there is no definition of "row" or "column" 
  // in C++, so the use of "rows" and "cols" here is arbitrary.

  // Let's assign random values to each element
  // using a nested for loop:
  srand(time(NULL));           // initialize the random seed
  for (int i=0; i<r; i++) {    // go through each row
    for (int j=0; j<c; j++) {  // for the current row, go through each column
      myArray[i][j] = rand()%10;     // assign random values from 0->9
    }
  }

  cout << endl;
  // Now let's display the array, row by row, using nested for() loops.
  // (just as a single for() loop is the friend of 1D arrays,
  // nested for() loops are the friends of 2D arrays).
  cout << "Values in myArray:" << endl;
  for (int i=0; i<r; i++) {    
    for (int j=0; j<c; j++) {  
      cout << myArray[i][j] << " ";
    }
    cout << endl;
  }

  // We can initialize the values in multidimensional arrays
  // at declaration using similar syntax as 1D arrays:

  float newArray[2][3] = {{1,2},{3,4,5}};

  
  // Multidimensional arrays are not limited to two indices 
  // (two dimensions); they can contain as many indices as needed. 
  // Be careful though: the memory needed for an array increases 
  // geometrically with each dimension.
  //
  // For example:
  //
  // char century [100][365][24][60][60];
  //
  // declares an array of type char for each second in a century,
  // requiring 3 billion char values (close to 3 GB of memory!)

 
  // Multidimensional arrays are just an abstraction for programmers
  // since the same results can be achieved with a 1D array!
  //
  // To see that this is true, consider the two blocks of code
  // below:

  // Create a "true" 2D array:
  cout << "2D array:" << endl;
  int myarray1 [ROWS][COLS];            // initialize 2D array
  for (int i=0; i<ROWS; i++) {
    for (int j=0; j<COLS; j++) {
      myarray1[i][j] = i+j;     // define [i][j] value
      cout << myarray1[i][j] << " ";    // display the value
    }
    cout << endl;
  }
  cout << endl;

  // Create a pseudo-2D array:
  cout << "Pseudo 2D array:" << endl;
  int myarray2 [ROWS * COLS];             // initialize 1D array
  for (int i=0; i<ROWS; i++) {
    for (int j=0; j<COLS; j++) {
      myarray2[i*COLS + j] = i+j;   // define element value
      cout << myarray2[i*COLS + j] << " ";  // display the value
    }
    cout << endl;
  }

  // The results for each example above are identical.  The 
  // array elements are stored in memory in exactly the same
  // way for each case.
  
  return 0;
}
