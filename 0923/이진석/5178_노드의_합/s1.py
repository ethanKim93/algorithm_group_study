import sys

sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())  # 노드의개수 N, 리프 노드의 개수 M, 값을 출력할 노드번호 L
    tree = [0] * (N + 1)                 # 완전 이진트리
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value                # 트리에 값 입력
    for i in range(N, 0, -1):            # 가장 마지막 노드에서부터 root까지 순회
        tree[i//2] += tree[i]            # 자식노드의 값 부모노드에 합산
    print('#{} {}'.format(tc, tree[L]))