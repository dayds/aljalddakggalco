# 1st try - 시간 초과 (Swapping 때문에 시간 초과)
def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players

# 2nd try - 딕셔너리 사용
def solution(players, callings):
    # 딕셔너리 생성
    player_dict = {player: i for i, player in enumerate(players)}
    
    for call in callings:
        # 현재 등수
        current_rank = player_dict[call]
        # 이전 등수
        previous_rank = current_rank - 1
        # 이전 등수의 선수
        previous_player = players[previous_rank]
        
        # 선수 위치 교환
        players[current_rank], players[previous_rank] = players[previous_rank], players[current_rank]
        
        # 딕셔너리 업데이트
        player_dict[call] = previous_rank
        player_dict[previous_player] = current_rank
        
    return players
