import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())
arr = [list(map(int, line.split())) for line in data[1:]]

room = [None] * n  # 방 상태 초기화
result = []

for i in arr:
    room_num, start, end = i[0] - 1, i[1], i[2]
    if room[room_num] is None or room[room_num][1] <= start:
        room[room_num] = (start, end)
        result.append("YES")
    else:
        result.append("NO")

print("\n".join(result))
