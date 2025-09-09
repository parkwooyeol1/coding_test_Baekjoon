n, k = map(int, input().split())
circle = []
result = []

for i in range(1, n+1):
    circle.append(i)

idx = 0
while circle:
    idx = (idx + k - 1) % len(circle)
    result.append(circle.pop(idx))

print('<' + ', '.join(map(str, result)) + '>')