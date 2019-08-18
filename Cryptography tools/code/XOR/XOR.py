# -*- coding: cp936 -*-

A=[]
B=[]
f=open('1.txt','r')
c=[]
for i in range(0,16):
    a = f.readline()
    b = a.split()
    c.append(b)
#print(c)
for i in c:
    A.append(i[0])
    B.append(i[1])
#print (A)
#print (B)
xor=[]
for i in range(0,len(A)):
    for j in range(0,len(A[0])):
        d = int(A[i][j])^int(B[i][j])
        xor.append(d)
#print (xor)
#print (len(xor))
j=0
C=""
D=[]
for i in xor:
    #print (i,end="")
    C+=str(i)
    j=j+1
    if j==8:
        #print()
        D.append(C)
        C=""
        j=0

#print(D)
for i in D:
    print(i)
