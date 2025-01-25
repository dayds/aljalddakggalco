import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
arr = [int(line) for line in data[1:]]
count = 0

while max(arr) != arr[0] or arr.count(arr[0]) > 1:  # 첫 번째 요소가 최대값이고 유일할 때까지 반복
    second = arr[1:]
    second_max = max(second)
    second_max_index = second.index(second_max) + 1
    arr[second_max_index] -= 1
    arr[0] += 1
    count += 1

print(count)
