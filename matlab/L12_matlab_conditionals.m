%
%  ENME202 Matlab
%

% ==========================================================================
%
%  CONDITIONALS
%


%{
  TOPICS:
    logical comparisons
        ==    -- equality comparison
        >, <  -- greater than / less than comparisons
        ~=    -- inequality comparison
    Boolean operators
        &     -- AND operator
        |     -- OR operator
        ~     -- NOT operator
        xor() -- EXCLUSIVE OR function
    if / elseif / else statements
    switch / case statements
    combining if statements with for & while loops
    flags
    any() / all() functions
%}

% Conditional expressions let us choose different paths in
% the code depending on the value of one or more logical
% expressions that result in true or false outcomes.

% Logical expressions return logical values of
% 1 for true and 0 for false:

2 < 3     % ans = 1
2 < 1     % ans = 0
2 <= 2    % ans = 1
2 < 2     % ans = 0
3 >= 2    % ans = 1

% We can also use the "true" and "false" keywords for both
% logical comparisons and direct math with true=1 and false=0:

true > 0    % ans = 1
false > 0   % ans = 0
2*true + 1  % ans = 3

% The equality comparison operator is '=='
% (entirely different from the  assignment operator '=')

3 == 3    % ans = 1
3 == 4    % ans = 0
3 = 3     % ERROR!
a = 3     % OK, but this is an assignment, not a comparison
a == 3    % ans = 1 (since we just assigned 3 to a)
a == 2    % ans = 0

% The opposite for '==' is the 'not equals' test '~='
% The tilde (~) means 'not' in Matlab (unlike C++ as we will see)

a ~= b    % ans = 1
3 ~= 4    % ans = 1
3 ~= 3    % ans = 0

% We can (and should!) think of the output of these 
% comparisons as bits, i.e. single true/false data points,
% also called "Booleans", see below. 


%%%%%%%%%%%%%  BOOLEAN OPERATIONS  %%%%%%%%%%%%%
%
% Logical comparisons (AND, OR, NOT, XOR) between single 
% true/false (1/0) values (bits) can also be performed. 
% These comparisons are known as Boolean operations (named after
% the 19th century mathemetician George Boole).

% Boolean Truth tables:

% NOT:
%
%   X  | ~X 
%  --- | --- 
%   0  |  1  
%   1  |  0  

% AND:
%
%   X   Y  | X&Y
%  --- --- | ---
%   0   0  |  0
%   0   1  |  0
%   1   0  |  0
%   1   1  |  1

% OR:
%
%   X   Y  | X|Y
%  --- --- | ---
%   0   0  |  0
%   0   1  |  1
%   1   0  |  1
%   1   1  |  1

% Exclusive OR:
%
%   X   Y  | xor(X,Y)
%  --- --- | ---
%   0   0  |  0
%   0   1  |  1
%   1   0  |  1
%   1   1  |  0   <-- pay attention here!


% Logical AND is indicated with an ampersand (&)
% x&y is true if both values are true, false otherwise

1 & 1     % ans = 1
1 & 0     % ans = 0
0 & 1     % ans = 0
0 & 0     % ans = 0

% Logical OR is indicated with the vertical bar (|)
% x|y is false if both propositions are false, true otherwise

0 | 0     % ans = 0
0 | 1     % ans = 1
1 | 0     % ans = 1
1 | 1     % ans = 1
 
% Here is a typical use of the AND/OR operators:

x = 2.06;
(x<3) & (x>1)   % ans = 1

x = 4;
(x<3) & (x>1)   % ans = 0
(x<3) | (x>1)   % ans = 1


% Logical NOT is indicated with the tilde symbol (~)
% ~y is false if y is true, and true if y is false
% (flip the bit):

~1      % ans = 0
~0      % ans = 1


% XOR is the "exclusive OR" logical operator.  The XOR operator
% yields true if ONE AND ONLY ONE of the two values being compared
% is true.  Matlab does not have a symbol for the XOR operator,
% so instead use the xor() function:

xor(0,0)    % ans = logical 0
xor(1,0)    % ans = logical 1
xor(1,1)    % ans = logical 0

% Note that and() and or() functions also exist in Matlab, with 
% the same functionality as & and |

% Any sequence of logical operators can be combined into a single 
% Boolean expression:

a=1; b=0; c=1; 
(a & ~b) | ((c & a) | xor(a,b))

