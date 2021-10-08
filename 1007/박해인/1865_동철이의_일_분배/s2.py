import sys
sys.stdin = open('input.txt')

def perm(k, sumV):
    global maxV

    if sumV == 0:
        return

    # 원래 최대를 구하는 것은 backtracking이 불가능
    # 이 문제의 경우 *0.01을 하기 때문에
    if sumV < maxV:
        return

    if k == N:
        # sumV = 1
        # for i in range(N):
        #     workp = res[i]
        #     sumV *= P[i][workp] * 0.01
        if maxV < sumV:
            maxV = sumV

    for i in range(N):
        if used[i]: continue
        res[k] = i
        used[i] = True
        perm(k+1, sumV*P[k][i]*0.01)
        used[i] = False

TC = int(input())
# TC = 1
for tc in range(1, TC+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    res = [-1] * N
    used = [False] * N
    maxV = 0
    perm(0, 1)
    print('#{0} {1:.6f}'.format(tc, maxV*100))