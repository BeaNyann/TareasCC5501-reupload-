from os import remove
from Vertex import*
from Triangle import get_third_pos, find_common_vertexes, find_neighbor, Triangle, find_vertex, find_new_vertex, find_new_neighbor
from Draw import draw, draw_triangles
import numpy as np
import sys
import csv
import random

# Una triangulación
# Contiene la lista de vertices y la lista de triangulos
class Triangulation:
    def __init__(self, vertexes, triangles):
        self.vertexes = vertexes
        self.triangles = triangles

dibujar_triangulacion = False
dibujar_restricted = False

# Printea dos triangulos t y n, principalmente util para debugueo
# Triangle x Triangle -> void
def printear(t,n):
    if t != None:
        print(t.vertexes, "vertexes de t")
        print(f"{t.vertexes[0].x:.3f}, {t.vertexes[0].y:.3f}") 
        print(f"{t.vertexes[1].x:.3f}, {t.vertexes[1].y:.3f}")
        print(f"{t.vertexes[2].x:.3f}, {t.vertexes[2].y:.3f}")
    else:
        print("t is none")
    if n != None:
        print(n.vertexes,"vertexes de n")
        print(f"{n.vertexes[0].x:.3f}, {n.vertexes[0].y:.3f}") 
        print(f"{n.vertexes[1].x:.3f}, {n.vertexes[1].y:.3f}")
        print(f"{n.vertexes[2].x:.3f}, {n.vertexes[2].y:.3f}")
    else:
        print("n is none")

# Agrega un punto en una cara
# Entrega una triangulación local con el nuevo vertice y los nuevos triangulos
# Point x Triagle -> Triangulation
def add_point_in_face(p, t): #si se añaden counter clock wise

    #hacer u vertice con el punto p
    v = Vertex(*p) 
    vertexes = t.vertexes
    neighbors = t.neighbors

    #creo las vertex list para cada
    #triangulo nuevo
    vl3 = [vertexes[0], vertexes[1], v]
    vl2 = [vertexes[0], v, vertexes[2]]
    vl1 = [vertexes[2], v, vertexes[1]]

    t1 = Triangle(vl1)
    t2 = Triangle(vl2)
    t3 = Triangle(vl3)

    #creo las neighbors list para 
    #cada triangulo nuevo 
    nl3 = [t1, t2, neighbors[2]]
    nl2 = [t1, neighbors[1], t3]
    nl1 = [t3, neighbors[0], t2]

    t1.neighbors = nl1
    t2.neighbors = nl2
    t3.neighbors = nl3
    
    #actualizar los nuevos vecinos de los vecinos que existan
    n1 = neighbors[0]
    n2 = neighbors[1]
    n3 = neighbors[2]

    #quiero encontrar en el vecino n cual es la posicion en sus vecinos donde esta t
    if n1 != None:
        pos_n1 = find_neighbor(n1, t)
        n1.neighbors[pos_n1] = t1  
    if n2 != None:
        pos_n2 = find_neighbor(n2, t)
        n2.neighbors[pos_n2] = t2
    if n3 != None:
        pos_n3 = find_neighbor(n3, t) 
        n3.neighbors[pos_n3] = t3
    
    new_t = [t1, t2, t3]
    new_T = Triangulation([v], new_t)

    return new_T

