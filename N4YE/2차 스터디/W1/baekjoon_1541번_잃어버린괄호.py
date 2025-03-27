import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

text = input().strip()
arr = text.split('-')

for x in range(len(arr)) :
    if '+' in arr[x] :
        arr[x] = sum(map(int, arr[x].split('+')))
    else :
        arr[x] = int(arr[x])

answer = arr[0]
for x in range(1,len(arr)) :
    answer -= arr[x]
print(answer)

