import matplotlib.pyplot as plt

# Dibuja un poligono
# Array -> void
def draw(points):
    points.append(points[0]) 
    xs, ys = zip(*points) 
    plt.plot(xs,ys) 

# Dibuja los triangulos de una triangulación
# Triangulation -> void
def draw_triangles(T):
    plt.figure()
    for t in T.triangles:
        vl = t.vertexes
        points = [(vl[0].x,vl[0].y),(vl[1].x,vl[1].y),(vl[2].x,vl[2].y)]
        draw(points)
    plt.axis('square')
    plt.show()
