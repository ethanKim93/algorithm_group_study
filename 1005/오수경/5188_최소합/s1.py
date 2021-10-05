import sys
sys.stdin = open ('sample_input.txt')

def find_min(i, j, cnt):
    global N, ans, board
    if i == N-1 and j == N-1:
        if cnt < ans:
            ans = cnt
        return
    else:
        way = []
        way.append([i,j])
        visited[i][j] = 1

        # 우, 하
        di = [0, 1]
        dj = [1, 0]

        while way:
            if ans < cnt:
                return
            now = way.pop(0)
            for k in range(2):
                ni = now[0] + di[k]
                nj = now[1] + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if visited[ni][nj] == 0:
                        x = board[ni][nj]
                        find_min(ni, nj, cnt + x)
                        visited[ni][nj] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 9*(2*N-1)
    find_min(0, 0, board[0][0])
    print('#{} {}'.format(tc, ans))