
def polygonn_area(X, Y, n):
    area = 0.0
    j = n - 1
    for i in range(0,n):
        area += (int(X[j]) + int(X[i])) * (int(Y[j]) - int(Y[i]))
        j = i   
    return int(abs(area / 2.0))

def distance(X, Y, n):
    d = []
    x = int(X[0])
    y = int(Y[0])
    for i in range(1,n):
        dist = pow(((int(X[i])-x)**2 + (int(Y[i])- y)**2),0.5)
        d.append(dist)
    return d.sort()

def angle(points):
    n = len(points)
    angles = []
    for i in range(n - 2):
        p1, p2, p3 = points[i], points[i+1], points[i+2]
        s1 , s2 = 0, 0
        if((p1[0]-p2[0]) != 0):
            s1 = (p1[1]-p2[1])/(p1[0]-p2[0])
        else:
            angles.append(float('INF'))
            
        if((p2[0]-p3[0]) != 0):
            s2 = (p2[1]-p3[1])/(p2[0]-p3[0])
        else:
            angles.append(float('INF'))
            
        angles.append((s1-s2)/(1+(s1*s2)))
    return angles.sort()


'''1'''

ct = 0
#new line 
flag = 0
f1=open("op1.txt",'w')
with open('1.txt','r') as f:
    content = f.readlines()
    for i in content:
        if 'boundary' in i:
            flag = 1
            ct += 1
        if flag==1 and ct<=2:
            f1.write(i)
        if 'endel' in i:
            flag = 0
            continue
        if flag == 0:
            f1.write(i)      
f1.close()
f.close()


'''2'''

f1 = open('2.txt','r')
f2 = open("op2.txt",'w')
refArea = 0.0
refSides = 0
refDist = []
with open('poi2.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
            refDist = distance(x,y,refSides)
#print("ref area , ref sides", refArea,refSides)
flag1 = 0
flag2 = 0
with open('2.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
                area = polygonArea(x, y, n-2)
                dist = distance(x,y,len(x))
                if area == refArea and n-2 == refSides and refDist == dist:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            if flag2 == 1:
                s = "".join(res)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []

        
'''3'''

f1 = open('3.txt','r')
f2 = open("op3.txt",'w')
refArea = 0.0
refSides = 0
with open('poi3.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
           
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
#print("ref area , ref sides", refArea,refSides)
flag1 = 0
flag2 = 0
with open('3.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
            #res.append(i)
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
                #print(ls)
                #print(x,y)
                area = polygonArea(x, y, n-2)
                if area == refArea and n-2 == refSides:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            #res.append(i)
            if flag2 == 1:
                s = "".join(res)
                #print("s",s)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []

        
'''4'''
#APPROACH 1
# using area, angle, num of sides

#APPROACH 2

f1 = open('4.txt','r')
f2 = open("op4.txt",'w')
refArea = 0.0
refSides = 0
with open('poi4.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
            #print(ls)
            #print(x,y)
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
#print("ref area , ref sides", refArea,refSides)
flag1 = 0
flag2 = 0
with open('4.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
            #res.append(i)
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
               
                area = polygonArea(x, y, n-2)
                if area == refArea and n-2 == refSides:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            #res.append(i)
            if flag2 == 1:
                s = "".join(res)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []




'''5'''

f1 = open('5.txt','r')
f2 = open("op5.txt",'w')
refArea = 0.0
refSides = 0
with open('poi5.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
           
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
#print("ref area , ref sides", refArea,refSides)
flag1 = 0
flag2 = 0
with open('5.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
            #res.append(i)
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
                
                area = polygonArea(x, y, n-2)
                if area == refArea and n-2 == refSides:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            #res.append(i)
            if flag2 == 1:
                s = "".join(res)
                #print("s",s)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []


'''6'''
f1 = open('6.txt','r')
f2 = open("op6.txt",'w')
refArea = 0.0
refSides = 0
ref = []
with open('poi6.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            coordinates = []
            refDist = []
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
                coordinates.append([int(temp[0]),int(temp[1])])
           
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
            refAngles = angle(coordinates)
            ref.append([refArea,refSides,refAngles])

flag1 = 0
flag2 = 0
with open('6.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
            #res.append(i)
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                coordinates = []
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
                    coordinates.append([int(temp[0]),int(temp[1])])
                area = polygonArea(x, y, n-2)
                angles = angle(coordinates)
                temp=[area,n-2,angles]
                if temp in ref:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            #res.append(i)
            if flag2 == 1:
                s = "".join(res)
                #print("s",s)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []


'''7'''

f1 = open('7.txt','r')
f2 = open("op7.txt",'w')
refArea = 0.0
refSides = 0
ref = []
with open('poi7.txt','r') as f:
    lines = f.readlines()
    for i in lines:
        if 'xy' in i:
            ls = i.split('  ')
            x, y = [], []
            n = len(ls)
            for j in range(2,n):
                temp = ls[j].split(' ')
                x.append(temp[0])
                y.append(temp[1])
            
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
            ref.append([refArea,refSides])
flag1 = 0
flag2 = 0
with open('7.txt','r') as f1:
    lines = f1.readlines()
    res = []
    for i in lines:
        if 'boundary' in i:
            flag1 = 1
        if flag1 == 1:
            if 'xy' in i:
                ls = i.split('  ')
                x, y = [], []
                n = len(ls)
                for j in range(2,n):
                    temp = ls[j].split(' ')
                    x.append(temp[0])
                    y.append(temp[1])
                area = polygonArea(x, y, n-2)
                temp=[area,n-2]
                if temp in ref:
                    flag2 = 1
            res.append(i)
        if 'endel' in i:
            #res.append(i)
            if flag2 == 1:
                s = "".join(res)
                f2.write(s)
            flag2 = 0
            flag1 = 0
            res = []



