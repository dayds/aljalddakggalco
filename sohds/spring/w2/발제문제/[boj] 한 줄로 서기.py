import sys
input = sys.stdin.readline

def line_up(n, line):
    result = [0] * n
    
    for i in range(n):
        # 현재 사람의 왼쪽에 서야 하는 빈 자리의 개수를 카운트
        cnt = 0
        # 0번 위치부터 n-1번 위치까지 순회하면서 적절한 위치를 찾음
        for j in range(n):
            # 만약 현재까지 세었던 빈 자리의 개수가 line[i]와 같고
            # 해당 위치가 아직 비어있다면(0이라면)
            # i+1번 사람을 그 위치에 배치
            if cnt == line[i] and result[j] == 0:
                result[j] = i + 1
                break
            # 아직 적절한 위치를 찾지 못했고, 현재 위치가 비어있다면
            # 빈 자리 카운트를 증가
            elif result[j] == 0:
                cnt += 1
    return result

n = int(input())
line = list(map(int, input().split()))

# 출력 (*를 사용하면 리스트의 대괄호 []를 제거하고 각 요소를 공백으로 구분하여 출력함)
print(*line_up(n, line))
