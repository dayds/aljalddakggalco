'''
<문제설명>
상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다.
이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다.
로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input())
system_log = {}

for _ in range(N) :
    name, TF_log = map(str, input().split())
    system_log[name] = TF_log

    if TF_log == 'leave' :   #퇴근하면 이름 삭제
        del system_log[name]

for k in sorted(system_log.keys(), reverse=True):
    print(k)