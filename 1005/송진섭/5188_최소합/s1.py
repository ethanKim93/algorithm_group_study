import sys
sys.stdin = open('sample_input.txt')
dr = [0, 1]
dc = [1, 0]


def num_sum(row, col, total):
    global ans
    total += num_map[row][col]
    if total > ans:
        return
    if row == N-1 and col == N-1:
        if ans > total:
            ans = total
        return
    for k in range(2):
        nr = row + dr[k]
        nc = col + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] == 0:
                visited[row][col] = 1
                num_sum(nr, nc, total)
                visited[row][col] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    ans = 13 * 2 * 10
    num_sum(0, 0, 0)
    print(ans)
