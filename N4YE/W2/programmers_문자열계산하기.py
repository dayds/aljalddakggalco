'''
<문제 설명>
my_string은 "3 + 5"처럼 문자열로 된 수식입니다.
문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return
'''

def solution(my_string):
    answer = eval(my_string)
    return answer

'''
# 모범답안
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
'''

