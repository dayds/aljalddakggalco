from collections import deque

n = int(input()) 
stepstone = list(map(int, input().split()))  

a, b = map(int, input().split()) 

visited = [-1] * n

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    
    while queue:
        x= queue.popleft()
        if x == b-1:
            print(visited[x])
            return
        
        jump = stepstone[x]
        
        i=1
        while True:
            next = x + jump * i
            if next >= n :
                break
            if visited[next] ==-1:
                visited[next] = visited[x] +1
                queue.append(next)
            i +=1
            
        i=1
        while True:
            next = x - jump * i
            if next < 0 :
                break
            if visited[next] ==-1:
                visited[next] = visited[x] +1
                queue.append(next)
            i +=1
    print(-1)
        

bfs(a - 1) 
