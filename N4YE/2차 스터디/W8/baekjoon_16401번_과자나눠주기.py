import sys
input = sys.stdin.readline

m, n = map(int, input().split())     # 사람 m명, 쿠기 n개
cookies = list(map(int, input().split()))

start, end = 1, max(cookies)
answer = 0

while start <= end :
    middle = (start + end) // 2      # 중앙값 설정

    pieces = 0
    for cookie in cookies:
        pieces += cookie // middle   # 길이가 middle인 쿠키 개수 (몫 더하기)

    if pieces >= m :                 # m명에게 모두 쿠키가 돌아갈때
        answer = middle
        start = middle + 1           # 쿠키 길이 늘리기
    else :
        end = middle - 1             # 아닐경우 쿠키 길이 줄이기

print(answer)
