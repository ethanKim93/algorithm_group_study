import sys
sys.stdin = open('input.txt')

d = [0, 0, -1, 1]
def bfs(i, j):
    Q = [(i, j)]
    time[i][j] = 0
    for r, c in Q:
        for k in range(4):
            nr, nc = r+d[k], c+d[k-2]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            if arr[nr][nc]:         # 공사를 진행해야 되는 경우
                if time[nr][nc] > time[r][c] + arr[nr][nc]:
                    time[nr][nc] = time[r][c] + arr[nr][nc]
                    Q.append((nr, nc))
            else:                               # 
                if time[nr][nc] > time[r][c]:
                    time[nr][nc] = time[r][c]
                    Q.append((nr, nc))
    return time[-1][-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    INF = 1000000
    time = [[INF]*N for _ in range(N)]
    print('#{} {}'.format(tc, bfs(0, 0)))