# Agrega un punto en una arista
# Entrega una triangulación local con el nuevo vertice y los nuevos triangulos
# Point x Triagle x Triangle -> Triangulation
def add_point_in_edge(p, t1, t2): #no se estan añadiendo counter clock wise!

    #hacer u vertice con el punto p
    v = Vertex(*p) 
    
    #obtengo los vertices D y B (los extremos)
    positions = find_common_vertexes(t1, t2)
    pos_D = get_third_pos(positions[0], positions[2])
    pos_B = get_third_pos(positions[1], positions[3])

    #tengo D, A es pos D+1 y C es pos D-1 
    #tengo B, A es pos B-1 y C es pos B+1

    #obtengo sus sucesores y antecesores
    pos_C2 = (pos_B+1)%3 
    pos_A2 = (pos_B-1)%3

    pos_A1 = (pos_D+1)%3
    pos_C1 = (pos_D-1)%3

    #obtengo lista de vertices y de vecinos de los triangulos
    vl_t1 = t1.vertexes
    vl_t2 = t2.vertexes
    nl_t1 = t1.neighbors
    nl_t2 = t2.neighbors

    vD = vl_t1[pos_D]
    vB = vl_t2[pos_B]
    
    vA1 = vl_t1[pos_A1] #Vertice A para el triangulo 1
    vC1 = vl_t1[pos_C1] #Vertice C para el triangulo 1

    vA2 = vl_t2[pos_A2]
    vC2 = vl_t2[pos_C2]
    
    #obtener los vecinos 
    #siguiendo el orden el vecino NA1 debería estar 
    #en la misma posición que el vertice A y así
    nA1 = nl_t1[pos_A1]
    nC1 = nl_t1[pos_C1]

    nA2 = nl_t2[pos_A2]
    nC2 = nl_t2[pos_C2]
    
    #Triangulos a armar
    # D D+1 v = D A1 v = t1A
    # D v D-1 = D v C1 = t1C
    # B B+1 v = B C2 v = t2C
    # B v B-1 = B v A2 = t2A

    #creo las vertex list para cada
    #triangulo nuevo
    vl1A = [vD, vA1, v]
    vl1C = [vD, v, vC1]
    vl2A = [vB, v, vA2]
    vl2C = [vB, vC2, v]

    t1A = Triangle(vl1A)
    t1C = Triangle(vl1C)
    t2A = Triangle(vl2A)
    t2C = Triangle(vl2C)

    #creo las neighbors list para 
    #cada triangulo nuevo 
    nl1A = [t2A, t1C , nC1]
    nl1C = [t2C, nA1, t1A]
    nl2A = [t1A, nC2, t2C]
    nl2C = [t1C, t2A, nA2]

    t1A.neighbors = nl1A
    t1C.neighbors = nl1C
    t2A.neighbors = nl2A
    t2C.neighbors = nl2C

    #actualizar los nuevos vecinos de los vecinos
    #los vecinos son nA1 nC1 nA2 nC2
    if nA1 != None:
        pos_nA1 = find_neighbor(nA1, t1)
        nA1.neighbors[pos_nA1] = t1C
    if nC1 != None:
        pos_nC1 = find_neighbor(nC1, t1)
        nC1.neighbors[pos_nC1] = t1A
    if nA2 != None:
        pos_nA2 = find_neighbor(nA2, t2) 
        nA2.neighbors[pos_nA2] = t2C
    if nC2 != None:
        pos_nC2 = find_neighbor(nC2, t2)
        nC2.neighbors[pos_nC2] = t2A

    new_t = [t1A, t1C, t2A, t2C]
    new_T = Triangulation([v], new_t)

    return new_T

# Cambia la diagonal del poligono formado por t1 y t2
# Entrega una triangulación local con el nuevo vertice y los nuevos triangulos
# Triangle x Triagle -> Triangulation
def change_diagonal(t1, t2):

    #encontrar vertices comunes
    positions = find_common_vertexes(t1, t2)

    if positions == None:
        return None
    #tercer vertice de t1 y de t2
    pos_B = get_third_pos(positions[1], positions[3])
    pos_D = get_third_pos(positions[0], positions[2])

    #tengo D, A es pos D+1 y C es pos D-1 
    #tengo B, A es pos B-1 y C es pos B+1

    #obtengo sus sucesores y antecesores
    pos_C2 = (pos_B+1)%3 
    pos_A2 = (pos_B-1)%3

    pos_A1 = (pos_D+1)%3
    pos_C1 = (pos_D-1)%3

    #defino verties y vecinos
    vl1 = t1.vertexes
    vl2 = t2.vertexes
    nl1 = t1.neighbors
    nl2 = t2.neighbors

    vA1 = vl1[pos_A1] #Vertice A para el triangulo 1
    vC1 = vl1[pos_C1] #Vertice C para el triangulo 1

    vB = vl2[pos_B]
    vD = vl1[pos_D]

    #obtener los vecinos 
    #siguiendo el orden el vecino NA1 debería estar 
    #en la misma posición que el vertice A y así
    nA1 = nl1[pos_A1]
    nC1 = nl1[pos_C1]

    nA2 = nl2[pos_A2]
    nC2 = nl2[pos_C2]

    #creo las vertex list para cada
    #triangulo nuevo
    vlA = [vA1, vB, vD]
    vlC = [vC1, vD, vB]

    tA = Triangle(vlA)
    tC = Triangle(vlC)

    #creo las neighbors list para 
    #cada triangulo nuevo 
    nlA = [tC, nC1, nC2]
    nlC = [tA, nA2, nA1]

    tA.neighbors = nlA
    tC.neighbors = nlC

    #actualizar los nuevos vecinos de los vecinos
    #los vecinos son nA1 nC1 nA2 nC2
    if nA1 != None:
        pos_nA1 = find_neighbor(nA1, t1)
        nA1.neighbors[pos_nA1] = tC
    if nC1 != None:
        pos_nC1 = find_neighbor(nC1, t1)
        nC1.neighbors[pos_nC1] = tA
    if nA2 != None:
        pos_nA2 = find_neighbor(nA2, t2) 
        nA2.neighbors[pos_nA2] = tC
    if nC2 != None:
        pos_nC2 = find_neighbor(nC2, t2)
        nC2.neighbors[pos_nC2] = tA

    new_t = [tA, tC]
    new_T = Triangulation([], new_t)

    return new_T

