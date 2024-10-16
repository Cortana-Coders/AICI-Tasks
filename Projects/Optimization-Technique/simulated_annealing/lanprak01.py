import random
import math

class SimulatedAnnealing:
    def __init__(self, varRanges, numOfInitSolution, maxIter, stoppingValue, minTemp):
        self.varRanges = varRanges
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemp = minTemp

    def getSolution(self, var):
        return var**2

    def getInitTemperature(self):
        ret = 0
        for _ in range(self.numOfInitSolution):
            for i in range(len(self.varRanges)):
                solution = self.getSolution(random.uniform(self.varRanges[0], self.varRanges[1]))
                ret += solution
        return ret / self.numOfInitSolution

    def getCandidate(self, varRanges):
        u = random.uniform(0, 1)
        val = varRanges[0] + u * (varRanges[1] - varRanges[0])
        return val

    def mainSA(self):
        temperature = self.getInitTemperature()
        solutionVals = random.uniform(self.varRanges[0], self.varRanges[1])
        solution = self.getSolution(solutionVals)

        candidate = self.getCandidate(self.varRanges)
        varRanges = self.getNewRanges(candidate)

        while temperature > self.stoppingValue:
            for i in range(self.maxIter):
                candidate = self.getCandidate(varRanges)
                varRanges = self.getNewVarRanges(candidate)

                neighbor = self.getSolution(candidate)
                deltaE = neighbor - solution
                metropolis = math.exp(-deltaE / temperature)

                if deltaE <= 0 or random.uniform(0, 1) < metropolis:
                    solutionVals, solution = candidate, neighbor
            if solution < self.stoppingValue and temperature <= self.minTemp:
                print(solution, solutionVals)
                break
            else:
                temperature = 0.8 * temperature

varRanges = [-5, 5]
numOfInitSolution = 4
maxIter = 5
stoppingValue = 0.005
minTemp = 1

run = SimulatedAnnealing(varRanges, numOfInitSolution, maxIter, stoppingValue, minTemp)
print(run)