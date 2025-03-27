'''
N 강의실 번호
M 예약 요청 횟수
s e 예약 시작과 끝
'''
# 모르겠어서 답변 서치해서 공부했습니다!

N, M = map(int, input().split())

dic = {}
for _ in range(M):
    x = list(map(int, input().split()))
    if x[0] not in dic:               # 강의실 번호(N)가 key값
        dic[x[0]] = [x[1], x[2]]      # 예약시간(s,e) 입력
        print('YES')

    else:
        if dic[x[0]][1] > x[1]:       # 강의실 번호(N)의 끝시간(e)이 새로운 시작시간(s)보다 클때
            print('NO')               # 예약 불가
        else:
            dic[x[0]] = [x[1], x[2]]  # 작거나 같을 때
            print('YES')              # 예약 가능