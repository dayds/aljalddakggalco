import sys
from collections import deque
input = sys.stdin.readline

# 지도의 크기
n = int(input())
# 지도
graph = [list(map(int, input().strip())) for _ in range(n)]
# 방문 여부
visited = [[False] * n for _ in range(n)]
# 단지 번호
complex_num = 0

# bfs 함수
def bfs(x, y):
    global complex_num
    complex_num = 0  # 각 단지마다 초기화
    queue = deque([(x, y)])
    visited[x][y] = True
    complex_num += 1

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 좌표 꺼내기
        x, y = queue.popleft()

        # 상, 하, 좌, 우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 방문하지 않았고, 1인 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                # 큐에 좌표 추가
                queue.append((nx, ny))  
                # 방문 처리
                visited[nx][ny] = True
                # 단지 번호 증가
                complex_num += 1


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 단지 번호 저장
complex_list = []

# 단지 번호 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            complex_list.append(complex_num)

# 오름차순 정렬
complex_list.sort()

# 출력
print(len(complex_list))
for i in complex_list:
    print(i)