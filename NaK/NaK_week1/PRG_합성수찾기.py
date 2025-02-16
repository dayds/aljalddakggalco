# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다.
# 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []

    # n값들을 2개씩 모아서 합성수인지 확인
    for i in range(1, n + 1):
        divisors = []

        for j in range(1, i + 1):

            # 해당 값을 그보다 작은 수로 나누었을 때 나머지가 0인 것들은 모두 약수
            if i % j == 0:
                divisors.append(j)

        # 약수가 3개 이상인 값들은 합성수
        if len(divisors) >= 3:
            answer.append(i)

    return len(answer)


## 성공!