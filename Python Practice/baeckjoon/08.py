N, M = map(int, input().split())
board = [input() for i in range(N)]
result = []
for i in range(N-7):
    for j in range(M-7):
        first = 0
        second = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    if board[x][y] != 'W':
                        first += 1
                    if board[x][y] != 'B':
                        second += 1
                else:
                    if board[x][y] != 'B':
                        first += 1
                    if board[x][y] != 'W':
                        second += 1
        result.append(first)
        result.append(second)
print(min(result))

