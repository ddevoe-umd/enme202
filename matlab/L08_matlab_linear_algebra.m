%
%  ENME202 Matlab
%

%
%  LINEAR ALGEBRA
%

% ==========================================================================

%{
  TOPICS:
    vector and matrix formation & manipulation
    matrix slicing
    row & column expansion
    vector and matrix algebra

  FUNCTIONS:
    dot()   -- dot product
    cross() -- cross product
    norm()  -- vector norm (magnitude)
    size()  -- find matrix dimensions
    eye()   -- identity matrix
    diag()  -- create a diagonal matrix / return diagonal
    inv()   -- matrix inverse
    det()   -- determinant of a square matrix
%}

%
%  ARRAYS AS VECTORS
%

% So far we have used arrays for two things:
%   1. holding a list of numbers
%   2. representing polynomials
%
% Another key use for Matlab arrays is to represent physical
% vectors, e.g. the coordinates of a point or the components
% of a force or velocity. We often express such vectors as
% column vectors, e.g.:

x = [1 0 -1]       % row vector
y = [1 2 3]'       % column vector

% Vector arithmetic works as expected:

x'+y     % addition (note the transpose to make dimensions match!)
x-y'     % subtraction
2*x     % scalar multiplication

% While we cannot multiply (or divide) a vector with another
% vector, there are two important related operations that 
% can be performed: the dot product and cross product


% Most functions will operate on an element-by-element
% basis, e.g.:
round(sqrt(x))


% Norm:

% The norm() function yields the L2 norm (Euclidean norm),
% interpreted as the vector length in n-dimensional space.
%
% IMPORTANT: this is not to be confused with length(), which
% just gives the number of elements in an array!

norm(x)

