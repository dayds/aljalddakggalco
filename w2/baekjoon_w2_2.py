n = int(input())


dasom_votes = int(input())


other_votes = [int(input()) for _ in range(n-1)]


if n == 1:
    print(0)
    exit()

buy_count = 0

while dasom_votes <= max(other_votes):
    max_index = other_votes.index(max(other_votes))
    
    other_votes[max_index] -= 1
    dasom_votes += 1
    
    buy_count += 1

# 결과 출력
print(buy_count)
