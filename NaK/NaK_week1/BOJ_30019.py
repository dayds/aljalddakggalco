# 입력받은 변수 저장
N,M = map(int, input().split())

room = {}

# 입력되는 예약 건수 만큼 반복
for i in range(M):
    # 예약 건수는 리스트로 저장
    x = list(map(int, input().split()))

    # 딕셔너리에 룸넘버가 저장이 안 된 경우(룸이 비어있는 경우)
    if x[0] not in room:
        room[x[0]] = [x[1],x[2]] # 딕셔너리에 예약 확정된 것 저장
        print('YES')

    # 룸이 차있는 경우
    else:
        # 예약 시작 시간이 같은 룸에 마지막으로 저장된 예약 마지막 시간보다 큰 경우(예약이 불가한 경우)
        if room[x[0]][1] > x[1]:
            print('NO')

        # 예약이 가능한 경우
        else:
            room[x[0]] = [x[1],x[2]] # 딕셔너리에 예약 확정된 것 저장
            print('YES')


## 파이참에서 출력은 잘 되는데 문제 제출 후 런타임 에러가 남..