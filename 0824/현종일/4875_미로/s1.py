import sys
sys.stdin = open("sample_input.txt")

def dfs():

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while stack:
        now = stack.pop()
        r, c = now[0], now[1]
        maze[r][c] = 1
        for i in range(4):
            nr, nc = r + dr[i], c+ dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 0:
                    stack.append([nr,nc])
                elif maze[nr][nc] == 3:
                    print("#{} 1".format(tc,))
                    return
    print("#{} 0".format(tc))

for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    stack = []

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                stack.append([i, j])
    dfs()