import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def DFS():

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    while stack:
        now = stack.pop()               #[4, 3]
        r, c = now[0], now[1]           # r = 4, c = 3
        maze[r][c] = '1'
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '0':
                    stack.append([nr, nc])
                elif maze[nr][nc] == '3':
                    return 1
    return 0

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    stack = []                #stack = [[4,3]]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                stack.append([i,j])

    print(DFS())