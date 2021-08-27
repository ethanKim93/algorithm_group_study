import sys
sys.stdin = open('input.txt')

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
            if 0 <= a < 16 and 0 <= b < 16:
                if visit[a][b] == 0 and board[a][b] == 0:
                    queue.append([a, b])
                    visit[a][b] = visit[x][y] + 1
                elif board[a][b] == 3:
                    return 1
    return 0

for tc in range(1, 11):
    T = int(input())
    board = [list(map(int, list(input()))) for i in range(16)]
    visit = [[0]*16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                start = [i, j]

    print('#{} {}'.format(tc, check(start)))