import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

while start <= end:
  mid = (start + end) // 2 

  total = 0 # 저장하려는 분 수 
  count = 1 # 나뉘어지는 블루레이 개수
  
  # 블루레이 개수 구하기
  for t in arr:
    # 분 수가 mid보다 커지면 블루레이 개수 추가 및 분 수 초기화
    if total + t > mid:
      count += 1
      total = 0
    total += t   # 아니라면 순서대로 분 수 더함

  # 블루레이 개수가 m 보다 작거나 같다면
  if count <= m:
    bluray = mid   # 답에 mid값을 저장해두고 크기를 줄임
    end = mid - 1
  else:
    start = mid + 1 # 크기를 늘림
    
print(bluray)
