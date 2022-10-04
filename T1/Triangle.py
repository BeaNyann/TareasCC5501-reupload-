from Vertex import Vertex

# Un triangulo (una cara)
# Se representa con sus vertices y sus vecinos triangulos
class Triangle:
    def __init__(self, vertexes):
        self.vertexes = vertexes #lista de vertices del triangulo
        self.neighbors = [None, None, None] #Los vecinos se le asignan cuando sea necesario

# Encuentra en el triangulo t la posición en donde se encuentra su vecino n
# Posiciones posibles 0 1 2
# Triangle x Triangle -> int
def find_neighbor(t, n):
    pos = -1
    neighbors = t.neighbors
    for i in range(3):
        if neighbors[i] == n:
            pos = i
            break
    return pos

# Encuentra en el triangulo t la posición en donde se encuentra su vertice v
# posiciones posibles 0 1 2
# Triangle x Vertex -> int
def find_vertex(t, v):
    pos = -1
    vertexes = t.vertexes
    for i in range(3):
        if vertexes[i] == v:
            pos = i
            break
    return pos

# Encuentra los vertices comunes de dos triangulos vecinos
# Arreglo [pos_v1t1, pos_v1t2, pos_v2t1. pos_v2t2]
# Posiciones posibles 0 1 2
# Triangle x Triangle -> Array
def find_common_vertexes(t1, t2):

    pos_arr = []
    vl_t1 = t1.vertexes
    for i in range(3):
        pos = find_vertex(t2, vl_t1[i])
        if  pos != -1: #realmente lo encontró
            pos_arr.append(i) #posición del vertice i en t1
            pos_arr.append(pos) #posición del vertice i en t2

    return pos_arr

# Dada la posicion de dos vertices en el vertex array
# Encuetra la posicion del tercero
# int x int -> int
def get_third_pos(pos1, pos2):
    pos = 3
    pos -= pos1
    pos -= pos2
    return pos