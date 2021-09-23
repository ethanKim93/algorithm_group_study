import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for i in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    print(tree)