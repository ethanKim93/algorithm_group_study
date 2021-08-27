import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def check(start):
    queue = [start]
    row = [0,1,0,-1]
    col = [1,0,-1,0]

    while queue:
        now = queue.pop(0)
        x = now[0]
        y = now[1]
        for i in range(4):
            a = x + row[i]
            b = y + col[i]
            if 0 <= a < N and 0 <= b < N:
                if visit[a][b] == 0 and board[a][b] == 0:
                    queue.append([a, b])
                    visit[a][b] = visit[x][y] + 1
                elif board[a][b] == 3:
                    return visit[x][y]
    return 0

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = [i, j]

    print('#{} {}'.format(tc, check(start)))