# Triangulo tC y t son vecinos, revisa si cumplen el test del circulo o no
# Circulo se inscribe tC, de t se saca el vertice a revisar
# Da true si esta dentro del circulo
# Triangle x Triangle -> bool
def circle_test(tC, t):

    #encontrar vertices comunes
    positions = find_common_vertexes(tC, t)

    #tercer vertice de t y de tC
    pos_D = get_third_pos(positions[1], positions[3])
    pos_B = get_third_pos(positions[0], positions[2])

    #con todas las posiciones defino los vertices a usar en el test
    vlC = tC.vertexes
    vl = t.vertexes

    pos_C = (pos_B+1)%3 
    pos_A = (pos_B-1)%3

    vA = vlC[pos_A]
    vC = vlC[pos_C]
    vB = vlC[pos_B]
    vD = vl[pos_D]

    #crear matriz para calcular el determinante
    matrix = np.array([[vA.x - vD.x, vA.y - vD.y, (vA.x - vD.x)**2 + (vA.y - vD.y)**2],
                      [vB.x - vD.x, vB.y - vD.y, (vB.x - vD.x)**2 + (vB.y - vD.y)**2],
                      [vC.x - vD.x, vC.y - vD.y, (vC.x - vD.x)**2 + (vC.y - vD.y)**2]])

    determinante = np.linalg.det(matrix)

    if determinante > 0:
        return True
    return False   

# 0: Colinear points
# > 0: Clockwise points
# < 0: Counterclockwise
# Para estar dentro del triangulo debe dar clock wise en todos
# Vertex x Vertex x Vertex -> Float
def orientation(vb, va, vc): 

    val = (float(vb.y - va.y) * (vc.x - vb.x)) - \
           (float(vb.x - va.x) * (vc.y - vb.y))
           
    return val 
    
# Encuentra el triangulo en donde se encuentra el punto ingresado
# Entrega un arreglo con el número de triangulos a entregar y posteriormente los triangulos
# Si entrega un triangulo el punto se encontraba en una cara
# Si entregados triangulos el punto se econtraba en una arista
# Point x Triangulation -> Array
def find_triangle(p, T):
    
    for t in T.triangles:
        inside_count = 0
        in_edge = False
        for i in range(3):
            vp = Vertex(*p) 
            val = orientation(vp, t.vertexes[i%3], t.vertexes[(i+1)%3])
            if val == 0:
                in_edge = True
                #la posición del tercer vertice es la que estará opuesta al vecino que hay que devolver
                pos = get_third_pos(i%3, (i+1)%3)
                n = t.neighbors[pos]
            elif val > 0:
                inside_count+=1
            
        if inside_count == 3:
            return [1,t]  
        elif inside_count == 2 and in_edge:
            return [2, t, n]   

# encuentra los triangulos que poseen como vertice a p 
def find_point_triangles(v, T):
    triangles = []
    for t in T.triangles:
        for vertex in t.vertexes:
            if vertex.x == v.x:
                if vertex.y == v.y:
                    triangles.append(t) 
                    break
    return triangles      

# Remueve un triangulo o un vertice de una triangulación si este se encontraba ahí
# Triangulation x Vertex o Triangle -> void
def remove_if_posible(T,x):
    if x in T.triangles:
        T.triangles.remove(x)
    elif x in T.vertexes:
        T.vertexes.remove(x)

