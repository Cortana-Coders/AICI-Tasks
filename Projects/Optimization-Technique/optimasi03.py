import random

num_points = 7
distance_matrix = [[0 if i == j else round(random.uniform(1, 10), 1) for j in range(num_points)] for i in range(num_points)]

print("Distance Matrix:")
for row in distance_matrix:
    print(row)

# Define the fixed path: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0
fixed_path = [0, 1, 2, 3, 4, 5, 6, 0]

# Calculate total distance
total_distance = 0
path_segments = []

for i in range(len(fixed_path) - 1):
    start = fixed_path[i] # jarak awal
    end = fixed_path[i + 1] # jarak akhir
    segment_distance = distance_matrix[start][end]
    total_distance += segment_distance
    path_segments.append(f"[{start},{end}] = {segment_distance} km")

# Print results
print("\nPath Segments:")
for segment in path_segments:
    print(segment)

print(f"\nTotal Distance: {round(total_distance, 1)} km")