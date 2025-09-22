'''
Author: Iniyan
Date: Sept 10 2025
Purpose: Read a STL file and calculate the model's surface area

STL file format
solid COMMENT (once on top only)
    facet normal i  j   k
        outer loop
        vertex1   x    y   z
        vertex2   x    y   z
        vertex3   x    y   z
        endloop
    endfacet
...
endsolids
[[i,j,k][x1,y1,z1][x2,y2,z2][x3,y3,z3]]
F = (x/3+(y**2)*(z**2)) +((y/3)+(z**2)*(x**2))+((z/3)+(x**2)*(y**2))
'''
from utilities import area_triangle,vector_scale,vector_dot,normalize_vector,centroid_triangle


def solve_f(pt):
    x,y,z = pt
    #make sure divergence is 1
    return [(x/3+(y**2)*(z**2)),((y/3)+(z**2)*(x**2)),((z/3)+(x**2)*(y**2))]
    
def read_stl(path):
    # read the data and return a string list
    with open(path,"r",encoding="UTF-8") as file:
        file.readline() #skip first line (comment)
        string_list = file.readlines()
    return string_list[:-1] #skip end solid


def calculate_area_and_volume(path : str)->tuple:
    surface_area = 0.0
    del_area = 0.0
    volume = 0.0
    del_volume = 0.0
    data = []
    string_list = read_stl(path)
    for i in string_list:
        if "normal" in i or "vertex" in i:
            data.append([float(x) for x in i.strip().split(' ')[-3:]])
    
    for i in range(1,len(data)-3,4):
        del_area = area_triangle(data[i],data[i+1],data[i+2])
        #del_volume = (vector_dot(normalize_vector(data[i-1]),centroid_triangle(data[i],data[i+1],data[i+2]))*del_area)/3
        del_volume = (vector_dot(normalize_vector(data[i-1]),solve_f(centroid_triangle(data[i],data[i+1],data[i+2])))*del_area)
        surface_area = surface_area+del_area
        volume = volume + del_volume
    return(surface_area,volume)
  
if __name__ == "__main__":
    path = input("Enter the Stl Path\n") or "Input/myTet 9.stl"
    area,volume = calculate_area_and_volume(path)
    print("Surface Area: ", area," squared unit")
    print("Volume: ", volume," cubic unit")