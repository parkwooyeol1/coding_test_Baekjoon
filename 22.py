from collections import defaultdict
N = int(input().strip())
M = int(input().strip())
computer = defaultdict(list)


for i in range(M):
    a, b = map(int, input().strip().split())
    computer[a].append(b)
    computer[b].append(a)

visited = set()
def dfs(node):
    visited.add(node)
    count = 0
    for i in computer[node]:
        if i not in visited:
            count += 1
            count += dfs(i)
    return count
print(dfs(1)) 