% Truth table:
% 
%  a   b   c   ~b   a&~b  c&a  xor(a,b)  (c&a)|xor(a,b)  (a&~b)|((c&a)|xor(a,b))
% --- --- ---  ---  ----  ---  --------  --------------  -----------------------
%  0   0   0    1     0    0       0            0                 0
%  0   0   1    1     0    0       0            0                 0
%  0   1   0    0     0    0       1            1                 1
%  0   1   1    0     0    0       1            1                 1
%  1   0   0    1     1    0       1            1                 1
%  1   0   1    1     1    1       1            1                 1
%  1   1   0    0     0    0       0            0                 0
%  1   1   1    0     0    1       0            1                 1


% Logical operator precedence: ~ > & > |
%
% A | B & C      -->  A | (B & C)
% A & B | C & D  --> (A & B) | (C & D)
% A & B & C | D  --> ((A & B) & C) | D
% ~A & B | C     --> ((~A) & B) | C



% Logical operators can also be applied to arrays, allowing
% multiple bits to be compared at once.  In this case we can 
% think of the arrays as representing "binary words" (bit 
% sequences of defined length).

[1 1 0 0] & [0 1 0 0]     % ans = 1×4 logical array  0   1   0   0

xor( [1 1 0 0], 
     [0 1 0 0] )          % ans = 1×4 logical array  1   0   0   0

~[1 0 0 1]                % ans = 1×4 logical array  0   1   1   0


% Consider the previous example of (a & ~b) | ((c & a) | xor(a,b))
% Can we build the full truth table using arrays?

a = [0 0 0 0 1 1 1 1];
b = [0 0 1 1 0 0 1 1];
c = [0 1 0 1 0 1 0 1];
(a & ~b) | ((c & a) | xor(a,b))   % matches above result, ok


% Logical operators are useful for a broad range of coding applications.
% For example, consider how to find all of the elements of an 
% array x that are NOT equal to either 1 or 3. 

x = [-2, 5, 1.5, 3, 1, 29, 1, 1];

find(x~=1 & x ~=3)     % ans =  1  2  3  6


%%%%%%%%%%%%%  Short Circuiting  %%%%%%%%%%%%%
%
% The AND and OR operators can be used with "short circuiting",
% meaning that if the first expression in the comparison has a value
% that ensures a particular output, regardless of the second
% expression's value, Matlab will not bother evaluating the second 
% expression.
%
% The short circuiting operators are:
%   AND --> &&
%   OR  --> ||
%
% The && and || operators can reduce the computation time


%%%%%%%%%%%%%  ANY, ALL  %%%%%%%%%%%%%
%
% any(x) returns 1 iff any element of x is true
% all(x) returns 1 iff all elements of x are true
%

x = [1 1 0 0];
y = [0 0 0 0];
z = [1 1 1 1];

any(x)  % true
all(x)  % false
any(y)  % false
all(z)  % true

% How would you write custom functions that have the
% same behavior as any() and all() ??


%%%%%%%%%%%%%%  Binary Mathematics  %%%%%%%%%%%%%
%
% While we can create an array of binary digits and perform
% logic operations on the entire array, we cannot perform
% binary math by simply adding or subtracting arrays.  Try it:

a = [1 1];    % binary 3
b = [0 1];    % binary 1
a - b         % ans:  1 0

% Hmmm...that seemed to work, since [1 0] is binary 2 (= 3-1)
% What about this:

a = [1 0 1];  % binary 5
b = [0 1 0];  % binary 2
a - b         % ans:  1 -1  1

% Clearly this is not the same as binary 3...
% Matlab is simply performing base 10 math on each respective
% array element.  To perform binary math, we must instead
% convert the binary numbers to base 10 (decimal), do the math,
% then convert back to base 2 using bi2de() and de2bi()

de2bi(bi2de(a) - bi2de(b))   % ans = 1  1

% Alternately, if the binary number is represented by a string
% instead of an array, bin2dec() and dec2bin() can be used
% instead:

a = '101';
b = '010';
dec2bin(bin2dec(a) - bin2dec(b))  % ans = '11'

% Matlab also supports bitwise operator functions that 
% operate on base 10 numbers for arguments:
%
%   bitand()
%   bitor()
%   bitxor()

x = bitand(3,6);   % 3 -> '011'   6 -> '110'
dec2bin(x)         % ans = '10'

x = bitor(3,6);    % 3 -> '011'   6 -> '110'
dec2bin(x)         % ans = '111'

x = bitxor(3,6);   % 3 -> '011'   6 -> '110'
dec2bin(x)         % ans = '101'


%%%%%%%%%%%  IF, ELSEIF, ELSE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% The "if" statement is a foundational element of programming,
% allowing us to decide on different courses of action based on 
% the state of a variable or other data element with our code.

