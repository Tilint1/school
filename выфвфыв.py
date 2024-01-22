f = open('a.txt')
A = []
max = 0
B = []
D = []
C = []
for i in range(130):
   b = f.readline()
   A.append(b)
for i in range(len(A)):
    if i != 129:
        c = A[i][-3:]
        d = A[i]
        e = A[i][-6:-3]
        B.append(int(c))
        D.append(d)
        C.append(int(e))
    else:
        c = A[i][-1:]
        d = A[i]
        e = A[i][-6:-3]
        B.append(int(c))
        D.append(d)
        C.append(int(e))
for i in range(len(B)):
    if int(B[i]) > max:
        max = B[i]
        l = i
print(D[l])
for i in range(len(C)):
    if int(C[i]) > max:
        max = B[i]
        l2 = i
print(D[l2])
for i in range(len(C)):
    for i in range(len(D)):
        if int(C[i]) + int(B[i]) > max:
            max = int(C[i]) + int(B[i])
            l3 = i
print(D[l3])
    


