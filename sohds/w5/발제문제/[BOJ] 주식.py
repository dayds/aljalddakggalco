import sys
input = sys.stdin.readline

# 이분 탐색
def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# 테스트 케이스 개수
t = int(input())

# 테스트 케이스 처리
for case in range(1, t+1):
    # 날짜 수, 거래 횟수
    n, k = map(int, input().split())
    # 주식 가격
    stock = list(map(int, input().split()))
    # 실제로 주식을 구매한 가격들을 저장
    ls = [stock[0]]
    
    # 주식 가격 처리
    for i in range(1, n):
        if ls[-1] < stock[i]:
            ls.append(stock[i])
        else:
            pos = binary_search(0, len(ls)-1, stock[i])
            ls[pos] = stock[i]
    
    print(f"Case #{case}")
    print(1 if len(ls) >= k else 0)