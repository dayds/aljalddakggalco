import sys
input = sys.stdin.readline

def binary_search(left, right, target): #이진탐색 함수 구현
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

test_case = int(input())

for tc in range(1, test_case+1): # 케이스 개수만큼 for문 실행
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    lis = [numbers[0]] # 첫 번째 숫자를 초기값으로 설정
    for i in range(1, N): 
        if lis[-1] < numbers[i]: # 현재보다 이전이 더 작다면(현재가 더 크다면)
            lis.append(numbers[i]) # 조건을 만족하므로 추가
        else:
            j = binary_search(0, len(lis)-1, numbers[i]) # 현재 숫자가 lis에 적절한 위치에 들어가도록 이진 탐색 수행
            lis[j] = numbers[i] # 해당 위치의 값을 현재 숫자로 교체

    print('Case #{}'.format(tc))
    if len(lis) >= K: # 길이가 K 이상이면 1 출력 , 아니면 0 출력
        print(1)
    else:
        print(0)
