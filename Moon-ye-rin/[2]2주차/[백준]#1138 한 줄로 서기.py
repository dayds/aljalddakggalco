import sys

# 입력 받기
input = sys.stdin.read
data = input().strip().splitlines()

n = int(data[0])
arr = list(map(int, data[1].split()))

# 정답 리스트 초기화
answer = [0] * n  

# 키가 작은 사람부터 배치
for i in range(n):
    count = arr[i]  # 왼쪽에 있어야 하는 큰 사람 수
    idx = 0  

    # count만큼 빈 자리(0)를 찾아야 함
    while count > 0 or answer[idx] != 0:
        if answer[idx] == 0:  # 빈 자리일 때만 count 감소
            count -= 1
        idx += 1

    answer[idx] = i + 1  # 키가 i+1인 사람 배치

print(*answer, sep='\n')
