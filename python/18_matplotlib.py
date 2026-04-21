# Introduction to Matplotlib

"""
Topics
------
Basic Plotting
Customizing Plots (Colors, Markers, Labels)
Multiple Plots and Subplots
Different Plot Types (Scatter, Bar, Histogram, Pie, Polar)
Saving Figures
"""

import matplotlib.pyplot as plt
import numpy as np

print()
print('Basic Plotting:')
print('---------------------------------------')

# Matplotlib is the most widely used library for creating static, animated,
# and interactive visualizations in Python. The pyplot module provides a
# MATLAB-like interface for making plots.

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
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# ---------------
# Adding Labels and Title
# ---------------

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
plt.plot(x, np.sin(x))
plt.plot(x, np.sin(2*x))
plt.plot(x, np.sin(3*x))
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
# Markers (optional): 'o' (circle), 's' (square), '^' (triangle), 'x', '+', '*'
# Line styles: '-' (solid), '--' (dashed), ':' (dotted), '-.' (dash-dot)

plt.plot(x, np.sin(x), 'b-')        # Blue + solid line
plt.plot(x, np.cos(x), 'r--')       # Red + dashed line
plt.plot(x, np.cos(x) * np.sin(x), 'ko-.')  # Black + circles + dash-dot line
plt.show()

# Use keyword arguments for more control. Here we add the _linewidth_
# and _alpha_ (transparency) options:
plt.plot(x, np.sin(x), color='blue', linestyle='-', linewidth=1.5)
plt.plot(x, np.cos(x), color='red', linestyle='--', linewidth=4, alpha=0.2)
plt.show()

# Multiple plots with custom formatting can be defined in a single plot() call:
xc = x[0:-1:4]
plt.plot(x, np.sin(x), 'b-', x, np.cos(x), 'ro-', xc, np.sin(xc)*np.cos(xc), 'ms-.')  
plt.show()

# ---------------
# Markers
# ---------------

x = np.linspace(0, 2 * np.pi, 20)   # Fewer points to see markers clearly

plt.plot(x, np.sin(x), 'go-')       # Green circles with solid line
plt.plot(x, np.cos(x), 'rs--')      # Red squares with dashed line
plt.show()

# More marker customization:
plt.plot(x, np.sin(x), marker='o',
         markersize=8,
         markerfacecolor='yellow',
         markeredgecolor='blue')
plt.show()

# ---------------
# Legends
# ---------------

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), 'b-', label='sin(x)')
plt.plot(x, np.cos(x), 'r--', label='cos(x)')
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend()      # Display the legend (label entries)
plt.show()

# Legend location can be specified with _loc_ parameter:
# 'best', 'upper right', 'upper left', 'lower left', 'lower right',
# 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.legend(loc='lower right')
plt.show()

# ---------------
# Grid and Axis Limits
# ---------------

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x))
plt.xlim(np.pi/2, 4*np.pi/3)              # Set x-axis limits
plt.ylim(-1.0, 2.5)                 # Set y-axis limits
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

# Syntax:
#     plt.subplot(row, column, plot# for current use)
# where plot# increments row-wise starting in upper left and ending lower right

# Method 1: plt.subplot() -- selects a specific figure panel
x = np.linspace(0, 2 * np.pi, 100)

plt.subplot(2, 1, 1)                # 2 rows, 1 column, first plot
plt.plot(x, np.sin(x))
plt.title('Sine')

plt.subplot(2, 1, 2)                # 2 rows, 1 column, second plot
plt.plot(x, np.cos(x))
plt.title('Cosine')

plt.tight_layout()                  # Adjust spacing between subplots
plt.show()

# Method 2: plt.subplots() -- returns figure and axes objects
#                      ^ plural!
# (this is part of the object-oriented plot interface that is discussed
# in more detail below)
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

# You can explore the wide variety of axes methods available for
# manipulating plots from the official matplotlib site:
#     https://matplotlib.org/stable/api/axes_api.html

