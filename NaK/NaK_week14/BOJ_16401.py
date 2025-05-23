# 모든 조카가 과자를 받도록 할 수 있는 최대 길이 구하기
# 이걸 이진탐색으로 어케 나눔?

# start = 1 (가장 짧은 가능한 길이), end = max(cookie) (가장 긴 과자의 길이)
# mid 길이로 잘랐을 때 나오는 조각 수 합: count
# 조각 수(count)와 조카 수 비교
# mid 길이로 자르면 조각 수가 조카 수보다 많거나 딱 맞음
# -> 길이 늘릴 수 있음 (start = mid + 1)
# mid 길이로 자르면 조각 수가 조카 수를 못 채움
# -> 길이 줄이기 (end = mid -1)


M, N = map(int, input().split())
cookie = list(map(int, input().split()))

start = 1
end = max(cookie)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(c // mid for c in cookie)

    if count >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)


# 다른 사람의 플로우를 참고하여 코드 작성해보았다.
# 이번에는 코드가 진행하는 과정을 노트에 적어가며 직접 계산 했는데 이해가 잘 되고 풀이도 쉽게 되었다.
# 앞으로 이런 방식으로 코드 풀이를 하면 좋을 것 같다.
# https://velog.io/@kmh9250/%EB%B0%B1%EC%A4%8016401-%EA%B3%BC%EC%9E%90-%EB%82%98%EB%88%A0%EC%A3%BC%EA%B8%B0