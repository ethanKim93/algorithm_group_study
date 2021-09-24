import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        temp = list(map(int, input().split()))
        tree[temp[0]] = temp[1]

    for idx in range(N, 1, -1):
        tree[idx//2] += tree[idx]

    print('#{} {}'.format(tc, tree[L]))