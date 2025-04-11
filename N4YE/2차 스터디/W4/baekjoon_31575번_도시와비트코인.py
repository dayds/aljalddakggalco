import sys
from collections import deque
input = sys.stdin.readline   #input 함수 덮어쓰기

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(M)]

q = deque([(0, 0)])                    # 시작점 설정

while q:                               # 조건 : q에 값이 존재
    r, c = q.popleft()                 # q의 값을 왼쪽으로 pop

    for i in [(0, 1), (1, 0)]:         # 우측 / 하단 이동
        nr = r + i[0]                  # x값 이동 더하기
        nc = c + i[1]                  # y값 이동 더하기

        if 0<=nr<M and 0<=nc<N and graph[nr][nc] == 1:	# 이동 가능 : M과 N 이하 / graph가 1
            graph[nr][nc] += graph[r][c]
            q.append((nr, nc))                          # 이동 후 q에 추가

if graph[M-1][N-1]+1 == N+M:
    print('Yes')
else:
    print('No')
