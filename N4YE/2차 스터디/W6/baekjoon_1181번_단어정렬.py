'''
import sys
input = sys.stdin.readline   #input 함수 덮어쓰기

N = int(input().strip())
word = [input().strip() for _ in range(N)]
word = sorted(list(set(word)))
word.sort(key=len)

for x in word :
    print(x)
'''

import sys
input = sys.stdin.readline

N = int(input())
words = {input().strip() for _ in range(N)}
sorted_words = sorted(words, key=lambda x: (len(x), x))

print('\n'.join(sorted_words))
