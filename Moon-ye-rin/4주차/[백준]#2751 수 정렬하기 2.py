import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
arr = list(map(int, data[1:]))

# Python 내장 함수
arr.sort()

# 결과 출력
print(*arr, sep='\n')

'''
# 퀵 정렬
def quick_sort(array, start, end):
    if start >= end:   # 원소가 1개 이하면 종료
        return
    pivot = start   # 첫번째 원소를 피벗으로 설정
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1   # 왼쪽으로부터 피벗보다 큰 데이터를 찾을 때까지 이동
        while right > start and array[right] >= array[pivot]:
            right -= 1   # 끝에서부터 오른쪽으로 피벗보다 작은 데이터를 찾을 때까지 이동
        if left > right:   # 왼쪽과 오른쪽이 엇갈린다면
            array[right], array[pivot] = array[pivot], array[right]   # 피벗을 작은 데이터와 교체
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array,start,right-1)   #피벗 기준으로 분할 이후 왼쪽, 오른쪽 부분을 각각 정렬
    quick_sort(array,right+1, end)

quick_sort(arr,0,len(arr)-1)
print(*arr, sep='\n')
'''
