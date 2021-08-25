import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def check(now):
    stack.append(now)
    visit[now[0]][now[1]] = 1



    for i in range(4):
        if 0 <= stack[-1][0] + row[i] <= N and 0 <= stack[-1][1] + col[i] <= N and visit[stack[-1][0]][stack[-1][1]] == 0:
            if board[stack[-1][0]][stack[-1][1]] == 0:
                visit[stack[-1][0]][stack[-1][1]] = 1
                now = [stack[-1][0] + row[i], stack[-1][1] + col[i]]
                check(now)
            if board[stack[-1][0]][stack[-1][1]] == 3:
                return 1
    return 0

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    now = ''
    stack = []
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                now = [i, j]
                break
    row = [0,1,0,-1]
    col = [1,0,-1,0]
    print(check(now))



