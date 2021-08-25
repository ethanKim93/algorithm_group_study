import sys
sys.stdin = open("input.txt")
#4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

def dfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while stack:
        r, c = stack.pop()
        maze[r][c] = 1

        for j in range(4):
            nr = r + dr[j]
            nc = c + dc[j]

            if 0 <= nr < N and 0 <= nc < N : #범위제한
                if maze[nr][nc] == 0: #0이면 이동
                    stack.append([nr,nc])
                elif maze[nr][nc] == 3:
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    stack = []

    #출발 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                stack.append([i,j])

    print('#{} {}'.format(tc, dfs()))
