# N개의 수로 이루어진 수열
# 병합정렬
# swap의 count

# 입력 받기
N = int(input())
arr = list(map(int,input().split()))

# swap count
k = 0

def merge(left, right):
    sorted_list = []
    i, j = 0, 0

    global k

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            k += len(left)-i

    # 남은 값들을 삽입한다.
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

merge_sort(arr)
print(k)