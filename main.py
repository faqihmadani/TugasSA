import time

# Backtracking

class Graph():
    def __init__(self, vertex):
        self.graph = [[0 for column in range(vertex)]
                            for row in range(vertex)]
        self.V = vertex

    #Backtracking
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
        start_time = time.time()
        path = [-1] * self.V
 
        #Menjadikan vertex A sebagai starter
        path[0] = 0
 
        if self.rekursifHam(path,1) == False:
            print ("Solusi tidak ditemukan\n")
            return False
 
        self.printSolusi(path)
        print("Waktu untuk menyelesaikan program ini adalah", time.time() - start_time, "detik")
        return True
 
    def printSolusi(self, path):
        print ("Solusi Ditemukan : ")
        n = 'A'
        for vertex in path:
            print (chr(ord(n) + vertex), end = "-")
            n = 'A'
        print (chr(ord(n) + path[0]), "\n")
        
    # Dynamic Programming
    def dynamicProgramming(self):
     
      dp = [[False for i in range(1 << self.V)]
                   for j in range(self.V)]
   
      # Setting dp[i][(1 << i)] menjadi true
      for i in range(self.V):
          dp[i][1 << i] = True
   
      # Iterasi ke seluruh subset dari suatu nodes
      for i in range(1 << self.V):
          for j in range(self.V):
   
              # Jika nodes ke j termasuk dalam subset
              if ((i & (1 << j)) != 0):
   
                  # Mencari tetangga dari j juga terdapat pada subset
                  for k in range(self.V):
                      if ((i & (1 << k)) != 0 and
                               self.graph[k][j] == 1 and
                                       j != k and
                            dp[k][i ^ (1 << j)]):
                           
                          # Update dp[j][i]
                          # to true
                          dp[j][i] = True
                          break
       
      # Traverse the vertices
      for i in range(self.V):
   
          # Hamiltonian ditemukan
          if (dp[i][(1 << self.V) - 1]):
              return True
   
      # Jika tidak return false
      return False

    def printDynamicProgramming(self):
      start_time = time.time()
      if self.dynamicProgramming():
        print("Ya, terdapat hamiltonian circuit")
      else:
        print("Tidak terdapat hamiltonian circuit")
      print("Waktu untuk menyelesaikan program ini adalah", time.time() - start_time, "detik")
      
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

ulang = 'Y'
while(ulang == 'Y'):
  print("\n Selesaikan menggunakan algoritma :\n1. Backtracking\n2. Dynamic Programming")
  pilihan = int(input())
  if pilihan == 1:
    g1.hamilton()
  elif pilihan == 2:
    print("jalankan dynamic programming:")
    g1.printDynamicProgramming()
  print("Apakah anda ingin mengulangi lagi? Y/N")
  ulang = input()
