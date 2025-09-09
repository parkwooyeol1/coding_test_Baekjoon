import collections
# 위상정렬 (topological sort)
def topolgical_sort(n, edges):
    graph = collections.defaultdict(list)
    indeg = [0] * n
    order = []
    for a, b in edges:
        graph[a].append(b)
        indeg[b] += 1
    q = collections.deque([i for i in range(n) if indeg[i] == 0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != n:
        return -1
    return order
n = 4
edges = [(0, 2), (1, 2), (2, 3)]
print(topolgical_sort(n, edges))