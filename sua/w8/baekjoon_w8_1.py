import sys

input = sys.stdin.readline
M, N = map(int, input().strip().split())
snacks = list(map(int, input().split()))
min_length, max_length = 1, max(snacks)

while min_length <= max_length:
    mid = (min_length + max_length)//2
    children = 0
    for i in range(N):
        children = children + (snacks[i] // mid)
        
    if children >= M:
        min_length = mid +1
    else:
        max_length = mid -1
        
        
print(max_length)