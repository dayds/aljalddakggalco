# 처음 시간 초과 버전
# 약수의 개수를 저렇게 구하면, 시간 복잡도가 O(N)이 되기 때문에 시간초과로 통과할 수가 없음
def solution(number, limit, power):
    answer = 0
    f = [1] * number
    for i in range(2, 1+number):
        for factor in range(2, i+1):
            if i % factor == 0:
                f[i-1] = f[i-1]+1
                if f[i-1] > limit:
                    f[i-1] = power
    return sum(f)

# 약수의 개수를 구하는 함수 - 제곱근 사용해서 진행
def solution(number, limit, power):
    # 각 숫자의 약수의 개수를 계산하는 함수
    def divisor_count(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                # 제곱근이 정수인 경우
                if i == (n // i):
                    count += 1
                # 제곱근이 정수가 아닌 경우
                else:
                    count += 2
        return count

    answer = 0
    for i in range(1, number + 1):
        weapon_power = divisor_count(i)
        if weapon_power > limit:
            answer += power
        else:
            answer += weapon_power
            
    return answer