n =  int(input())
ruler = 16384
rulers = [16384]

while sum(rulers) > n:
    min_rulers = min(rulers)
    rulers.remove(min_rulers)
    a = min_rulers / 2
    rulers.append(a)
    if sum(rulers) < n:
        rulers.append(a)

print(len(rulers))
