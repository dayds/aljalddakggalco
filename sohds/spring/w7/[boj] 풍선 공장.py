import sys
input = sys.stdin.readline

def balloon_factory(n, m, a):
    low, high = 1, min(a)*m
    
    while low <= high:
        mid = (low + high) // 2
        total = 0
        for i in range(n):
            total += mid // a[i]
            
        if total < m:
            low = mid + 1
        else:
            high = mid - 1
                
    return low

n, m = map(int, input().split())
a = list(map(int, input().strip().split()))

print(balloon_factory(n, m, a))
