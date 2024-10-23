import random, sys
from itertools import permutations 

class SimulatedAnnealing:

    def _init_(self, priceComponent, numOfInitSolution, maxIter, stoppingValue, minTemperature): 
        self.priceComponent = priceComponent
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemperature = minTemperature 

    def getInitRep(self):

        repSol = []
        for components in self.priceComponent:
            randomIndex = random.randint(0, len(components)-1)
            repSol.append(randomIndex)
        return repSol

    def calcObjFunction(self, solRep):
        total = 0
        for i in range(len(solRep)):
            total += self.priceComponent[i][solRep[i]]
        return total
    
    from itertools import permutations
        solusi = list(permutations(range(1,4)))
        indexOfRepresentation = random.randint(0, len(solusi)-1)
5. print(solusi[indexOfRepresentation])

    def mainSA(self):
        temperature = 1000
        solRep = self.getInitRep()
        objValue = self.calcObjFunction(solRep)
        print(solRep, objValue)


# Rep. Biner
location = 8
# dataHarga = [324,34,343,434,4545 ]
priceComponent = [[432243, 2342, 245],
 [234, 0, 245, 2342, 34234, 243, 234342, 43 ], 
 [234, 2342, 0, 2342, 34234], 
 [234, 2342, 245, 0, 34234, 243, 234342, 43 ],
 [234, 2342, 245, 2342, 34234, 243, 234342, 43 ],
 [234, 2342, 245, 2342, 34234, 234342, 43 ],
 [234, 2342, 34234, 243, 234342, 43 ],
 [234, 2342, 245, 2342, 34234, 243, 234342, 43 ]
]

numOfInitSolution = 4 
maxIter = 5 
stoppingValue = 0.005 
minTemperature = 1 
  
run = SimulatedAnnealing(priceComponent, numOfInitSolution, maxIter, stoppingValue, minTemperature) 
run.mainSA()