# ---------------
# Figure Size
# ---------------

# Control the size of the figure using OO interface:
fig, ax = plt.subplots(figsize=(10, 4))   # width, height (inches)
ax.plot(x, np.sin(x))
ax.set_title('Wide Figure')
plt.show()


print()
print('Saving Plots:')
print('---------------------------------------')

# Plots can be saved after calling plt.show() by manually clicking the save icon,
# or by calling the savefig() method (no need to display the plot):

plt.savefig('plot.png')

# Raster formats:
#    png — raster, default format
#    jpg / jpeg — raster, compressed
#    tiff / tif — raster, high quality
#    webp — raster, modern web format
#    raw / rgba — raw pixel data
# Vector formats:
#    pdf — vector, great for editing
#    svg — vector, great for web
#    eps — vector, PostScript
#    ps — vector, PostScript

# Common parameters:

plt.savefig('plot.png', dpi=300, bbox_inches='tight', transparent=True, facecolor='white')


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

# ---------------
# Polar Plots
# ---------------

# Polar plots display data using polar coordinates (radius and angle)
# instead of the usual Cartesian coordinates (x and y). 
# To create a polar plot, add projection='polar' to subplot():
plt.subplot(projection='polar')

# Basic polar plot
theta = np.linspace(0, 4*np.pi, 100)    # Angle values (radians)
r = theta                               # Radius values
plt.plot(theta, r)
plt.title('Spiral in Polar Coordinates')
plt.show()

# Polar plot with sine wave
theta = np.linspace(0, 2*np.pi, 100)
r = 2 + np.sin(5*theta)                 # Radius varies with sine
plt.subplot(projection='polar')
plt.plot(theta, r, 'b-')
plt.title('Polar Rose (r = 2 + sin(5θ))')
plt.show()

# Multiple data sets with different colors and markers
theta1 = np.linspace(0, 2*np.pi, 20)
r1 = 1 + 0.3*np.cos(3*theta1)
r2 = 1.5 + 0.2*np.sin(4*theta1)

plt.subplot(projection='polar')
plt.plot(theta1, r1, 'ro-', label='Dataset 1')
plt.plot(theta1, r2, 'bs-', label='Dataset 2')
plt.legend()
plt.title('Multiple Datasets on Polar Plot')
plt.show()

# Polar scatter plot with colors
np.random.seed(42)  # For reproducible random numbers
n_points = 50
theta = 2*np.pi * np.random.random(n_points)
r = np.random.random(n_points)
colors = theta      # Color by angle

plt.subplot(projection='polar')
plt.scatter(theta, r, c=colors, cmap='hsv', s=50, alpha=0.7)
plt.colorbar(label='Angle (radians)')
plt.title('Polar Scatter Plot')
plt.show()

# Customizing polar plots (using the OO interface)
theta_custom = np.linspace(0, 2*np.pi, 100)
r_custom = 1 + 0.5*np.cos(theta_custom)

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.plot(theta_custom, r_custom, 'r-', linewidth=3)
ax.set_ylim(0, 2)           # Set radial limits
ax.set_title('Customized Polar Plot')
ax.grid(True)
plt.show()

# Key concepts for polar plots:
#   - theta: angle coordinate (radians), corresponds to x in regular plots
#   - r: radius coordinate, corresponds to y in regular plots
#   - Use np.linspace(0, 2*np.pi, N) to create full circle of angles
#   - Convert degrees to radians: radians = degrees * np.pi/180
#   - For FFT phase plots: theta = phase, r = frequency (or vice versa)

# ---------------
# Scatter Plots (Advanced)
# ---------------

# Basic scatter plot with random data
np.random.seed(42)  # For reproducible results
n_points = 50
x = np.random.randn(n_points)        # Normal distribution
y = 2*x + np.random.randn(n_points)  # Correlated data with noise

