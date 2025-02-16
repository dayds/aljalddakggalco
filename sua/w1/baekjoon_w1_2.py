import sys

def process_reservations(N, M, reservations):
    last_end_time = {}  
    results = []

    for k, s, e in reservations:
        if k in last_end_time and last_end_time[k] > s:
            results.append("NO")  
        else:
            results.append("YES")  
            last_end_time[k] = e  
    
    sys.stdout.write("\n".join(results) + "\n")

# 입력 받기
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    reservations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    process_reservations(N, M, reservations)
