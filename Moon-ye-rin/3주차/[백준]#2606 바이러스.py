import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])   
arr = [tuple(map(int, line.split())) for line in data[2:]]

# 그래프 인접 리스트 생성
agi_list = [[] for _ in range(n + 1)]
for a, b in arr:
    agi_list[a].append(b)
    agi_list[b].append(a)

# BFS 탐색
def bfs(start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(agi_list[node])  # 현재 노드와 연결된 노드 추가
            
    return len(visited) - 1  # 1번 노드 제외 후 반환

# 1번 노드에서 연결된 모든 노드 개수 출력
print(bfs(1))
