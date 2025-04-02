import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline

# 방향 설정(대각선도)
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# bfs 탐색 함수 정의
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # 방문 표시
  visited[x][y] = 1

  while queue:
    # 앞에서부터 빠져나감
    x, y = queue.popleft()

    # 방향을 돌면서
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위 내에서
      if 0 <= nx < h and 0 <= ny < w:
        # 이동한 위치가 섬이고 방문한 적이 없다면
        if arr[nx][ny] == 1 and visited[nx][ny] == 0:
          # 방문으로 변경
          visited[nx][ny] = 1
          queue.append((nx, ny))



while True:
  # 테스트 케이스 입력받기
  w, h = map(int, input().split())
  # h 깊이 만큼 매트릭스 리스트 받기
  arr = [list(map(int, input().split())) for _ in range(h)]
  # 방문 리스트 생성
  visited = [[0]*w for _ in range(h)]
  # 섬의 개수를 카운트할 변수 생성
  land = 0

  for i in range(h):
    for j in range(w):
      # 해당 위치가 섬이고 방문한 적이 없다면
      if arr[i][j] == 1 and visited[i][j] == 0:
        bfs(i, j)
        land += 1

  print(land)
