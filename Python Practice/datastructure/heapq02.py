import heapq

def solution(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cost = [[float('inf')]*cols for _ in range(rows)]
    cost[0][0] = grid[0][0]

    heap = []
    heapq.heappush(heap, (cost[0][0], 0, 0)) # (비용, x, y)
    cnt = 0
    while heap:
        current_cost, x, y = heapq.heappop(heap)

        if (x, y) == (rows -1, cols - 1):
            return current_cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = current_cost + grid[nx][ny]

                if cost[nx][ny] > new_cost:
                    cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    
grid = [
    [0, 1, 2],
    [1, 2, 3],
    [4, 2, 1]
]

print(solution(grid))