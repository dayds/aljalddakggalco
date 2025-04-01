import sys

# 입력 받기
input = sys.stdin.read
data = input().strip().splitlines()

n, k, a, b = map(int, data[0].split())

# 수분량 저장을 위한 리스트 생성(초기값 k)
arr = [k] * n
day = 0

# 수분량이 0 이 되기 전까지 반복
while all(x > 0 for x in arr):  # `0`이 하나라도 나오면 종료 
  day += 1
  # 수분 증발
  arr = [x - 1 for x in arr]
  # 수분량이 적은 순서대로 인덱스 정렬
  idx = sorted(range(n), key=lambda i: arr[i])  # 가장 건조한 순서대로 정렬

  for i in idx[:a]:
        arr[i] += b  # 물 추가

print(day)
