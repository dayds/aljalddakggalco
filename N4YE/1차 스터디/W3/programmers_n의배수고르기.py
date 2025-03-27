'''
<문제 설명>
정수 n과 정수 배열 numlist가 매개변수로 주어질 때,
numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return
'''

def solution(n, numlist):
    answer = []

    for x in numlist:
        if x % n == 0:
            answer.append(x)

    return answer

# 모범답안?
## 1
# def solution(n, numlist):
    # return list(filter(lambda v: v%n==0, numlist))

## 2
# answer = [i for i in numlist if i%n==0]