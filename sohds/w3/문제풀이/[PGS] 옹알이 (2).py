def solution(babbling):
    answer = 0
    say = ['aya', 'ye', 'woo', 'ma']
    
    for bab in babbling:  # babbling의 단어 하나씩 확인
        for can in say:
            if can * 2 not in bab:  # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(can, '0' * len(can))
                
        if bab.count('0') == len(bab):  # 0으로만 이루어져 있으면 answer+1
            answer += 1
            
    return answer