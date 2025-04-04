### Brute Force 알고리즘으로 해결

import sys
input = sys.stdin.readline

# 입력
e, s, m = map(int, input().split())

# 브루투포스 알고리즘으로 해결
year = 1

while True:
    if ((year - e) % 15 == 0) and ((year - s) % 28 == 0) and ((year - m) % 19) == 0:
        break
    # 년도 증가
    year += 1

# 출력
print(year)