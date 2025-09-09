from collections import deque
n = int(input())
cards = []

for i in range(1, n+1):
    cards.append(i)

q = deque(cards)

while len(q) != 1:
    q.popleft()
    k = q.popleft()
    q.append(k)
print(q[0])