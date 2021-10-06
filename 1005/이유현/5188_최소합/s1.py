import sys
sys.stdin = open('sample_input.txt')


dr = [0, 1]
dc = [1, 0]


def dfs(r, c):
    global sub_total, minV

    if minV < sub_total:
        return

    if r == N-1 and c == N-1:
        if minV > sub_total:
            minV = sub_total
            return

    for d in range(2):
        nr, nc = r + dr[d], c + dc[d]
        if nr in range(N) and nc in range(N) and visit[nr][nc] != 1:
            visit[nr][nc] = 1
            sub_total += arr[nr][nc]
            dfs(nr, nc)
            visit[nr][nc] = 0
            sub_total -= arr[nr][nc]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    minV = 987654321
    sub_total = arr[0][0]

    dfs(0, 0)
    print('#{} {}'.format(tc, minV))
