import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        l, n = map(int, input().split())
        tree[l] = n
    for i in range(N, 0, -1):
        tree[i//2] += tree[i]
    print('#{} {}'.format(tc, tree[L]))

