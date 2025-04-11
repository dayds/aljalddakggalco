from collections import deque

n, m = map(int, input().split()) 

city = []
for _ in range(m): 
    city.append(list(map(int, input().split())))
    
visited = [[False]*n for _ in range(m)]

directions = [(0, 1), (1, 0)]  # (dy, dx)

def bfs(city, start, visited):
    m= len(city)
    n= len(city[0])
    
    queue = deque([start])
    visited[0][0] = True
    
    while queue:
        y,x = queue.popleft()
        if (y, x) == (m-1, n-1):
            print("Yes")
            return
        
        for dy, dx in directions:
            ny = y +dy
            nx = x+dx
            
            if 0 <= ny < m and 0 <=nx < n:
                if city[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    
    print("No")

bfs(city, (0, 0), visited)
        


