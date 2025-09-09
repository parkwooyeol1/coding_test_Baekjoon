import sys
N = int(sys.stdin.readline().strip())
result = []

def fibonacci_count(n):
    fib = {0: [1, 0], 1: [0, 1]} 

    for i in range(2, n + 1):
        fib[i] = [
            fib[i - 1][0] + fib[i - 2][0],  
            fib[i - 1][1] + fib[i - 2][1]   
        ]
    return fib[n]

for _ in range(N):
    T = int(sys.stdin.readline().strip())
    result.append(fibonacci_count(T))

for i, j in result:
    print(f"{i} {j}")