from bisect import bisect_left, bisect_right
import sys

n, m = map(int, sys.stdin.readline().split())     # n개의 네잎클로버, m개의 명령
x_aliens, y_aliens = {}, {}                       # X좌표 Y좌표가 들어갈 딕셔너리

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split()) # 네잎클로버의 좌표
    if x_aliens.get(x):                           # X좌표를 기준으로 Y좌표 저장
        x_aliens[x].append(y)
    else:
        x_aliens[x] = [y]

    if y_aliens.get(y):                           # Y좌표를 기준으로 X좌표 저장
        y_aliens[y].append(x)
    else:
        y_aliens[y] = [x]

commands = str(input())                           # 이동 명령어 input

for key, value in x_aliens.items():               # 순서대로 정렬
    x_aliens[key] = sorted(value)
for key, value in y_aliens.items():
    y_aliens[key] = sorted(value)

current_x, current_y = 0, 0
for command in commands:
    if command == "U":
        current_y = x_aliens[current_x][bisect_right(x_aliens[current_x], current_y)]
    elif command == "D":
        current_y = x_aliens[current_x][bisect_left(x_aliens[current_x], current_y) - 1]
    elif command == "R":
        current_x = y_aliens[current_y][bisect_right(y_aliens[current_y], current_x)]
    elif command == "L":
        current_x = y_aliens[current_y][bisect_left(y_aliens[current_y], current_x) - 1]

print(current_x, current_y)