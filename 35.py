from itertools import combinations_with_replacement

n, m = map(int, input().split())
temp = [i for i in range(1, n+1)]

for comb in combinations_with_replacement(temp, m):
    print(*comb)



# product 순서O 중복O
# permutations 순서O 중복X
# combinations 순서X 중복X
# combinations_with_replacement 순서X 중복O