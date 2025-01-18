'''
<문제 설명>
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return.
'''

def solution(my_string, num1, num2):
    answer = list(my_string)

    answer[num1] = my_string[num2]
    answer[num2] = my_string[num1]

    return ''.join(answer)

print(solution("hello", 1, 2))	     #"hlelo"
print(solution("I love you", 3, 6))  #"I l veoyou"