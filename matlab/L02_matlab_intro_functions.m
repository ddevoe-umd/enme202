%
%  ENME202 Matlab
%

%
%  INTRODUCTION
%

% ==========================================================================

%
% MATLAB INTERFACE
%

% Current Folder:
%    - Displays Matlab files ("m-files" or scripts) in the current directory.
% Editor:
%    - Built-in editor for writing m-files.
%    - You can copy & paste from a plain text file.
% Command Window:
%    - Use to directly enter any Matlab command.
%    - You can run an m-file from this window by entering the file name,
%      provided the file directory is part of your path.
% Workspace:
%    - Shows all currently active variables


%
% RUNNING MATLAB THROUGH UMD VIRTUAL LAB
%

% Installing a native version of Matlab is recommended! However,
% if you are unable to install Matlab on your computer for
% any reason, Matlab can run without being installed by using the
% Virtual Computer Lab: http://virtlab.eng.umd.edu
%
% When using Virtual Lab, always save your files to the U: volume to
% ensure that your code will remain available after closing the current
% Citrix session


%
% HELP COMMANDS:
%
%    help      --> local help file
%    lookfor   --> search local help files for keyword
%
%    doc       --> online help file
%    docsearch --> search online docs for keyword
%

% Help topics are organized by classes of operators and functions.
% In addition to the core language elements under the "matlab" topic,
% specific help is also available for different packages (simulink,
% control, curvefit, etc.) available in Matlab.

help            % Context-relevant help based on last command
help lang       % view a summary of built-in programming language constructs
help if         % view details on "if" statement usage
help helptools  % view all available help tools

% "doc" will display the HTML document page for a given topic, often with
% more discussion and examples than the help page. When available, 
% the document page can also be accessed from a link to the 
% "Reference page" at the bottom of the help page:

doc if    % bring up document page for the "if" conditional statement

% "lookfor" / "docsearch" will display a list of local / online 
% help files containing the desired term:

lookfor dot 



% ==========================================================================

%
% BASIC ARITHMETIC AND COMPUTATIONAL ERROR
%

% Typing a mathematical expression in the command window will
% yield a result, similar to the functionality of a calculator:

% Basic arithmetic (+, -)
2+2
2-2

% multiplication (*)
2*3

% exponentiation (^) (caret)
2^3

% Fractional powers
2^0.5

% Scientific notation
1e6
12e2
2e-2

% Increase number of significant digits displayed
format long
2^0.5

% Go back to default number of sig digits
format short
sqrt(2)


% There is a finite precision with which numbers can be represented, 
% leading to rounding errors:

sqrt(2)^2 - 2   % Should be zero, but...

% eps (epsilon) is the smallest significand (decimal part) difference 
% that Matlab can represent

format long
eps         % ans = 2.220446049250313e-016

% Matlab uses the international standard IEEE 754 for "high" precision 
% representation of decimal numbers. This standard uses 52 bits to
% represent the significand.  There are thus "gaps" between the
% numbers of length:

1 / 2^52    % ans = 2.220446049250313e-016

% (this result is exactly the value of eps)

% Two numbers whose significand differs by less than eps (after rounding) are 
% identical to the computer.  For example, (1+eps/2) is rounded down to nearest 
% representable number, 1:

(1+eps/2) - 1

% Here, (1+2*eps/3) is rounded up to nearest representable number, 1+eps:

(1+2*eps/3) - 1

% Let's try

(1-1)+eps/2   % same as (1+eps/2) - 1, but with the parentheses moved

% Note: (1+eps/2)-1 produces 0 but (1-1)+eps/2 produces eps/2!
% This shows that the round-off error should be thought of
% in a "relative" sense (relative to the numbers
% involved in the calculation).

% Just to confirm this, try

1e-30 - 1e-31

% Clearly Matlab can take differences (and multiplication, etc.) of 
% numbers smaller than eps, so we need to think of the round-off error
% as "relative".

% Note that successive calculations can *each* incur round-off 
% error on the order of eps, so large expressions or repeated
% calculations can build up significant error if you are not
% careful!

% ==========================================================================

%
%  CORE FUNCTIONS
%

% sqrt() is one of the many built-in (core) functions in Matlab.
% Each function does a mathematical calculation on the argument (input) being
% passed to the function.  

% exp() is Euler's number (e):
% e^x = exp(x) 

format short
exp(1)    % e^1 = e, so ans = 2.7183

% log() is log base e (equivalent to natural log; ln)

log(exp(1))    % log base e, so log(e) = 1

exp(log(8))

% Just for fun, what is exp(log(8))-8?

exp(log(8)) - 8     % ans = -1.7764e-15 = 8*eps

% log10() is log base 10

log10(8)

10^(log10(8))

% abs() is absolute value

abs(-2)

% Trigonometric functions (arguments in radians)

sin(30 * pi/180)

% Append a "d" to the function name to work in degrees

sind(30)

% Note that pi is pre-defined

pi    % ans = 3.1416

% List all elementary math functions

help elfun