# Responde si un triangulo o un vertice se encontraba en la triangulacion
# Triangulation x Vertex o Triangle -> bool
def is_in_Triangulation(T,x):
    if x in T.triangles:
        return True
    elif x in T.vertexes:
        return True
    else:
        return False

# Crea la triangulación inicial a partir del input de entrada
# Array -> Triangulation
def make_initial_rectangle(pointslist):
    
    triangulation = Triangulation([],[])

    max_x = -sys.maxsize
    max_y = -sys.maxsize
    min_x = sys.maxsize
    min_y = sys.maxsize
    for point in pointslist:
        if(point[0] > max_x):
            max_x = point[0]
        if(point[0] < min_x):
            min_x = point[0]
        if(point[1] > max_y):
            max_y = point[1]
        if(point[1] < min_y):
            min_y = point[1]

    # p4                p3
    # 
    # 
    # 
    # p1                p2 
    
    p1 = (min_x - 0.5, min_y - 0.5)
    p2 = (max_x + 0.5, min_y - 0.5)
    p3 = (max_x + 0.5, max_y + 0.5)
    p4 = (min_x - 0.5, max_y + 0.5)

    v1 = Vertex(*p1)
    v2 = Vertex(*p2)
    v3 = Vertex(*p3)
    v4 = Vertex(*p4)

    vl1 = [v1, v2, v3]
    vl2 = [v3, v4, v1]

    t1 = Triangle(vl1)
    t2 = Triangle(vl2)

    nl1 = [None, t2, None]
    nl2 = [None, t1, None]
    
    t1.neighbors = nl1
    t2.neighbors = nl2

    triangulation.vertexes.append(v1)
    triangulation.vertexes.append(v2)
    triangulation.vertexes.append(v3)
    triangulation.vertexes.append(v4)
    
    triangulation.triangles.append(t1)
    triangulation.triangles.append(t2)

    if(dibujar_triangulacion):
        draw_triangles(triangulation)

    if circle_test(t1, t2):
        new_data = change_diagonal(t1, t2)
        triangulation.triangles += new_data.triangles
        triangulation.triangles.remove(t1)
        triangulation.triangles.remove(t2)
        if(dibujar_triangulacion):
            draw_triangles(triangulation)

    return triangulation

#Legalizar los 3 edges de un triangulo
# recibe el punto insertado, el triangulo involucrado y la triangulacion
def legalize_triangle(P, triangle, triangulation):

    pos_P = find_vertex(triangle, P)
    neighbor = triangle.neighbors[pos_P] #vecino exterior
    if neighbor != None:
        if(circle_test(triangle, neighbor)): #comparo con el vecino exterior
            new_T = change_diagonal(triangle, neighbor)

            remove_if_posible(triangulation, triangle)
            remove_if_posible(triangulation, neighbor)

            new_triangles = new_T.triangles
            triangulation.triangles += new_triangles

            if(dibujar_triangulacion):
                draw_triangles(triangulation)

            legalize_triangle(P, new_triangles[0], triangulation)
            legalize_triangle(P, new_triangles[1], triangulation)

# Crea una triangulación a partir de un arreglo de puntos
# Array -> Triangulation
def make_triangulation(pointslist):

    triangulation = make_initial_rectangle(pointslist)

    for point in pointslist:

        t_array = find_triangle(point, triangulation)

        if t_array[0] == 1: #viene un triangulo, quedo en face
            t = t_array[1]
            new_data = add_point_in_face(point, t)
            remove_if_posible(triangulation, t)

        else: #vienen 2 triangulos, quedo en edge
            ta = t_array[1]
            tb = t_array[2]
            new_data = add_point_in_edge(point, ta, tb)
            remove_if_posible(triangulation, ta)
            remove_if_posible(triangulation, tb)

        new_vertexes = new_data.vertexes
        new_triangles = new_data.triangles
        triangulation.vertexes += new_vertexes
        triangulation.triangles += new_triangles

        if(dibujar_triangulacion):
                draw_triangles(triangulation)

        for new_t in new_triangles:
            legalize_triangle(new_vertexes[0], new_t, triangulation)

    return triangulation

# Evalua los candidatos a formar parte de la lista de triangulos a recorrer
# Array x Vertex x Vertex -> Triangle
def evaluar_candidatos(candidatos, vi, vf):

    for triangle in candidatos:
        if evaluar_cruce(triangle, vi, vf):
            return triangle
    
    for triangle in candidatos:
        if evaluar_colineal(triangle, vi, vf):
            return triangle

