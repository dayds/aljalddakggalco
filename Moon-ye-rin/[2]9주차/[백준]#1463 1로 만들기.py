import sys
input = sys.stdin.readline

num = int(input())

arr = [0]*(num+1) # 최소 연산 횟수를 저장할 리스트

for i in range(2, num+1):
  arr[i] = arr[i-1] +1 # 1을 빼는 경우(이전연산횟수에 +1)
  if i%2 ==0:
    # 2로 나눌 수 있는 경우
    arr[i] = min(arr[i], arr[i//2]+1) # 최소 연산 횟수 비교(2로 나눈 몫의 최소 연산 횟수에 +1)
  if i%3 == 0:
    # 3으로 나눌 수 있는 경우
    arr[i] = min(arr[i], arr[i//3]+1) # 3으로 나눈 몫의 최소 연산 횟수에 +1

print(arr[num])
