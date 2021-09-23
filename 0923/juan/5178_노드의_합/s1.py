import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N,M,L = map(int, input().split())
    tree = [0] * (N+1)                          # tree 배열 초기화
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num                        # 입력되는 leaf 노드 값들을 tree 배열에 할당
    for j in range(N, 0, -1):
        tree[j//2] += tree[j]                   # leaf 노드들을 순차적으로 순회하면서 부모 노드에 값을 합산
    print('#{} {}'.format(tc, tree[L]))