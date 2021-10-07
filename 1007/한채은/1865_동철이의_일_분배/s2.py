import sys
sys.stdin = open('input.txt')

def perm(k, sumV):
    global maxV

    if sumV == 0:
        return

    if sumV < maxV:
        return

    if k == N:
    #     sumV = 1
    #     for i in range(N):
    #         workp = res[i]
    #         sumV *= P[i][workp] * 0.01
        if maxV < sumV:
            maxV = sumV

    for i in range(N):
        if used[i]: continue
        res[k] = i
        used[i] = True
        perm(k+1, sumV * P[k][i] * 0.01)
        used[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    res = [-1] * N
    used = [False] * N
    perm(0, 1)

    print('#{} {:6f}'.format(tc, maxV * 100))