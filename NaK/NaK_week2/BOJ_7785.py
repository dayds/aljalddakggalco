import sys

# 1. 출입기록 수(count) input
count = int(sys.stdin.readline())

# list 생성
company = []

# 2. for문 안에서 진행(count만큼 반복)
for i in range(count):
    # 3. 사람(name)과 출입기록(el) input
    name,el = map(str, sys.stdin.readline().split())

    # 4. el이 enter일 경우 name을 list(company)에 입력
    if el == 'enter':
        company.append(name)

    # 5. el이 leave일 경우 name을 list(company)에서 제거
    elif el == 'leave':
        company.remove(name)

# 6. 사전 순의 역순으로 출력
for x in reversed(sorted(company)):
    print(x)