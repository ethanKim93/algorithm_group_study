import sys
sys.stdin = open('sample_input.txt')

def min_sum(j, k, s):
    global result

    if N == k:
        if result > s:
            result = s

    if result < s:
        return

    else:
        for i in range(N):
            if vs[i] == 0:
                vs[i] = 1
                min_sum(N, k+1, s+ num[k][i])
                vs[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [list(map(int,input().split())) for _ in range(N)]
    vs = [0] * N

    k = 0
    result = 10*N
    min_sum(N, 0, 0)
    print('#{} {}'.format(tc, result))




