import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def post(idx, N):
    result = 0
    if idx <= N:
        result = tree[idx] + post(2*idx, N) + post(2*idx + 1, N)
        tree[idx] = result
    return result

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    post(1, N)

    print("#{} {}".format(tc, tree[L]))
