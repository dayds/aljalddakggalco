import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = []
for _ in range(N):
    visited.append([0 for _ in range(N)])


def dfs(x, y, arr):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    k = arr[x][y]
    if visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x + k, y, arr)
        dfs(x, y + k, arr)
        return True


dfs(0, 0, arr)
if visited[n - 1][n - 1] == 1:
    print("HaruHaru")
else:
    print("Hing")