# 점프왕 쩰리(Small)

import sys

def dfs(x,y):
    # 영역을 벗어났거나 이미 방문했을 때
    if x <= -1 or x >= N or y <= -1 or y >= N or visit[x][y] == 1:
        return

    # 방문한 곳의 칸 수가 -1
    if gamemap[x][y] == -1:
        visit[x][y] = 1
        return

    # 방문했다고 표시
    visit[x][y] = 1

    # 칸에 적힌 수만큼 점프
    dfs(x+gamemap[x][y], y)
    dfs(x, y+gamemap[x][y])

N = int(sys.stdin.readline())

# 게임판 입력
gamemap = []
for _ in range(N):
    gamemap.append(list(map(int, sys.stdin.readline().split())))

# 방문여부 저장
visit = []
for _ in range(N):
    visit.append([0]*N)

dfs(0,0)

# 결과
if visit[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')