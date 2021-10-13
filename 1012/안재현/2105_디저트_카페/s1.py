import sys
sys.stdin = open('sample_input.txt')


def solve(r, c, dir, l):

    if dir == 0:
        solve(r + dr[0], c + dc[0], 0, l + 1)
        solve(r + dr[1], c + dc[1], 1, l + 1)
    elif dir == 1:
        pass
    elif dir == 2:
        if si - sj != r - c:
            pass
        else:
            pass
    else:
        pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    dr = [1, 1, -1 - 1]
    dc = [-1, 1, 1, -1]
    for i in range(N):
        for j in range(N):
            si = i
            sj = j
            solve(i, j, 0, 1)

    print('#{} {}'.format(tc, max_v))
