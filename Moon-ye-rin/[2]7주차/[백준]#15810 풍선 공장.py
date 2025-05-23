import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = m* max(arr) # 가장 오래걸리는 스태프를 기준으로 한 최대값

while start <= end: # 이진탐색 시작
    mid = int((start + end) / 2)
    balloon = 0
    for i in arr:
        balloon += int(mid/i)   # 중간값동안 만들 수 있는 풍선의 개수

    if balloon < m:   # 풍선의 개수가 필요한 풍선보다 작다면 시작 시간 증가
        start = mid + 1
    else:
        end = mid - 1   # 풍선의 개수가 필요한 풍선보다 크다면 끝 시간 감소
        

print(start)
