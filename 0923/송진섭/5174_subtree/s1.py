import sys
sys.stdin = open('sample_input.txt')


def in_order(v):
    global cnt
    if v:
        in_order(left[v])
        cnt += 1
        in_order(right[v])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    in_order(N)
    print('#{} {}'.format(tc, cnt))

