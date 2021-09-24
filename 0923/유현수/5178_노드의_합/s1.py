import sys
sys.stdin = open('sample_input.txt')


def post_order(n):
    if n * 2 > N:
        return heap[n]
    elif n * 2 + 1 > N:
        heap[n] = post_order(n * 2)
        return heap[n]
    else:
        heap[n] = post_order(n * 2) + post_order(n * 2 + 1)
        return heap[n]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    heap = [0] * (N + 1)
    for _ in range(M):
        i, v = map(int, input().split())
        heap[i] = v

    post_order(1)

    print('#{} {}'.format(tc, heap[L]))
