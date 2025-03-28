def solution(quiz):
    answer = []
    for i in quiz:
        i = i.replace("=", "==")

        if eval(i) == True:
            answer.append("O")
        else:
            answer.append("X")

    return answer