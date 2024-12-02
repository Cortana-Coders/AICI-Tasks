import random, sys, math
from itertools import permutations

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
    'rho': 0.6, # penguapan feromon(seberapa cepat feromon menguap dari jalur)
    'antSize': 15, 
    'matriks': matriks, 
    'maxIter': 25,
    'cityNames': cityNames # daftar nama kota
}

class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start
    
    # Primary Method untuk menyimpan seluruh alamt yang dikunjungi oleh setiap semut
    def ACOTSProblem(self):
        tabulist = []; feromon = 1/len(self.params['matriks']); finalDistance = []; allDistances = []; finalResults = []; bestSolutions = [] # inisialisasi feromon
        for iter in range(self.params['maxIter']):
            print(f"iterasi ke-{iter}")
            for i in range(self.params['antSize']): # tabulist dihasilkan []..15x
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabulist.append([nextCity])
            print(tabulist)
            

            temp = []; city = []; pairedCity = []; matriks = self.params['matriks']
            for i in range(len(matriks) - 1):
                for j in range(len(tabulist)):
                    r = random.uniform(0,1) #bangkitkan bilangan acak antara 0 dan 1
                    # print(tabulist[j])

                    for cityID in range(len(matriks)):
                        for k in tabulist[j]:
                            temp.append(k)
                            temp.append(cityID)
                        # jika tabulist[j] == banyak elemen cityID pada larik temp(lakukan penambahan elemen ke larik city)
                        if temp.count(cityID) == len(tabulist[j]):
                            city.append(tabulist[j][-1])
                            city.append(cityID)
                        # tambahkan elemen ke larik city. Menunjukan bahwa pasangan kota atau alamatnya sama. Contoh: Jogja ke Jogja
                        else:
                            city.append(cityID)
                            city.append(cityID)
                        pairedCity.append(city)
                        city = []; temp = []
                    # Panggil method getDistance dalam method utama ACOTSProblem
                    pairedDistance = self.getDistance(pairedCity)
                    pairedCity = []
                    # Panggil method probNextCities dalam method utama ACOTSProblem
                    probNextCities = self.getProbNextCities(pairedDistance, feromon)
                    # Panggil method getNextCities dalam method utama ACOTSProblem
                    nextCities = self.getNextCities(probNextCities, r)
                    tabulist[j].append(nextCities)
            print(tabulist)
            print()
            # pairedDistance = []

            for k in range(len(tabulist)):
                for l in range(len(tabulist[k])-1):
                    city.append(tabulist[k][l]) 
                    city.append(tabulist[k][l+1]) 
                    pairedCity.append(city) 
                    city = [] 
                pairedCity.append([tabulist[k][-1], tabulist[k][0]])         
                pairedDistance = self.getDistance(pairedCity)
                name = self.getPairedCityName(tabulist[k])
                finalDistance.append([name, pairedDistance])
                allDistances.append(sum(pairedDistance))
                pairedCity = []
            minIndex = allDistances.index(min(allDistances))
            finalResults.append(finalDistance[minIndex])
            bestSolutions.append(min(allDistances))
            finalDistance = []; allDistances = []; tabulist = []
        shortestRoutes = finalResults[bestSolutions.index(min(bestSolutions))]
        print(f"Rute terpendek ziarah makan wali songo: ")
        for i in shortestRoutes[0]:
            print(i)
        print(shortestRoutes[0][0])
        print(sum(shortestRoutes[1]), 'Kilometer')
                
    
    def getInitialSolution(self):
        # Menghasilkan solusi awal secara acak dari permutasi lokasi
        solusi = list(permutations(range(1, self.location + 1)))
        indexOfRepresentation = random.randint(0, len(solusi) - 1)
        # print(solusi[indexOfRepresentation])
        # sys.exit()
        return list(solusi[indexOfRepresentation])

    # Mendapatkan jarak berdasarkan pasangan matriks antara barisxkolom.
    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.params['matriks'])):
                for k in range(len(self.params['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.params['matriks'][j][k])
        return rets 
    
    # # Menghitung probabilitas tujuan kota atau alamat berikutnya
    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1/distance) * feromon
            ret.append(val)
        return ret 
    
    # # Memberikan kembalian berupa id kota(int) yg merupakan kota berikutnya yg akan dikunjungi oleh semut.
    def getNextCities(self, probNextCities, r):
        temp = 0
        for i in range(len(probNextCities)):
            if sum(probNextCities) != 0:
                temp += (probNextCities[i] / sum(probNextCities))
            else:
                temp = 0
            
            if r < temp:
                i
                break
        return i
    
    def getPairedCityName(self, tabulist):
        rets = []
        for i in tabulist:
            for j in range(len(self.params['cityNames'])):
                if i == j:
                    rets.append(self.params['cityNames'][j])
        return rets
        

# Start = [], titik awal berangkat setiap semut berawal di kota ke-0(jogja)
# jika titik awal kosong, maka setiap semut akan ditugaskan ke titik awal berbeda-beda karena fungsi random di line 52(ACOTSProblem)
aco = AntColonyOptimizationTSP(parameters, start = [])
aco.ACOTSProblem() 