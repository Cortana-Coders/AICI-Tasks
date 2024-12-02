#untuk kos ke mana - ke mana - ke mana
import random
import sys
from itertools import permutations

distanceLibrary = {
    (0, 1): 4.4, (0, 2): 1.8, (0, 3): 3.4, (0, 4): 0.650, (0, 5): 0.700, (0, 6): 36,
    (1, 2): 3.3, (1, 3): 2.2, (1, 4): 4.9, (1, 5): 4, (1, 6): 34,
    (2, 3): 2, (2, 4): 2.9, (2, 5): 1.9, (2, 6): 35,
    (3, 4): 3.7, (3, 5): 2.8, (3, 6): 35,
    (4, 5): 0.9, (4, 6): 37,
    (5, 6): 36
}

# Fungsi untuk mengambil jarak antara dua titik
def get_distance(a, b):
    if (a, b) in distanceLibrary:
        return distanceLibrary[(a, b)]
    elif (b, a) in distanceLibrary:  # Jarak antara A ke B sama dengan B ke A
        return distanceLibrary[(b, a)]
    else:
        return 0  # Default jika tidak ada di library

solusi = list(permutations(range(0, 7)))

random_combination = random.choice(solusi)

total_distance = 0
for i in range(len(random_combination) - 1):
    total_distance += get_distance(random_combination[i], random_combination[i + 1])


# for combination in solusi:
#     total_distance = 0
#     for i in range(len(combination) - 1):
#         total_distance += get_distance(combination[i], combination[i + 1])
    
    total_distance += get_distance(random_combination[-1], 0)

    print(f"Trip: {random_combination}, Total Jarak: {total_distance}")
    sys.exit()