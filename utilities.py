'''
Author: Iniyan
purpose: seperate helper functions
'''
import math
import time

def average(*args):
    if(len(args)==0):
        return 0
    return(sum(*args)/len(*args))

def distance_2points(point1,point2):
    '''
    return the distance between two points
    where point[3]
    '''    
    return(math.sqrt((point2[0]-point1[0])**2+
                     (point2[1]-point1[1])**2+
                     (point2[2]-point1[2])**2))

def mid_2points(point1,point2):
    #(X1,X2),(Y1,Y2),(Z1,Z2)
    return [average(x) for x in map(point1,point2)]

def split_triangle_1to4(point1,point2,point3):
    
    mid_a = mid_2points(point1,point2)
    mid_b = mid_2points(point1,point3)
    mid_c = mid_2points(point3,point2)
    
    return[[point1,mid_a,mid_b],[point2,mid_a,mid_c],[point3,mid_c,mid_b],[mid_a,mid_b,mid_c]]
    

def area_triangle(point1,point2,point3):
    ''' compute area using heron's formula'''  
    len_a = distance_2points(point1,point2)
    len_b = distance_2points(point2,point3)
    len_c = distance_2points(point3,point1)
    semi_perimeter = (len_a+len_b+len_c)/2
    return (math.sqrt(semi_perimeter*(semi_perimeter-len_a)*(semi_perimeter-len_b)*(semi_perimeter-len_c)))

def vector_scale(vector1,scale_factor):
    ''' k[x1,x2,x3]'''
    return[scale_factor*x for x in vector1]

def vector_dot(vector1,vector2):

    return(vector1[0]*vector2[0]+vector1[1]*vector2[1]+vector1[2]*vector2[2])

def vector_cross(vector_1,vector_2):
    i = vector_1[1]*vector_2[2] - vector_1[2]*vector_2[1]
    j = vector_1[2]*vector_2[0] - vector_1[0]*vector_2[2]
    k = vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0]
    return [i,j,k]

def centroid_triangle(vector1,vector2,vector3):
    ''' average of the vertices '''
    return [(vector1[0]+vector2[0]+vector3[0])/3,
            (vector1[1]+vector2[1]+vector3[1])/3,
            (vector1[2]+vector2[2]+vector3[2])/3]

def vector_mag(vector1):
    
    return(math.sqrt(vector1[0]**2+vector1[1]**2+vector1[2]**2))

def normalize_vector(vector1):
    
    mag = vector_mag(vector1)
    return [x/mag for x in vector1]


def timeit(functionptr):
    def inner_func(*vals,**keyvals):
        start = time.time()
        func = functionptr(*vals,**keyvals)
        end = time.time()
        print("Executed",functionptr.__name__,"in "+ str(end-start) + " seconds.")
        return func
    return inner_func


def hail(functionptr):
    def inner_func(*vals,**keyvals):
        print(f"Function {functionptr.__name__} Started!")
        func = functionptr(*vals,**keyvals)
        print(f"Function {functionptr.__name__} Ended!")
        return func
    return inner_func

def vector_add(v1,v2):
    return[ i+j for i,j in zip(v1,v2)]

def vector_2point(p1,p2):
    '''first,second -> second-first'''
    return[ j-i for i,j in zip(p1,p2)]
    