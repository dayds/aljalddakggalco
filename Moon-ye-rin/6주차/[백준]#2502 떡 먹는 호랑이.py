import sys
from sympy import symbols, solve
# 입력 받기
input = sys.stdin.read
data = input().splitlines()

d, k = map(int, data[0].split())
dayList = [] # 날짜당 떡 개수를 저장할 리스트

for i in range(d):
  if i == 0:   # 1일차
    dayList.append('a')
  elif i == 1:   # 2일차
    dayList.append('b')
  else:
    dayList.append(dayList[i-2] + dayList[i-1])

# 마지막 날의 a, b 계수 확인
a_count = dayList[-1].count("a")
b_count = dayList[-1].count("b")

# 마지막 날의 a와 b의 개수를 세고 해당 결과가 k인 값을 찾기
x, y = symbols("x y", integer=True)   # 정수로 설정
eq1 = Eq((a_count * x) + (b_count * y), k)  # 방정식
solutions = solve(eq1, (x, y), dict=True)

result = []   # 결과를 저장할 리스트 
# (1 ≤ x ≤ y) 조건을 만족하는 해 찾기
for sol in solutions:
    if 1 <= sol[x] <= sol[y]:
        result.append([sol[x], sol[y]])

# 출력 (조건을 만족하는 해 출력)
print(result[0][0])
print(result[0][1])
