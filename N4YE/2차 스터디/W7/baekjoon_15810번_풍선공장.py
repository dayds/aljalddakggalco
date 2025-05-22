import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))

start, end = 0, max(time)*m                 # 최소시간, 최대시간
res = 0
while start <= end:
    middle = (start + end)//2
    if sum([middle//n for n in time]) >= m: # 모든 staff가 부는 풍선 수의 합 >= m 이면
        res = middle                        # 후보값 갱신
        end = middle-1                      # 더 적은 시간 확인
    else:
        start = middle+1                    # 실패 : 더 많은 시간 확인
print(res)