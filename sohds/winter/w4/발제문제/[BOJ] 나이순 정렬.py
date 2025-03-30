import sys
# 입력
n = int(sys.stdin.readline())
arr = []

# 입력받은 나이와 이름을 배열에 저장
for _ in range(n):
    age, name = sys.stdin.readline().split()
    arr.append((int(age), name))

# 나이순으로 정렬
arr.sort(key=lambda x: x[0])

# 출력
for i in arr:
    print(i[0], i[1])