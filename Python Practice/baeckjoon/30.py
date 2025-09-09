from collections import Counter

n = int(input().strip())
nums1 = list(map(int, input().strip().split()))
m = int(input().strip())
count = Counter(nums1)
nums2 = list(map(int, input().strip().split()))
result = []

for i in nums2:
    if count[i]:
        result.append(count[i])
    else:
        result.append(0)

print(*result)

