# 변수 입력
N,K = map(int, input().split())
chocolate = list(map(int, input().split()))

day = 0
cho_count = 0

# 초콜릿 병 개수만큼 반복
for i in range(1, len(chocolate)):

    # 해당 초콜릿 병의 개수가 그 전 병의 개수보다 클 때
    if chocolate[i] > chocolate[i-1]:

        # 두 병의 초콜릿 개수가 같아질 때까지
        while chocolate[i] > chocolate[i-1]:
            chocolate[i] -= 1
            cho_count += 1
        day += 1

print(cho_count,day)


## 성공!