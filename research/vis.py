import matplotlib.pyplot as plt
import numpy as np

# Dimensions of the main rectangle
main_dim = (244, 122)

# Dimensions of the planks
plank_dims = [
    (150, 80),
    (100, 80),
    (150, 5),
    (100, 5),
    (98, 7),
    (82, 7),
    (82, 7),
    (70, 7)
]

# Generate random colors for the planks
colors = np.random.rand(len(plank_dims), 3)

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the limits of the x and y axes
ax.set_xlim(0, main_dim[0])
ax.set_ylim(0, main_dim[1])

# Add a rectangle to represent the main dimension
rect = plt.Rectangle((0, 0), main_dim[0], main_dim[1], linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(rect)

# Add rectangles to represent the planks
for i, dim in enumerate(plank_dims):
    # Set the lower left corner of the rectangle
    x = np.random.uniform(0, main_dim[0] - dim[0])
    y = np.random.uniform(0, main_dim[1] - dim[1])
    # Add the rectangle to the axis
    rect = plt.Rectangle((x, y), dim[0], dim[1], linewidth=1, edgecolor='black', facecolor=colors[i])
    ax.add_patch(rect)

# Show the plot
plt.show()
