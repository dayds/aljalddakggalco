# 테스트 케이스 입력: T
# A의 수: N, B의 수: M 입력
# A의 크기 입력 -> 리스트: Asize
# B의 크기 입력 -> 리스트: Bsize

# for문으로 Asize 개수만큼 돌리고 Bsize의 각 값들과 하나씩 비교
# -> 이진탐색, 중간점 탐색소거 방식으로 변경

# A가 B보다 큰 쌍의 개수 출력

# 테스트 케이스 개수
T = int(input())

answer = []

# N과 M의 수
for _ in range(T):
    N,M = map(int,input().split())

    # A.B의 크기 입력
    Asize = list(map(int, input().split()))
    Bsize = list(map(int, input().split()))

    # A와 B의 크기 비교
    count = 0

    for i in Asize:
        for j in Bsize:
            if i > j:
                count += 1

    answer.append(count)

for k in answer:
    print(k)

# 시간 초과...


# 모듈 사용한 이진탐색
import bisect

# 테스트 케이스 개수
T = int(input())

answer = []

for _ in range(T):
    N, M = map(int, input().split())
    Asize = list(map(int, input().split()))
    Bsize = list(map(int, input().split()))

    # B 정렬 (이진 탐색을 위해)
    Bsize.sort()

    count = 0

    for a in Asize:
        # bisect_left: B에서 a보다 작은 원소 개수 찾기
        count += bisect.bisect_left(Bsize, a)

    answer.append(count)

for k in answer:
    print(k)


# 모듈 없이 이진탐색
# lower_bound 함수 정의
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# 테스트 케이스 개수
T = int(input())

answer = []

for _ in range(T):
    N, M = map(int, input().split())
    Asize = list(map(int, input().split()))
    Bsize = list(map(int, input().split()))

    Bsize.sort()  # 이진 탐색을 위한 정렬

    count = 0

    for a in Asize:
        count += lower_bound(Bsize, a)

    answer.append(count)

# 출력
for k in answer:
    print(k)


# 확실히 모듈을 사용하는 것이 코드가 더 간결하고 속도도 빨랐다.