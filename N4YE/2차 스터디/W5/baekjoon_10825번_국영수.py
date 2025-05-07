import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
students = [input().split() for _ in range(N)]
students = [[name, int(kor), int(eng), int(math)] for name, kor, eng, math in students]

# 정렬 기준: 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])
