# Introduction to Matplotlib

"""
Topics
------
What is Matplotlib and Basic Plotting
Customizing Plots (Colors, Markers, Labels)
Multiple Plots and Subplots
Different Plot Types (Scatter, Bar, Histogram, Pie)
Saving Figures
"""

import matplotlib.pyplot as plt
import numpy as np


print()
print('What is Matplotlib and Basic Plotting:')
print('---------------------------------------')

# Matplotlib is the most widely used library for creating static, animated,
# and interactive visualizations in Python. The pyplot module provides a
# MATLAB-like interface for making plots.

# The basic workflow for creating a plot:
#   1. Prepare your data
#   2. Create a figure and axes
#   3. Plot your data
#   4. Customize the plot (labels, title, etc.)
#   5. Show or save the plot

# ---------------
# Simple Line Plot
# ---------------

# The simplest way to create a plot:
x = [0, 2, 4, 6, 8]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()

# If you only provide one list, it is used as y-values
# and x-values are automatically generated as indices (0, 1, 2, ...):
plt.plot([1, 4, 9, 16, 25])
plt.show()

# plot() simply displays each (x,y) pair in sequence:
x = [-5, -5, 5, 5,-5]
y = [-2, 2, 5, -5, -2]
plt.plot(x, y)
plt.show()

# ---------------
# Plotting NumPy Arrays
# ---------------

# Matplotlib works seamlessly with NumPy arrays:
x = np.linspace(0, 2 * np.pi, 100)   # 100 points from 0 to 2*pi
y = np.sin(x)

plt.plot(x, y)
plt.show()

# ---------------
# Adding Labels and Title
# ---------------

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x (radians)')           # Label for x-axis
plt.ylabel('sin(x)')                # Label for y-axis
plt.title('Sine Wave - Single Period')              # Title of the plot
plt.show()

# ---------------
# Multiple Lines on One Plot
# ---------------

x = np.linspace(0, 2 * np.pi, 100)

# Simply call plot() multiple times before show():
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.sin(2*x), label='sin(2x)')
plt.plot(x, np.sin(3*x), label='sin(3x)')
plt.title('Multiple Lines')
plt.show()


print()
print('Customizing Plots:')
print('---------------------------------------')


# ---------------
# Line Styles and Colors
# ---------------

# You can customize the appearance of lines using format strings
# or keyword arguments.

x = np.linspace(0, 2 * np.pi, 100)

# Format string: 'color''marker''linestyle'
# Colors: 'b' (blue), 'g' (green), 'r' (red), 'c' (cyan),
#         'm' (magenta), 'y' (yellow), 'k' (black), 'w' (white)
# Markers: 'o' (circle), 's' (square), '^' (triangle), 'x', '+', '*'
# Line styles: '-' (solid), '--' (dashed), ':' (dotted), '-.' (dash-dot)

plt.plot(x, np.sin(x), 'b-')        # Blue solid line
plt.plot(x, np.cos(x), 'r--')       # Red dashed line
plt.title('Format String Examples')
plt.show()

# Using keyword arguments for more control:
plt.plot(x, np.sin(x), color='blue', linestyle='-', linewidth=2)
plt.plot(x, np.cos(x), color='red', linestyle='--', linewidth=1.5)
plt.title('Keyword Argument Examples')
plt.show()

# ---------------
# Markers
# ---------------

x = np.linspace(0, 2 * np.pi, 20)   # Fewer points to see markers clearly

plt.plot(x, np.sin(x), 'go-')       # Green circles with solid line
plt.plot(x, np.cos(x), 'rs--')      # Red squares with dashed line
plt.title('Markers Example')
plt.show()

# More marker customization:
plt.plot(x, np.sin(x), marker='o', markersize=8,
         markerfacecolor='yellow', markeredgecolor='blue')
plt.title('Custom Markers')
plt.show()

# ---------------
# Legend
# ---------------

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), 'b-', label='sin(x)')
plt.plot(x, np.cos(x), 'r--', label='cos(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.title('Trigonometric Functions')
plt.legend()                        # Display the legend
plt.show()

# Legend location can be specified:
# 'best', 'upper right', 'upper left', 'lower left', 'lower right',
# 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.legend(loc='lower left')
plt.show()

# ---------------
# Grid and Axis Limits
# ---------------

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x))
plt.xlim(0, 2 * np.pi)              # Set x-axis limits
plt.ylim(-1.5, 1.5)                 # Set y-axis limits
plt.grid(True)                      # Add grid lines
plt.title('Plot with Grid and Custom Limits')
plt.show()

