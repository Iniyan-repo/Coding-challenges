'''
Author: Iniyan
purpose: seperate helper functions
'''
import math

def distance_2points(point1,point2):
    '''
    return the distance between two points
    where point[3]
    '''
    point1 = [float(pt) for pt in point1]
    point2 = [float(pt) for pt in point2]
    
    return(math.sqrt((point2[0]-point1[0])**2+
                     (point2[1]-point1[1])**2+
                     (point2[2]-point1[2])**2))


def area_triangle(point1,point2,point3):
    ''' compute area using heron's formula'''   
    len_a = distance_2points(point1,point2)
    len_b = distance_2points(point2,point3)
    len_c = distance_2points(point3,point1)
    semi_perimeter = (len_a+len_b+len_c)/2
    return (math.sqrt(semi_perimeter*(semi_perimeter-len_a)*(semi_perimeter-len_b)*(semi_perimeter-len_c)))