# Evalua al candidato a formar parte de la lista de triangulos a recorrer
# Array x Vertex x Vertex -> bool
def evaluar_candidato(candidato, vi, vf):
        
    if evaluar_cruce(candidato, vi, vf):
        return True
    elif evaluar_colineal(candidato, vi, vf):
        return True        
    return False

# Evalua si el candidato cruza o no la arista vi vf
# Array x Vertex x Vertex -> bool
def evaluar_cruce(candidato, vi, vf):
        
    for i in range(0, 3):
        v1 = candidato.vertexes[i%3]
        v2 = candidato.vertexes[(i+1)%3]
        val1 = orientation(v1, vi, vf)
        val2 = orientation(v2, vi, vf)
        val3 = orientation(vi, v1, v2)
        val4 = orientation(vf, v1, v2)
        if ((val1 > 0 and val2 < 0) or (val1 < 0 and val2 > 0))\
             and ((val3 > 0 and val4 < 0) or (val3 < 0 and val4 > 0)):
            return True
    return False

# Evalua si el candidato es colineal o no a la arista vi vf
# Array x Vertex x Vertex -> bool
def evaluar_colineal(candidato, vi, vf):
    neutral = False
    bounds = False
    for vertex in candidato.vertexes:
        val = orientation(vertex, vi, vf)
        if val == 0:
            neutral = True
            if vi.x < vertex.x < vf.x or vi.x > vertex.x > vf.x or vi.y < vertex.y < vf.y or vi.y < vertex.y < vf.y:
                bounds = True
    if neutral and bounds:
        return True

# Arma la lista de triangulos a recorrer
# Array x Vertex x Vertex -> Array
def find_ordered_triangles(initial_triangles, vi, vf):

    ordered_triangles = []

    candidato = evaluar_candidatos(initial_triangles, vi, vf)
    ordered_triangles.append(candidato)
    t_actual = candidato
    t_prev = None
    #tenemos el triangulo inicial, ahora el resto
    while t_prev != t_actual:  
        neighbors = []
        for neighbor in t_actual.neighbors:
            if t_prev != None:
                if neighbor != t_prev and neighbor != None:
                    neighbors.append(neighbor)
            elif neighbor != None:
                neighbors.append(neighbor)
        t_prev = t_actual

        candidato = evaluar_candidatos(neighbors, vi, vf)
        if candidato != None and candidato not in ordered_triangles:
            ordered_triangles.append(candidato)
            t_actual = candidato

    return ordered_triangles

# Revisa si es posible cambiar la diagonal en los triangulos que toca, de ser posible lo hace
# int x Array x Array x Vertex x Vertex x Array
def check_convex_poligon(indice, ordered_triangles, triangulation, vi, vf, tested):

    if len(ordered_triangles) > indice+1:
        actual = ordered_triangles[indice]
        siguiente = ordered_triangles[indice+1]
    else:
        return [triangulation, tested]

    if evaluar_cruce(actual, vi, vf):

        new_data = change_diagonal(actual, siguiente)

        new_triangles = new_data.triangles
        new_1 = new_triangles[0]
        new_2 = new_triangles[1]
        
        malo = False
        if (evaluar_cruce(new_1, new_2.vertexes[0],  new_2.vertexes[1]) or
            evaluar_cruce(new_1, new_2.vertexes[1],  new_2.vertexes[2]) or
            evaluar_cruce(new_1, new_2.vertexes[2],  new_2.vertexes[0]) or 
            evaluar_cruce(new_2, new_1.vertexes[0],  new_2.vertexes[1]) or 
            evaluar_cruce(new_2, new_1.vertexes[1],  new_2.vertexes[2]) or 
            evaluar_cruce(new_2, new_1.vertexes[2],  new_2.vertexes[0])):
            malo = True

        for vertex in new_1.vertexes:
            if orientation(vertex, new_2.vertexes[0],  new_2.vertexes[1]) >0:
                if orientation(vertex, new_2.vertexes[1],  new_2.vertexes[2]) >0: 
                    if orientation(vertex, new_2.vertexes[2],  new_2.vertexes[0]) >0: 
                        malo = True

        for vertex in new_2.vertexes:
            if orientation(vertex, new_1.vertexes[0], new_1.vertexes[1]) >0:
                if orientation(vertex, new_1.vertexes[1], new_1.vertexes[2]) >0: 
                    if orientation(vertex, new_1.vertexes[2], new_1.vertexes[0]) >0: 
                        malo = True

        # Revisar si los puntos del mismo triangulo quedaron colineales o no 
        if orientation(new_1.vertexes[0], new_1.vertexes[1], new_1.vertexes[2]) == 0:
            malo = True
        if orientation(new_2.vertexes[0], new_2.vertexes[1], new_2.vertexes[2]) == 0:
            malo = True
        
        tested.append([actual,siguiente])

        if malo:
            resultado = check_convex_poligon(indice+1, ordered_triangles, triangulation, vi, vf, tested)
            triangulation = resultado[0]
            tested = resultado[1]
        else:
            remove_if_posible(triangulation, actual)
            remove_if_posible(triangulation, siguiente)
            triangulation.triangles += new_triangles
            pos = ordered_triangles.index(actual)

            if pos != 0:
                if find_common_vertexes(new_1, ordered_triangles[pos-1]) != None:
                    pos_1 = pos
                    pos_2 = pos+1
                else:
                    pos_1 = pos+1
                    pos_2 = pos
            else:
                pos_1 = 0
                pos_2 = 1
        
            reemplazar = False
            if evaluar_candidato(new_1, vi, vf):
                reemplazar = True
            if evaluar_candidato(new_2, vi, vf):
                reemplazar = True
                
            if reemplazar:
                ordered_triangles[pos_1] = new_1
                ordered_triangles[pos_2] = new_2


            else:
                t1 = ordered_triangles[pos_1]
                t2 = ordered_triangles[pos_2]
                ordered_triangles.remove(t1)
                ordered_triangles.remove(t2)
            
    else:
        ordered_triangles.remove(actual)

    return [triangulation, tested] 

