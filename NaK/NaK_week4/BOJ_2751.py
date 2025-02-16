import sys

n = int(sys.stdin.readline()) # 수의 개수
count = []

# list에 입력
for i in range(n):
    count.append(int(sys.stdin.readline()))

# 리스트 정렬
count.sort()

# 정렬한 순서대로 출력
for i in range(n):
    print(count[i])