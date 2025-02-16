# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    max_number = []

    for i in numbers:
        for j in numbers:
            # 매개변수의 2개의 값들을 한번씩 곱하여 리스트로 나열
            max_number.append(i * j)

    # 리스트 정렬
    max_number.sort()

    # 매개변수 중 최대값을 두번 곱하는 중복값은 제외하기 때문에 뒤에서 두번째 수가 가장 큰 값
    return max_number[-2]


## 성공!