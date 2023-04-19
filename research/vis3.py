import numpy as np
import matplotlib.pyplot as plt

# Define the main dimension and plank dimensions
# main_dim = [2.44, 1.22]

main_dim = [3, 3]

mainplank = [2.44, 1.22]

plank_dims = [
    [1.40, 0.8], 
    [1.00, 0.8], 
    [1.50, 0.05], 
    [1.00, 0.05], 
    [0.98, 0.07], 
    [0.82, 0.07], 
    [0.82, 0.07], 
    [0.70, 0.07]
]
# Generate random colors for each plank
colors = np.random.rand(len(plank_dims), 3)

# Create the figure and axis
fig, ax = plt.subplots()

# Set the x and y limits of the axis
ax.set_xlim([0, main_dim[0]])
ax.set_ylim([0, main_dim[1]])

# Set the background color of the figure
fig.patch.set_facecolor('white')

# Create a rectangle for the main dimension and add it to the axis
main_rect = plt.Rectangle((0, 0), main_dim[0], main_dim[1], linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(main_rect)


mainplank_rect = plt.Rectangle((0, 0), mainplank[0], mainplank[1], linewidth=2, edgecolor='black', facecolor='grey')
ax.add_patch(mainplank_rect)

# Try to add each plank to the figure
x, y = 0, 0

rect = plt.Rectangle((x, y), plank_dims[0][0], plank_dims[0][1], linewidth=1, edgecolor='black', facecolor=colors[0])
ax.add_patch(rect)

# print(plank_dims[0][0],plank_dims[0][1])

x, y = plank_dims[0][0], 0

rect = plt.Rectangle((x, y), plank_dims[1][0], plank_dims[1][1], linewidth=1, edgecolor='black', facecolor=colors[1])
ax.add_patch(rect)


x, y = 0, plank_dims[0][1]

rect = plt.Rectangle((x, y), plank_dims[2][0], plank_dims[2][1], linewidth=1, edgecolor='black', facecolor=colors[2])
ax.add_patch(rect)

x, y = 0, plank_dims[0][1] + plank_dims[2][1]

rect = plt.Rectangle((x, y), plank_dims[3][0], plank_dims[3][1], linewidth=1, edgecolor='black', facecolor=colors[3])
ax.add_patch(rect)


x, y = 0, plank_dims[0][1] + plank_dims[2][1] + plank_dims[3][1]

rect = plt.Rectangle((x, y), plank_dims[4][0], plank_dims[4][1], linewidth=1, edgecolor='black', facecolor=colors[4])
ax.add_patch(rect)

x, y = 0, plank_dims[0][1] + plank_dims[2][1] + plank_dims[3][1] + plank_dims[4][1]

rect = plt.Rectangle((x, y), plank_dims[5][0], plank_dims[5][1], linewidth=1, edgecolor='black', facecolor=colors[5])
ax.add_patch(rect)

x, y = 0, plank_dims[0][1] + plank_dims[2][1] + plank_dims[3][1] + plank_dims[4][1] + plank_dims[5][1]

rect = plt.Rectangle((x, y), plank_dims[6][0], plank_dims[6][1], linewidth=1, edgecolor='black', facecolor=colors[6])
ax.add_patch(rect)

x, y = 0, plank_dims[0][1] + plank_dims[2][1] + plank_dims[3][1] + plank_dims[4][1] + plank_dims[5][1] + plank_dims[6][1]

rect = plt.Rectangle((x, y), plank_dims[7][0], plank_dims[7][1], linewidth=1, edgecolor='black', facecolor=colors[7])
ax.add_patch(rect)

# Show the plot
plt.show()
