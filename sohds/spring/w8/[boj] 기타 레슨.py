import sys
input = sys.stdin.readline

def divide_lesson(n, m, lesson):
    start, end = max(lesson), sum(lesson)
    answer = 0

    while start <= end:
        mid = (start + end) // 2
        total, cnt = 0, 1
        for i in lesson:
            if total + i > mid:
                cnt += 1
                total = 0
            total += i

        if cnt <= m:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer


n, m = map(int, input().split())
lesson = list(map(int, input().split()))

print(divide_lesson(n, m, lesson))







