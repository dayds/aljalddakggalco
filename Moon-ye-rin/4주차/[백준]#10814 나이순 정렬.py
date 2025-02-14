import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
# 나이와 이름을 공백으로 구분하여 리스트로 저장
arr = [list(data[i + 1].split()) for i in range(n)]

# 나이를 정수로 변환
for i in range(n):
    arr[i][0] = int(arr[i][0])

for i in sorted(arr, key=lambda x: x[0]):
    print(i[0], i[1])
