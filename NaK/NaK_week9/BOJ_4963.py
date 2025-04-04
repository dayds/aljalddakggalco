# 섬의 개수

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000) # 무한 재귀호출 방지

def dfs(x,y):
    dx = [1,1,1,0,0,-1,-1,-1] # 인접한 8방향 검사
    dy = [1,0,-1,1,-1,1,0,-1]

    field[x][y] = 0 # 방문한 땅 제거

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx,ny) # 연결된 다른 땅(1)을 따라 계속 탐색

while True:
    w,h = map(int, read().split())
    if w == 0 and h == 0:
        break

    field = []
    count = 0

    for i in range(h):
        field.append(list(map(int, read().split())))

    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                dfs(i,j)
                count += 1 # 섬 개수 카운트

    print(count)