# 1️⃣ 입력 받기
n = int(input())  # 컴퓨터 개수
m = int(input())  # 연결된 쌍 개수

# 2️⃣ 그래프 만들기
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):  
    a, b = map(int, input().split())  
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# 3️⃣ 방문 여부 체크할 리스트 만들기
visited = [False] * (n + 1)

# 4️⃣ DFS 함수 정의
def dfs(node):
    visited[node] = True  # 현재 노드 방문 처리
    count = 1  # 현재 노드 감염 카운트 (자기 자신)
    
    for neighbor in graph[node]:  # 연결된 컴퓨터들 탐색
        if not visited[neighbor]:  # 방문하지 않았다면
            count += dfs(neighbor)  # 재귀적으로 탐색하면서 개수 누적
    
    return count

# 5️⃣ DFS 실행 (1번 컴퓨터부터 시작)
infected_count = dfs(1) - 1  # 1번 컴퓨터 제외한 감염된 컴퓨터 개수

# 6️⃣ 결과 출력
print(infected_count)
