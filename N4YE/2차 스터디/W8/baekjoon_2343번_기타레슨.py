import sys
input = sys.stdin.readline

n, m = map(int, input().split())     # n: 강의의 수 / m: 블루레이의 수
times = list(map(int, input().split()))

start, end = max(times), sum(times)  # 블루레이 용량 기준으로 탐색

while start <= end :
    middle = (start + end) // 2      # 용량(middle) 설정

    total = 0                        # 용량 현황
    num = 1                          # 블루레이 개수
    for t in times:
        if total + t > middle:       # 용량(middle) 보다 넘치면
            num += 1                 # 블루레이 개수 늘리기
            total = 0
        total += t

    if num <= m:                     # "블루레이 수"보다 작으면
        answer = middle
        end = middle - 1             # 개당 용량 줄이기 (블루레이 수 늘리기)
    else:
        start = middle + 1           # 아니면 개당 용량 늘리기 (블루레이 수 줄이기)

print(answer)