% Syntax:
% if LOGICAL_EXPRESSION
%   DO_IF_TRUE
% end


if x > 2
  disp('x is greater than 2')
end

% We can also define a path that occurs only when the argument
% in the if statement is false using if/else:

if x > 2
  disp('x is greater than 2')
else
  disp('x is NOT greater than 2')
end


% Example: compute the total cost of buying N widgets,
% if the cost per widget is $0.90 for N<=50 but $0.70 for N>50.
N = 56;
if ( N <= 50 )
  totalCost = 0.90*N;
else
  totalCost = 0.70*N;
end


% Another version of the same example
if ( N <= 50 )
  costPerWidget = 0.90;
else
  costPerWidget = 0.70;
end
totalCost = costPerWidget * N;


% Yet another version, without an else statement
totalCost = 0.90 * N ;
if ( N > 50 )
  totalCost = 0.70 * N ;
end


% The elseif statement enables >2 possible
% outcomes (vs. just 2 with if/else)

if x > 10
  disp('x is greater than 10')
elseif x >= 5
  disp('x is between 5 and 10, inclusive')
elseif x == 0
  disp('x is zero')
else
  disp('x is less than 5 and non-zero')
end



% If statements can use complex Boolean expressions as
% the conditional, for example:

x = 10*rand();     % random number from 0-10
if ((x > 2) & (x < 5)) | x > 9.9
  disp(x)
end


% Below are several exaples showing the use of if statements in
% different contexts, combined with functions and for() loops.

% Compute the value of a piecewise function of x.
% Use an if() statement with appropriate logical expressions 
% to break down each piece of the function.

if (x<-1)
  y = 1;
elseif (x>=-1) & (x<=2)
  y = 4;
elseif (x>2) & (x<3)
  z = x-2;
  y = 4-2*z^2;
elseif (x>=3)
  z = x-3;
  y = sqrt(z);
end

% Note: be careful when setting up the conditions for
% situations like this to make sure that all cases (here, all possible
% values of x) have been covered.  Otherwise, y will not have a proper
% numerical value assigned to it, and you will get errors.

% Clauses in conditionals are evaluated from top to
% bottom in the order they appear.  Only the code block in
% the first "true" clause found is executed, the others are skipped.
%
% Knowing this we can often simplify our conditions by
% ordering them correctly.
%
% Thus, the elseif/else statements below are equivalent to 
% the previous example:

  if (x<-1)
    y = 1;
  elseif (x<=2)  % if we get here we already know x>=-1
    y = 4;
  elseif (x<3)  % if we get here we already know x>2
    z = x-2;
    y = 4-2*z^2;
  else          % if we get here we already know x>=3
    z = x-3;
    y = sqrt(z);
  end

end


% The power of your code increases vastly by *combining*
% different techniques.  Here is an example of using
% a loop and a conditional together, to evaluate our
% piecewise function at an *array* of points x

x = [10 -9 8 -7 6 -5];
for k = 1:length(x)
  if x(k)<-1
    y(k) = 1;
  elseif x(k)<=2
    y(k) = 4;
  elseif x(k)<3
    z = x(k)-2;
    y(k) = 4-2*z^2;
  else    
    z = x(k)-3;      
    y(k) = sqrt(z);
  end   % if
end   % for
disp(y)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% FLAGS

% If statements make it possible to use Boolean variables
% as "flags".  A flag is a true/false variable (i.e. a Boolean) 
% that can be flipped "on" or "off" to keep track of the state
% of some property within our code.
%
% For example, here is a loop that checks to see if an array
% contains any even values:

a = [1.2 4.33  5 9  7.1  8.1 21 -3];
isEven = false;  % start by assuming there are no even values
for i = a
  if mod(i,2) == 0
    isEven = true;
  end
end

if isEven
  disp('There was at least one even value')
else
  disp('There were no even values')
end




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% SWITCH / CASE
%
% The switch() statement provides another conditional that 
% makes it easy to choose different outcomes based on the value
% of an input:

color = 'red';   % the quotes denote a variable of type "string"
 
switch color
  case {'Blue' 'blue'}  % use {} for multiple cases
    disp('blue sky')
  case 'red'
    disp('red fire')
  case 'green'          % more than one line of code can run per case
    disp('green tree')
    disp('green tea')  
  otherwise             % do if no case comparison is true (optional)
    disp('Not blue, red, or green')
end

% Notes:
%  * The "otherwise" statement is optional
%  * Only the first matching case will be activated (this is
%    very different from other languages like C++)
%  * A switch statement can always be performed using if/else
%    statements, but if/else  offers functionality
%    that cannot be replicated using switch






