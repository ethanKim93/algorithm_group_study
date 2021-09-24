import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)
    for _ in range(M):
        node, num = map(int, input().split())
        nodes[node] = num

    for i in range(N, 0, -1):
        if nodes[i] == 0:
            if (2*i + 1) <= N:
                nodes[i] = nodes[i*2 + 1] + nodes[i*2]
            else:
                nodes[i] = nodes[i*2]

    print('#{} {}'.format(tc, nodes[L]))
