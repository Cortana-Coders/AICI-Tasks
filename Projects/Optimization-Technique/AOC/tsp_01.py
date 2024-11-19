import random, sys

matriks = [
    [0, 360, 185, 335, 160, 340, 334, 362, 163, 204],
    [360, 0, 293, 579, 269, 601, 583, 610, 370, 318],
    [185, 293, 0, 405, 261, 408, 409, 202, 80.6, 21.4],
    [335, 579, 405, 0, 313, 4, 24, 56.5, 164, 241],
    [160, 269, 26.1, 313, 0, 383, 382, 225, 104, 45.8],
    [340, 601, 408, 4, 383, 0, 22.5, 56.5, 164, 244],
    [334, 583, 409, 24, 382, 22.5, 0, 75.9, 181, 336],
    [362, 610, 202, 56.5, 225, 56.5, 75.9, 0, 120, 200],
    [163, 370, 80.6, 164, 104, 164, 181, 120, 0, 80.9],
    [204, 318, 21.4, 241, 45.8, 244, 336, 200, 80.9, 0]
]

# Nama kota
cityNames = [
    "Jogja", 
    "Sunan Gunung Jati (Cirebon)", 
    "Sunan Kudus", 
    "Sunan Giri (Gresik)", 
    "Sunan Kalijaga (Demak)",
    "Sunan Gresik", 
    "Sunan Ampel (Surabaya)", 
    "Sunan Drajat (Lamongan)", 
    "Sunan Bonang (Tuban)", 
    "Sunan Muria (Kudus)"
]

parameters = {
    'Q': 100, 
    'rho': 0.6, 
    'antSize': 15, 
    'matriks': matriks, 
    'maxIter': 25
}

class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start
    
    # Primary Method untuk menyimpan seluruh alamt yang dikunjungi oleh setiap semut
    def ACOTSProblem(self):
        tabulist = []

        for iter in range(self.params['maxIter']):
            for i in range(self.params['antSize']):
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabulist.append([nextCity])
            print(tabulist)
            tabulist = []


aco = AntColonyOptimizationTSP(parameters, start = [0])
aco.ACOTSProblem() 