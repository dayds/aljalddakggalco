import sys

T = int(sys.stdin.readline())
answer = []

for i in range(T):
    n = int(sys.stdin.readline())
    sum_number = []

    for j in range(1,n+1):

        if j == 1:
            sum_number.append(1)

        elif j == 2:
            sum_number.append(2)

        elif j == 3:
            sum_number.append(4)

        else:
            sum_number.append(sum_number[j-4] + sum_number[j-3] + sum_number[j-2])

    answer.append(sum_number[-1])

for k in range(T):
    print(answer[k])

# ------------------------------------------------------
import sys

T = int(sys.stdin.readline())
answer = []

for i in range(T):

    n = int(sys.stdin.readline())

    dp = [0] * (n+1)

    for j in range(1,n+1):

        if j == 1:
            dp[j] = 1

        elif j == 2:
            dp[j] = 2

        elif j == 3:
            dp[j] = 4

        else:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    answer.append(dp[n])

for k in range(T):
    print(answer[k])