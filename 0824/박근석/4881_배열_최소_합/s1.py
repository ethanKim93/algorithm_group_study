import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def check(row, t_max, c_max):
    if N == row:
        if c_max < t_max:
            t_max = c_max
        return

    if c_max > t_max:
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            check(row+1, t_max, c_max + board[row][i])
            visit[i] = 0
    return


for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, list(input().split()))) for _ in range(N)]
    row = 0
    t_max = 10*N
    c_max = 0
    visit = [0]*N

    check(row, t_max, c_max)
    print(t_max)







