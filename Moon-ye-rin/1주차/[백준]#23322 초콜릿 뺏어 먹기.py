import sys

# 입력을 한 번에 처리
input = sys.stdin.read
data = input().splitlines()

n, k = map(int, data[0].split())
arr = list(map(int, data[1].split()))

day = 0
num = 0
min_num = min(arr)
for i in range(1, len(arr)):
    if arr[i - 1] <= arr[i] and min_num < arr[i]:
      num += arr[i] - arr[i-1]
      arr[i] = arr[i] - arr[i-1]
      day += 1

print(num, day)
