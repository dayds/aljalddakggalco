import sys

input = sys.stdin.readline
N, M = map(int, input().strip().split())

time = list(map(int, input().strip().split()))

low, high = 1, min(time)*M

while low <= high:
    mid = (low + high) // 2
    ballons = 0
    for i in range(N):
        ballons  = ballons + (mid // time[i])

    if ballons < M:
        low = mid + 1
    elif ballons >= M:
        high = mid - 1
print(low)