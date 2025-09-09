N = int(input().strip())
result = []

for i in range(N):
    m = int(input().strip())
    if result and m == 0:
        result.pop()
    else:
        result.append(m)

print(sum(result))