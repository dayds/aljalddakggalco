import sys
input = sys.stdin.readline

n = int(input())

def word_sort(n, words):
    words = list(set(words))
    words.sort()
    words.sort(key=len)
    return words

words = [input().strip() for _ in range(n)]
words = word_sort(n, words)

print(*words, sep='\n')
