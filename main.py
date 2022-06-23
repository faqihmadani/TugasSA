# Backtracking

class Graph():
    def __init__(self, vertex):
        self.graph = [[0 for column in range(vertex)]
                            for row in range(vertex)]
        self.V = vertex
      
    def aman(self, v, pos, path):
        # Mengecek apakah vertex tersebut merupakan tetangga 
        if self.graph[ path[pos-1] ][v] == 0:
            return False
 
        # Mengecek apakah vertex pernah dilalui atau tidak
        for vertex in path:
            if vertex == v:
                return False
 
        return True
 
    # Fungsi rekursif
    def rekursifHam(self, path, pos):
 
        # Apabila semua vertex telah dilalui
        if pos == self.V:
            # Mengecek apakah vertex pertama terhubung sehingga bisa membuat sirkuit
            if self.graph[ path[pos-1] ][ path[0] ] == 1:
                return True
            else:
                return False
 
        # Apabila belum melalui seluruh vertex maka akan mengecek vertex yang lain
        for v in range(1,self.V):
 
            if self.aman(v, pos, path) == True:
 
                path[pos] = v
 
                if self.rekursifHam(path, pos+1) == True:
                    return True
 
                # Mengisikan nilai -1
                path[pos] = -1
 
        return False
 
    def hamilton(self):
        path = [-1] * self.V
 
        #Menjadikan vertex 0 sebagai starter
        path[0] = 0
 
        if self.rekursifHam(path,1) == False:
            print ("Solusi tidak ditemukan\n")
            return False
 
        self.printSolusi(path)
        return True
 
    def printSolusi(self, path):
        print ("Solusi Ditemukan : ")
        n = 'A'
        for vertex in path:
            print (chr(ord(n) + vertex), end = "-")
            n = 'A'
        print (chr(ord(n) + path[0]), "\n")


     
print("Banyak vertex : ")
vertex = int(input())

g1 = Graph(vertex)
alp = 'A'


# Initialize matrix
matrix = []
  
# For user input

for i in range(vertex):          # Masukkan baris
    print("Masukkan ketetanggaan dari", alp)
    a =[]
    alp2 = 'A'
    for j in range(vertex):      # Masukkan kolom
        print(alp, "dengan", alp2, ":")
        a.append(int(input()))
        alp2 = chr(ord(alp2) + 1)
    matrix.append(a)
    alp = chr(ord(alp) + 1)

g1.graph = matrix
print(g1.graph)
g1.hamilton()


