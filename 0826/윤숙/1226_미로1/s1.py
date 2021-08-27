def DFS(sx, sy):
    global flag
    delx = [1, -1, 0, 0]
    dely = [0, 0, -1, 1]
    for i in range(4):
        nx = sx + delx[i]
        ny = sy + dely[i]
        if nx >= 0 and ny >= 0 and nx < M and ny < M:
            if miro[nx][ny] == 0:
                miro[nx][ny] = 1
                DFS(nx, ny)
            if miro[nx][ny] == 3:
                flag = 1
                return



import sys

sys.stdin = open('input.txt')
T = 10
for tc in range(1, T + 1):
    N = int(input())
    M = 16
    miro = [list(map(int, input())) * M for _ in range(M)]
    sx = 0
    sy = 0
    dx = 0
    dy = 0
    flag=0
    for i in range(0, M):
        for j in range(0, M):
            if miro[i][j] == 2:
                sx = i
                sy = j
        if sx and sy:
            break
    DFS(sx,sy)
    print('#{} {}'.format(tc, flag))
