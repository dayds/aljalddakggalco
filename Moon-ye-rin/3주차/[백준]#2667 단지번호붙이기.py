import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])   
arr = [list(map(int, line.split())) for line in data[1:]]

#DFS 탐색
visited = [[False] * n for _ in range(n)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < n and 0 <= nx < n):
            continue
        if arr[ny][nx] == 0:
            continue
        if not visited[ny][nx]:
            dfs(ny, nx)

dfs(0, 0)
