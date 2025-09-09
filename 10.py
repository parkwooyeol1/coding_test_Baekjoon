s = input().strip()
s = s.replace(",", "").replace(":", " ")
month, d, y, h, m = s.split()

days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

if leap_year(int(y)):
    days["February"] = 29

def countminutes(month, d, h, m):
    total_m = 0
    for mon in list(days.keys()):
        if mon == month:
            break
        total_m += days[mon] * 24 * 60
    total_m += (int(d) - 1) * 24 * 60  
    total_m += int(h) * 60
    total_m += int(m)
    return total_m

elapsed_minutes = countminutes(month, d, h, m)
year_minutes = 366 * 24 * 60 if leap_year(int(y)) else 365 * 24 * 60
result = elapsed_minutes / year_minutes * 100

print(result)
