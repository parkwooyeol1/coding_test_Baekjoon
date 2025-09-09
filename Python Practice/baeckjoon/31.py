from itertools import combinations

N, M = map(int, input().split())
temp = [i for i in range(1, N+1)]  
result = list(combinations(temp, M))  

for comb in result:
    print(*comb)