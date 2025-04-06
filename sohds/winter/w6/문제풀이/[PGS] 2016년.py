def solution(a, b):

    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diff = b-1
    for idx in range(a-1):
        diff += month[idx]

    return date[diff % 7]
