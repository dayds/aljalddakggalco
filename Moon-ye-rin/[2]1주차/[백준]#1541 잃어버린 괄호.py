import sys

# 입력 받기
input = sys.stdin.read
data = input().strip().splitlines()

arr = data[0].split('-')  # 마이너스기호를 기준으로 분리

# 리스트의 모든 요소를 정수(int)로 변환하여 저장
for i in range(len(arr)):
    if '+' in arr[i]:
        arr[i] = sum(map(int, arr[i].split('+')))  # + 연산을 수행한 값 저장
    else:
        arr[i] = int(arr[i])  # 단일 숫자도 int로 변환

# 첫 번째 값을 기준으로 빼기 연산 수행
answer = arr[0]
for j in range(1, len(arr)):
    answer -= arr[j]

print(answer)
