n, m = map(int, input().strip().split())
temp = set()
result = set()
for _ in range(n+m):
    a = input()
    if a in temp:
        result.add(a)
    else:
        temp.add(a)
result = sorted(list(result))
print(len(result))
for i in result:
    print(i) 


