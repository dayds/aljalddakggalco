'''
#1차 시도

import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
list_num = list(map(int, input().split()))
sorted_num = sorted(list_num)
answer = 0

while True :
    if list_num == sorted_num :
        break
    else :
        for i in range(len(list_num)-1) :
            if list_num[i] > list_num[i+1] :
                list_num[i], list_num[i+1] = list_num[i+1], list_num[i]
                answer += 1
            else :
                continue

print(answer)
'''


'''
#2차 시도

import sys
input = sys.stdin.readline

N = int(input().strip())
nums  = list(map(int, input().split()))
answer = 0

for i in range(N):
    swapped = False
    for j in range(N - 1 - i):   #맨뒤=최대값/ 탐색범위 좁히기
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            answer += 1
            swapped = True
    if not swapped:              #swap 발생 없을시 그대로 종료
        break

print(answer)
'''


import sys
input = sys.stdin.readline

def merge_sort(start, end):               # merge sort(병합 정렬)
    global answer, arr

    if start < end:
        mid = (start + end) // 2          # mid 설정 후 앞/뒤 나누기
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        temp = []
        x, y = start, mid + 1             # 앞(x)/뒤(y)의 시작 값 지정

        while x <= mid and y <= end:
            if arr[x] <= arr[y]:          # 뒤가 클때는 temp에 앞을 저장
                temp.append(arr[x])
                x += 1
            else:
                temp.append(arr[y])      # 앞이 클때는 역순쌍 발생
                y += 1
                answer += (mid - x) + 1  # ㄴ앞의 길이만큼 수행 횟수 추가

        if x <= mid:                     # 남은게 있으면 temp에 추가
            temp = temp + arr[x:mid + 1]
        if y <= end:
            temp = temp + arr[y:end + 1]
        for i in range(len(temp)):       # 병합된 temp를 arr에 복사
            arr[start + i] = temp[i]

n = int(input())
arr = list(map(int, input().split()))
answer = 0
merge_sort(0, n - 1)

print(answer)