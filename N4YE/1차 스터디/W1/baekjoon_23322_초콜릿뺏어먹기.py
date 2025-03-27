'''
N 초콜릿 통 개수
K ... (i-K)라는걸 이해 못함
chocolate 초콜릿 통 배열
'''

'''
def solution(N, K, chocolate):
    count = 0  # 최대 초콜릿
    day = 0    # 최소 날짜
    min_choco = min(chocolate)  # 초콜릿 개수 기준값

    for i in range(N):
        if chocolate[i] > min_choco:  # 초콜릿이 기준 값보다 많을 경우
            count += (chocolate[i] - min_choco)  # 초콜릿 냠냠
            chocolate[i] = min_choco  # 냠냠 -> 최소 개수
            day += 1  # 하루 종료!

    return count, day

print(solution(4, 2, [1,2,2,3]))  # 4, 3
print(solution(2, 1, [5, 5]))     # 0, 0
'''

N, K = map(int, input().split())
chocolate = list(map(int, input().split()))

count = 0  # 최대 초콜릿
day = 0    # 최소 날짜
min_choco = min(chocolate)  # 초콜릿 개수 기준값

for i in range(N):
    if chocolate[i] > min_choco:  # 초콜릿이 기준 값보다 많을 경우
        count += (chocolate[i] - min_choco)  # 초콜릿 냠냠
        chocolate[i] = min_choco  # 냠냠 -> 최소 개수
        day += 1  # 하루 종료!

print(count, day)