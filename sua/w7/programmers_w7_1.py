def solution(array, n):
    answer = []

    dict = {}
    for i in array:
        dict[i] = abs(i-n)

    print(dict)

    dic_min = min(dict.values())
    print(dic_min)

    for key,value in dict.items():
        if value == dic_min:
            answer.append(key)
    return min(answer)