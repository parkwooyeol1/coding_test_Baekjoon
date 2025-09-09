"""
def solution(s):
    a = []
    count = 0
    for i in s:
        a.append(i)
        if i == "(" or ")" or "[" or "]" or "{"or "}" :
            count += 1
        else:
            return False
    if count % 2 == 0:
        if (a.count("(") + a.count("(")) % 2 == 0 and (a.count("{") + a.count("}"))% 2 == 0 and (a.count("[") + a.count("]"))% 2 == 0:
            #if "(" and ")" or "{" and "}"or "[" and "]" in a:
            return True
        else:
            return False
    else:
        return False
s = "([}])"
print(solution(s))
"""
            
def solution(s):
    stack = []
    dictionary = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    for i in s:
        if i in dictionary.values():
            stack.append(i)
        elif i in dictionary.keys():
            if not stack or stack.pop() != dictionary[i]:
                return False
    return not stack
s = "(())())"
s = "가나"
print(solution(s))
