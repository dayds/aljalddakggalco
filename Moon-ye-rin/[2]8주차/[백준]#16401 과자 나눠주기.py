import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, m):
  start = 1
  end = max(arr)
  result = 0 # 결과 값 저장 변수

  # 이진탐색 시작
  while start <= end:
    mid = (start + end) // 2
    snack = 0

    # 과자 개수 구하기
    for i in arr:
      snack += i // mid  # 가능한 개수를 모두 구함

    if snack >= m:
      result = mid  # 가능한 경우 저장
      start = mid + 1  # 더 긴 길이로 시도
    else:
      end = mid - 1  # 부족하면 더 짧은 길이로
  return result

print(binary_search(arr, m))
