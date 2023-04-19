import numpy as np
import matplotlib.pyplot as plt

# Define the main dimension and plank dimensions
# main_dim = [2.44, 1.22]

main_dim = [3, 3]
mainplank = [2.44, 1.22]

cut = 0.006

plank_dims = [
    [1.40, 0.8], 
    [1.50, 0.05], 
    [1.00, 0.05], 
    [0.98, 0.07], 
    [1.00, 0.8], 
    [0.82, 0.07], 
    [0.82, 0.07], 
    [0.70, 0.07],
    # [1.50, 0.8],
    # [0.82, 0.07]
]

plank_dims = sorted(plank_dims, key=lambda x: x[1],reverse=True)

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

savey = 0

for a,plank_dim in enumerate(plank_dims):

    abort = False
    # Check if the plank can fit horizontally
    if plank_dim[0] > mainplank[0] or plank_dim[1] > mainplank[1]:
        abort = True
        # print(f"Can't fit plank with dimensions {plank_dim}")

    if not abort:
        if x + plank_dim[0] <= mainplank[0]:
            if x > 0:
                x += cut

            rect = plt.Rectangle((x, y), plank_dim[0], plank_dim[1], linewidth=1, edgecolor='black', facecolor=colors[a])
            ax.add_patch(rect)
            
            x += plank_dim[0]
            
            print(x,y,'added hor')

            savey = plank_dim[1] + cut
        # Check if the plank can fit vertically
        elif y + plank_dim[1] <= mainplank[1]:
            x = 0

            if savey > 0:
                y += savey
                savey = 0
            else:
                y += plank_dim[1] + cut

            rect = plt.Rectangle((x, y), plank_dim[0], plank_dim[1], linewidth=1, edgecolor='black', facecolor=colors[a])
            ax.add_patch(rect)
            x += plank_dim[0]
            print(x,y,'added ver')
        else:
            print(f"we need another plaat for this {plank_dim}")
            abort = True
        
    if abort:
        print(f"Can't fit plank with dimensions {plank_dim}")

# Show the plot
plt.show()
