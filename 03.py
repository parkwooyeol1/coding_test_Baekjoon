N =  int(input().strip())
result = []
for i in range(N):
    result.append(input().strip())

result = set(result)
result = list(result)

result.sort(key=lambda x:(len(x),x))

for i in result:
    print(i)
