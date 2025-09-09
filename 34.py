N, M = map(int, input().strip().split())
nums = list(map(int, input().split()))
print(nums)

for _ in range(M):
    i, j = map(int, input().strip().split())
    a = sum(nums[i-1:j])
    print(a)