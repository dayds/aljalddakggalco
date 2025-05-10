import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# 리스트 오름차순 정렬
arr.sort()

# 최대 중량값을 저장하는 변수
max_weight = 0

# 중량값을 계산
for i in range(n):
    weight = arr[i] * (n - i)
    max_weight = max(max_weight, weight) # 두 값을 비교해 최대값을 갱신

print(max_weight)
