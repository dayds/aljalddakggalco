import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

answer = 0

while True :
    start = a
    end = b

    if (end-start) % bridge[start] == 0 :
        answer = 1
        break
    else :
        start += bridge[start]
        if start > end :
            answer = -1
            break

print(answer)