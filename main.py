# with open('1.txt','r') as f:
#     content = f.read()
#     temp = content.split('\n')
#     n = len(temp)
#     dummy = []
#     res = []
#     for i in range(n):
#         #print(i,temp[i])
        
#         if temp[i] == 'boundary':
#             dummy=temp[:i]
#             res.append(dummy)
#             temp = temp[i:]
#             break
#     n = len(temp)
#     ls = []
    
#     ct = 0
#     for i in temp:
#         if i == 'boundary' and ct<3:
#             ls = ls[:-1]
#             res.append(''.join(ls))
#             res.append('\n')
#             ls = []
#             ct += 1
#             #print("ct",ct)
#         s = i.split(' ')
#         for j in s:
#             if j == '':
#                 pass
#             ls.append(j)
#             ls.append(' ')
        
#     for i in ls:
#         if i == '':
#             ls.remove(i)
# res=res[1:-1]
# print(dummy)
# print(res)
# print(''.join(res))
# fp = open("op1.txt",'w')
# fp.write(''.join(res))
# fp.close()
# f.close()

#print(n,len(temp)


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
def polygonArea(X, Y, n):
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


f1 = open('2.txt','r')
f2 = open("op2.txt",'w')
st = ''
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
            #print(ls)
            #print(x,y)
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
            refDist = distance(x,y,refSides)
print("ref area , ref sides", refArea,refSides)
flag1 = 0
flag2 = 0
with open('2.txt','r') as f1:
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
                dist = distance(x,y,len(x))
                if area == refArea and n-2 == refSides and refDist == dist:
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
        
#print(res)

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
            #print(ls)
            #print(x,y)
            refArea = polygonArea(x, y, n-2)
            refSides = len(x)
print("ref area , ref sides", refArea,refSides)
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
#65.912
# def perimeter(X, Y, n):
#     area = 0.0
#     j = n - 1
#     for i in range(0,n):
#         area += (int(X[j]) + int(X[i])) * (int(Y[j]) - int(Y[i]))
#         j = i   
#     return int(abs(area / 2.0))

f1 = open('4.txt','r')
f2 = open("op4.txt",'w')
ref = []
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
            dist = distance(x, y, len(x))
            #print(ls)
            #print(x,y)
            ref.append([polygonArea(x, y, n-2),len(x),dist])
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
                #print(ls)
                #print(x,y)
                area = polygonArea(x, y, n-2)
                sides = n-2
                dist = distance(x, y, len(x))
                temp=[area, sides, dist]
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
f.close()
f1.close()
f2.close()
print(ref)

