n = int(input()) 
students = []

for _ in range(n):
    student = input().split()
    name = student[0]
    korean = int(student[1])
    english = int(student[2])
    math = int(student[3])
    students.append((name, korean, english, math))


for i in range(n):
    for j in range(i + 1, n):
        if students[i][1] < students[j][1]:
            students[i], students[j] = students[j], students[i]
        elif students[i][1] == students[j][1] and students[i][2] > students[j][2]:
            students[i], students[j] = students[j], students[i]
        elif students[i][1] == students[j][1] and students[i][2] == students[j][2] and students[i][3] < students[j][3]:
            students[i], students[j] = students[j], students[i]
        elif students[i][1] == students[j][1] and students[i][2] == students[j][2] and students[i][3] == students[j][3] and students[i][0] > students[j][0]:
            students[i], students[j] = students[j], students[i]


for student in students:
    print(student[0])