plt.scatter(x, y)
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Basic Scatter Plot')
plt.grid(True, alpha=0.3)
plt.show()

# Scatter plot with color-coding and size variation
# This is common in engineering when you have a third parameter
# (temperature, pressure, time, etc.) that affects the relationship
temperature = 20 + 30*np.random.random(n_points)
stress = 100 + 50*x + 10*temperature + np.random.randn(n_points)*5  # Fn of both x and temperature
marker_sizes = temperature * 2  # Size proportional to temperature

plt.scatter(x, stress, c=temperature, s=marker_sizes, alpha=0.6, cmap='coolwarm')
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Load Factor')
plt.ylabel('Stress (MPa)')
plt.title('Stress vs Load\n(color=temperature, size=temperature)')
plt.grid(True, alpha=0.3)
plt.show()

# Scatter plot with different marker types for categories
# Useful when comparing different materials, conditions, or groups
materials = ['Steel', 'Aluminum', 'Titanium']
markers = ['o', 's', '^']  # Circle, square, triangle
colors = ['blue', 'green', 'red']

plt.figure()
for i, material in enumerate(materials):
    # Generate data for each material with different properties
    n_samples = 15
    strength = np.random.normal(200 + i*300, 50, n_samples)  # Different mean strength
    cost = np.random.normal(5 + i*10, 2, n_samples)          # Different cost

    plt.scatter(strength, cost, 
                marker=markers[i], 
                olor=colors[i],
                s=80, 
                alpha=0.7, 
                label=material, 
                edgecolor='black')

