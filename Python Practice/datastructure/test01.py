def factorial(n):
    result = 1
    for i in range(n, 0 , -1):
        result *= i
    return result

print(factorial(5))

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial2(5))