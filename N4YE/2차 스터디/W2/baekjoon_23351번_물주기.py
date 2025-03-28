import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N, K, A, B = map(int, input().split())

plant = [K for _ in range(N)]
day = 0

while True :
    plant.sort()
    for i in range(A) :
        plant[i] = plant[i] + B
    for x in range(N) :
        plant[x] = plant[x] - 1
    day += 1

    if 0 in plant :
        break
    else :
        continue

print(day)

