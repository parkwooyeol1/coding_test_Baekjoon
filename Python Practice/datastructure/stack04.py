def solution(s):
    stack1 = []
    stack2 = []
    dictionary = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }
    # 2 + 2 * 3 - 2  : 2 2 3 * + 2 -  
    for i in s:
        if i == " ":
            continue         
        if i.isdigit(): 
            stack1.append(i)
        elif i in dictionary:
            while (stack2 and stack1[-1]in dictionary and dictionary[i] <= dictionary[stack2[-1]]):
                stack1.append(stack2.pop())
            stack2.append(i)
        elif i == '(':
            stack2.append(i)
        elif i == ')':
            while stack2 and stack1[-1] != '(':
                stack1.append(stack2.pop())
            stack1.pop()
    while stack2:
        stack1.append(stack2.pop()) 
    return ''.join(stack1)
s = "(2 + 2) * 3 - 2"
print(solution(s))
        