# Grid customization:
plt.plot(x, np.sin(x))
plt.grid(True, linestyle='--', alpha=0.7)   # Dashed grid with transparency
plt.show()


print()
print('Multiple Plots and Subplots:')
print('---------------------------------------')

# ---------------
# Subplots
# ---------------

# Create multiple plots in a single figure using subplot(rows, cols, index)
# or the more flexible subplots() function.

# Method 1: plt.subplot()
x = np.linspace(0, 2 * np.pi, 100)

plt.subplot(2, 1, 1)                # 2 rows, 1 column, first plot
plt.plot(x, np.sin(x))
plt.title('Sine')

plt.subplot(2, 1, 2)                # 2 rows, 1 column, second plot
plt.plot(x, np.cos(x))
plt.title('Cosine')

plt.tight_layout()                  # Adjust spacing between subplots
plt.show()

# Method 2: plt.subplots() - returns figure and axes objects
fig, axes = plt.subplots(2, 2)      # 2x2 grid of subplots

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('sin(x)')

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('cos(x)')

axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_ylim(-5, 5)          # Limit y-axis for tangent
axes[1, 0].set_title('tan(x)')

axes[1, 1].plot(x, x**2)
axes[1, 1].set_title('x^2')

plt.tight_layout()
plt.show()

# ---------------
# Figure Size
# ---------------

# Control the size of the figure:
fig, ax = plt.subplots(figsize=(10, 4))   # width, height (inches)
ax.plot(x, np.sin(x))
ax.set_title('Wide Figure')
plt.show()



print()
print('Different Plot Types:')
print('---------------------------------------')

# ---------------
# Scatter Plot
# ---------------

# Scatter plots show individual data points:
x = np.random.randn(50)
y = np.random.randn(50)
colors = np.random.rand(50)         # Random colors
sizes = 100 * np.random.rand(50)    # Random sizes

plt.scatter(x, y)
plt.title('Basic Scatter Plot')
plt.show()

# Scatter plot with color and size variations:
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar()                      # Add color bar
plt.title('Scatter Plot with Color and Size')
plt.show()

# ---------------
# Bar Chart
# ---------------

categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.bar(categories, values)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()

# Horizontal bar chart:
plt.barh(categories, values)
plt.xlabel('Value')
plt.ylabel('Category')
plt.title('Horizontal Bar Chart')
plt.show()

# Grouped bar chart:
x_pos = np.arange(len(categories))
values1 = [23, 45, 56, 78, 32]
values2 = [30, 40, 50, 60, 70]
width = 0.35

plt.bar(x_pos - width/2, values1, width, label='Group 1')
plt.bar(x_pos + width/2, values2, width, label='Group 2')
plt.xticks(x_pos, categories)
plt.legend()
plt.title('Grouped Bar Chart')
plt.show()

# ---------------
# Histogram
# ---------------

# Histograms show the distribution of data:
data = np.random.randn(1000)        # 1000 random values from normal distribution

plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Customized histogram:
plt.hist(data, bins=30, edgecolor='black', alpha=0.7, color='steelblue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Customized Histogram')
plt.show()

# ---------------
# Pie Chart
# ---------------

sizes = [35, 25, 20, 15, 5]
labels = ['Python', 'Java', 'JavaScript', 'C++', 'Other']
explode = (0.1, 0, 0, 0, 0)         # "Explode" the first slice

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title('Programming Language Popularity')
plt.axis('equal')                   # Equal aspect ratio for circular pie
plt.show()

# ---------------
# Error Bars
# ---------------

x = np.arange(1, 6)
y = np.array([2.3, 3.1, 4.5, 3.8, 5.2])
errors = np.array([0.3, 0.4, 0.2, 0.5, 0.3])

plt.errorbar(x, y, yerr=errors, fmt='o-', capsize=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot with Error Bars')
plt.show()

# ---------------
# Fill Between
# ---------------

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='sin(x) + 0.5')
plt.fill_between(x, y1, y2, alpha=0.3)
plt.legend()
plt.title('Fill Between')
plt.show()



