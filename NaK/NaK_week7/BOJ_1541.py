import sys

num = sys.stdin.readline().strip().split('-') # '-' 기준으로 분할
cal = [] # 괄호 안의 수식 계산 후 리스트로 저장

for i in num:
    cal.append(eval(i)) # 괄호 안 수식 계산

answer = cal[0]

for j in range(1,len(cal)):
    answer -= cal[j]

print(answer)




# 수정한 코드
num = input().strip().split('-')
cal = [sum(map(int, part.split('+'))) for part in num]

answer = cal[0]
for j in range(1, len(cal)):
    answer -= cal[j]

print(answer)