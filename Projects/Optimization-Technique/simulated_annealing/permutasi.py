import random
from itertools import permutations
from math import exp

class SimulatedAnnealing:
    def __init__(self, distanceLibrary, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemp):
        self.distanceLibrary = distanceLibrary
        self.varRanges = varRanges
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemp = minTemp
        self.best_solution = None
        self.best_distance = float('inf')

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

        return random_combination, total_distance

    def changeTwoElement(self, neighbors):
        twoElement = 2
        randomIndex = set()
        while len(randomIndex) < twoElement:
            randomIndex.add(random.randint(0, len(neighbors)-1))
        
        randomIndex = list(randomIndex)
        
        # Swap the two elements
        temp = neighbors[randomIndex[0]]
        neighbors[randomIndex[0]] = neighbors[randomIndex[1]]
        neighbors[randomIndex[1]] = temp

        return neighbors

    def mainSA(self):
        temperature = 1000  # Initial temperature
        solution, solution_distance = self.randomSolution()
        self.best_solution = solution
        self.best_distance = solution_distance

        print(f"Initial Solution: {solution}, Objective Value: {solution_distance}")

        neighbor = self.changeTwoElement(list(solution))
        neighbor_distance = 0
        for j in range(len(neighbor) - 1):
            neighbor_distance += self.getDistance(neighbor[j], neighbor[j + 1])
        neighbor_distance += self.getDistance(neighbor[-1], 0)

        print(f"Solution 2 Element: {neighbor}, Objective Value: {neighbor_distance}")

        while temperature > self.stoppingValue:
            for i in range(self.maxIter):
                neighbor = self.changeTwoElement(list(solution))
                neighbor_distance = 0
                for j in range(len(neighbor) - 1):
                    neighbor_distance += self.getDistance(neighbor[j], neighbor[j + 1])
                neighbor_distance += self.getDistance(neighbor[-1], 0)

                deltaE = neighbor_distance - solution_distance
                metropolis = exp(-deltaE / temperature)

                if deltaE <= 0 or random.uniform(0, 1) < metropolis:
                    solution, solution_distance = neighbor, neighbor_distance

                if solution_distance < self.best_distance:
                    self.best_solution, self.best_distance = solution, solution_distance

            temperature *= 0.8  # Cooling schedule

        print(f"Optimum Solution: {self.best_solution}, Objective Value: {self.best_distance}")

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

run = SimulatedAnnealing(distanceLibrary, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemp)
run.mainSA()