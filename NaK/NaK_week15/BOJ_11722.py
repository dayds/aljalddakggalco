n = int(input())

arr = list(map(int,input().split()))

dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# arr 안의 수에 대해 가장 긴 감소하는 부분 수열의 길이 구하기
# 앞의 수가 다음 수보다 크다면 문제의 조건 만족
# 각 인덱스에 대해 자신보다 인덱스가 작은 값을 검색하여 조건을 만족하는 수의 개수 찾기
# 앞의 인덱스에서 조건을 만족하는 수의 개수를 찾으면, 다음 계산시에 이를 이용