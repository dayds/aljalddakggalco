import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

T = int(input())
dic = []

for _ in range(T) :
    N, K = map(int, input().split())
    date = list(map(int, input().split()))
    count = 1

    for i in range(2,N) :
        if date[i-1] < date[i] :
            count += 1
        else :
            continue

    dic.append([K, count])

for x in range(T) :
    print(f'case #{x+1}')
    if dic[x][1] >= dic[x][0] :
        print('1')
    else :
        print('0')