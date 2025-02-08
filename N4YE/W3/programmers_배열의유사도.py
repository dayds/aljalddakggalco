'''
<문제 설명>
두 배열이 얼마나 유사한지 확인해보려고 합니다.
문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return
'''

def solution(s1, s2):
    answer = 0

    for i in s1:
        if i in s2:
            answer += 1
    return answer

# 모범답안?
# def solution(s1, s2) :
# return len(set(s1)&set(s2));
