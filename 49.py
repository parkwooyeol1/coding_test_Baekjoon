nums = []
count = 0

def prime(a):
    for i in range(2, int(a**0.5)+1):
        if a % i ==0:
            return False
    return True

while True:
    k = int(input())
    if k == 0:
        break
    nums.append(k)
    
for num in nums:
    for i in range(num+1, 2*num+1):
        if prime(i):
            count += 1
    print(count)
    count = 0

        


