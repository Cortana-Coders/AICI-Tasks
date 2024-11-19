import random, math, sys
from itertools import permutations
import math

class SimulatedAnnealingPermutation:
    def __init__(self, distances, initTemp, minTemp, coolingRate, maxIter):
        self.distances = distances
        self.initTemp = initTemp
        self.minTemp = minTemp
        self.coolingRate = coolingRate
        self.maxIter = maxIter
        self.location = len(distances)

    def getInitialSolution(self):
        # Menghasilkan solusi awal secara acak dari permutasi lokasi
        solusi = list(permutations(range(1, self.location + 1)))
        indexOfRepresentation = random.randint(0, len(solusi) - 1)
        # print(solusi[indexOfRepresentation])
        # sys.exit()
        return list(solusi[indexOfRepresentation])


    def calculateTotalDistance(self, solution):
        # Menghitung total jarak untuk suatu solusi permutasi
        total_distance = 0
        for i in range(len(solution) - 1):
            total_distance += self.distances[solution[i] - 1][solution[i + 1] - 1]
        return total_distance

    def getNeighbour(self, solution):
        neighbour = solution[:]
        idx = random.randint(0, len(solution) - 1)

        idxList = [(idx + i) % len(solution) for i in range(4)] # Menentukan indeks rotasi dengan memperhatikan wrap-around

        for i in range(2):
            neighbour[idxList[i]], neighbour[idxList[3 - i]] = neighbour[idxList[3 - i]], neighbour[idxList[i]]  # Balik urutan keempat elemen tersebut
        
        return neighbour
    
    def acceptanceProbability(self, oldCost, newCost, temperature):
        # Jika solusi baru lebih baik, terima langsung
        if newCost < oldCost:
            return 1.0
        # Jika lebih buruk, terima dengan probabilitas tertentu
        return math.exp((oldCost - newCost) / temperature)
    
    def mainSA(self):
        # Inisialisasi solusi awal dan suhu
        currentSolution = self.getInitialSolution()
        currentCost = self.calculateTotalDistance(currentSolution)
        bestSolution = currentSolution[:]
        bestCost = currentCost

        temperature = self.initTemp
        iteration = 0

        # Simulated Annealing loop
        while temperature > self.minTemp and iteration < self.maxIter:
            newSolution = self.getNeighbour(currentSolution)
            newCost = self.calculateTotalDistance(newSolution)            

            print(f"Iterasi {iteration + 1}:")
            print(f"Solusi saat ini: {currentSolution}, Biaya: {currentCost:.2f}")
            print(f"Solusi tetangga: {newSolution}, Biaya: {newCost:.2f}")

            # Tentukan apakah akan menerima solusi baru
            if self.acceptanceProbability(currentCost, newCost, temperature) > random.random():
                currentSolution = newSolution
                currentCost = newCost

            # Perbarui solusi terbaik jika ditemukan solusi yang lebih baik
            if newCost < bestCost:
                bestSolution = newSolution
                bestCost = newCost

            # Kurangi suhu
            temperature *= self.coolingRate
            iteration += 1
            print(f"Temperatur: {temperature:.2f}, Best Cost: {bestCost:.2f}\n")
        # sys.exit()
        return bestSolution, bestCost

# Matrix dari jarak antar lokasi
distancesLibrary = [
    [0, 4.4, 2.3, 3.3, 0.6, 0.6, 37.8, 4.5],
    [4.4, 0, 3.4, 2.2, 5.3, 4.0, 33.6, 5.5],
    [2.3, 3.0, 0, 2.0, 3.3, 2.0, 35.0, 6.5],
    [3.3, 1.9, 2.0, 0, 4.1, 2.8, 34.5, 3.2],
    [0.6, 5.4, 2.4, 3.9, 0, 1.2, 38.2, 7.5],
    [0.6, 3.9, 2.0, 2.8, 1.2, 0, 37.1, 6.6],
    [37.8, 33.6, 35.0, 34.5, 38.2, 37.1, 0, 4.4],
    [4.5, 5.5, 6.5, 3.2, 7.5, 6.6, 4.4, 0]
]

# Inisialisasi Simulated Annealing dengan parameter
run = SimulatedAnnealingPermutation(
    distances=distancesLibrary,
    initTemp=1000,
    minTemp=0.01,
    coolingRate=0.95,
    maxIter=500
)
# # Dapatkan solusi awal acak
# initial_solution = run.getInitialSolution()
# initial_cost = run.calculateTotalDistance(initial_solution)

# print(f"{initial_solution} {initial_cost:.2f}")

# # Dapatkan solusi tetangga dari solusi awal
# neighbour_solution = run.getNeighbour(initial_solution)
# neighbour_cost = run.calculateTotalDistance(neighbour_solution)

# print(f"{neighbour_solution} {neighbour_cost:.2f}")

# Jalankan algoritma
best_solution, best_cost = run.mainSA()

# Tampilkan hasil
print(f"Solusi terbaik: {best_solution}")
print(f"Biaya terbaik (total jarak): {best_cost:.2f} KM")