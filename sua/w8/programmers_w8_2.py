def solution(my_string, num1, num2):
    a = list(map(str,my_string))
    b = a[num1]
    a[num1] = a[num2]
    a[num2] = b
    return ''.join(a) 