# Post procesado de respetado de aristas
# Triangulation x Array            
def restricted_postprocess(triangulation, restrictedlist):

    for arista in restrictedlist:
        # extraer los puntos de la arista
        p_ini = arista[0] 
        p_fin = arista[1]

        vi = Vertex(*p_ini) 
        vf = Vertex(*p_fin) 

        candidatos = find_point_triangles(vi, triangulation)
        ordered_triangles = find_ordered_triangles(candidatos, vi, vf) 

        tested = []
        while len(ordered_triangles) >= 2:

            resultado = check_convex_poligon(0, ordered_triangles, triangulation, vi, vf, tested)
            triangulation = resultado[0]
            tested = resultado[1]
            if(dibujar_restricted):
                draw_triangles(triangulation)

    return triangulation
    
# Crea una triangulación a partir de un arreglo de puntos y de una lista de aristas restringidas
# Array x Array -> Triangulation
def make_restringed_triangulation(pointlist, restrictedlist):

    triangulation = make_triangulation(pointlist)
    if dibujar_restricted:
        draw_triangles(triangulation)
    restricted_triangulation = restricted_postprocess(triangulation, restrictedlist)
    
    return restricted_triangulation

def test_Delaunay(T):
    cuenta = 0
    for triangle in T.triangles:
        for neighbor in triangle.neighbors:
            if neighbor != None:
                if circle_test(triangle, neighbor):
                    cuenta += 1
                    #printear(triangle, neighbor)
    if cuenta>0:
        return cuenta
    else:
        return 0

def recibir_puntos():
    print("Ingrese puntos, para detenerse aprete enter sin ingresar nada :3")
    points = []
    contador = 1
    while(True):
        print("Punto",contador)
        x = input("x: ")
        if(x == ""):
            break
        y = input("y: ")
        if(y == ""):
            break
        point = (float(x),float(y))
        points.append(point)
        contador+=1
    return points

