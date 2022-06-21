# Backtracking

class Graph():
    def __init__(self, vertex):
        self.graph = [[0 for column in range(vertex)]
                            for row in range(vertex)]
        self.V = vertex


print("Banyak vertex : ")
vertex = int(input())
print([-1] * vertex)

g1 = Graph(vertex)
alp = 'A'

# Initialize matrix
matrix = []
  
# For user input
for i in range(vertex):          # A for loop for row entries
    print("Masukkan ketetanggaan dari", alp)
    a =[]
    alp2 = 'A'
    for j in range(vertex):      # A for loop for column entri
        print(alp, "dengan", alp2, ":")
        a.append(int(input()))
        alp2 = chr(ord(alp2) + 1)
    matrix.append(a)
    alp = chr(ord(alp) + 1)

g1.graph = matrix
print(g1.graph)
x = [[0 for i in range(vertex)]

# def hamiltonian(k):
#     while True :
#         nextVertex(k)
#         if x[k] ==  0 :
#           return None
#         if k == self.V :
#           print(x)
#         else
#           hamiltonian(k+1)

# def nextVertex(k) :
#     while True :
#       x[k] = 
  
