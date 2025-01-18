'''
<문제설명>
문자열 s가 매개변수.
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return.
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return.
'''

def solution(s):
    answer = []
    alphabet = list(set(s))

    for i in alphabet:
        if s.count(i) == 1:
            answer.append(i)
    return ''.join(sorted(answer))

print(solution("abcabcadc"))  # "d"
print(solution("abdc"))       # "abcd"
print(solution("hello"))      # "eho"

# 모범답안? - 이렇게까지 코드를 줄여쓸 수 있군..
# answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
