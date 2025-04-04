import sys
input = sys.stdin.readline

# computer 개수
n = int(input())
# 연결된 컴퓨터 쌍의 수
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n+1)]
# 방문 여부
visited = [False] * (n+1)

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 쌍방 연결

# dfs 함수
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(visited.count(True) - 1)  # 1번 컴퓨터 제외