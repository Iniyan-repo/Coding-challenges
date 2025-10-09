'''
Author: Iniyan
Exercise problems on generators
'''
import random
import csv
from utilities import *
  
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
    pt = a + alpha(AB) + beta(AC)
    '''
    X = vector_2point(v1,v2)
    Y = vector_2point(v1,v3)
    while True:
        alpha = random.random() 
        beta = random.random()
        if(alpha+beta > 1):
            alpha = 1-alpha
            beta  = 1-beta
        
        rel_pt = vector_add(vector_scale(X,alpha),vector_scale(Y,beta))
        yield vector_add(v1,rel_pt)

def quadgen(*points):
    ''' given points of a quad in a cyclic manner uses triagen to create interior points '''
    sign = []
    '''check if there is any concave vertex in the polygon by finding the orientation'''
    for i in range(4):
        va = vector_2point(points[i],points[i-1])
        vb = vector_2point(points[i],points[(i+1)%4])
        vx = vector_cross(va,vb)
        sign.append(vx[2]/abs(vx[2]) if vx[2]!=0 else 1)

    if(len(set(sign))>1):
        #concave vertex , find the concave vertex and split tria with it as one of diagonal 
        indicator = sum(sign)
        if(indicator > 0):
            vtx = sign.index(-1)
        else:
            vtx = sign.index(1)
        opp = (vtx +2) % 4
        tria1 = triagen(points[vtx],points[opp],points[(opp+1)%4])
        tria2 = triagen(points[vtx],points[opp],points[(opp-1)%4])
        
    else:
        #general case
        tria1 = triagen(points[0],points[1],points[2])
        tria2 = triagen(points[0],points[2],points[3])
        
    while True:
        yield next(tria1)
        yield next(tria2)

        
if('__main__' == __name__) : 
     

    b_tria = triagen([0,0,0], [0,1,0], [-1,0,0])

    with open('trial.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(1000):   
            point = next(b_tria)
            writer.writerow(point)  
          
       
    #b_quad = quadgen([0,0,0],[1,0,0],[1,1,0],[0,1,0])
    b_quad = quadgen([0.2,0,0],[0,-1,0],[1,1,0],[-1,0,0])
    with open('quad.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(10000):   
            point = next(b_quad)
            writer.writerow(point)  
          
       