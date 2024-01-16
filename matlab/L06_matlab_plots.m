%
%  ENME202 Matlab
%

% ==========================================================================

%
%  PLOTS
%

% Simple plots are easily created by passing arrays to the plot()
% function. 
%
% When passing a single array as plot(y), Matlab will generate
% a graph with the array index values on the x-axis, and the
% corresponding array values on the y-axis:

theta = (-1:.01:1)*pi;
y = sin(theta);
plot(y)

% When passing two arrays as plot(x,y), the resulting graph will
% contain points with coordinates x(i) and y(i) for each index i 
% in the arrays:

clf               % clears the plot window
plot(theta,y)

% Note that arrays theta and y must have the same length

% By default, each pair of (theta,y) values is shown as a dot on the 
% graph, and Matlab draws a smooth line connecting them. 
%
% The points are connected *in sequence*, which can lead to unexpected
% results if the point pairs are not properly ordered:

x = [-8 -5 0 0 5 8];    % increasing x values
y = [5 -8 8 8 -8 5];
plot(x,y)

% vs:

x = [0 -5 8 -8 5 0];    % same x,y pairs, but different order
y = [8 -8 5 5 -8 8];
plot(x,y)

% Try another example:

x = (-1:.01:1)*pi;
y = sin(x);
plot(x,y)

% By default, the plot linearly interpolates between x,y data points.
% Can plot just the data points using a third argument in plot():
plot(x,y,'.')

% A variety of point markers are available, like triangles:
plot(x,y,'>')

% Draw the data with markers, *and* the interpolated line between points
plot(x,y,'>-')

% Can control the color of markers and lines ("r","g","b","k", etc colors)
plot(x,y,'r>-')

% Can control the style of the line (dashed "--", dotted ":", etc)
plot(x,y,'r>--')

% Can combine multiple plots in a single function call:
plot(x,y,'x', x-2.5,y.^2,'o')

% Many combinations of colors, markers, and linestyles, check
% the help file for details:
help plot

% Formatting plots -- adding grids, axis labels, and titles (note
% the "see also" options under "help plot"):
plot(x,y)
grid
xlabel('x')
ylabel('sin(x)')
title('Plot of sin(x)');

% The range for each axis can be specified using the axis command,
% with syntax: axis([XMIN XMAX YMIN YMAX])

axis([-2 2 -1.5 3])

% Each new plot command will completely overwrite previous plot
% and formatting.  To keep the previous plot, put new plot in
% a different "figure" window
%
% Create a new figure window and put a different plot in it:

figure(2)
plot(x, sin(2*x))

% Figures can be saved to different graphics formats, ranging
% from png to Adobe Illustrator (saved as vector art -- very
% useful if you want to customize your plots later)

% We won't do a lot with multiple figure windows in this class
% but the functionality is there to open up as many different
% figure windows as you like, with different plots on each.

% To "redirect" subsequent plots to a specific, already open figure window,
% type figure(n) before the next plot command, where "n" is
% the number of the window you want to use.  If a window with that number
% doesn't exist, a new window will be opened and given the number indicated
% by "n".

% Get rid of an unneeded figure window with the close command

close(2)

% We can also close all figure windows:

close all

% As we saw previously, multiple plots can be placed in a single figure
% by specifying 2 (or more) x-y datasets in a single plot command:

plot(x, y, x, sin(2*x))

% Can control the color and linestyle of each plot separately:

plot(x, y, 'r-', x, sin(2*x), 'k:')

% Can alternately use "hold on" to tell Matlab to keep the previous plot 
% in a window in order to overlay an additional plot onto it at a later time

plot(x,y)
hold on
plot(x, sin(2*x))

% Use "hold off" to revert to original plot behavior (replacing the old plot
% completely when a new plot command is given)

hold off
plot(x,y)  % plot from above is replaced entirely here
hold on
plot(x, sin(2*x), 'r') % different colored plot overlaid
plot(x, sin(3*x), 'm') % yet another plot overlaid; 3 total now
hold off

% To make the graph have one color, and the data points another,
% plot twice with hold on:

plot(x,y)  % draw the original graph
hold on
plot(x(1:2:end),y(1:2:end),'g>') % Mark every other datum a different color

% Clear a figure without removing the window with "clf":

clf

% Multiple *independent* plots can also be created in a single figure 
% window using the "subplot" command. You are not responsible for this
% in ENME202, but it is a useful command to be aware of:

help subplot

% A final note:
% Matlab plots are extremely powerful, and we are just touching
% the surface here. There is a wide variety of 2D and 3D plot
% options, and your code can also manipulate plots at a very 
% low level using more advanced commands than covered here.


