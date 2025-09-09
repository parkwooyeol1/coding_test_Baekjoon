# dfs를 Stack으로 구현하여 미로찾기

def solution(grid):
    start = (0, 0)
    stack = [(start, [(0, 0)])] # (시작위치, 도착 경로)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False]*cols for _ in range(rows)]
    visited[0][0] = True

    end = (rows - 1, cols - 1)
    while stack:
        (x, y), path = stack.pop() 

        if (x, y) == end:
            return path
        
        for dx, dy in directions:
            nx, ny = dx + x, dy + y

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append(((nx, ny), path+[(nx, ny)]))

grid = [
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 0, 0]
]





distance = solution(grid)
print(distance)
print(len(distance))

