import sys

input = sys.stdin.readline

nodes = int(input())  
edges = int(input())  

visited = [False] * (nodes + 1)  
visited[1] = True  

graph = [[] for _ in range(nodes + 1)]  
for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, start_node):
    for neighbor in graph[start_node]:
        if not visited[neighbor]:  
            visited[neighbor] = True  
            dfs(graph, visited, neighbor) 

dfs(graph, visited, 1)

print(visited.count(True) - 1) 