plt.xlabel('Tensile Strength (MPa)')
plt.ylabel('Cost ($/kg)')
plt.title('Material Properties Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Key scatter plot concepts:
#   - Use c parameter for color-coding a third variable
#   - Use s parameter for size-coding (area proportional to value)
#   - Use alpha for transparency when points overlap
#   - Use different markers for categorical data
#   - Add colorbar() when using color mapping
#   - Use edgecolor to make markers more distinct


print()
print('Object-Oriented Interface:')
print('---------------------------------------')

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
#   Regular             Object-Oriented
#   ------              ---------------
#   plt.plot()          ax.plot()        also ax.scatter(), ax.bar(), etc.
#   plt.xlabel()        ax.set_xlabel()
#   plt.ylabel()        ax.set_ylabel()
#   plt.title()         ax.set_title()
#   plt.xlim()          ax.set_xlim()
#   plt.ylim()          ax.set_ylim()
#   plt.legend()        ax.legend()
#   plt.grid()          ax.grid()
#   plt.savefig()       ax.savefig()

# Example using the OO interface:
fig, ax = plt.subplots()

ax.plot(x, np.sin(x), label='sin(x)')   
ax.plot(x, np.cos(x), label='cos(x)')

ax.set_xlabel('x (radians)')
ax.set_ylabel('y')
ax.set_title('Object-Oriented Style')
ax.legend()
ax.grid(True)
plt.show()

# The OO interface is preferred when:
#   - Working with multiple figures or subplots
#   - Writing functions that create plots (pass ax as parameter)
#   - You need to modify a plot after creating it
#   - Building complex visualizations

# There are many other features that can be accessed through the OO interface,
# (annotations, arrows, layout control, tick mark fomatting, etc.), see
# https://matplotlib.org for the full API.


print()
print('Color Plots:')
print('---------------------------------------')

# matplotlib.colors is essential for generating color plots such as heatmaps,
# contour plots, and 2D scalar field visualizations commonly used when working
# with FEA results, fluid dynamics, sensor data, etc.

import matplotlib.colors as mcolors

# Simulate a 2D temperature field with a hot spot and a cold spot.
# This mimics the kind of scalar field data engineers work with
# in thermal analysis, FEA results, or sensor array readings.
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Hot spot centered at (2, 2), cold spot at (-2, -2)
temp = 50 * np.exp(-((X - 2)**2 + (Y - 2)**2)) \
     - 30 * np.exp(-((X + 2)**2 + (Y + 2)**2)) \
     + 20  # ambient baseline of 20 degrees

# --- Example 1: Default normalization ---
# By default, imshow maps the min value in the data to the bottom
# of the colormap and the max to the top. This uses the full color
# range but gives you no control over what value maps to what color.
fig, axes = plt.subplots(1, 3, figsize=(16, 4))

im0 = axes[0].imshow(temp,
                     extent=[-5, 5, -5, 5],
                     origin='lower',
                     cmap='coolwarm')
axes[0].set_title('Default Normalize')
plt.colorbar(im0, ax=axes[0], label='Temp (°C)')

# --- Example 2: Manual normalization with Normalize ---
# Normalize lets you set explicit vmin and vmax boundaries.
# Useful when you have a known safe operating range and want
# the colormap to reflect that range, not the data extremes.
# Here we set 0-40 as our range — anything above 40 saturates
# to the top color, making hot spots immediately obvious.
norm1 = mcolors.Normalize(vmin=0, vmax=40)

im1 = axes[1].imshow(temp, extent=[-5, 5, -5, 5], origin='lower',
                      cmap='coolwarm', norm=norm1)
axes[1].set_title('Normalize (vmin=0, vmax=40)')
plt.colorbar(im1, ax=axes[1], label='Temp (°C)')

# --- Example 3: TwoSlopeNorm for asymmetric data ---
# TwoSlopeNorm is ideal when your data has a meaningful center
# point that isn't the midpoint of the range. For example, if
# 20°C is ambient and you want blue for below-ambient, red for
# above-ambient, with the white/neutral color pinned at exactly 20.
# This prevents the colormap from being skewed by an asymmetric
# range (here the hot spot is stronger than the cold spot).
norm2 = mcolors.TwoSlopeNorm(vcenter=20, vmin=-10, vmax=50)

im2 = axes[2].imshow(temp, extent=[-5, 5, -5, 5], origin='lower',
                      cmap='coolwarm', norm=norm2)
axes[2].set_title('TwoSlopeNorm (center=20°C)')
plt.colorbar(im2, ax=axes[2], label='Temp (°C)')

for ax in axes:
    ax.set_xlabel('X position (m)')
    ax.set_ylabel('Y position (m)')

plt.tight_layout()
plt.show()


print()
print('3D Plots using mpl_toolkits.mplot3d:')
print('---------------------------------------')

# pyplot cannot directly generate 3D plots (response surfaces, vector field
# visualization, etc.).  Instead, use mpl_toolkits.mplot3d to support a third
# dimension.  We still use pyplot to handle the figure lifecycle (creating,
# displaying, saving) but leverage mplot3d to create the 3D plots themselves.

from mpl_toolkits.mplot3d import Axes3D

# Create 1D arrays of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# meshgrid converts two 1D arrays into two 2D arrays.
# X varies along columns, Y varies along rows.
# This gives us a grid of (x, y) coordinate pairs that
# plot_surface needs to evaluate z = f(x, y) at every point.
X, Y = np.meshgrid(x, y)

# Compute z values across the entire grid in one step
# (no loops needed thanks to NumPy broadcasting)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Create the figure and add a 3D axes.
# The projection='3d' argument is provided by mpl_toolkits.mplot3d
# and tells matplotlib to use 3D axes instead of the default 2D.
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface.
# cmap='viridis' maps z values to colors using the viridis colormap.
# Other options include 'plasma', 'coolwarm', 'inferno', etc.
# See matplotlib.cm for the full list of available colormaps.
#
# edgecolor='none' removes the wireframe grid lines on the surface,
# giving a smooth appearance. Try removing this argument to see the
# difference — it adds a black wireframe overlay on each grid cell.
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('z = sin(√(x² + y²))')

plt.tight_layout()
plt.show()

# Try dragging the plot with the mouse to rotate.
