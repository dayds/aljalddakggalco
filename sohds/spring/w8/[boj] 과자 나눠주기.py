import sys
input = sys.stdin.readline

def divide_snacks(m, n, snack):
    start, end = 1, max(snack)
    answer = 0
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in snack:
            if i < mid:
                continue
            else:
                cnt += i // mid
        if cnt >= m:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    
    return answer

# 입력 받기
m, n = map(int, input().split())
snack = list(map(int, input().split()))

# 결과 출력
print(divide_snacks(m, n, snack))
