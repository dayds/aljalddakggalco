import sys
input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))

numList = [1]*num # 각자 본인을 수열로 가지므로 길이 1

for i in range(1, num): # 2번째부터 끝까지
  for j in range(i, num): # 현재 값에서 끝까지
    if arr[i] < arr[j]: # 현재 값에서 오른쪽에 있는 값보다 작다면
      numList[i] = max(numList[i], numList[j]+1) # 현재값의 수열과 오른쪽 값의 수열을 추가한 값 중 max값을 저장

print(max(numList)) # 저장된 수열 길이중 max값을 출력
