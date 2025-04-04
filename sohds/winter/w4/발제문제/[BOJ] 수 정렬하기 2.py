import sys

# 입력
n = int(sys.stdin.readline())
arr = []

# 입력받은 수를 배열에 저장
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 출력(1) - 파이썬 내장함수 사용
for i in sorted(arr):
    print(i)

# ==============================================

# 출력(2) - 정렬 함수 직접 구현 (병합 정렬)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # 분할
    # 재귀 호출로 분할 진행
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 병합
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    # 두 배열의 원소를 비교하여 작은 원소를 결과 배열에 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 남은 원소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 정렬된 배열 출력
sorted_arr = merge_sort(arr)
for i in sorted_arr:
    print(i)
