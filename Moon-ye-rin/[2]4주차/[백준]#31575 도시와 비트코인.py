import sys

# 입력 받기
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

# 방향 설정(오른쪽 아니면 아래)
dx = [1, 0]
dy = [0, 1]

# 방문 표시
visited = [[0]*n for _ in range(m)]

# dfs 함수 정의
def dfs(x, y):
  # 목적지에 도착했다면
  if  x == m-1 and y == n-1:
    return "Yes"
  
  visited[x][y] = 1

  # 오른쪽, 아래만 탐색
  for i in range(2):
    nx = x + dx[i]
    ny = y + dy[i]

    # 이동한 위치가 범위 내에 있다면
    if 0 <= nx < m and 0 <= ny < n:
      # 이동한 위치가 1이고 방문하지 않았다면
      if arr[nx][ny] == 1 and visited[nx][ny] == 0:
        # dfs탐색을 실행, 목적지에 도착할 수 있다면 yes 리턴
        if dfs(nx, ny) == "Yes":
          return "Yes"

  return "No" # 탐색이 실패하면 no 리턴
    
print(dfs(0, 0))
