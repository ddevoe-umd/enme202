%
%  ENME202 Matlab
%

%
%  COMPLEX VARIABLES, FUNCTIONS, and OPERATIONS
%

% ==========================================================================

% Matlab understands complex values:

sqrt(-4)    % ans = 0 + 2.0000i

% The result is shown in the standard "cartesian" or "rectangular" form
% for a complex number: a+b*i, where a,b are real, and 
% i is the "imaginary" number whose square is -1.

i     % ans = 0 + 1.0000i
i^2   % ans = -1

% Matlab also understands complex number calculations like:

i^i
sin(i)
exp(i*pi)

% Engineers often use "j" instead of "i" for the "imaginary"
% number j^2 = -1.  While Matlab will always use i to display 
% complex values, the definition for j is also built in.

j     % ans = 0 + 1.0000i
j^2   % ans = -1

% Let's look at the quadratic formula again, but with coefficients
% that yield complex roots:

a = 2; b = 4; c = 10;
x1 = (-b+sqrt(b^2-4*a*c))/(2*a)     % x1 = -1.0000 + 2.0000i
x2 = (-b-sqrt(b^2-4*a*c))/(2*a)     % x2 = -1.0000 - 2.0000i

% We can also directly define complex variables like:

z1 = -1 + 2*j

% Note: You don't need "*" before i or j when explicitly defining
% a complex number (although you can, if you want to). This is the one 
% (and only) situation where Matlab will understand implied 
% multiplication without explicitly using "*".

z2 = -2 + 3.5j

% However, you can only use the "implicit multiply" with i or j
% if the thing that precedes it is a real number
% (not just something that *evaluates* to a real number)

(2+3)*i   % This is fine, but
(2+3)i    % this is not

% You also can't use the "implied multiply" shorthand with variables:

c = 3;
c*i       % This is fine, but
ci        % this is not

% Can you see why the latter couldn't work?  Matlab can't know 
% if ci is meant to be a separate variable name!

%
% Complex functions and operations
%

% The real() and imag() functions can be used to break a complex
% number into its real and imaginary parts:

real(z1)    % Real part of a complex number
imag(z1)    % Imaginary part of a complex number
conj(z1)    % Complex conjugate

% Matlab knows how to do complex arithmetic, so you don't have to do
% implement these operations manually:

z1 + z2
z1 - z2
z1 * z2
z3 = z1 / z2

% Just as an exercise/check, let's do the above division
% for z3 manually using complex functions, without using complex 
% arithmetic.
%
% To divide two complex numbers, multiply top & bottom by the complex
% conjugate of the denominator (z2):

z2c = conj(z2)                      % complex conjugate of z2
denom = real(z2)^2 + imag(z2)^2     % Denominator (always real)
numReal = real(z1)*real(z2c) - imag(z1)*imag(z2c)   % numerator (real)
numImag = real(z1)*imag(z2c) + imag(z1)*real(z2c)   % numerator (imag)
z3 = numReal/denom + j*numImag/denom    % z3 = z1/z2

% The result should be the same as typing z3 = z1/z2

% Complex magnitude (absolute value)

abs(z1)

% The following statements are equivalent:

abs(z1)
sqrt(z1*conj(z1))
sqrt(real(z1)^2 + imag(z1)^2)

% Complex exponential function -- Euler's formula

theta = 3*pi/4      % pick an angle
exp(j*theta)        % A*exp(j*theta) = A*(cos(theta) + j*sin(theta))

% Use abs() and angle() to convert a complex # to 
% polar form (magnitude & angle):

z = -1+j
r = abs(z)
theta = angle(z)    % extract the angle

% Visualizing z on the complex plane, it is clear that theta should 
% be 3*pi/4 = 135 deg:

theta * 180/pi    % should be 135 deg

% Now convert from polar to cartesian form using Euler's formula:

r * exp(j*theta)  % ans = -1.0000 + 1.0000i

% We could also do explicit rectangular conversion:

r*(cos(theta) + j*sin(theta))     % ans = -1.0000 + 1.0000i

% Careful with the polar angle!
% You might be tempted to use:

theta = atan(imag(z)/real(z))

% Which yields -0.7854 = -pi/4, not the (correct) 3*pi/4 value

% The above atan() trig won't always work.  In this case, 
% z is in the wrong *quadrant* of the plane for a simple atan()
% calculation.  Looking at the planar geometry/trig for this problem, 
% we'd actually need to use the supplement of this angle:

theta = atan(imag(zz)/real(zz)) + pi    % --> 2.3562 rad = 3*pi/4

% It is fairly common in planar geometry, when doing polar coordinate
% conversions, to encounter such a problem.  Matlab, and most computer
% languages, have a built-in "4 quadrant" atan function to handle it.
%
% To get the correct polar angle for a point at coordinates (x,y) in
% the plane, use atan2(y,x) 
%
% Note there are *two* separate inputs, and note their order!
% Applied to a complex number, the "x" coordinate is the real part,
% the "y" coordinate is the imag part, so:

theta = atan2(imag(zz), real(zz))

% gives the right polar angle.

% This 4 quadrant atan2() functionality is built into the 
% angle() function for complex numbers, without you needing
% to separate out real and imag parts.

% Finally, note (again) that *all* Matlab's built-in functions can 
% work with complex numbers

sqrt(2j)    % ans = 1.0000 + 1.0000i




