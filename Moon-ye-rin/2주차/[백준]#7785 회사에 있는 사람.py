import sys

n = int(sys.stdin.readline().strip())  # 첫 번째 줄에서 n 입력받기

person = set()  # 회사에 있는 사람을 저장하기 위한 집합 사용

for i in range(n):
    name, action = sys.stdin.readline().strip().split()  # 이름과 행동 입력받기

    if action == 'enter':  # 'enter'일 경우
        person.add(name)  # 집합에 사람 추가
    else:  # 'leave'일 경우
        person.discard(name)  #집합에 사람 삭제


# 사전 역순으로 정렬 후 출력
for name in sorted(person, reverse=True):
    print(name)
