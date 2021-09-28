import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for m in range(M):
        leaf_node, num = map(int, input().split())
        node[leaf_node] = num  # leaf_node위치에 있는 노드들에 num 부여

    for n in range(N, 0, -1):  # 거꾸로 순회하여 바로 앞에 있는 조상확인(순차적 진행할시 루트를 먼저 거치므로 오류)
        if node[n] == 0:
            if 2*n == N:  # 2*n가 N과 같다면 우측노드가 없다.
                node[n] = node[2*n]
            else:
                node[n] = node[2*n] + node[2*n+1]

    print(f'#{tc} {node[L]}')