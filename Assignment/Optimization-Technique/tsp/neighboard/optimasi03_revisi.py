import random

num_points = 7
distance_matrix = [[0 if i == j else round(random.uniform(1, 10), 1) for j in range(num_points)] for i in range(num_points)]

print("Distance Matrix:")
for row in distance_matrix:
    print(row)

middle_points = list(range(1, num_points))
random.shuffle(middle_points)
random_path = [0] + middle_points + [0]

total_distance = 0
path_segments = []

for i in range(len(random_path) - 1):
    start = random_path[i]
    end = random_path[i + 1]
    segment_distance = distance_matrix[start][end]
    total_distance += segment_distance
    path_segments.append(f"[{start},{end}] = {segment_distance} km")

# Print results
print("\nRandom Path:")
print(" -> ".join(map(str, random_path)))

print("\nPath Segments:")
for segment in path_segments:
    print(segment)

print(f"\nTotal Distance: {round(total_distance, 1)} km")