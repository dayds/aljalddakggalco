# 효율 극악
def solution(s):
    answer = ''
    temp = ''
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 
               'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9'}
    
    for char in s:
        if temp in list(numbers.values()):
            answer += numbers[temp]
            temp = ''
            
        if str.isdigit(char) == True:
            answer += char
            
        elif str.isdigit(char) == False:
            temp += char

    return int(answer)

# 효율적으로!
def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 
           'four': '4', 'five': '5', 'six': '6', 'seven': '7', 
           'eight': '8', 'nine': '9'}
    for key in dic:
        s = s.replace(key, dic[key])
    return int(s)