# Soal 1
import random
def representasiBiner(jumlahBit):
    ret = []
    for _ in range(jumlahBit):
        ret.append(random.randint(0, 1))
    return ret

jumlahBit = 8
solusi = representasiBiner(jumlahBit)
print(solusi)

# Soal 2
def representasiDiskrit(variables):
    ret = []
    for i in range(len(variables)):
        ret.append(random.randint(variables[i][0], variables[i][1]))
    return ret

variables = [
    [1, 5],
    [1, 8],
    [1, 15],
    [1, 3]
]
solusi = representasiDiskrit(variables)
print(solusi)

# Soal 3
from itertools import permutations
solusi = list(permutations(range(1,9)))
indexOfRepresentation = random.randint(0, len(solusi)-1)
print(solusi[indexOfRepresentation])


# Soal 4
def representasiReal(variables):
    ret = []
    for i in range(len(variables)):
        ret.append(random.uniform(variables[i][0], variables[i][1]))
    return ret

variables = [
    [5, 7.49],
    [7.5, 12.49],
    [12.5, 15]
]
solusi = representasiReal(variables)
print(solusi)