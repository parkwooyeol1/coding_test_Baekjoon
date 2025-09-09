n, k =  map(int, input().split())
coins = []
count = 0
for _ in range(n):
    coin = int(input().strip())
    if coin <= k:
        coins.append(coin)
for i in sorted(coins, reverse = True):
    if i <= k:
        count += k // i
        k = k%i
    elif k == 0:
        break
print(count)