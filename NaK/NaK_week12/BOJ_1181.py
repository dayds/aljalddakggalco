# 첫째 줄에 단어의 개수 N
# 길이가 짧은 것부터, 길이가 같으면 사전 순으로
# 중복은 제거
# 길이는 len 사용?
# 정렬 뭐 쓰지.. 삽입? 퀵?
## word 길이로 정렬해야 하는데 퀵으로 어떻게 쓸지 잘 모르겠음...

# 입력 받기
N = int(input())
word = []

# 중복 제거하고 리스트 저장
for _ in range(N):
    w = input()
    if w not in word:
        word.append(w)

# 정렬 시작 ><
for i in range(1,len(word)):
    for j in range(i,0,-1):

        if (len(word[j]) < len(word[j-1]) # 길이로
                or (len(word[j]) == len(word[j-1]) and word[j] < word[j-1])): # 사전 순으로
            word[j], word[j - 1] = word[j - 1], word[j]

        else:
            break

for k in word:
    print(k)


# 시간초과 발생
# 수정해도 시간초과 발생

# 지피티가 알려준 코드
N = int(input())
words = {input() for _ in range(N)}  # set으로 중복 제거
sorted_words = sorted(words, key=lambda x: (len(x), x))
print('\n'.join(sorted_words))

# 파이썬 내장 함수가 좋긴하구나...
# 나는야 빡대가뤼

# 다른 사람은 알파벳으로 정렬(sort)하고 길이로 정렬(sort(key=len)했는데 왜 난 반대로할 생각을 못했을까...