def find_AB(D, K):
    # Step 1: 피보나치 계수 구하기
    fib = [0] * (D + 1)
    fib[1], fib[2] = 1, 1  # 기본 피보나치 수열 초기값

    for i in range(3, D + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    c1, c2 = fib[D - 2], fib[D - 1]  # 계수 찾기

    # Step 2: A와 B 찾기
    for A in range(1, K // c1 + 1):  # A의 가능한 범위 탐색
        if (K - c1 * A) % c2 == 0:  # B가 자연수인지 확인
            B = (K - c1 * A) // c2
            if A <= B:  # A ≤ B 조건 확인
                print(A)
                print(B)
                return

# 예제 입력
D, K = map(int, input().split())
find_AB(D, K)
