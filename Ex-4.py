'''
Author: Iniyan
Exercise problems on generators
'''
import random
import csv
from utilities import area_triangle,vector_scale,vector_add,vector_2point,distance_2points
  
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
        
    
def quadgen((v1=[],v2=[],v3=[],v4=[]):
    ''' given points of a quad in a cyclic manner uses triagen to create interior points '''
    tri1 = triagen(v1, v2, v3)  
    tri2 = triagen(v1, v4, v3)  
    while True:
        if random.random() > 0.5:
            yield next(tri1)
        else:
            yield next(tri2)
        
if('__main__' == __name__) : 
     

    b_tria = triagen([0,0,0], [0,1,0], [-1,0,0])

    with open('trial.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(1000):   
            point = next(b_tria)
            writer.writerow(point)  
          
       
    b_quad = quadgen([0,0,0],[0,-1,0],[1,1,0],[-1,0,0])
    with open('quad.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',')
        for _ in range(1000):   
            point = next(b_quad)
            writer.writerow(point)  
          
       