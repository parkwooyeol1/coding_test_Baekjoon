T = int(input().strip())
b = {
    ')':'('
}
for i in range(T):
    a = input().strip()
    stack = []
    for j in range(len(a)):
        if a[j] in b.values():
            stack.append(a[j])
        elif a[j] in b.keys():
            if not stack or stack.pop() != b[a[j]]:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