def recibir_puntos_csv():
    points = []
    while True:
        try:
            name = input("Introduzca el nombre del csv con los puntos :D (tiene que estar en la misma carpeta desde donde ejecuto esto) ")
            with open(name, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    point = (float(row[0]), float(row[1]))
                    points.append(point)
            break
        except FileNotFoundError:
            print("No lo encontre :( pon otro")
    return points 

def puntos_aleatorios():

    while(True):
        sup = input("Introduzca el límite superior de los puntos: ")
        inf = input("Introduzca el límite inferior de los puntos: ")
        if float(sup) < float(inf):
            print("El límite superior debe ser mayor al inferior >:c")
        else:
            break
    cant = input("Introduzca la cantidad de puntos que quiere: ")
    cantint = int(cant) + 1
    points = []
    contador = 0
    while(cantint!=1):
        x = random.random()
        y = random.random()
        xof = (float(sup) - float(inf))*x + float(inf)
        yof = (float(sup) - float(inf))*y + float(inf)
        print("Punto",contador)
        print("(" + str(xof) + "," + str(yof) + ")")
        punto = (xof,yof)
        points.append(punto)
        cantint-=1
        contador+=1
    return points

def recibir_aristas():

    print("Ingrese aristas, para detenerse aprete enter sin ingresar nada :3")
    aristas = []
    contador = 1
    while(True):
        print("Arista",contador)
        print("Punto inicial de la arista:")
        xini = input("x: ")
        if(xini == ""):
            break
        yini = input("y: ")
        if(yini == ""):
            break
        print("Punto inicial de la arista:")
        xfin = input("x: ")
        if(xfin == ""):
            break
        yfin = input("y: ")
        if(yfin == ""):
            break
        p_ini = (float(xini),float(yini))
        p_fin = (float(xfin),float(yfin))
        aristas.append([p_ini, p_fin])
        contador+=1
    return aristas

def recibir_aristas_csv():
    aristas = []
    while True:
        try:
            name = input("Introduzca el nombre del csv con las aristas :D (tiene que estar en la misma carpeta desde donde ejecuto esto) ")
            with open(name, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';')
                for row in spamreader:
                    points = row[0].split(';')
                    pointini = points[0].split(',')
                    pointini = (float(pointini[0]), float(pointini[1]))
                    pointfin = points[1].split(',')
                    pointfin = (float(pointfin[0]), float(pointfin[1]))

                    aristas.append([pointini, pointfin])
            break
        except FileNotFoundError:
            print("No lo encontre :( pon otro")
    return aristas 

def aristas_restrigidas(points):

    global dibujar_restricted
    while(True):
        resp1 = input("Quieres que el programa dibuje cada paso de respetado de aristas? (y/n) ")
        if resp1 == "Y" or resp1 == "y":
            dibujar_restricted = True
            break
        elif resp1 == "N" or resp1 == "n":
            dibujar_restricted = False
            break
        else:
            print("No entendí :C porfi pon y o n")
        
    while(True):
        print("Que deseas hacer?")
        print("1- Ingresar las aristas a mano")
        print("2- Usar un csv")
        resp2 = input("(1/2)")
        if resp2 == "1":
            restrictedlist = recibir_aristas()
            break
        elif resp2 == "2":
            restrictedlist = recibir_aristas_csv()
            break
        else:
            print("No entendí :C porfi pon 1 o 2")

    #tengo las aristas ahora veo si los puntos de las aristas son eee en la wea
    for arista in restrictedlist:
        if arista[0] not in points:
            points.append(arista[0])
        if arista[1] not in points:
            points.append(arista[1])

    return make_restringed_triangulation(points, restrictedlist)

while(True):
    resp1 = input("Hola! :) Quieres que el programa dibuje cada paso? (y/n) ")
    if resp1 == "Y" or resp1 == "y":
        dibujar_triangulacion = True
        break
    elif resp1 == "N" or resp1 == "n":
        dibujar_triangulacion = False
        break
    else:
        print("No entendí :C porfi pon y o n")

while(True):
    print("Que deseas hacer?")
    print("1- Ingresar los puntos a mano")
    print("2- Usar un csv")
    print("3- Generar puntos aleatorios")
    resp2 = input("(1/2/3)")
    if resp2 == "1":
        points = recibir_puntos()
        break
    elif resp2 == "2":
        points = recibir_puntos_csv()
        break
    elif resp2 == "3":
        points = puntos_aleatorios()
        break
    else:
        print("No entendí :C porfi pon 1, 2 o 3")

while(True):
    resp1 = input("Desea agregar aristas restringidas? (y/n) ")
    if resp1 == "Y" or resp1 == "y":
        T = aristas_restrigidas(points)
        break
    elif resp1 == "N" or resp1 == "n":
        T = make_triangulation(points)
        break
    else:
        print("No entendí :C porfi pon y o n")

print("Este es el resultado final!")
draw_triangles(T)

# Descomentar si quiere realizar test para ver si es delaunay
# x = test_Delaunay(T)
# if x == 0:
#     print("congratulaciones")
# else:
#     print("Chale",x)
