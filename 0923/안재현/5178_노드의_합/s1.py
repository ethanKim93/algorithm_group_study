import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(0, T):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value
    n = len(tree) - 1
    for i in range(n, 0, -1):
        if not tree[i]:
            if i * 2 + 1 <= N:
                tree[i] = tree[i * 2] + tree[i * 2 + 1]
            elif i * 2 <= N:
                tree[i] = tree[i * 2]
            else:
                continue
    print('#{} {}'.format(tc + 1, tree[L]))