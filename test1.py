dummyArray = []
Area,volume = 0,0
with open('Input/myTet 9.stl')as file:
    for line in file:
        if "normal" in line or "vertex" in line:
            dummyArray.append([float(x) for x in line.split()[-3:]])
            if(len(dummyArray) == 4):
                n,v1,v2,v3 = dummyArray
                a = ((v2[0]-v1[0])**2+(v2[1]-v1[1])**2+(v2[2]-v1[2])**2)**0.5
                c = ((v3[0]-v1[0])**2+(v3[1]-v1[1])**2+(v3[2]-v1[2])**2)**0.5
                b = ((v2[0]-v3[0])**2+(v2[1]-v3[1])**2+(v2[2]-v3[2])**2)**0.5
                s = (a+b+c)/2
                ctr = [sum(v)/3 for v in zip(v1,v2,v3)]
                dA = (s*(s-a)*(s-b)*(s-c))** 0.5
                Area+=dA
                volume = volume + (ctr[0]*n[0]+ctr[1]*n[1]+ctr[2]*n[2])*dA/3
                dummyArray.clear()
    print(Area,volume)
                