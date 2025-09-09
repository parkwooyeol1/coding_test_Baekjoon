n1 = int(input().strip())
nums1 = set(list(map(int, input().strip().split())))
n2 = int(input().strip())
nums2 = list(map(int, input().strip().split()))

for i in nums2:
    if i in nums1:
        print(1)
    else:
        print(0)