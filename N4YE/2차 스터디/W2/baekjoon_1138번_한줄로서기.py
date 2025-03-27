import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
index = list(map(int, input().split()))
people = [i+1 for i in range(N)]
answer = []

x = -1
for i in range(N) :
    answer.insert(index[x], people[x])
    x -= 1

for i in answer:
    print(i , end = ' ')