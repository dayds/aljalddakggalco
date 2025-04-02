import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방향 설정(오른쪽 아니면 아래)
dx = [1, 0]
dy = [0, 1]

# 방문 표시 (기본을 1로)
visited = [[0]*n for _ in range(n)]

# bfs 탐색 함수 정의
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # 방문 표시
  visited[x][y] = 1

  while queue:
    # 앞에서부터 빠져나감
    x, y = queue.popleft()

    # 현재가 끝점이라면 성공
    if x == n-1 and y == n-1:
      return "HaruHaru"

    for i in range(2):
      # 칸에 적인 숫자만큼 오른쪽 혹은 아래로 이동
      nx = x + dx[i] * arr[x][y]
      ny = y + dy[i] * arr[x][y]

      # 이동한 위치가 범위 내에 있고 방문하지 않았다면
      if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
        # 방문으로 변경
        visited[nx][ny] = 1
        queue.append((nx, ny))
  return "Hing"

print(bfs(0, 0))
