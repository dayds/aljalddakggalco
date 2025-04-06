def solution(data, ext, val_ext, sort_by):
    # 올바른 인덱스 매핑 (0부터 시작)
    idx = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    # 조건에 맞는 데이터 필터링
    answer = [row for row in data if row[idx[ext]] < val_ext]
    # sorted 함수로 정렬 (sort_by 기준으로)
    answer = sorted(answer, key=lambda x: x[idx[sort_by]])
    return answer