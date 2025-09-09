result = set()
a = set()
for i in range(1,10001):
    result.add(i)

self_number = 0
for i in range(1,10001):
    self_number = 0
    self_number += i
    for j in(str(i)):
        self_number += int(j)
    if self_number <= 10000:
        a.add(self_number)
result -= a
for i in sorted(result):
    print(i)