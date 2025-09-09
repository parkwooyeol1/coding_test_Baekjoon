y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    return year%4 == 0 and year%100 != 0 or year%400 == 0

def countday(y, m, d):
    total = 0
    for i in range(1,y):
        if leap_year(i):
            total += 366
        else:
            total += 365

    for i in range(1,m):
        if i == 2 and leap_year(y):
            total += 29
        else:
            total += days[i]
        
    total += d
    return total

start = countday(y1,m1,d1)
end = countday(y2,m2,d2)


if (y2 > y1 + 1000) or (y2 == y1 + 1000 and (m2, d2) >= (m1, d1)):
    print("gg")
else:
    print(f"D-{end-start}")
    