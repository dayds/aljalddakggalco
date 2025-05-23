# 강의 수: N, 블루레이 수: M
# start = max(guitar) (입력받은 배열의 최대값), end = sum(guitar) (입력받은 배열의 총합)
# count: mid의 길이로 배열을 담을 때 필요한 블루레이수
# mid로 자른 강의 수(cnt)와 블루레이 수(M) 비교
#  cnt가 M보다 많거나 같음
# -> 길이 늘릴 수 있음 (start = mid + 1)
# cnt가 M을 못 채움
# -> 길이 줄이기 (end = mid - 1)

N,M = map(int, input().split())
guitar = list(map(int, input().split()))

start,end = max(guitar), sum(guitar)
result = 0

while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1
    for i in guitar:
        if total + i > mid:
            count += 1
            total = 0
        total += i

    if count > M:
        start = mid + 1

    else:
        end = mid - 1
        result = mid

print(result)