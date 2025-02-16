import sys

# 입력 받기
n = int(sys.stdin.readline().strip())
members = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), i, name))  # 나이, 가입 순서, 이름 저장

# 정렬: 나이 오름차순, 가입 순서 유지
members.sort(key=lambda x: (x[0], x[1]))

# 출력
for age, _, name in members:
    print(age, name)