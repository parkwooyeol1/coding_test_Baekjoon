"""
students = {
    "Alice": {"Math": 85, "English": 78, "Science": 92},
    "Bob": {"Math": 90, "English": 85, "Science": 88},
    "Charlie": {"Math": 72, "English": 80, "Science": 75},
}
n = len(students.values())
max = -1
maxStudent = ""
for i in students.keys():
    totalScore = sum(students[i].values())
    average = round(totalScore / n, 3)
    print(f"{i} = {average}")

    if students[i]['Math'] > max :
        max = students[i]['Math']
        maxStudent = i
print(f"{maxStudent} = {max}")

products = {
    "A101": {"이름": "노트북", "가격": 1200000, "재고": 5},
    "B202": {"이름": "마우스", "가격": 15000, "재고": 50},
    "C303": {"이름": "키보드", "가격": 45000, "재고": 20},
}
a = dict()
for product in products.keys() :
    a = products[product]['가격']
    if a == 15000 :
        print (products[product]['이름'])

students = {
    "학생1": {"국어": 80, "수학": 92, "영어": 85, "보너스": 0},
    "학생2": {"국어": 75, "수학": 88, "영어": 90, "보너스": 0},
    "학생3": {"국어": 85, "수학": 95, "영어": 78, "보너스": 0},
}

for name in students.keys() :
    if students[name]['수학'] >= 90 :
        students[name]['보너스'] += 5
print (students)

books = {
    "책1": {"제목": "파이썬 기초", "저자": "김철수", "출판연도": 2020, "재고": 5},
    "책2": {"제목": "자료구조", "저자": "박영희", "출판연도": 2018, "재고": 2},
    "책3": {"제목": "알고리즘", "저자": "정우성", "출판연도": 2021, "재고": 7},
}
books['책4'] = {"제목": "파이썬 심화", "저자": "이강준", "출판연도": 2024, "재고": 12}
books['책4']['출판연도'] = 2025
print(books)


employees = {
    "E001": {"이름": "김철수", "나이": 35, "직급": "매니저", "부서": "영업"},
    "E002": {"이름": "이영희", "나이": 28, "직급": "사원", "부서": "개발"},
    "E003": {"이름": "박지훈", "나이": 40, "직급": "팀장", "부서": "마케팅"},
    "E004": {"이름": "최민호", "나이": 33, "직급": "과장", "부서": "개발"},
    "E005": {"이름": "정유진", "나이": 38, "직급": "매니저", "부서": "재무"},
}
k = dict()
for i in employees.keys() :
    if employees[i]['나이'] >= 30 and employees[i]['직급'] == "팀장" or employees[i]['직급'] == "매니저" :
        a = employees[i]['이름']
        b = employees[i]['부서']
        k[a] = b

k = k.items()
print(k)
print (list(k))


students = {
    "S101": {"이름": "김철수", "국어": 80, "수학": 85, "영어": 78},
    "S102": {"이름": "이영희", "국어": 90, "수학": 95, "영어": 88},
    "S103": {"이름": "박지훈", "국어": 85, "수학": 89, "영어": 92},
    "S104": {"이름": "최민호", "국어": 70, "수학": 60, "영어": 75},
}


for i in students.keys() :
    students[i]['수학'] += 10
    if students[i]['수학'] > 100 :
        students[i]['수학'] = 100
    total = students[i]['국어'] + students[i]['수학'] + students[i]['영어'] 
    average = round(total / 3, 2)
    students[i]['평균'] = average
a = students.values()
print(list(a))

numbers = [3, 6, 9, 12, 15, 18, 21]
a = list()
for i in numbers :
    if i%2 == 0 :
        a.append(i)
print(a)

print(numbers[1::2])

data = [5, 3, 8, 3, 1, 5, 7, 8, 2]
data = set(data)
data = list(data)
data = sorted(data)
print(data)
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
a  = list()
for i in matrix :
    a.extend(i)
print(a)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a = matrix[1]
print(a[2])

matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 9, 11]
]
a1 = [] 
b1 = []

for i in range(0,3):
    a1.append(sum(matrix[i]))
print(a1)

for i in range(0,3):
    b = 0
    for j in range(0,3) :
        b += matrix[j][i]
    b1.append(b)
print(b1)

matrix = [
    [5, 1, 9],
    [2, 7, 6],
    [8, 3, 4]
]
a = 0
for i in range(0,3):
     a += matrix [i][i]
print(a)
b=0
for i in range(0,3):
    b += matrix[i][-1*i+2]
print(b)

"""
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]

d = []
a = []
b = []
c = []
for i in range (0,3):
    a.append(matrix[i][0])
    b.append(matrix[i][1])
    c.append(matrix[i][2])
a = sorted(a, reverse=True)
b = sorted(b, reverse=True)
c = sorted(c, reverse=True)
d.append(a)
d.append(b)
d.append(c)
print(d)