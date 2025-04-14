def water(n, k, a, b):
    pot = [k] * n
    day = 0  # 물을 준 날짜
    
    # 모든 캣닢이 죽지 않았다면 물 주기
    while min(pot) > 0:
        # 연속된 a개의 화분이 수분 b개 만큼 증가
        for i in range(a):
            pot[i] += b
        # 모든 화분의 수분은 1씩 매일 감소
        for i in range(n):
            pot[i] -= 1
        # 수분이 작은 순서대로 화분을 오름차순 정렬
        pot.sort()
        # 물을 준 날짜 추가가
        day += 1
        
    return day

n, k, a, b = map(int, input().split())
print(water(n, k, a, b))
        
