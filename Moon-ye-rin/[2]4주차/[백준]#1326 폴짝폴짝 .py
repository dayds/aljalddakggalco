import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

visited = [0] * n

def bfs(start, end):
    queue = deque([(start, 0)])
    visited[start] = 1

    while queue:
        v, count = queue.popleft()

        # 도착하면 종료
        if v == end:
            return count

        # 오른쪽 방향 탐색
        for i in range(v + arr[v], n, arr[v]):
            if not visited[i]:
                visited[i] = 1
                queue.append((i, count + 1))

        # 왼쪽 방향 탐색
        for i in range(v - arr[v], -1, -arr[v]):
            if not visited[i]:
                visited[i] = 1
                queue.append((i, count + 1))

    return 0  # 도달 불가

# 시작점, 도착점은 인덱스 조정 필요
result = bfs(a - 1, b - 1)

# 결과 출력
if result == 0:
    print(-1)
else:
    print(result)
