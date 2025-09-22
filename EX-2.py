'''
returns average of n number of values * is unpacking operator
'''
def average(*args):
    return(sum(*args)/len(*args))

'''
returns the centroid of n number of n dimentional points'''
def centroid(*points):
    max_dim = 0
    size_list=[]
    #find max dim of the imput and assume 0 for missing dims in lower dimention points
    for point in points:
        tmp_len = len(point)
        if(tmp_len>max_dim):
            max_dim = tmp_len
        size_list.append(tmp_len)
    #create a tuple saying how many zeros to add for each point      
    pt_sz_map = zip(points,size_list)
    
    #adding the zeros
    for pt,sz in pt_sz_map:
        pt+= [0]*(max_dim-sz)
        
    return [average(values) for values in zip(*points)]


if __name__ == '__main__':
    print(centroid([1],[0,1,2],[1,32,-2,4]))