print()
print('Saving Figures:')
print('---------------------------------------')

# ---------------
# savefig()
# ---------------

# Save a figure to a file using savefig():

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.title('Sine Wave')

# Format options:
# plt.savefig('sine_wave.png')              # PNG format
# plt.savefig('sine_wave.pdf')              # PDF format
# plt.savefig('sine_wave.svg')              # SVG format

# Control resolution and quality:
# plt.savefig('sine_wave_hires.png', dpi=300)   # High resolution
# plt.savefig('sine_wave_tight.png', bbox_inches='tight')  # Remove extra whitespace

plt.show()

# ---------------
# Object-Oriented Interface
# ---------------

# Matplotlib has two interfaces:
#   1. Pyplot interface (plt.plot, plt.xlabel, etc.) - simple, stateful
#   2. Object-oriented interface (fig, ax) - explicit, more control
#
# The pyplot interface uses a "current figure" and "current axes" that
# change implicitly. This works for simple plots but can be confusing
# when working with multiple figures or subplots.
#
# The OO interface explicitly references Figure and Axes objects:
#   - Figure: the entire window/canvas (can contain multiple plots)
#   - Axes: a single plot area with its own coordinate system
#
# Key differences in method names:
#   Pyplot              Object-Oriented
#   ------              ---------------
#   plt.plot()          ax.plot()
#   plt.xlabel()        ax.set_xlabel()
#   plt.ylabel()        ax.set_ylabel()
#   plt.title()         ax.set_title()
#   plt.xlim()          ax.set_xlim()
#   plt.ylim()          ax.set_ylim()
#   plt.legend()        ax.legend()
#   plt.grid()          ax.grid()

# Example using the OO interface:
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')

ax.set_xlabel('x (radians)')
ax.set_ylabel('y')
ax.set_title('Object-Oriented Style')
ax.legend()
ax.grid(True)

# fig.savefig('oo_style.png', dpi=150)
plt.show()

# The OO interface is preferred when:
#   - Working with multiple figures or subplots
#   - Writing functions that create plots (pass ax as parameter)
#   - You need to modify a plot after creating it
#   - Building complex visualizations


"""
PRACTICE PROBLEMS

Easy
1. Basic Plot: Create a line plot of the function y = x^2 for x values from
   -10 to 10.
2. Labels and Title: Plot sin(x) from 0 to 2*pi with appropriate axis labels
   and a title.
3. Multiple Lines: Plot sin(x), cos(x), and tan(x) on the same graph (limit
   y-axis to [-2, 2] for tan). Add a legend.
4. Scatter Plot: Create a scatter plot of 30 random (x, y) points.

Medium
5. Subplots: Create a 2x2 grid of subplots showing sin(x), cos(x), x^2, and
   sqrt(x) respectively.
6. Bar Chart: Create a bar chart showing the average temperature for each month
   of the year (use made-up data).
7. Histogram: Generate 500 random numbers from a normal distribution with mean=10
   and std=2. Plot a histogram with 25 bins.
8. Customization: Plot y = e^(-x) * sin(2*pi*x) from x=0 to 5 with a red dashed
   line, grid, and appropriate labels.
9. Error Bars: Create a plot with error bars for 5 data points. Use random data
   for y values and errors.

Hard
10. Combined Plot: Create a figure with a main plot showing sin(x) and a smaller
    inset plot (using axes.inset_axes) showing a zoomed-in region.
11. Dual Y-Axes: Create a plot with two different y-axes (left and right) showing
    sin(x) on the left axis and x^2 on the right axis. Use ax.twinx().
12. 3D Surface: Use mpl_toolkits.mplot3d to create a 3D surface plot of
    z = sin(sqrt(x^2 + y^2)).
13. Animation Prep: Create a function that generates and saves 10 PNG frames
    of a sine wave shifting phase from 0 to 2*pi.
14. Statistical Plot: Create a box plot comparing 4 different datasets (use
    np.random.randn to generate data with different means).
15. Custom Styling: Create a professional-looking plot using plt.style.use()
    (try 'seaborn' or 'ggplot') with custom fonts and colors.
"""
