import random
import math
import itertools

class SimulatedAnnealing:
    def __init__(self, components, numOfInitSolution, maxIter, stoppingValue, minTemp):
        self.components = components
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemp = minTemp

    def getSolution(self, permutation):
        # Example evaluation function: sum of ASCII values of component names
        return sum(sum(ord(char) for char in component) for component in permutation)

    def getInitTemperature(self):
        ret = 0
        for _ in range(self.numOfInitSolution):
            permutation = random.sample(self.components, len(self.components))
            solution = self.getSolution(permutation)
            ret += solution
        return ret / self.numOfInitSolution

    def getCandidate(self):
        return random.sample(self.components, len(self.components))

    def mainSA(self):
        temperature = self.getInitTemperature()
        solution = random.sample(self.components, len(self.components))
        solutionVal = self.getSolution(solution)

        while temperature > self.stoppingValue:
            for _ in range(self.maxIter):
                candidate = self.getCandidate()
                candidateVal = self.getSolution(candidate)
                deltaE = candidateVal - solutionVal
                metropolis = math.exp(-deltaE / temperature)

                if deltaE <= 0 or random.uniform(0, 1) < metropolis:
                    solution, solutionVal = candidate, candidateVal
            if solutionVal < self.stoppingValue and temperature <= self.minTemp:
                print(solution, solutionVal)
                break
            else:
                temperature = 0.8 * temperature

components = ["Monitor", "RAM", "CPU", "GPU", "Motherboard", "Power Supply", "SSD", "HDD", "Case", "Cooling Fan"]
numOfInitSolution = 4
maxIter = 5
stoppingValue = 0.005
minTemp = 1

run = SimulatedAnnealing(components, numOfInitSolution, maxIter, stoppingValue, minTemp)
run.mainSA()