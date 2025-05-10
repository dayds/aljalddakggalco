import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False] * (n+1)

def bfs(start):
    visited[start] = True
    q = deque([(start, 0)])
    
    while q:
        current, jump = q.popleft()
        
        if current == b:
            return jump
        
        num = bridge[current - 1]

        for direction in [1, -1]:
            mul = 1
            while True:
                next_pos = current + num * mul * direction
                if next_pos < 1 or next_pos > n:
                    break
                if not visited[next_pos]:
                    visited[next_pos] = True
                    q.append((next_pos, jump + 1))
                mul += 1
    return -1

print(bfs(a))

