import sys
input = sys.stdin.readline

def ab_pair(n, m, a, b):
    cnt = 0
    pair = 0
    
    a.sort()
    b.sort()
    
    for i in range(n):
        while 1:
            if cnt == m or a[i] <= b[cnt]:
                pair += cnt
                break
            else:
                cnt += 1
    return pair

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(ab_pair(n, m, a, b))

