"""
words = ["apple", "hi", "banana", "wow", "cherry"]
a = []
for i in range (0, len(words)):
    if len(words[i]) >= 5:
        a.append(words[i])
print(a)

words = ["cat", "dog", "apple", "banana"]
a = []
for i in range(0, len(words)):
    a.append(words[i][0])
print(a)

data = [1, 3, 1, 3, 2, 1, 4, 3, 3]
m = list(set(data)) #[1,3,2,4]
max = -1
for i in range (len(m)):
    if data.count(m[i]) > max:
        max = m[i]
print(max)"

words = ["kiwi", "watermelon", "fig", "apple"]
print(sorted(words, key=len))

matrix = [
    [3, 8, 1],
    [9, 2, 4],
    [6, 7, 5]
]
max = -1
max1 = (-1, -1)
m = []
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max1 = (i, j)
print(f"최대값 : {max}")
print(f"위치 : {max1}")

data = [1, 1, 2, 2, 2, 3, 3]
a = list(set(data)) #[1,2,3]
c= []
b = tuple()
for i in a:
    b = (i, data.count(i))
    c.append(b)
print(c)


matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]
total = 0
n = 0
for i in range (len(matrix)):
    for j in (matrix[i]) :
        total += j
        n += 1
print(total/n)

matrix = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]
a = []
result = []
for i in range (len(matrix[0])):
    for j in range (len(matrix)):
        a.append(matrix[j][i])
    result.append(a)
    a = []
print(result)
matrix = [
    [1, 2, 3], 
    [2, 3, 4], 
    [4, 5, 6]
]
a = []

for i in range (len(matrix)): # 0, 1, 2
    for j in range (len(matrix[i])): # 0,1 
        a.append(matrix[i][j])

print(list(set(a)))



students = {
    "Alice": {"math": 80, "english": 85},
    "Bob": {"math": 90, "english": 70},
    "Charlie": {"math": 75, "english": 95}
}
total = 0
n = 0
for i in students.keys():
    total += students[i]['math']
    n+=1
print(round(total/n, 2))
"""

for i in range (7):
    for j in range(i-1):
        print("@", end="")