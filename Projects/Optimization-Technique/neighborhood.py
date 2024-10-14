import itertools

# Generate the Cartesian product and convert it to a list
neighborhood = list(itertools.product([0, 1], repeat=3))

# Print the resulting list
print(neighborhood)