import sys
sys.stdin = open('sample_input.txt')


def postorder(n):
    if n <= N:
        postorder(n * 2)
        postorder(n * 2 + 1)
        tree[n // 2] += tree[n]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    postorder(1)
    print('#{} {}'.format(tc, tree[L]))