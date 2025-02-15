'''
<문제 설명>
정수 num과 k가 매개변수로 주어질 때,
num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고
없으면 -1을 return
'''

def solution(num, k):
    anwer = 0
    num = list(str(num))

    if str(k) in num:
        answer = num.index(str(k)) + 1
    else:
        answer = -1

    return answer

# 모범답안?
# def solution(num, k):
    # for i, n in enumerate(str(num)):
        # if str(k) == n:
            # return i + 1
    # return -1
