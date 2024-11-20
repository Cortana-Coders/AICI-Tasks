import random
import sys

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
    'maxIter': 25,
    'cityNames': cityNames
}

class AntColonyOptimizationTSP:
    def __init__(self, parameters, start):
        self.params = parameters
        self.start = start
    
    # Primary Method untuk menyimpan seluruh alamt yang dikunjungi oleh setiap semut
    def ACOTSProblem(self):
        tabulist = []; feromon = 1/len(self.params['matriks']) # inisialisasi feromon
        for iter in range(self.params['maxIter']):
            print(f"iterasi ke-{iter}")
            for i in range(self.params['antSize']): # tabulist dihasilkan []..15x
                if self.start:
                    nextCity = self.start[0]
                else:
                    nextCity = random.randint(0, len(self.params['matriks'])-1)
                tabulist.append([nextCity])
            print(tabulist)
            # tabulist = []

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
                    print(pairedCity)
                    
                    # Panggil method getDistance dalam method utama ACOTSProblem
                    pairedDistance = self.getDistance(pairedCity)
                    pairedCity = []
                    # Panggil method probNextCities dalam method utama ACOTSProblem
                    probNextCities = self.getProbNextCities(pairedDistance, feromon)
                    print(probNextCities, sum(probNextCities))
                    print(pairedDistance)
                    print()
                # pairedDistance = []
                sys.exit()
    
    # Mendapatkan jarak berdasarkan pasangan matriks antara barisxkolom.
    def getDistance(self, pairedCities):
        rets = []
        for i in pairedCities:
            for j in range(len(self.params['matriks'])):
                for k in range(len(self.params['matriks'][j])):
                    if i[0] == j and i[1] == k:
                        rets.append(self.params['matriks'][j][k])
        return rets 
    
    # Menghitung probabilitas tujuan kota atau alamat berikutnya
    def getProbNextCities(self, distancePaired, feromon):
        ret = []
        for distance in distancePaired:
            if distance == 0:
                val = 0
            else:
                val = (1/distance) * feromon
            ret.append(val)
        return ret 
    
    # 
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
        

# Start = [], titik awal berangkat setiap semut berawal di kota ke-0(jogja)
# jika titik awal kosong, maka setiap semut akan ditugaskan ke titik awal berbeda-beda karena fungsi random di line 52(ACOTSProblem)
aco = AntColonyOptimizationTSP(parameters, start = [])
aco.ACOTSProblem() 