% norm() is the same as:
sqrt(dot(x,x))
sqrt(x*x')


% Dot products:
dot(x,y)
dot(y,x)
dot(x,x)

% Manuall calculation of dot(x,y):
x(1)*y(1) + x(2)*y(2) + x(3)*y(3)

% dot(x,y) = norm(x)*norm(y)*cos(q)
% where q = angle between x and y
%
% A physical interpretation of the dot product is that
% dot(x,y) yields the length of the projection of x onto y, 
% multiplied by the length of y
%
% This interpretation allows us to determine the angle
% between two vectors:

q = acos(dot(x,y)/(norm(x)*norm(y))) 

% dot() does not care if the arrays are row vectors, column 
% vectors, or a mix of both:

dot(x',y)           % ans = -2


% Cross product:
cross(x,y)
cross(y,x)      % = -cross(x,y)

% A physical interpretation of the cross product is that
% the magnitude of cross(x,y) is the area of a parallelogram
% with sides |x| and |y|, and the direction of cross(x,y)
% is orthogonal to the plane containing the parallelogram:
%
% cross(x,y) = norm(x)*norm(y)*sin(q)*n_hat
%
% where n_hat is a unit normal vector orthogonal
% to x and y (using the right hand rule).
%
% so if we want to find the plane in which x and y lie:

n_hat = cross(x,y)/(norm(x)*norm(y)*sin(q))   % q was found via dot(x,y)

% Note that n_hat has unit length:
norm(n_hat)

% Matlab can work with *any* length vector
% not just 2 or 3.  Indeed, you will often need to deal
% with very large vectors in advanced engineering problems.

x=[1 -2 3 4 -5 7 9 -pi]';
y=(1:8)';
norm(x)
dot(x,y)        % length(x) must be same as length(y)

% Cross products, however, are ONLY defined between
% 3 dimensional vectors, so cross(x,y) will not work here!
% The cross product *can* be extended to n>3 dimensions, but
% Matlab's cross() does not support this generalization...


%
%  MATRICES
%

% Matrices are rectangular arrays of numbers, that 
% have their own special arithmetic rules
%
% Note that a vector can be viewed as a special
% case of a matrix containing only a single row
% (or column, depending on orientation)

% Define a matrix in Matlab by specifying the numbers
% in each row, separated by spaces or commas.
% Start a new row with a semicolon

A = [1 2 3 -1; 4 5 6 0; 7 8 9 1]

% Can also put each row on a separate line
% (semicolons optional):

A = [ 1 2 3 -1
      4 5 6  0 
      7 8 9  1 ]

% This matrix A is 3x4 (3 rows, 4 columns)

% When defining a matrix, *all* rows & columns must have
% the same number of elements

AA = [1 2 3 -1; 4 5 0; 7 8 9 1]      % ERROR

% Oops; 2nd row only had 3 elements in above,
% while the other two rows had 4.

% Index into a matrix to get one of its elements
% by specifing both the row and column number of 
% the element

% Element of A in 1st row, 3rd column:

r = 1;
c = 3;
A(r,c)      % ans = 3

% Element of A in 2nd row, 4th column:

A(2,4)      % ans = 0

% If only one argument is given for the index, Matlab will
% start counting at the upper left corner and work down each
% *column* in sequence:

A(1)        % ans = 1

A(4)        % ans = 2

% We can change an individual matrix element:

A(2,4) = pi

% or change multiple elements at once:

A(1:2,2) = [-1; -1]

% Multiple elements can also be changed to a single scalar value:

A(2:3,3) = -100

% size() returns an array containing the number of rows and 
% columns in a matrix:

[m,n] = size(A)     % m = 3, n = 4

% We previously used sum() to find the summation of all
% values in an array (vector).  When applied to a matrix,
% sum() will return the summation of values within each
% *column* of the matrix:

sum(A)      

% Concatenating linear arrays into (longer) vectors
% or into rectangular arrays (matrices)

x = [1 2 3];
y = [-3 -2 -1];

z = [x y]           % z = [1 2 3 -3 -2 -1]

A1 = [x
      y]          % A1 = [1 2 3; -3 -2 -1]

A2 = [x' y']        % A2 = [1 -3; 2 -2; 3 -1] 

% Recall colon notation to "pull out"
% a range of elements in a linear array:

x = [1 0 -1 2];
x(2:3)              % ans = [0 -1]

% Same notation can also be used for the row
% or column index (or both) in a matrix.
%
% Pull out elements in 1st and 2nd rows, 3rd and 4th columns:
A(1:2, 3:4)         % ans = [3 -1; 6 0]

% Pull out elements in 1st and 2nd rows, 2nd through 4th columns:
A(1:2, 2:4)         % ans = [2 3 -1; 5 6 0]

% colon ":" by itself as an index means "all".
%
% Pull out all rows of the 2nd column:
A(:,2)              % ans = [2; 5; 8]

% Pull out all the columns of the 2nd row:
A(2,:)              % ans = [4 5 6 0]

% Matrices may be "partitioned" into a set of rows
% or columns. Here is an example of column partitioning:
C1 = A(:,1)
C2 = A(:,2)
C3 = A(:,3)
C4 = A(:,4)

% Now reconstruct the original matrix from the columns:
A = [C1 C2 C3 C4]

% We can also use row partitioning to break a
% matrix into rows (noting there are only n=3 rows
% vs. m=4 columns for A):
R1 = A(1,:)
R2 = A(2,:)
R3 = A(3,:)

A = [ R1
      R2
      R3 ]

% Matrix partitioning is a key step to understanding how
% arithmetic operations between matrices and vectors are
% defined.


%
%  MATRIX-VECTOR MULTIPLICATION
%

% Given A is a matrix and x is a column vector,
% matrix-vector multiplication (A*x) requires that x has
% the same number of elements as A has columns, i.e.
% the inner dimensions of A and x must match.

A = [1 2 3 -1; 4 5 6 0; 7 8 9 1];   % A is 3x4
x = [-2; -1; 1];                    % x is 3x1
A*x                 % ERROR (4 vs. 3 for inner dimensions)

% When the dimensional condition is satisfied, the
% resultant vector y=A*x will be a column vector
% with the same number of elements as A has rows:

x = [-2; -1; 1; 2];
A*x                 % ans = [-3; -7; -11]

% The formal definition of the product can be given 
% expressed as the **weighted sum of the columns of A**
%
% Remember, we defined above C1...C4 to be the respective
% columns of A, so let's apply the weighted sum concept:

y = x(1)*C1 + x(2)*C2 + x(3)*C3 + x(4)*C4

% A*x can also be written as a vector consisting of the 
% products of the *rows* of A with the vector x:

y = [ R1*x
      R2*x
      R3*x ] 

% Both row and column expansions of the product are consistent
% and equivalent, and lead to Matlab's reported result for the
% product A*x.  Matlab applies such rules automatically when
% the multiplication is valid; you don't need to manually
% apply the expansion (but be aware of it!)


%
%  MATRIX-MATRIX MULTIPLICATION
%

% Define 2 matrices A and B

A = [1 2 3 -1
     4 5 6 0
     7 8 9 1];
 
B = [-1 0 1
     1 2 3];

% A is 3x4, B is 2x3

A*B         % ERROR (inner dimensions are different)

% Product A*B is not defined since inner dimensions don't match
% (4 vs 2)
 
B*A         % yields a 2x4 matrix result

% Product BA is defined since inner dimensions match
% (both are 3), and result matrix is 2x4 (outer dimensions)

A = [1 2
     3 4
     5 6];   % 3x2 matrix

A*B                    % 3x2 * 2x3 --> 3x3

% Product is defined since inner dimensions match (both are 2)
% Result is 3x3 (outer dimensions)
    
B*A         % 2x3 * 3x2 --> 2x2

% Product is also defined since inner dimensions also match,
% and result is 2x2

% Note from the three examples above that matrix multiplication
% is NOT COMMUTATIVE: generally A*B is different from B*A.
% Order *must be preserved* when multiplying matrices.

% The row,column value resulting from matrix multiplication
% is given by the product of the row from the 1st
% matrix and the column of the 2nd matrix:

AB = A*B;

AB(2,3)             % ans = 15
A(2,:) * B(:,3)     % ans = 15

% Similarly, ith column of C_AB = A*B
% is given by A * (ith column of B)

AB(:,2)         
A * B(:,2)

% Both these equivalent ways of viewing the matrix-matrix
% product give the same results, and agree with Matlab's
% reported result for A*B


% Matrix transpose:
% A' turns the rows of A into columns, and vice-versa
% (just remember that if your matrix contains imaginary numbers
% you will need to use .' instead of ' for the non-conjugate
% transpose!)

A
A'


% Identity matrix:
% The identity matrix is a square matrix (same number of rows
% and columns), with "1" on the diagonal and "0" everywhere
% else:

I = [ 1 0 0
      0 1 0
      0 0 1 ]

% Identity matrices are equivalent to the number 1 in ordinary
% scalar arithmetic.  However, keep in mind that dimensions
% matter:

I*A         % 3x3 * 3x2 --> 2x2
A*I         % 3x2 * 3x3 --> ERROR

I*B         % 2x3 * 3x3 --> 2x3
B*I         % 3x3 * 2x3 --> ERROR

% Also true for vectors, assuming they are of correct size for
% multiplication

A2 = A(:,2)     % Second column of A

I*A2            % 3x3 * 3x1 --> 3x1

% We can easily generate identity matrices of any size
% using Matlab's "eye" function

I = eye(4)      % 4x4 identity matrix

% Input to eye() is the desired array size (rows or cols)

% If given a matrix as its input, the Matlab
% diag() function returns a column array with only
% the diagonal elements of that matrix

diag(I)     % ans = [1; 1; 1; 1]

C = [1 0 1; 2 2 0; 3 1 5]
diag(C)     % ans = [1; 8; 23]

% diag() can also be used to *create* a square matrix
% If diag is given a (linear) array as its input,
% it creates a square matrix with the elements of the array on
% the diagonal, and zeros elsewhere.
%
% This is an easy way to "strip" all but the diagonal 
% elements from a matrix (setting the others to 0):

C1 = diag(diag(C))

% As another example, use diag() to generate an identity matrix:

diag([1 1 1])


%
%  INVERSES OF SQUARE MATRICES
%

% Inverting a 2x2 matrix by hand is easy (assuming you've taken a 
% Linear Algebra course that is).  Inverting a 3x3 is not too bad.
% Inverting a 4x4, 5x5, ... by hand is a nightmare!  Matlab makes
% this easy using the inv() function:

A = [1 2; 
     3 4]

inv(A)

% Product of matrix and its inverse is always the identity matrix:

A * inv(A)          % ans = [1 0; 0 1]

inv(A) * A          % ans = [1 0; 0 1]


% Let's look at a larger matrix

A2 = [ 1  2  3 
       4 -5  6
       9  8  7 ]

inv(A2)

% Inverse is not defined if the determinant of the matrix is zero
% such a matrix is "singular" (again, stuff you'll learn in
% Linear Algebra).
%
% det() calculates determinant of any size matrix:

A = [ 1 1
      3 3 ]

det(A)      % close to zero!

inv(A)      % {Warning: Matrix is singular to working precision.} 

% Determinant of A is zero here, so inverse is not defined!
% Singluar matrices are the like the number zero in scalar
% arithmetic; they do not have a defined inverse.

% More precisely, in scalar arithmetic, there is no meaningful
% solution for x in the equation a*x = b when a=0 and b<>0 
% (and if b=0, *any* numerical value for x will work!)

% We can encounter, and solve, similar problems in matrix
% arithmetic, provided the matrix square and nonsingular
%
% Solve A2*x = b for x:

b = [-1;0;1];
x = inv(A2)*b 

A2*x      % same as b since x is a solution of A2*x=b


% Multiplication by the inverse of a matrix can be
% simplified in Matlab using the backslash (\) operator.
% For example, instead of "inv(A2) * b" we can say:

A2 \ b   % Note the order -- read from right to left!


