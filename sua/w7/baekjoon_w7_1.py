from bisect import bisect_left

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    count = 0
    for a in A:
        count += bisect_left(B, a)
    
    print(count)
