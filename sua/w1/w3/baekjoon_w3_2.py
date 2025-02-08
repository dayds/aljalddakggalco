from collections import deque

# 1️⃣ 입력 받기
n = int(input())  # 지도 크기 입력
graph = [list(map(int, input())) for _ in range(n)]  # 지도 입력 받기

# 2️⃣ 방향 설정 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (x, y) 방향

# 3️⃣ BFS 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])  # 큐에 현재 위치 넣기
    graph[x][y] = 0  # 시작 지점 방문 처리
    count = 1  # 시작 집을 카운트

    while queue:
        cx, cy = queue.popleft()  # 큐에서 현재 위치 꺼내기

        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            # 범위 내에서 방문하지 않은 집을 찾으면 큐에 추가
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))  # 큐에 추가
                count += 1  # 집 개수 증가

    return count  # 해당 단지의 집 개수 반환

# 4️⃣ 단지 번호 매기기 및 집 개수 카운트
complexes = []  # 각 단지의 집 개수를 저장할 리스트

# 지도 전체를 순회하면서 단지를 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 집이 있으면
            complex_size = bfs(i, j)  # 단지 크기 계산
            complexes.append(complex_size)  # 단지 크기 리스트에 추가

# 5️⃣ 결과 출력
print(len(complexes))  # 총 단지 수
complexes.sort()  # 단지 크기 오름차순 정렬
for size in complexes:
    print(size)  # 각 단지의 집 수 출력
