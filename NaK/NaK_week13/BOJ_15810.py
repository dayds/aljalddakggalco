# 스태프 수: N, 풍선 개수: M 입력
# 각 스태프 들이 풍선 하나를 만드는데 걸리는 시간 입력 -> 리스트: BT

# 1분이 지날 때마다 시간에 맞춰 각 스태프가 만드는 풍선의 개수 1씩 추가

# input
N,M = map(int, input().split())
BT = list(map(int, input().split()))

time = 0
balloon = 0

while True:
    time += 1
    balloon = sum(time // b for b in BT)

    if balloon >= M:
        break


print(time)

# 이것도 시간초과...

# 입력
N, M = map(int, input().split())
BT = list(map(int, input().split()))

# 이진 탐색 범위 설정
left = 1
right = max(BT) * M  # 최악의 경우: 가장 느린 사람이 혼자 다 만드는 경우

answer = right

while left <= right:
    mid = (left + right) // 2
    balloons = sum(mid // b for b in BT)

    if balloons >= M:
        answer = mid  # 가능한 시간, 더 줄일 수 있을지 확인
        right = mid - 1
    else:
        left = mid + 1

print(answer)

# 이진탐색의 동작 방식은 이해하였지만 아직 코드로 작성하는 것은 어려운 것 같다.
# 다음주에는 확실히 코드로 작성 가능하도록 더 연습해야할 것 같다.