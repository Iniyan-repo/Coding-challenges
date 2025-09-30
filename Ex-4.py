
import random
import csv
from utilities import area_triangle
  
PARAMTOL = 1E-9    
def myRange(start,stop = None,step=1):
    # copy of range function
    if stop is None:
        stop = start
        start = 0
    if step == 0:
        raise ValueError("Step cannot be 0")
    if step > 0:
        while start<stop:
            yield start
            start = start + step
    else:
        while start > stop:
            yield start
            start = start + step               




def triagen(v1=[],v2=[],v3=[]):
    
    '''
    Given 3 points of a triangle, gives a generator that returns points inside the triangle 
    '''
    A = area_triangle(v1,v2,v3)
    limits =  [(min(i),max(i)) for i in  zip(v1,v2,v3)]
    #spray points in bonding box and if area of subtriangles created by point and vertices equals area of whole triangle yeild
    while True:
        v4 = [ random.uniform(a,b) for a,b in limits ]
        A1 = area_triangle(v1,v2,v4)
        A2 = area_triangle(v2,v4,v3)
        A3 = area_triangle(v4,v3,v1)
        if abs((A1 + A2 + A3) - A) < PARAMTOL: 
            yield v4


def quadgen(v1=[],v2=[],v3=[],v4=[]):
    
    '''
    Given 4 points of a quad in cyclic order, gives a generator that returns points inside the quad 
    '''
    A = area_triangle(v1, v2, v3)
    B = area_triangle(v1, v4, v3)
    quad_area = A + B
    if quad_area < PARAMTOL or A < PARAMTOL or B<PARAMTOL:
        raise ValueError("Deformed quadrilateral!")
    # same logic as above
    limits = [(min(i), max(i)) for i in zip(v1, v2, v3, v4)]

    while True:
        vx = [random.uniform(a, b) for a, b in limits]
        A1 = area_triangle(v1, v2, vx)
        A2 = area_triangle(v2, v3, vx)
        A3 = area_triangle(v3, v4, vx)
        A4 = area_triangle(v4, v1, vx)

        if abs((A1 + A2 + A3 + A4) - quad_area) < PARAMTOL:
            yield vx

        
if('__main__' == __name__) : 
     

    b_tria = triagen([0,0,0], [0,1,0], [-1,0,0])
    b_quad = quadgen([0,0,0],[1,0,0],[1,1,0],[0,1,0])

    with open('trial.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(1000):   
            point = next(b_tria)
            writer.writerow(point)  
          
       
    with open('quad.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(1000):   
            point = next(b_quad)
            writer.writerow(point)  
          
       