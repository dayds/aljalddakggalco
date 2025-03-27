'''
<문제설명>
다솜이는 기호 1번이다.
다솜이는 사람들의 마음을 읽어서 자신을 찍지 않으려는 사람을 돈으로 매수해서 국회의원에 당선이 되게 하려고 한다.
다른 모든 사람의 득표수보다 많은 득표수를 가질 때, 그 사람이 국회의원에 당선된다.
다솜이가 매수해야하는 사람의 최솟값을 출력하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input())
candidate = []
count = 0

for i in range(N) :
    candidate.append(int(input()))
git
if len(candidate) != 1 :                                       #후보자가 1명이 아닐 때 / go
    if candidate.count(max(candidate)) == len(candidate) :     #모두 같은 값일 때 / 1번
        count = 1
    else:
        while max(candidate) > candidate[0] :                  #1번 후보가 max보다 작으면 / go
            candidate[candidate.index(max(candidate))] -= 1
            candidate[0] += 1
            count += 1

        if candidate.count(max(candidate)) != 1:               #최대값이 같아졌을 경우 한번 더 go
            count += 1

print(count)
