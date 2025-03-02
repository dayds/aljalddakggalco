import sys
input = sys.stdin.readline

# 테스트 케이스 개수
t = int(input())
n_limit = 11

# dp 배열 초기화
dp = [0] * (n_limit)
dp[1], dp[2], dp[3] = 1, 2, 4

# 4부터 11까지 반복하면서 dp 배열 채우기 (점화식)
for i in range(4, n_limit):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 테스트 케이스 개수만큼 반복하면서 dp 배열 출력
for _ in range(t):
    test_no = int(input())
    print(dp[test_no])