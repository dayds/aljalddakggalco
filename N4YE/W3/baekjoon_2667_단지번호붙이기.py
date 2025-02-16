import sys
from collections import deque
input = sys.stdin.readline   #input 함수 덮어쓰기


N = int(input())
graph = [list(map(int, input())) for _ in range(N)]  # 행렬 생성


def bfs(graph, x, y):             # 너비우선탐색 함수 정의
    dx = [-1, 1, 0, 0]            # graph[x][y]로 상하좌우 이동
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0                  # 첫번째집 방문 기록 (0)
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):           # 좌표마다 상하좌우로 (4번) 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:   # 미방문 상태(1) 일때
                graph[nx][ny] = 0    # 방문 기록 (0)
                queue.append((nx, ny))
                cnt += 1
    return cnt


count = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]
'''
# 한줄 쓰기 연습!
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
'''

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])
