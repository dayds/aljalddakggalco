L = list(map(int, input().split()))
N,K,A,B = L[0],L[1],L[2],L[3]

plant = [K]*N
day = 0

while 0 not in plant:
    for i in range(A):
        plant[i] += B

    for i in range(len(plant)):
        plant[i] -= 1

    plant.sort()
    day += 1

print(day)