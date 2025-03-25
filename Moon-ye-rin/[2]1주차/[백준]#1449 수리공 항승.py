import sys

# 입력 받기
input = sys.stdin.read
data = input().strip().splitlines()

n, l = map(int, data[0].split())
arr = list(map(int, data[1].split()))
# 리스트 오름차순 정렬
arr.sort()
count = 1
start = arr[0]  # 첫 번째 구멍 위치

for i in arr[1:]:
    # 현재 테이프의 범위를 넘어가는 경우 (테이프가 덮을 수 없는 위치가 나왔을 때)
    if i >= start + l:
        count += 1  # 새로운 테이프 사용
        start = i  # 새로운 테이프의 시작 위치

print(count)
