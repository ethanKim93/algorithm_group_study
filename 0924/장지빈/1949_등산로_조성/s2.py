import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def route(x, y, RouteCnt, K):
    global ans
    if RouteCnt > ans : ans = RouteCnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if matrix[x][y] > matrix[nx][ny]:
                route(nx, ny, RouteCnt+1, K)
            elif matrix[x][y] > matrix[nx][ny] - K and K:
                tmp = matrix[nx][ny]
                matrix[nx][ny] = matrix[x][y]-1
                route(nx, ny, RouteCnt+1, 0)
                matrix[nx][ny] = tmp

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    m_peak = matrix[0][0]
    peak_xy = []
    ans = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > m_peak:
                m_peak = matrix[i][j]
                peak_xy = [[i, j]]
            elif matrix[i][j] == m_peak:
                peak_xy.append([i,j])
    for i in range(len(peak_xy)):
        route(peak_xy[i][0], peak_xy[i][1], 1, 1)

    print('#{} {}'.format(tc, ans))
