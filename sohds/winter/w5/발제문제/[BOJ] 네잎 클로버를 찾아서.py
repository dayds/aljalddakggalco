import sys
input = sys.stdin.readline 

from collections import defaultdict
# 파이썬 이진 탐색 라이브러리 (bisect)
from bisect import bisect_left, bisect_right   # left: 왼쪽 인덱스, right: 오른쪽 인덱스

# 네잎 클로버 개수, 외계인 전송 명령 수
n, m = map(int, input().split())

# 네잎 클로버 위치
dict_x = defaultdict(list)
dict_y = defaultdict(list)

# 네잎 클로버 위치 입력
for _ in range(n):
    x, y = map(int, input().split())
    dict_x[x].append(y)
    dict_y[y].append(x)

# 네잎 클로버 위치 정렬
for key in dict_x:
    dict_x[key].sort()
for key in dict_y:
    dict_y[key].sort()

# 외계인 전송 명령
cmds = input().rstrip()

# 외계인 전송 명령 실행
x = y = 0
for cmd in cmds:
    if cmd == "L":
        # 왼쪽으로 이동
        x = dict_y[y][bisect_left(dict_y[y], x) - 1]     # 배열 dict_y[y]의 정렬된 상태를 유지하면서 원소 x를 삽입할 수 있는 가장 왼쪽 인덱스를 리턴
    elif cmd == "R":
        # 오른쪽으로 이동
        x = dict_y[y][bisect_right(dict_y[y], x)]        # 배열 dict_y[y]의 정렬된 상태를 유지하면서 원소 x를 삽입할 수 있는 가장 오른쪽 인덱스를 리턴
    elif cmd == "U":
        # 위로 이동
        y = dict_x[x][bisect_right(dict_x[x], y)]         # 배열 dict_x[x]의 정렬된 상태를 유지하면서 원소 y를 삽입할 수 있는 가장 오른쪽 인덱스를 리턴
    elif cmd == "D":
            # 아래로 이동
            y = dict_x[x][bisect_left(dict_x[x], y) - 1]  # 배열 dict_x[x]의 정렬된 상태를 유지하면서 원소 y를 삽입할 수 있는 가장 왼쪽 인덱스를 리턴

print(x, y)