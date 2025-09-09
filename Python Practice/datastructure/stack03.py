def solution(s): 
    stack = []
    A = s.split()      
    for i in A:
        if i in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if i == "+":
                stack.append(a+b)
            elif i == "-":
                stack.append(a-b)
            elif i == "*":
                stack.append(a*b)
            elif i == "/":
                stack.append(a/b)
        else:
            stack.append(int(i))
    return stack[0]


s = "8 2 / 3 - 3 2 * +"
print(solution(s))

