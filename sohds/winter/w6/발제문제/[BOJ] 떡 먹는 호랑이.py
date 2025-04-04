import sys
input = sys.stdin.readline

# 할머니가 넘어온 날 d, 그 날 호랑이에게 준 떡의 개수 k
d, k = map(int, input().split())

# dp 배열 초기화
dp = [0 for _ in range(d)]
dp[0], dp[1] = 1, 1

# 첫째날과 둘째날의 떡의 개수를 1씩 증가시키면서 d번째 날의 떡의 개수가 k가 될 때까지 찾기
while True:
    for i in range(2, d):   # 셋째날부터 d번째 날까지의 떡의 개수는 전날과 전전날 떡의 합
        dp[i] = dp[i-1] + dp[i-2]

    # d번째 날의 떡의 개수가 k와 같으면 첫째날과 둘째날의 떡의 개수 출력
    if dp[d-1] == k:
        print(dp[0])
        print(dp[1])
        break
    
    # d번째 날의 떡의 개수가 k보다 크면 첫째날 떡의 개수를 늘리고 둘째날도 같은 개수로 설정
    elif dp[d-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    
    # d번째 날의 떡의 개수가 k보다 작으면 둘째날 떡의 개수만 늘리기
    else:
        dp[1] += 1
