n = int(input())
students = []

for _ in range(n):
    student = input().split()
    name = student[0]
    korean = int(student[1])
    english = int(student[2])
    math = int(student[3])
    students.append((name, korean, english, math))


students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
