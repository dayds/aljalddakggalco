def solution(n):
    answer = 1
    f = 1
    while f <= n:
        answer += 1
        f = f *answer
    answer = answer -1
    return answer