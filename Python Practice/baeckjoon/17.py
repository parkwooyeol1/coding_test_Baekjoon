N = int(input().strip())
k = list(map(int, input().strip().split()))
result = 0
a = []
for i in sorted(k):
    result += i
    a.append(result)
print(sum(a))