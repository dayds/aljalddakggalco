'''import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input())   # 컴퓨터의 수
X = int(input())   # 네트워크 상 연결된 컴퓨터 쌍의 수

infection = [0]*(N+1)

for _ in range(X) :
    a, b = map(str, input().split())

    if a in infection :
        infection.append(b)

infection.remove('1')

print(len(set(infection)))'''


import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input())   # 컴퓨터의 수
M = int(input())   # 네트워크 상 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(N+1)]        # 그래프 생성
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)               # 방문여부 표시
count = -1                          # 1번째 컴퓨터 제외

def DFS(v):                         # 깊이우선탐색 함수 정의
    global count
    visited[v] = 1                  # v = 방문 완료 (1)
    count += 1
    for i in graph[v]:              # v의 그래프에서 확인
        if not visited[i]:          # 아직 방문 안되었으면 과정 반복
            DFS(i)

DFS(1)
print(count)