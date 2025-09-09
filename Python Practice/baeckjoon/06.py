n =  int(input().strip())
stu_map = []
for i in range(n):
    a = input().strip().split()
    numbers = list(map(int, a))
    stu_map.append(numbers)

count = [0] * n

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(5):
            if stu_map[i][k] == stu_map[j][k]:
                count[i] += 1
                break 
max_count = max(count)
for i in range(n):
    if count[i] == max_count:
        print(i+1)
        break


