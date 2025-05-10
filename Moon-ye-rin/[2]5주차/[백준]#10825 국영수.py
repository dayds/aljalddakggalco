import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

# 숫자형 요소 int로 변환
arr = [(name, int(kor), int(eng), int(math)) for name, kor, eng, math in arr]

# 정렬: 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순
sort_list = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름만 출력
for i in sort_list:
    print(i[0])
