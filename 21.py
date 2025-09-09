import math
m, n = map(int, input().split())

table = [True]*(n+1)
table[0]=False
table[1]=False

for i in range(2, int(math.sqrt(n))+1):
    if table[i]:
        for j in range(i*i, n+1, i):
            table[j] = False
for i in range(m,n+1):
    if table[i]:
        print(i)