import sys
from bisect import bisect_left
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  # 오름차순 정렬
  A.sort()
  B.sort()
  count = 0
  for a in A:
        # B에서 a보다 작은 원소의 개수
        count += bisect_left(B, a)
  print(count)
