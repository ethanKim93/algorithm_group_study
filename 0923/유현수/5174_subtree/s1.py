import sys
sys.stdin = open('sample_input.txt')


def pre_order(n):
    if n:
        return 1 + pre_order(left[n]) + pre_order(right[n])
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    V = E + 1   # 노드의 개수
    left = [0] * (V+1)
    right = [0] * (V+1)
    for i in range(E):
        p, c = edges[i*2], edges[i*2+1]
        if not left[p]:
            left[p] = c
        else:
            right[p] = c

    print('#{} {}'.format(tc, pre_order(N)))
