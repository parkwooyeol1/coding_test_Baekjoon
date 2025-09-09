st =  input().strip()

if len(st) == 3:
    print(st)
else:
    result = []
    for i in range(1, len(st)-1):
        for j in range(i+1, len(st)):
            a = st[:i][::-1]
            b = st[i:j][::-1]
            c = st[j:][::-1]
            result.append(a+b+c)
    print(min(result))