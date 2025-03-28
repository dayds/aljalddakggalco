n = int(input())
length = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if result[j] == 0:
            if count == length[i]:
                result[j] = i+1
                break
            count +=1
print(" ".join(map(str, result)))