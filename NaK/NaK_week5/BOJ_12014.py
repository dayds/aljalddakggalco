import sys

T = int(sys.stdin.readline()) # 케이스 개수

answer =[]

for i in range(T):
    n,k = map(int, sys.stdin.readline().split())
    stock = list(map(int, sys.stdin.readline().split()))
    count = 0

    for i in range(1,n):
        if stock[i] >= stock[i-1]:
            count += 1

    if count < k:
        answer.append(0)
    else:
        answer.append(1)

for i in range(T):
    print(f'Case #{i+1}')
    print(answer[i])