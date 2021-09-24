import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for m in range(M):
        leaf_node, num = map(int, input().split())
        node[leaf_node] = num

    for n in range(N, 0, -1):
        if node[n] == 0:
            if N%2 ==0 and (2*n == N):
                node[n] = node[2*n]
            else:
                node[n] = node[2*n] + node[2*n+1]

    print(f'#{tc} {node[L]}')