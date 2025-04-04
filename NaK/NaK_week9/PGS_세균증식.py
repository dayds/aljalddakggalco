def solution(n, t):
    for i in range(t):
        n *= 2
    return n


# for문 제외
def solution(n, t):
    return n*(2**t)


# 비트연산
def solution(n, t):
    return n << t