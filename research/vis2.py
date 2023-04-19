import matplotlib.pyplot as plt
import numpy as np

main_dim = [2.44, 1.22]
plank_dims = [[1.5, 0.8], [1, 0.8], [1.5, 0.05], [1, 0.05], [0.98, 0.07], [0.82, 0.07], [0.82, 0.07], [0.7, 0.07]]

# Generate random colors for the planks
colors = np.random.rand(len(plank_dims), 3)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, main_dim[0]])
ax.set_ylim([0, main_dim[1]])

# Draw the main rectangle
main_rect = plt.Rectangle((0, 0), main_dim[0], main_dim[1], linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(main_rect)

# Draw the planks
for i, dim in enumerate(plank_dims):
    # Try to place the plank randomly
    while True:
        x = np.random.uniform(0, main_dim[0] - dim[0])
        y = np.random.uniform(0, main_dim[1] - dim[1])
        plank_rect = plt.Rectangle((x, y), dim[0], dim[1], linewidth=1, edgecolor='black', facecolor=colors[i])
        
        # Check if the plank overlaps with any previous plank
        overlaps = False
        for rect in ax.patches:
            if rect == main_rect:
                continue
            if plank_rect.bounds[0] < rect.bounds[2] and plank_rect.bounds[2] > rect.bounds[0] and \
               plank_rect.bounds[1] < rect.bounds[3] and plank_rect.bounds[3] > rect.bounds[1]:
                overlaps = True
                break
                
        if not overlaps:
            ax.add_patch(plank_rect)
            break

# Show the plot
plt.show()
