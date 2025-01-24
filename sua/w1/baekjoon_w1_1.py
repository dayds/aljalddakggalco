def take_away_chocolate(chocolate):
    day = 0
    cnt = 0
    min_chocolate_cnt = min(chocolate)
    for i in range(1, len(chocolate)):
        if chocolate[i - 1] <= chocolate[i] and min_chocolate_cnt < chocolate[i]:
            while chocolate[i] > chocolate[i - 1]:
                chocolate[i] -= 1
                cnt += 1
            day += 1

    print(cnt, day)


n, k = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
take_away_chocolate(sorted(arr))
