X =  int(input().strip())
count = 1
while X > count:
    X -= count
    count +=1
a = 1
if count%2 == 0:
    for i in range(X-1):
        count -= 1
    print(f"{X}/{count}")
else:
    for i in range(X-1):
        a += 1
        count -= 1
    print(f"{count}/{a}")