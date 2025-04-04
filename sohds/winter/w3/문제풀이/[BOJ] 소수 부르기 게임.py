### Greedy 알고리즘으로 해결

import sys
input = sys.stdin.readline

# 소수 찾기 함수
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 입력
a, b = map(int, input().split())
c, d = map(int, input().split())

# 각자가 부를 수 있는 소수 집합 생성
yt_primes = set(num for num in range(a, b+1) if is_prime(num))
yj_primes = set(num for num in range(c, d+1) if is_prime(num))

# 공통으로 부를 수 있는 소수와 각자만 부를 수 있는 소수 구분
common_primes = yt_primes & yj_primes
yt_only = yt_primes - yj_primes
yj_only = yj_primes - yt_primes

# 승자 결정
# 용태가 먼저 시작하므로, 용태만의 소수 개수 + (공통 소수 개수 + 1) // 2가
# 유진이만의 소수 개수 + 공통 소수 개수 // 2보다 크거나 같으면 용태 승
yt_count = len(yt_only) + (len(common_primes) + 1) // 2
yj_count = len(yj_only) + len(common_primes) // 2

if yt_count > yj_count:
    print("yt")
else:
    print("yj")
