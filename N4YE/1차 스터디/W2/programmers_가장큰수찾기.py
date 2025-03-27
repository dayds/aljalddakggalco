'''
<문제 설명>
정수 배열 array가 매개변수로 주어질 때,
가장 큰 수와 그 수의 인덱스를 담은 배열을 return
'''

def solution(array):
    answer = [0]
    for i in array :
        if i > answer[0] :
            answer[0] = i
    answer.append(array.index(answer[0]))
    return answer

# 모범답안?
# return [max(array), array.index(max(array))]

