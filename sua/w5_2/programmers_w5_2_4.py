def solution(sides):
    triangle = sum(sides) - max(sides)
    
    if max(sides) < triangle:
        return 1
    else:
        return 2