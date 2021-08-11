import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    answer = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    cnt = 1
    i = 0
    j = -1
    k = 0

    while cnt <= N ** 2:
        ni = i + di[k]
        nj = j + dj[k]
        if ni < N and nj < N and not answer[ni][nj]:
            answer[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4
    print('#{}'.format(tc))
    for idx in range(len(answer)):
        print(*answer[idx])
