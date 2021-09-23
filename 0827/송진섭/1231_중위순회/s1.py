import sys
sys.stdin = open('input.txt')


def in_order(v):
    global res
    if bt[v]:
        in_order(left[v])
        res += bt[v]
        in_order(right[v])


for tc in range(1, 11):
    N = int(input())
    E = N - 1
    edge = list(list(input().split()) for _ in range(N))

    left = [0] * (N+1)
    right = [0] * (N+1)
    bt = [0] * (N+1)
    for i in range(N):
        p = int(edge[i][0])
        bt[p] = edge[i][1]
        if len(edge[i]) > 2:
            left[p] = int(edge[i][2])
            if len(edge[i]) > 3:
                right[p] = int(edge[i][3])
    res = ''
    in_order(1)
    print('#{} {}'.format(tc, res))
