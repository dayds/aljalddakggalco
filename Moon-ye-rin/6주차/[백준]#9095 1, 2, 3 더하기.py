import sys
from itertools import *
# 입력 받기
input = sys.stdin.read
data = input().splitlines()

# n: 리스트 길이, arr: 1차원 리스트
n = int(data[0])
arr = list(map(int, data[1:]))
num = [1, 2, 3]

permutation = [] # 해당 숫자의 순열을 모두 저장할 리스트

result = [] # 각 테스트 케이스 마다 방법의 수를 저장할 리스트
count = 0 # 경우의 수 카운트

for i in arr:
  for j in range(1, i+1):
    numList = list(product(num, repeat = j))   # 1,2,3에 대하여 중복순열(1부터 해당 숫자까지repeat)
    permutation.extend(numList)  # permutation에 추가
  for k in permutation:
    if sum(k) == i:
      count += 1
  permutation.clear()
  result.append(count)
  count = 0

# result 리스트를 한 줄로 출력
print(*result, sep='\n')
