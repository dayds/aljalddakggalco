'''
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
'''

def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)) :
        answer += int(n[i])
    return answer


# 모범답안
# return sum(int(i) for i in str(n))