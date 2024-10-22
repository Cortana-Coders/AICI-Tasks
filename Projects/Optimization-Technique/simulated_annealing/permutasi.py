import random
import math

class SimulatedAnnealing:
    def __init__(self, components, numOfInitSolution, maxIter, stoppingValue, minTemp):
        self.components = components
        self.numOfInitSolution = numOfInitSolution
        self.maxIter = maxIter
        self.stoppingValue = stoppingValue
        self.minTemp = minTemp
        self.best_solutions = []

    def getSolution(self, permutation):
        # Menggunakan random seed berbeda setiap kali evaluasi
        random.seed() 
        total = sum(len(comp) for comp in permutation)
        return total + random.uniform(-10, 10)  # Memperbesar rentang variasi

    def getRandomPermutation(self):
        # Memastikan random seed berbeda setiap pemanggilan
        random.seed()
        permutation = []
        indices = []
        for i, component_list in enumerate(self.components):
            idx = random.randint(0, len(component_list)-1)
            permutation.append(self.components[i][idx])
            indices.append(idx + 1)
        return permutation, indices

    def mainSA(self, num_runs=5):
        random.seed()  # Reset random seed di awal proses
        all_solutions = []
        
        for run in range(num_runs):
            temperature = 1000 * random.uniform(0.5, 1.5)  # Temperatur awal yang lebih tinggi dan bervariasi
            solution, current_indices = self.getRandomPermutation()
            solutionVal = self.getSolution(solution)
            
            best_solution = solution.copy()
            best_indices = current_indices.copy()
            best_value = solutionVal
            
            iterations = 0
            while temperature > self.minTemp and iterations < random.randint(50, 150):  # Iterasi random
                iterations += 1
                for _ in range(self.maxIter):
                    candidate, candidate_indices = self.getRandomPermutation()
                    candidateVal = self.getSolution(candidate)
                    deltaE = candidateVal - solutionVal
                    
                    # Meningkatkan probabilitas penerimaan solusi yang lebih buruk
                    if deltaE < 0 or random.random() < math.exp(-deltaE / (temperature + 1)):
                        solution = candidate.copy()
                        current_indices = candidate_indices.copy()
                        solutionVal = candidateVal
                        
                        if solutionVal < best_value:
                            best_solution = solution.copy()
                            best_indices = current_indices.copy()
                            best_value = solutionVal

                temperature *= random.uniform(0.8, 0.98)  # Cooling rate yang bervariasi
                
                # Meningkatkan probabilitas random restart
                if random.random() < 0.2:
                    solution, current_indices = self.getRandomPermutation()
                    solutionVal = self.getSolution(solution)

            all_solutions.append((best_solution.copy(), best_indices.copy(), best_value))
            print(f"\nHasil Run ke-{run+1}:")
            print("Permutasi =", best_indices)
            print("Kombinasi Komponen:")
            for i, comp in enumerate(best_solution):
                print(f"{i+1}. {comp}")
            print("Nilai Solusi:", best_value)
            print("-" * 50)

        # Pilih solusi terbaik dari semua run
        best_overall = min(all_solutions, key=lambda x: x[2])
        print("\nSolusi Terbaik Keseluruhan:")
        print("Permutasi =", best_overall[1])
        print("Kombinasi Komponen:")
        for i, comp in enumerate(best_overall[0]):
            print(f"{i+1}. {comp}")
        print("Nilai Solusi:", best_overall[2])
        
        return best_overall[0], best_overall[2]

# Data komponen
components = [
    ["Monitor Alienware AW34QWD", "Monitor Samsung Odysey 34WAQ", "Monitor Benq 24O14N", "Monitor Acer 38ST21MKQ"],
    ["RAM Samsung 32x2", "RAM Asus Daxa 16x2", "RAM MSI G4800 32x2", "RAM MSI QWAD10 64x2"],
    ["Intel I9 16200HK CPU", "Intel 13 11200X", "Intel I7 13200HK"]
]

# Parameter yang lebih sesuai untuk menghasilkan variasi
numOfInitSolution = 5  # Lebih banyak solusi awal
maxIter = 15  # Lebih banyak iterasi per temperature
stoppingValue = 0.0001  # Nilai stopping yang lebih kecil
minTemp = 0.01  # Temperatur minimal yang lebih kecil

# Jalankan algoritma
sa = SimulatedAnnealing(components, numOfInitSolution, maxIter, stoppingValue, minTemp)
solution, value = sa.mainSA(num_runs=5)