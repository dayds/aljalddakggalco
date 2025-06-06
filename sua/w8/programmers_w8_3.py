def solution(s):
    dic = {}
    answer = ''
    for i in s:
        if i in dic:
            dic[i] = dic[i] +1
        else:
            dic[i] =1
    for key in dic.keys():
        if dic[key] ==1:
            answer += key
    return ''.join(sorted(list(answer)))