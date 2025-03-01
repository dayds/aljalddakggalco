import sys

t = int(sys.stdin.readline().strip())  # 테스트 케이스 개수 입력
cases = [int(sys.stdin.readline().strip()) for _ in range(t)]  # 각 테스트 케이스 입력

max_n = max(cases)  # 입력된 값 중 가장 큰 n을 찾음 (미리 dp 배열을 채우기 위해)
dp = [0] * (max_n + 1)  # DP 배열 초기화

# 초기 값 설정
dp[0] = 1  
if max_n >= 1:
    dp[1] = 1
if max_n >= 2:
    dp[2] = 2
if max_n >= 3:
    dp[3] = 4

# DP 테이블 채우기
for i in range(4, max_n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# 각 테스트 케이스에 대한 결과 출력
for n in cases:
    print(dp[n])
