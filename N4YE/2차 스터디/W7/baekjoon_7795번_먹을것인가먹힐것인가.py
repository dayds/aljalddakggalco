import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    answer = 0
    for i in range(n):
        for j in range(m):
            if a[i] > b[j]:
                answer += 1
            else:
                break
    print(answer)