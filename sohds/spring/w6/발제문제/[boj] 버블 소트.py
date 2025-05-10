import sys
input = sys.stdin.readline

def merge_sort(n, arr):
    answer = 0
    
    def merge(start, end):
        nonlocal answer
        if start >= end:
            return
            
        mid = (start + end) // 2
        merge(start, mid)
        merge(mid + 1, end)
        
        temp = []
        x, y = start, mid + 1
        
        while x <= mid and y <= end:
            if arr[x] <= arr[y]:
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])
                y += 1
                answer += (mid - x) + 1
                
        if x <= mid:
            temp.extend(arr[x:mid + 1])
        if y <= end:
            temp.extend(arr[y:end + 1])
            
        for i in range(len(temp)):
            arr[start + i] = temp[i]
    
    merge(0, n-1)
    return answer

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(merge_sort(n, arr))
