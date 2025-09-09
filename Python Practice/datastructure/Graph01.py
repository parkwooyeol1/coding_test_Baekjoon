import collections
def reconstruct_itinerary(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets): # [[‘ATL’, ‘JFK’], [‘ATL’, ‘SFO’], [‘JFK’, ‘ATL’], [‘JFK’, ‘SFO’], [‘SFO’, ‘ATL’]]
        graph[a].append(b)
    # graph: {‘ATL’: [‘JFK’, ‘SFO’], ‘JFK’: [‘ATL’, ‘SFO’], ‘SFO’: [‘ATL’]}
    print(graph)
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    dfs('JFK')
    return route[::-1]