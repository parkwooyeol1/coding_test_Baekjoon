"""
employees = {
    "Engineering": {
        "Alice": {"age": 29, "salary": 95000},
        "Bob": {"age": 35, "salary": 87000}
    },
    "HR": {
        "Charlie": {"age": 30, "salary": 60000},
        "David": {"age": 40, "salary": 65000}
    },
    "Sales": {
        "Eve": {"age": 28, "salary": 72000},
        "Frank": {"age": 33, "salary": 70000}
    }
}
max = -1
a = {}
for i in employees.keys() :
    for j in employees[i].keys():
        if employees[i][j]['salary'] > max:
            max = employees[i][j]['salary']
            a[i] = (j, max)
    max = -1
print(a)


triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

q = len(triangle) # 5
for i in range(q-2,-1,-1): # 3, 2, 1, 0
    for j in range(len(triangle[i])):   # 0, 1, 2 ,3 
        a = [triangle[i+1][j], triangle[i+1][j+1]]
        triangle[i][j] += max(a)
        
print(triangle[0][0])


a = input()
a = a[::-1]
print(a)

k = 0
a = input()
for i in a :
    if i == "a" or i == "e" or i == "i" or i == "o" or  i == "u" :
        k +=1
print(k)

a = input()
b = ""
for i in a: 
    if i.isupper() == True:
        b += i.lower()
    else : 
        b += i.upper()
print(b)


a = input()
fir = a[0]
result = []
count = 1
#aaabbbc

result.append(f"{fir}")
for i in a[1:]:
    if fir == i:
        count += 1
    else:
        result.append(f"{count}")
        fir = i
        count = 1
        result.append(f"{fir}")
result.append(f"{count}")

print("".join(result))

"""
#a3b2c1 -> aaabbc

a = "a3b2c1"
b = []
k = []
for i in a:
    if i.isalpha():
        b.append(i)
    else:
        b = (int(i) * b)
        k.extend(b) 
        b = []

print("".join(k))

result = ""
for i in range(len(a)):
    if a[i].isalpha():
        result += a[i] # a 
    else: # i = 1
        result += result[-1] * (int(a[i]) - 1) # 'a' * 3 -1 = aa

print(result)