import sys

for line in sys.stdin:
    s = line.rstrip("\n")
    if s == ".":
        break

    stack = []
    ok = True

    for ch in s:
        if ch == "(" or ch == "[":
            stack.append(ch)
        elif ch == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                ok = False
                break
        elif ch == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                ok = False
                break

    print("yes" if ok and not stack else "no")
            
        





