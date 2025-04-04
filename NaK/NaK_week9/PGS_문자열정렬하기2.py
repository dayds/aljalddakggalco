def solution(my_string):
    return ''.join(sorted(my_string.lower()))


# 다른 사람의 풀이(정석 풀어쓰기)
def solution(my_string):
    answer = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            answer.append(chr(ord(i)+32))
        else:
            answer.append(i)
    return ''.join(sorted(answer))