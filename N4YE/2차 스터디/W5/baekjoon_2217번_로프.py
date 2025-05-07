import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
rope = [int(input()) for _ in range(N)]
rope.sort()

answer = 0
for i in range(N):
    weight = rope[i] * (N - i)
    if weight > answer:
        answer = weight

print(answer)