import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

# N : 물이 새는 곳 개수 / L : 테이프의 길이
# x : 물이 새는 곳 위치

N, L = map(int, sys.stdin.readline().split())
data = list(map(int, input().split()))
data.sort()

start = data[0]                                 # 시작 지점 설정
count = 1                                       # 시작 지점 테이프 (1개)

for x in data[1:] :
    if (x - start) < L :                        # 테이프 길이내에 x가 있으면 계속
        continue
    else :                                      # 없으면 x를 start로 바꾸고 테이프 (+1개)
        start = x
        count += 1

print(count)
