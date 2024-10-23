import random
import sys
from itertools import permutations

class SimulatedAnnealing:
    def __init__(self, distanceLibrary, numOfInitSolution, maxIter, stoppingValue, minTemp):
        self.distanceLibrary = distanceLibrary
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemp = minTemp
        self.best_solutions = []

    def getDistance(self, a, b):
        if (a, b) in self.distanceLibrary:
            return self.distanceLibrary[(a, b)]
        elif (b, a) in self.distanceLibrary:
            return self.distanceLibrary[(b, a)]
        else:
            return 0

    def randomSolution(self):
        solusi = list(permutations(range(0, 7)))
        random_combination = random.choice(solusi)

        total_distance = 0
        for i in range(len(random_combination) - 1):
            total_distance += self.getDistance(random_combination[i], random_combination[i + 1])

        total_distance += self.getDistance(random_combination[-1], 0)

        print(f"Solusi Awal: {random_combination}, Total Jarak: {total_distance}")
        return random_combination

    def changeTwoElement(self, neighbors):
        twoElement = 2
        randomIndex = set()
        while len(randomIndex) < twoElement:
            randomIndex.add(random.randint(0, len(neighbors)-1))
        
        randomIndex = list(randomIndex)
        
        # Tukar kedua elemen
        temp = neighbors[randomIndex[0]]
        neighbors[randomIndex[0]] = neighbors[randomIndex[1]]
        neighbors[randomIndex[1]] = temp

        return neighbors

    def mainSA(self):
        temperature = self.getInitTemprature()
        solutionVals = random.uniform(self.varRanges[0], self.varRanges[1])
        solution = self.getSolution(solutionVals)
        candidate = self.getCandidate(self.varRanges)
        varRanges = self.getNewVarRanges(candidate)

# Data komponen
distanceLibrary = {
    (0, 1): 4.4, (0, 2): 1.8, (0, 3): 3.4, (0, 4): 0.65, (0, 5): 0.70, (0, 6): 36,
    (1, 2): 3.3, (1, 3): 2.2, (1, 4): 4.9, (1, 5): 4, (1, 6): 34,
    (2, 3): 2, (2, 4): 2.9, (2, 5): 1.9, (2, 6): 35,
    (3, 4): 3.7, (3, 5): 2.8, (3, 6): 35,
    (4, 5): 0.9, (4, 6): 37,
    (5, 6): 36
}

varRanges = [-5, 5]
numOfInitSolution = 5
maxIter = 15
stoppingValue = 0.0001
minTemp = 0.01

run = SimulatedAnnealing(distanceLibrary, numOfInitSolution, maxIter, stoppingValue, minTemp)
initial_solution = run.randomSolution()
changed_solution = run.changeTwoElement(list(initial_solution))

total_distance_changed = 0
for i in range(len(changed_solution) - 1):
    total_distance_changed += run.getDistance(changed_solution[i], changed_solution[i + 1])

total_distance_changed += run.getDistance(changed_solution[-1], 0)

print(f"Solusi Two Element: {changed_solution}, Nilai Objektif: {total_distance_changed}")