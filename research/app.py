import math

# Main dimensions
main_dim_1 = 2.44
main_dim_2 = 1.22

# Plank dimensions to be cut
planks = [
    [1.50, 0.8],
    [1.00, 0.8],
    [1.50, 0.05],
    [1.00, 0.05],
    [0.98, 0.07],
    [0.82, 0.07],
    [0.82, 0.07],
    [0.70, 0.07]
]

# Calculate the total area of all planks
total_plank_area = sum([plank[0] * plank[1] for plank in planks])

# Calculate the total area of one main dimension
main_dim_area = main_dim_1 * main_dim_2

# Calculate the number of main dimensions needed
main_dim_count = math.ceil(total_plank_area / main_dim_area)

# Print the result
print(f"To cut all planks, you need {main_dim_count} main dimensions.")

print(total_plank_area)